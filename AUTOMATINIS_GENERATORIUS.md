# 🤖 Automatinis Taupuolis.lt Generatorius

Šis generatorius automatiškai generuoja visus svetainės puslapius iš Google Sheets duomenų.

## 🚀 Kaip veikia:

1. **Skaito duomenis iš Google Sheets** (kiekvienas pardavėjas turi savo sheet)
2. **Automatiškai generuoja:**
   - Pasiūlymų puslapius (`pasiulymai/`)
   - Pardavėjų puslapius (`pardavejai/`)
   - Kategorijų puslapius (`kategorijos/`)
   - JSON failus su duomenimis
3. **Atnaujina svetainę realiu laiku**

## 📋 Reikalavimai:

```bash
pip install -r requirements.txt
```

## 🔧 Nustatymai:

1. **Google Sheets API:**
   - Sukurkite `generator/credentials.json` failą
   - Pridėkite Google Sheets folder ID į `generate.py`

2. **Google Sheets struktūra:**
   ```
   A: Pavadinimas
   B: Aprašymas  
   C: nuotraukos_url
   D: Nuolaidos kodas
   E: nukreipimo_url
   F: Kategorija
   G: Terminas
   H: Pardavėjas
   I: Pardavėjo info
   J: Logo URL
   ```

## 🎯 Kaip paleisti:

### 1. Vieną kartą:
```bash
cd generator
python auto_generator.py --once
```

### 2. Nuolatinis procesas:
```bash
cd generator
python auto_generator.py
```

### 3. Cron job (Linux/Mac):
```bash
cd generator
python auto_generator.py --cron
```

Tada pridėkite gautą komandą į crontab:
```bash
crontab -e
```

### 4. Windows Task Scheduler:
```bash
python auto_generator.py --once
```

## 📊 Logging:

Visi veiksmai registruojami į `generator.log` failą:
- Pakeitimų aptikimas
- Generavimo rezultatai
- Klaidos ir įspėjimai

## 🔄 Automatinis atnaujinimas:

### Google Sheets pakeitimai:
- Kai pardavėjas atnaujina savo sheet
- Generatorius automatiškai aptinka pakeitimus
- Sugeneruoja naujus puslapius per 1-2 minutes

### Nauji pardavėjai:
- Pridėkite naują Google Sheet į folder
- Generatorius automatiškai sukurs:
  - Pardavėjo puslapį
  - Visus pasiūlymų puslapius
  - Atnaujins kategorijas

## 🛠️ Serverio nustatymai:

### VPS/Serveris:
```bash
# Paleisti kaip background procesas
cd generator
nohup python auto_generator.py > generator.log 2>&1 &

# Arba naudoti systemd service
sudo systemctl enable taupuolis-generator
sudo systemctl start taupuolis-generator
```

### Netlify/Vercel:
- Naudokite cron job funkciją
- Arba GitHub Actions su cron trigger

## 📈 Monitoring:

### Log failai:
- `generator.log` - visi veiksmai
- `error.log` - tik klaidos

### Svetainės atnaujinimai:
- Patikrinkite `visi_pasiulymai.json`
- Patikrinkite `vendors.json`
- Patikrinkite puslapių datų laiką

## 🔧 Troubleshooting:

### Klaidos:
1. **Google API klaidos:**
   - Patikrinkite `credentials.json`
   - Patikrinkite folder ID

2. **Šablonų klaidos:**
   - Patikrinkite `templates/` katalogą
   - Patikrinkite Jinja2 sintaksę

3. **Duomenų klaidos:**
   - Patikrinkite Google Sheets struktūrą
   - Patikrinkite stulpelio pavadinimus

### Debug:
```bash
# Išsamus logging
cd generator
python auto_generator.py --debug

# Tik vieną sheet
python generate.py --sheet-id YOUR_SHEET_ID
```

## 🎯 Rezultatas:

Po sėkmingo generavimo turėsite:
- ✅ Visus pasiūlymų puslapius
- ✅ Visus pardavėjų puslapius  
- ✅ Visus kategorijų puslapius
- ✅ Atnaujintus JSON failus
- ✅ Automatiškai atnaujinamą svetainę

**Svetainė visada bus atnaujinta su naujausiais duomenimis!** 🚀 