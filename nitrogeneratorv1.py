import os
from colorama import *
import string
import random
from time import *

list = list(string.ascii_letters + string.digits)


def Generator():
    codes = ""
    valid_url = random.randint(1, 1000)
    valid_test = -1
    while True:
        valid_test = random.randint(1, 1000)
        essay = int(input("Number of tests :"))
        for i in range(essay):
            codes=""
            sleep(0.2)
            for i in range(17):
                code = random.choice(list)
                codes += code
            url = "http://discord.gift/"+codes
            print(url)
        if valid_test == valid_url:
            print("gg")
            print(url)
            break
        

Generator()    
        
"""def Menu():
    choice = ""
    while choice not in ["1", "2", "3"]:
        print(Fore.WHITE+"["+Fore.CYAN+"1"+Fore.WHITE+"]"+Fore.CYAN+" Generator")
        print(Fore.WHITE+"["+Fore.CYAN+"2"+Fore.WHITE+"]"+Fore.CYAN+" Bank")
        print(Fore.WHITE+"["+Fore.CYAN+"3"+Fore.WHITE+"]"+Fore.CYAN+" Exit")
        choice = input()
        if choice == "1":
            print("")
            Generator()
        elif choice == "2":
            hit()
        elif choice == "3":
            break
        else:
            print(Fore.RED+"Error: your choice is not in the menu")
    
Generator()"""