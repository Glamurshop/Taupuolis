# 🔑 Google Cloud API Nustatymas

## 📋 Reikalavimai automatiniam generatoriui:

### 1. Google Cloud Projektas
1. Eik į [Google Cloud Console](https://console.cloud.google.com/)
2. Sukurk naują projektą pavadinimu "taupuolis-generator"
3. Pasirink projektą

### 2. API Įjungimas
1. Eik į "APIs & Services" → "Library"
2. Ieškok ir įjunk:
   - **Google Sheets API**
   - **Google Drive API**

### 3. Service Account Sukūrimas
1. Eik į "IAM & Admin" → "Service Accounts"
2. Spausk "Create Service Account"
3. Pavadinimas: `taupuolis-generator`
4. Aprašymas: `Automatinis Taupuolis.lt generatorius`
5. Spausk "Create and Continue"

### 4. Service Account Rolių Nustatymas
1. Role: **Editor** (pilnas prieiga)
2. Spausk "Continue"
3. Spausk "Done"

### 5. JSON Raktų Atsisiuntimas
1. Spausk ant sukurtos Service Account
2. Eik į "Keys" tab
3. Spausk "Add Key" → "Create new key"
4. Pasirink "JSON"
5. Spausk "Create"
6. Atsisiųsk failą

### 6. Failų Nustatymas
1. Pervadink atsisiųstą failą į `credentials.json`
2. Perkelk į `generator/` katalogą
3. Atnaujink `FOLDER_ID` `generate.py` faile

### 7. Google Drive Folder
1. Sukurk Google Drive folderyje naują katalogą
2. Pavadinimas: "Taupuolis Generator"
3. Nukopijuok folder ID iš URL
4. Atnaujink `FOLDER_ID` `generate.py` faile

## 🔧 Failų Atnaujinimas

### generate.py
```python
# Pakeisk šią eilutę:
FOLDER_ID = "JŪSŲ_FOLDER_ID_ČIA"
```

### credentials.json
Perkelk atsisiųstą JSON failą į `generator/credentials.json`

## 🧪 Testavimas

```bash
cd generator
python auto_generator.py --once
```

## ⚠️ Saugumas

- **Niekada necommitink** `credentials.json` į GitHub
- Pridėk į `.gitignore`:
  ```
  generator/credentials.json
  ```
- Naudok GitHub Secrets produkcijoje

## 🚀 Po Nustatymo

1. **Testuok generatorių:**
   ```bash
   python auto_generator.py --once
   ```

2. **Paleisk automatinį režimą:**
   ```bash
   python auto_generator.py
   ```

3. **Nustatyk cron job:**
   ```bash
   python auto_generator.py --cron
   ```

## 📞 Pagalba

Jei kyla problemų:
1. Patikrink, ar API įjungti
2. Patikrink, ar Service Account turi Editor rolę
3. Patikrink, ar folder ID teisingas
4. Patikrink, ar credentials.json failas teisingame kataloge

**Po šių nustatymų automatinis generatorius veiks puikiai!** 🎉 