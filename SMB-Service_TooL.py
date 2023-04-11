
import os


os.system("clear")
banner="""

██████╗ ██╗   ██╗ ██████╗ ███╗   ███╗███████╗██████╗ 
██╔══██╗╚██╗ ██╔╝██╔═══██╗████╗ ████║██╔════╝██╔══██╗
██████╔╝ ╚████╔╝ ██║   ██║██╔████╔██║█████╗  ██████╔╝
██╔══██╗  ╚██╔╝  ██║   ██║██║╚██╔╝██║██╔══╝  ██╔══██╗
██████╔╝   ██║   ╚██████╔╝██║ ╚═╝ ██║███████╗██║  ██║
╚═════╝    ╚═╝    ╚═════╝ ╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝

@1_omer.bck 
omerbocek1606@gmail.com
                                                     
"""


print(banner)

print("1 : SMB SERVİS TARAMASI \n2 : SMB Brute \n3 : Enum Shares \n4 : Enum Users")

lang = input("Yapmak İstediğiniz İşlemi Seçin : ")

match lang:
    case "1":
        ip_adres=input("Hedef İP : ")
        print("Yükleniyor...")
        os.system("nmap -sS -sV -p 139,445  {}".format(ip_adres))
    case "2":
        ip_adres=input("Hedef İP : ")
        print("Yükleniyor...")
        os.system("nmap --script smb-brute.nse -p 139,445 {}".format(ip_adres))
    case "3":
        print("http/https Olmadan!")
        url=input("Hedef URL : ")
        print("Yükleniyor...")
        os.system("enum4linux -M -S {}".format(url))
    case "4":
        print("http/https Olmadan!")
        url=input("Hedef URL : ")
        print("Yükleniyor...")
        os.system("enum4linux -M -U {}".format(url))
    case _:
        
        print("Boş Bırakamazsınız !")        




