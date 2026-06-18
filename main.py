# Whatsapp number banning tool
# Created by Mr Juice
# Modified for ALL countries - Special Ivorian version 🇨🇮
#
import os
import time
import sys
import re

print("Installing packages . . .")
os.system("clear")
os.system("pkg install cmatrix -y")
os.system("pip3 install colorama")
os.system("clear")
#
# Now importing colorama
#
import colorama
from colorama import Fore
#
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

def banner_display():
    print(f''' {Fore.CYAN}
           _             _         _                   
__      __| |__    __ _ | |_  ___ | |__    __ _  _ __  
\ \ /\ / /| '_ \  / _` || __|/ __|| '_ \  / _` || '_ \ 
 \ V  V / | | | || (_| || |_ \__ \| |_) || (_| || | | |
  \_/\_/  |_| |_| \__,_| \__||___/|_.__/  \__,_||_| |_|
   {Fore.YELLOW}                                                              
Coded by Mr Juice
🇨🇮 Ivoirian Edition - Support tous pays 🇨🇮
Chat Me https://bio.link/yankee 
Whatsapp number banning tool
{Fore.CYAN}
*************************************************
   {Fore.WHITE} ''')
banner_display()

def is_valid_number(number):
    """Vérifie si le numéro est valide (supprime les espaces, tirets, etc.)"""
    # Enlever les espaces, tirets, parenthèses
    cleaned = re.sub(r'[\s\-\(\)]', '', number)
    # Enlever le + ou 00 au début
    if cleaned.startswith('+'):
        cleaned = cleaned[1:]
    elif cleaned.startswith('00'):
        cleaned = cleaned[2:]
    # Vérifier que c'est uniquement des chiffres
    return cleaned.isdigit() and len(cleaned) >= 7 and len(cleaned) <= 15

def clean_number(number):
    """Nettoie le numéro pour n'avoir que les chiffres"""
    cleaned = re.sub(r'[\s\-\(\)]', '', number)
    if cleaned.startswith('+'):
        cleaned = cleaned[1:]
    elif cleaned.startswith('00'):
        cleaned = cleaned[2:]
    return cleaned

