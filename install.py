import os, sys, time

if sys.version_info[0] < 3:
    print("Python 2 nu este acceptat. Vă rugăm să utilizați python 3.")
    time.sleep(2)
    exit()

dir_path = os.path.dirname(os.path.realpath(__file__))
script_path = os.path.join(dir_path, ".")
icon_path = os.path.join(dir_path, "icon.ico")
python_path = sys.executable
config_path = os.path.join(dir_path, "config.py")

if os.name != "nt":
    print("Numai Windows este acceptat. Pentru Linux, puteți utiliza ramura „module”, https://github.com/shivamsn97/ScanIt/tree/module")
    time.sleep(2)
    exit()

try:
    import vt
    import colorama
except ModuleNotFoundError:
    print("Vă rog să instalați mai întâi modulele necesare folosind comanda: ")
    print("  > pip install -r requirements.txt")
    time.sleep(2)
    exit()

try:
    sys.path.append(dir_path)
    import config
except ModuleNotFoundError:
    print("Mai întâi trebuie să generați fișierul de configurare.")
    vt_url = "https://www.virustotal.com/gui/home"
    print("Vă rog să urmați cu atenție următorii pași:")
    try:
        import webbrowser
        webbrowser.open(vt_url)
        print("1. Browserul este deschis pentru pagina web a VirusTotal. ")
    except:
        print("1. Deschideți această pagină în browser: {}".format(vt_url))
    print("   - În colțul din dreapta sus, dați clic pe Sign up (sau conectați-vă dacă aveți deja un cont) și urmați pașii corespunzători pentru a vă crea (sau a vă conecta la) contul dvs.")
    print("   (În cazul în care ați creat un cont, verificați e-mailul pentru un mesaj de confirmare și activați-vă contul)")
    print("2. În colțul din dreapta sus, dați clic pe pictograma care conține numele dvs. și poza de profil, faceți clic pe Cheia API, copiați cheia API personală și inserați-o aici (doar faceți clic dreapta pe terminal după copiere.)")
    API_KEY = input("Introduceți cheia API aici ::>> ").strip()
    while not API_KEY:
        API_KEY = input("Ceva nu a funcționat. Introduceți cheia API aici ::>> ").strip()
    try:
        with vt.Client(API_KEY) as client:
            file = client.get_object("/files/44d88612fea8a8f36de82e1278abb02f")
    except vt.error.APIError as ex:
        if ex.code == "WrongCredentialsError":
            print("Cheia API pe care ați introdus-o nu este validă. Apliația se va închide...")
            time.sleep(3)
            exit()
    with open(config_path, "w") as fl:
        fl.write("api_key = '{}'".format(API_KEY))
    print("Instalare efectuată. config.py a fost creat")


import winreg

def define_action_on(filetype, registry_title, command, title=None, icon = None):
    """
    define_action_on(filetype, registry_title, command, title=None)
        filetype: either an extension type (ex. ".txt") or one of the special values ("*" or "Directory"). Note that "*" is files only--if you'd like everything to have your action, it must be defined under "*" and "Directory"
        registry_title: the title of the subkey, not important, but probably ought to be relevant. If title=None, this is the text that will show up in the context menu.
    """
    #all these opens/creates might not be the most efficient way to do it, but it was the best I could do safely, without assuming any keys were defined.
    reg = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\\Classes", 0, winreg.KEY_SET_VALUE)
    k1 = winreg.CreateKey(reg, filetype) #handily, this won't delete a key if it's already there.
    k2 = winreg.CreateKey(k1, "shell")
    k3 = winreg.CreateKey(k2, registry_title)
    k4 = winreg.CreateKey(k3, "command")
    if title != None:
        winreg.SetValueEx(k3, None, 0, winreg.REG_SZ, title)
    if icon != None:
        winreg.SetValueEx(k3, "Icon", 0, winreg.REG_SZ, icon)
    winreg.SetValueEx(k4, None, 0, winreg.REG_SZ, command)
    winreg.CloseKey(k3)
    winreg.CloseKey(k2)
    winreg.CloseKey(k1)
    winreg.CloseKey(reg)




choice = input("Sigur doriți să instalați Gersiu AV pe dispozitivul dvs.? (D/N): ")
if choice.lower() in ["d", "yes"]:
    define_action_on("*", "ScanItbyGersiuAV", "\"{}\" \"{}\" \"%1\"".format(python_path, script_path), "Scanează Online cu GersiuAV", icon_path)
    print("Instalare efectuată. GersiuAV a fost instalat cu succes. \nVă rog să nu ștergeți sau să mutați acest director în altă parte fără a dezinstala mai întâi.\n\nApăsați enter pentru a ieși. ")
    input()
    exit()