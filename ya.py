import time
import urllib.request as urlopen
import os

logo = """
\033[1;32m
\033[31m╔╗ ╦╔═╗╦ ╦╔═╗╔═╗╦ ╦\033[0m
\033[31m╠╩╗║╚═╗╠═╣║╣ ╚═╗╠═╣\033[0m
\033[37m╚═╝╩╚═╝╩ ╩╚═╝╚═╝╩ ╩\033[0m 

\033[1;32m-------------------------------------------------------- 
 Owner : Betryal Bishesh 
 Facebook : bisheshxd
 Tool Type : Facebook Cloning (Premium)
 Network : All Network
 Version : 5.7
\033[1;32m--------------------------------------------------------
"""

def linex():
    print('\033[93;1m════════════════════════════════════════════════════════') 

def clear():
    os.system('clear')

def subscription():
    key1 = open('/data/data/com.termux/files/usr/bin/.mrBALOCH -cov', 'r').read()
    modified_key = "BISHESH-" + key1

    os.system('clear')
    print(logo)

    r1 = str(urlopen("https://github.com/GodBishesh/tool-approval/blob/main/approvalSheet.txt").read())
    if modified_key in r1:
        os.system('clear')
        print(logo)
    else:
        os.system("clear")
        print(logo)
        print("\t \033[1;32m Please Get Approval First !!!! \033[1;37m ")
        time.sleep(1)
        os.system("clear")
        print(logo)
        print("")
        print(" \033[1;32m BETRAYAL BISHESH'S UNLIMITED ACCOUNT MAKER \033[1;37m\n")
        print(" \033[1;32m Note: THIS IS A PAID TOOL! & DON'T EMBRASS N WASTE MY TIME ASKING IT FOR FREE \033[1;37m")
        print("")
        print(" [ Mode of Payment: GCASH ] ")
        print("")
        print(" Your key is not Approved. ")
        print("")
        print(" Copy and Send Key To Alexander Grayson")
        print("")
        print(" Your Key: " + modified_key)
        print("")
        name = input(" Your Name: ")
        print("")
        lol = input(" Your Email: ")
        print("")
        user_input = input(" Press Enter To Send Key")
        time.sleep(3.5)
        tks = 'Dear Admin, Please Approved My Key To Premium Thank You ' + lol + ' My Name: ' + name + ' My Key: ' + modified_key
        os.system('am start https://m.me/AlexanderGraysonRecovery.IAmLimitless ' + tks)

subscription()