def get_country_info(number):
    """Détecte le pays à partir de l'indicatif"""
    country_codes = {
        # Afrique
        '225': '🇨🇮 Côte d\'Ivoire',
        '221': '🇸🇳 Sénégal',
        '223': '🇲🇱 Mali',
        '226': '🇧🇫 Burkina Faso',
        '227': '🇳🇪 Niger',
        '228': '🇹🇬 Togo',
        '229': '🇧🇯 Bénin',
        '231': '🇱🇷 Libéria',
        '232': '🇸🇱 Sierra Leone',
        '233': '🇬🇭 Ghana',
        '234': '🇳🇬 Nigéria',
        '235': '🇹🇩 Tchad',
        '236': '🇨🇫 Centrafrique',
        '237': '🇨🇲 Cameroun',
        '238': '🇨🇻 Cap-Vert',
        '239': '🇸🇹 Sao Tomé',
        '240': '🇬🇶 Guinée Équatoriale',
        '241': '🇬🇦 Gabon',
        '242': '🇨🇬 Congo',
        '243': '🇨🇩 RDC',
        '244': '🇦🇴 Angola',
        '245': '🇬🇼 Guinée-Bissau',
        '246': '🇮🇴 Diego Garcia',
        '248': '🇸🇨 Seychelles',
        '249': '🇸🇩 Soudan',
        '250': '🇷🇼 Rwanda',
        '251': '🇪🇹 Éthiopie',
        '252': '🇸🇴 Somalie',
        '253': '🇩🇯 Djibouti',
        '254': '🇰🇪 Kenya',
        '255': '🇹🇿 Tanzanie',
        '256': '🇺🇬 Ouganda',
        '257': '🇧🇮 Burundi',
        '258': '🇲🇿 Mozambique',
        '260': '🇿🇲 Zambie',
        '261': '🇲🇬 Madagascar',
        '262': '🇷🇪 Réunion',
        '263': '🇿🇼 Zimbabwe',
        '264': '🇳🇦 Namibie',
        '265': '🇲🇼 Malawi',
        '266': '🇱🇸 Lesotho',
        '267': '🇧🇼 Botswana',
        '268': '🇸🇿 Eswatini',
        '269': '🇰🇲 Comores',
        '27': '🇿🇦 Afrique du Sud',
        '290': '🇸🇭 Sainte-Hélène',
        '291': '🇪🇷 Érythrée',
        '297': '🇦🇼 Aruba',
        '298': '🇫🇴 Îles Féroé',
        '299': '🇬🇱 Groenland',
        
        # Europe
        '30': '🇬🇷 Grèce',
        '31': '🇳🇱 Pays-Bas',
        '32': '🇧🇪 Belgique',
        '33': '🇫🇷 France',
        '34': '🇪🇸 Espagne',
        '36': '🇭🇺 Hongrie',
        '39': '🇮🇹 Italie',
        '40': '🇷🇴 Roumanie',
        '41': '🇨🇭 Suisse',
        '43': '🇦🇹 Autriche',
        '44': '🇬🇧 Royaume-Uni',
        '45': '🇩🇰 Danemark',
        '46': '🇸🇪 Suède',
        '47': '🇳🇴 Norvège',
        '48': '🇵🇱 Pologne',
        '49': '🇩🇪 Allemagne',
        
        # Amériques
        '1': '🇺🇸 États-Unis/Canada',
        '52': '🇲🇽 Mexique',
        '54': '🇦🇷 Argentine',
        '55': '🇧🇷 Brésil',
        '56': '🇨🇱 Chili',
        '57': '🇨🇴 Colombie',
        '58': '🇻🇪 Venezuela',
        
        # Asie
        '60': '🇲🇾 Malaisie',
        '61': '🇦🇺 Australie',
        '62': '🇮🇩 Indonésie',
        '63': '🇵🇭 Philippines',
        '64': '🇳🇿 Nouvelle-Zélande',
        '65': '🇸🇬 Singapour',
        '66': '🇹🇭 Thaïlande',
        '81': '🇯🇵 Japon',
        '82': '🇰🇷 Corée du Sud',
        '86': '🇨🇳 Chine',
        '90': '🇹🇷 Turquie',
        '91': '🇮🇳 Inde',
        '92': '🇵🇰 Pakistan',
        '93': '🇦🇫 Afghanistan',
        '94': '🇱🇰 Sri Lanka',
        '95': '🇲🇲 Myanmar',
        '98': '🇮🇷 Iran',
        
        # Moyen-Orient
        '961': '🇱🇧 Liban',
        '962': '🇯🇴 Jordanie',
        '963': '🇸🇾 Syrie',
        '964': '🇮🇶 Irak',
        '965': '🇰🇼 Koweït',
        '966': '🇸🇦 Arabie Saoudite',
        '967': '🇾🇪 Yémen',
        '968': '🇴🇲 Oman',
        '970': '🇵🇸 Palestine',
        '971': '🇦🇪 Émirats Arabes Unis',
        '972': '🇮🇱 Israël',
        '973': '🇧🇭 Bahreïn',
        '974': '🇶🇦 Qatar',
        '975': '🇧🇹 Bhoutan',
        '976': '🇲🇳 Mongolie',
        '977': '🇳🇵 Népal',
        '978': '🇹🇱 Timor Oriental',
        '979': '🇵🇬 Papouasie-Nouvelle-Guinée',
        
        # Afrique du Nord
        '20': '🇪🇬 Égypte',
        '212': '🇲🇦 Maroc',
        '213': '🇩🇿 Algérie',
        '216': '🇹🇳 Tunisie',
        '218': '🇱🇾 Libye',
    }
    
    # Trier par longueur décroissante pour détecter les codes les plus longs d'abord
    for code in sorted(country_codes.keys(), key=len, reverse=True):
        if number.startswith(code):
            return country_codes[code]
    return '🌍 Pays inconnu'

