import vt
import config
import argparse
import os
import hashlib, time
import colorama
import time

colorama.init(convert=True)

def check_file_exists(given_path):
    if not os.path.isfile(given_path):
        raise argparse.ArgumentTypeError(f"{given_path} nu este un fișier valid. Asigurați-vă că încercați să scanați numai fișierul, nu directorul.")
    return given_path

def print_result(stats, file_path):
    print(colorama.Fore.MAGENTA)
    print("Rezultatele scanării pentru fișierul {}".format(file_path.split(os.sep)[-1]))
    print("-------------------------------------------------------"+colorama.Fore.RESET)
    for i in stats:
        print((colorama.Fore.RED if i in ["suspicious1", "malicious1"] else colorama.Fore.GREEN if i in ["harmless1", "undetected1"] else colorama.Fore.CYAN) + i + colorama.Fore.RESET + ": {}".format(stats[i]))
    print(colorama.Fore.MAGENTA + "-------------------------------------------------------")
    print("Verdictul: \n" + colorama.Fore.RESET)
    num_safe = stats["harmless"] + stats["undetected"]
    num_unsafe = stats["suspicious"] + stats["malicious"]
    if num_unsafe == 0 and num_safe >= 20:
        print(colorama.Fore.GREEN + "TOTAL SIGUR" + colorama.Fore.RESET)
    elif num_unsafe == 0 and num_safe >=5:
        print(colorama.Fore.GREEN + "SIGUR" + colorama.Fore.RESET)
    elif num_unsafe == 0 and num_safe:
        print(colorama.Fore.LIGHTGREEN_EX + "NECUNOSCUT" + colorama.Fore.RESET)
    elif num_unsafe == 0:
        print(colorama.Fore.YELLOW + "NECUNOSCUT" + colorama.Fore.RESET)
    elif num_safe > num_unsafe:
        print(colorama.Fore.LIGHTGREEN_EX + "NECUNOSCUT" + colorama.Fore.RESET)
    elif num_safe == 0:
        print(colorama.Fore.RED + "FOARTE NESICUR" + colorama.Fore.RESET)
    else:
        print(colorama.Fore.RED + "NESIGUR" + colorama.Fore.RESET)
    print(colorama.Fore.MAGENTA + "-------------------------------------------------------" + colorama.Fore.RESET)
    
parser = argparse.ArgumentParser()
parser.add_argument("filepath", help="Calea fișierului pe care doriți să-l scanați.", type=check_file_exists)
args = parser.parse_args()
file_path = args.filepath

print("Calcularea hash-ului.", end="")
with open(file_path,"rb") as f:
    # bytes = f.read() # read entire file as bytes
    # file_hash = hashlib.sha256(bytes).hexdigest()
    file_hash = hashlib.md5()
    while chunk := f.read(8192):
        file_hash.update(chunk)
file_hash = file_hash.hexdigest()

with vt.Client(config.api_key) as client:
    try:
        print("\rSe verifică dacă fișierul este deja disponibil în VirusTotal DB.", end="")
        stats = client.get_object("/files/{}".format(file_hash)).last_analysis_stats
        print("\rFișierul este deja disponibil în baza de date a VirusTotal.         ")
    except vt.error.APIError as ex:
        if not ex.code == "NotFoundError":
            raise
        with open(file_path, "rb") as f:
            choice = input("\rFișierul nu este disponibil în VirusTotal DB. Doriți să încărcați? (Se pot aplica taxe de internet) (D/N)\n :: ")
            if choice.lower() in ["d", "yes"]:
                print(colorama.Fore.GREEN + "Acum se încarcă. ")
                analysis = client.scan_file(f)
                while True:
                    analysis = client.get_object("/analyses/{}".format(analysis.id))
                    print("\r" + colorama.Fore.MAGENTA +  "Starea curentă: " + colorama.Fore.RESET + analysis.status, end="")
                    if analysis.status == "completed":
                        break
                    time.sleep(10)
                stats = analysis.stats
            else:
                print("Operațiunea anulată. ")
                time.sleep(2)
                exit()

    print_result(stats, file_path)
    input("Apăsați enter pentru a ieși...")
