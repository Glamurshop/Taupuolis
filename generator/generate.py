import os
import re
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from jinja2 import Environment, FileSystemLoader
from unidecode import unidecode
import json

# Nustatymai
FOLDER_ID = "1b20GxyX9QYCpgqIx86vmR6qY43RtYN8a"
TEMPLATES_DIR = "templates"
OUT_VENDOR_DIR = "pardavejai"
OUT_DEAL_DIR = "pasiulymai"
OUT_CATEGORY_DIR = "kategorijos"

# Google Sheets API prisijungimas
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
gc = gspread.authorize(creds)

# Jinja2 šablonų aplinka
env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))

def slugify(text):
    # Paverčia tekstą į draugišką URL: lietuviškos raidės -> lotyniškos, mažosios, be spec. simbolių
    text = unidecode(text)
    text = re.sub(r'[^a-zA-Z0-9]+', '-', text)
    return text.strip('-').lower()

def get_sheets_in_folder(folder_id):
    # Randa visus Google Sheets failus nurodytame folderyje
    from googleapiclient.discovery import build
    from googleapiclient.errors import HttpError

    creds2 = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', ['https://www.googleapis.com/auth/drive'])
    service = build('drive', 'v3', credentials=creds2)
    results = service.files().list(
        q=f"'{folder_id}' in parents and mimeType='application/vnd.google-apps.spreadsheet'",
        fields="files(id, name)").execute()
    return results.get('files', [])

def render_template(template_name, context):
    template = env.get_template(template_name)
    return template.render(context)

def main():
    os.makedirs(OUT_VENDOR_DIR, exist_ok=True)
    os.makedirs(OUT_DEAL_DIR, exist_ok=True)
    os.makedirs(OUT_CATEGORY_DIR, exist_ok=True)

    sheets = get_sheets_in_folder(FOLDER_ID)
    all_deals = []
    categories = {}
    vendors_json = {}

    for sheet_meta in sheets:
        sheet_id = sheet_meta['id']
        sheet_name = sheet_meta['name']
        sh = gc.open_by_key(sheet_id)
        worksheet = sh.sheet1
        data = worksheet.get_all_records()
        df = pd.DataFrame(data)

        # Pardavėjo info ir logo
        pardavejas = df['Pardavėjas'][0]
        pardavejo_info = worksheet.cell(2, 9).value  # I2
        logo_url = worksheet.cell(2, 10).value       # J2
        pardavejas_url = slugify(pardavejas)

        # Visi dealai
        deal_html_list = []
        vendor_deals = []
        for idx, row in df.iterrows():
            deal_slug = slugify(row['Pavadinimas'])
            kategorija_url = slugify(row['Kategorija'])
            deal_dict = {
                "pavadinimas": row['Pavadinimas'],
                "aprasymas": row['Aprašymas'],
                "nuotraukos_url": row['nuotraukos_url'],
                "nuolaidos_kodas": row['Nuolaidos kodas'],
                "nukreipimo_url": row['nukreipimo_url'],
                "kategorija": row['Kategorija'],
                "kategorija_url": kategorija_url,
                "pardavejas": pardavejas,
                "pardavejas_url": pardavejas_url,
                "pardavejo_logo": logo_url,
                "terminas": row['Terminas']
            }
            all_deals.append(deal_dict)
            vendor_deals.append(deal_dict)
            # Sugeneruoti deal puslapį
            deal_context = deal_dict
            deal_html = render_template("pasiulymas.html", deal_context)
            deal_path = os.path.join(OUT_DEAL_DIR, f"{deal_slug}.html")
            with open(deal_path, "w", encoding="utf-8") as f:
                f.write(deal_html)
            # Įtraukti į pardavėjo sąrašą
            deal_html_list.append(f"""
                <a href="/pasiulymai/{deal_slug}.html" class="block bg-white rounded shadow p-4 hover:bg-yellow-50 transition">
                  <img src="{row['nuotraukos_url']}" alt="{row['Pavadinimas']}" class="h-32 w-full object-contain mb-2 rounded" />
                  <div class="font-bold">{row['Pavadinimas']}</div>
                  <div class="text-sm text-gray-600">{row['Kategorija']}</div>
                </a>
            """)
            # Įtraukti į kategorijos sąrašą
            if kategorija_url not in categories:
                categories[kategorija_url] = {
                    "kategorija": row['Kategorija'],
                    "dealai": [],
                    "json": []
                }
            categories[kategorija_url]["dealai"].append(f"""
                <a href="/pasiulymai/{deal_slug}.html" class="block bg-white rounded shadow p-4 hover:bg-yellow-50 transition">
                  <img src="{row['nuotraukos_url']}" alt="{row['Pavadinimas']}" class="h-32 w-full object-contain mb-2 rounded" />
                  <div class="font-bold">{row['Pavadinimas']}</div>
                  <div class="text-sm text-gray-600">{pardavejas}</div>
                  <img src="{logo_url}" alt="{pardavejas} logo" class="h-8 w-8 rounded-full mt-2" />
                </a>
            """)
            categories[kategorija_url]["json"].append(deal_dict)

        # Sugeneruoti pardavėjo puslapį
        pardavejas_context = {
            "pardavejas": pardavejas,
            "pardavejo_info": pardavejo_info,
            "logo_url": logo_url,
            "dealai": "\n".join(deal_html_list)
        }
        vendor_path = os.path.join(OUT_VENDOR_DIR, f"{pardavejas_url}.html")
        vendor_html = render_template("pardavejas.html", pardavejas_context)
        with open(vendor_path, "w", encoding="utf-8") as f:
            f.write(vendor_html)
        # Sugeneruoti vendor JSON
        vendor_json_path = os.path.join(OUT_VENDOR_DIR, f"{pardavejas_url}.json")
        with open(vendor_json_path, "w", encoding="utf-8") as f:
            json.dump(vendor_deals, f, ensure_ascii=False, indent=2)

    # Sugeneruoti kategorijų puslapius ir JSON
    for kategorija_url, kat in categories.items():
        kategorija_context = {
            "kategorija": kat["kategorija"],
            "dealai": "\n".join(kat["dealai"])
        }
        kat_path = os.path.join(OUT_CATEGORY_DIR, f"{kategorija_url}.html")
        kat_html = render_template("kategorija.html", kategorija_context)
        with open(kat_path, "w", encoding="utf-8") as f:
            f.write(kat_html)
        # Kategorijos JSON
        kat_json_path = os.path.join(OUT_CATEGORY_DIR, f"{kategorija_url}.json")
        with open(kat_json_path, "w", encoding="utf-8") as f:
            json.dump(kat["json"], f, ensure_ascii=False, indent=2)

    # Bendras visų dealų JSON
    with open("visi_pasiulymai.json", "w", encoding="utf-8") as f:
        json.dump(all_deals, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()