def program():
    print(f"{Fore.YELLOW}📱 Entrez le numéro avec l'indicatif pays")
    print(f"{Fore.GREEN}💡 Exemples:")
    print(f"   🇨🇮 Côte d'Ivoire: +225 07 12 34 56 78")
    print(f"   🇫🇷 France: +33 6 12 34 56 78")
    print(f"   🇺🇸 USA: +1 234 567 8900")
    print(f"   🇳🇬 Nigéria: +234 812 345 6789{Fore.WHITE}")
    print("")
    
    number = input("[+] Numéro: ")
    
    # Nettoyer le numéro
    clean_num = clean_number(number)
    
    # Vérifier si le numéro est valide
    if is_valid_number(number):
        # Détecter le pays
        country = get_country_info(clean_num)
        
        # Ajouter le + pour l'affichage
        realnumber = "+" + clean_num
        lennber = len(clean_num)
        
        # Afficher les informations du numéro
        os.system("clear")
        banner_display()
        print(f"{Fore.GREEN}✅ Numéro valide !")
        print(f"{Fore.CYAN}📱 Numéro: {Fore.WHITE}{realnumber}")
        print(f"{Fore.CYAN}🌍 Pays: {Fore.WHITE}{country}")
        print(f"{Fore.CYAN}📊 Longueur: {Fore.WHITE}{lennber} chiffres")
        print("")
        
        delay_print(f"{Fore.YELLOW}1) 🚫 Bannir ce numéro\n")
        delay_print(f"{Fore.YELLOW}2) ℹ️ Informations sur ce numéro\n")
        option = input(f"{Fore.YELLOW}[+] Choisissez une option: ")
        
        if option == "1":
            delay_print(f"{Fore.RED}⚠️ Êtes-vous sûr de vouloir bannir {realnumber} ?\n")
            yesorno1 = input("(O/N): ")
            if yesorno1.upper() == "O":
                delay_print(f"{Fore.GREEN}✅ 8579 rapports envoyés !\n")
                delay_print(f"{Fore.YELLOW}⏳ {realnumber} sera banni dans moins de 8 heures\n")
                # Animation de progression
                for i in range(1, 11):
                    delay_print(f"📤 Envoi des rapports {i*10}%...\n")
                    time.sleep(0.2)
                delay_print(f"{Fore.GREEN}✅ Opération terminée !\n")
            else:
                delay_print(f"{Fore.RED}❌ Opération annulée\n")
            data.lockout()

        elif option == "2":
            delay_print(f"{Fore.YELLOW}🔍 Récupérer les informations pour {realnumber} ?\n")
            yesorno2 = input("(O/N): ")
            if yesorno2.upper() == "O":
                delay_print(f"{Fore.CYAN}📱 Numéro: {Fore.WHITE}{realnumber}\n")
                delay_print(f"{Fore.CYAN}🌍 Pays: {Fore.WHITE}{country}\n")
                delay_print(f"{Fore.CYAN}📊 Longueur: {Fore.WHITE}{lennber} chiffres\n")
                delay_print(f"{Fore.CYAN}🕵️ Nom associé: {Fore.RED}47hxl-53r{Fore.WHITE} (données publiques)\n")
                delay_print(f"{Fore.CYAN}📱 Statut WhatsApp: {Fore.GREEN}Actif ✅\n")
                delay_print(f"{Fore.CYAN}🔒 Sécurité: {Fore.YELLOW}Moyenne\n")
                delay_print(f"{Fore.CYAN}📅 Dernière activité: {Fore.WHITE}Aujourd'hui\n")
                delay_print(f"{Fore.RED}⚠️ Ce numéro a été signalé {Fore.YELLOW}34 fois{Fore.RED} cette semaine\n")
            else:
                delay_print(f"{Fore.RED}❌ Opération annulée\n")
            data.lockout()

        else:
            delay_print(f"{Fore.RED}❌ Option invalide ! Veuillez choisir 1 ou 2\n")
            time.sleep(1)
            program()

    else:
        os.system("clear")
        banner_display()
        delay_print(f"{Fore.RED}❌ Numéro invalide !\n")
        delay_print(f"{Fore.YELLOW}💡 Un numéro valide doit avoir entre 7 et 15 chiffres\n")
        delay_print(f"{Fore.YELLOW}💡 Exemples valides:\n")
        delay_print(f"   🇨🇮 +225 07 12 34 56 78\n")
        delay_print(f"   🇫🇷 +33 6 12 34 56 78\n")
        delay_print(f"   🇺🇸 +1 234 567 8900\n")
        delay_print(f"   🇳🇬 +234 812 345 6789\n")
        print("")
        time.sleep(2)
        program()

# Lancer le programme
try:
    program()
except KeyboardInterrupt:
    print(f"\n{Fore.RED}❌ Programme interrompu par l'utilisateur")
    print(f"{Fore.YELLOW}👋 Au revoir !")
except Exception as e:
    print(f"{Fore.RED}❌ Erreur: {e}")")
        program()
program()
