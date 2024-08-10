# GersiuAV
Cine păstrează antivirusul în zilele noastre? Nimeni nu vrea să-și încetinească computerul pentru un antivirus inutil. Dar uneori trebuie să scanăm un fișier pentru viruși. Deci aici este o soluție. GersiuAV scanează un fișier utilizând scanerul de fișiere online al VirusTotal.

# De ce GersiuAV?
Mulți oameni, inclusiv eu, preferă să nu păstreze antivirusul în computerul lor. Dar uneori chiar trebuie să scanăm un fișier pentru viruși. În astfel de momente folosim scanere de viruși online precum VirusTotal.com. GersiuAV a adus această funcționalitate în cli-ul tău. Puteți chiar să-l adăugați în meniul contextual folosind install.py, așa cum se arată în imaginea de mai jos, și ghiciți ce? Nu vă încetinește sistemul nici măcar cu 0,01%. Așa că este timpul să ne luăm rămas bun de la antivirusuri și să salutăm serviciile online de scanare a fișierelor.

![Captură de ecran a GersiuAV în meniul contextual.](https://telegra.ph/file/b2891e4f6ac3fcce0f578.png)

# Confidențialitate?
Scriptul trimite mai întâi hash-ul unui fișier către VirusTotal pentru a verifica dacă același fișier este deja disponibil pentru VirusTotal. În acest caz, datele dumneavoastră sunt complet securizate, deoarece fișierul nu este încărcat. Dar dacă VirusTotal nu recunoaște acel hash, atunci scriptul vă întreabă dacă doriți să încărcați fișierul, în cazul în care răspundeți cu da, fișierul va fi încărcat pe VirusTotal. Deci depinde de dvs. dacă doriți să încarcați fișierul sau nu. Fișierele sensibile nu trebuie încărcate.

# Instalare
Mai întâi asigurați-vă că aveți instalate python (versiunea >= 3) și pip în sistemul dvs.

### Mai întâi, instalați dependențele:
În linie de comandă (Command Prompt) rulați comanda
pip install -r requirements.txt
```
### Acum pentru a crea config.py și a adăuga la meniul contextual:
#### Metoda automată (recomandată)
- Rulați scriptul install.py. Urmați pașii de pe ecran și ați terminat.

##### Dezinstalare:
- Pur și simplu rulați uninstall.py

#### Metoda manuală (Nu este deloc recomandată decât dacă ești profesionist.)
- Redenumiți sample-config.py în config.py
- Accesați https://virustotal.com/, creați un cont, obțineți o cheie API și inserați acea cheie API în variabila api_key din config.py
- Deschideți editorul de regiștri (În meniul de pornire, căutați regedit)
- Accesați HKEY_CURRENT_USER > SOFTWARE > Classes > * > shell
- Dați clic dreapta pe shell, creați o cheie nouă (new > key)
- Numiți-o „ScanItbyGersiuAV”.
- În câmpul DATE pentru cheia `(Default)`, puneți valoarea datelor: `Scanează Online cu GersiuAV`
- Dați clic dreapta pe ScanItbyGersiuAV, creați new > String Value, puneți numele: `Icon` și valoarea datelor: `C:\calea\către\GersiuAV\icon.ico` (Asigurați-vă că înlocuiți calea cu calea reală)
- Dați clic dreapta pe ScanItbyGersiuAV, creați o cheie nouă >, redenumiți-o în `command`, în câmpul de date pentru `(Default)`, puneți valoarea: `"C:\calea\catre\python\python.exe" "C:\calea\către\GersiuAV”. „%1”`
- Gata

##### Dezinstalare:
- Deschideți editorul de regiștri (În meniul de pornire, căutați regedit)
- Accesați HKEY_CURRENT_USER > SOFTWARE > Classes > * > shell
- Dați clic dreapta pe ScanItbyGersiuAV și ștergeți-l.
- Confirmați ștergerea
- Gata

# Pentru utilizatorii Linux:

- Pentru a instala scanit-cli, utilizați următoarea comandă:
```bash
pip3 install scanit-cli
```
# Note
- Intimitatea dvs. este în mâinile dvs. Vă rugăm să nu încărcați fișiere sensibile în baza de date VirusTotal.

# Credite
- pictograma <a target="_blank" href="https://icons8.com/icons/set/security-checked">Pictograma Protejați</a> de <a target="_blank" href="https:// icons8.com">Icons8</a>
