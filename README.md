# Taupuolis.lt - Nuolaidų kodų platforma

Moderni nuolaidų kodų ir akcijų platforma Lietuvoje, skirta padėti vartotojams taupyti pinigus ir pardavėjams pasiekti naujus klientus.

## 🚀 Funkcionalumas

### Vartotojams:
- **Nuolaidų kodų paieška** - raskite geriausius pasiūlymus
- **Kategorijų naršymas** - naršykite pagal prekių kategorijas
- **Pardavėjų puslapiai** - peržiūrėkite konkretaus pardavėjo pasiūlymus
- **Paieškos sistema** - ieškokite pardavėjų ar pasiūlymų
- **Naujienlaiškis** - gaukite geriausius pasiūlymus el. paštu
- **Mobilus dizainas** - puiki patirtis bet kokiame įrenginyje

### Pardavėjams:
- **Partnerystės sistema** - prisijunkite prie mūsų platformos
- **Automatinis atnaujinimas** - CSV failų importavimas
- **Analitikos ataskaitos** - sekiite savo rezultatus
- **Komisinių sistema** - uždirbkite nuo sėkmingų pardavimų

## 🛠️ Technologijos

- **Frontend**: HTML5, CSS3 (Tailwind CSS), JavaScript
- **Backend**: Statinis hosting (Netlify)
- **Duomenys**: JSON failai
- **SEO**: Optimizuota struktūra, sitemap.xml, meta tagai
- **Saugumas**: HTTPS, CSP antraštės

## 📁 Projekto struktūra

```
Taupuolisgrududemo/
├── index.html                 # Pagrindinis puslapis
├── header.html               # Bendras header komponentas
├── styles.css                # Papildomi stiliai
├── visi_pasiulymai.json     # Visi pasiūlymai
├── vendors.json             # Pardavėjų sąrašas
├── sitemap.xml              # SEO sitemap
├── robots.txt               # Paieškos variklių nustatymai
├── netlify.toml             # Netlify konfigūracija
├── kategorijos/             # Kategorijų puslapiai
├── pardavejai/              # Pardavėjų puslapiai
├── pasiulymai/              # Individualūs pasiūlymų puslapiai
├── auth/                    # Autentifikacijos puslapiai
└── generator/               # Automatinio turinio generavimas
```

## 🚀 Diegimas ir paleidimas

### Lokaliam plėtojimui:
1. Nukopijuokite projektą
2. Atidarykite `index.html` naršyklėje
3. Arba naudokite lokalią serverį:
   ```bash
   python -m http.server 8000
   ```

### Produkcijai (Netlify):
1. Pridėkite projektą į GitHub
2. Prisijunkite prie Netlify
3. Importuokite projektą iš GitHub
4. Svetainė bus automatiškai išdėstyta

## 📊 Duomenų struktūra

### Pasiūlymo objektas:
```json
{
  "pavadinimas": "Produkto pavadinimas",
  "aprasymas": "Detalus aprašymas",
  "nuotraukos_url": "https://example.com/image.jpg",
  "nuolaidos_kodas": "TAUPUOLIS20",
  "nukreipimo_url": "https://parduotuve.lt?ref=taupuolis20",
  "kategorija": "Kvepalai",
  "pardavejas": "Douglas",
  "pardavejo_logo": "https://example.com/logo.jpg",
  "terminas": "2025-02-15",
  "kaina_nuo": "89.99€",
  "kaina_iki": "71.99€",
  "nuolaida_procentais": "20%",
  "vip": true
}
```

## 🔧 Konfigūracija

### SEO nustatymai:
- Atnaujinkite `sitemap.xml` su tikrais URL
- Pridėkite Google Analytics ID į `analytics.html`
- Konfigūruokite Facebook Pixel

### Pardavėjų pridėjimas:
1. Pridėkite pardavėją į `vendors.json`
2. Sukurkite pardavėjo puslapį `pardavejai/` kataloge
3. Atnaujinkite `sitemap.xml`

### Pasiūlymų pridėjimas:
1. Pridėkite pasiūlymą į `visi_pasiulymai.json`
2. Sukurkite individualų puslapį `pasiulymai/` kataloge
3. Atnaujinkite atitinkamą kategorijos puslapį

## 📈 Analitika ir stebėjimas

### Google Analytics:
- Puslapių peržiūros
- Vartotojų elgsena
- Konversijų stebėjimas

### Facebook Pixel:
- Retargeting kampanijos
- Konversijų stebėjimas
- Audiencijos kūrimas

## 🔒 Saugumas

- **HTTPS priverstinis** - visi puslapiai per HTTPS
- **CSP antraštės** - Content Security Policy
- **XSS apsauga** - Cross-Site Scripting apsauga
- **Duomenų validacija** - visi įvesties duomenys validuojami

## 📱 Mobilus dizainas

- **Responsive dizainas** - veikia visuose įrenginiuose
- **Touch-friendly** - optimizuota lietimui
- **Greitas kraunamumas** - optimizuoti paveikslėliai
- **PWA paruošta** - galima pridėti PWA funkcionalumą

## 🎯 Kiti planai

- [ ] Vartotojų registracija ir prisijungimas
- [ ] Mėgstamiausių pasiūlymų išsaugojimas
- [ ] Push pranešimai
- [ ] Pasiūlymų vertinimo sistema
- [ ] Komentarų sistema
- [ ] API endpoint'ai
- [ ] Automatinis pasiūlymų tikrinimas
- [ ] Daugiakalbystė

## 📞 Kontaktai

- **El. paštas**: info@taupuolis.lt
- **Svetainė**: https://taupuolis.lt
- **Pardavėjams**: https://taupuolis.lt/pardavejams.html

## 📄 Licencija

© 2025 Taupuolis.lt – Visos teisės saugomos.

---

**Pastaba**: Šis projektas yra demonstracinis. Produkcijai naudoti reikia pridėti tikrus duomenis ir konfigūruoti analitikos sistemas. 