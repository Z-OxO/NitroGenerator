import os
from colorama import *
import string
import random
from time import *
from banner import *

codes_list = list(string.ascii_letters + string.digits)
Fore.RESET


def Generator():
    for i in range(1, 9):
        loading(banner_generator1, banner_generator2, banner_generator3)
    Fore.RESET
    valid_url = random.randint(1, 100)
    valid_test = -1
    while True:
        #reset codes variable
        codes=""
        essay = input("Number of tests (type end if you want to exit):")
        if essay == "end":
            Menu()
        if not essay.isdigit() or int(essay) < 1:
            print("Invalid input")
            continue
        for i in range(int(essay)):
            codes=""
            sleep(0.1)
            valid_test = random.randint(1, 100)
            #codes generation
            for i in range(17):
                code = random.choice(codes_list)
                codes += code
            url = "http://discord.gift/"+codes
            print(Fore.CYAN+"| "+Fore.RED+url+Fore.CYAN+" |")
            if valid_test == valid_url:
                print(Fore.GREEN+"| "+url+" |")
                file = os.path.join("hit.txt")
                with open(file, "a+") as file_hit:
                    file_hit.write("\n--->  "+url)
                    Fore.RESET

        
def Menu():
    print(Fore.MAGENTA+banner_main)
    choice = ""
    while choice not in ["1", "2", "3"]:
        print(Fore.WHITE+"["+Fore.CYAN+"1"+Fore.WHITE+"]"+Fore.CYAN+" Generator")
        print(Fore.WHITE+"["+Fore.CYAN+"2"+Fore.WHITE+"]"+Fore.CYAN+" hit")
        print(Fore.WHITE+"["+Fore.CYAN+"3"+Fore.WHITE+"]"+Fore.CYAN+" Exit")
        choice = input()
        if choice == "1":
            print("")
            Generator()
        elif choice == "2":
            Hit()
        elif choice == "3":
            SystemExit
        else:
            print(Fore.RED+"Error: your choice is not in the menu")
  
  
def Hit():
    file = os.path.join("hit.txt")
    with open(file, "r") as file_hit:
        hit = file_hit.read()
        print(hit)
    hit_choice = input("Return Menu : (Y) ")
    while hit_choice not in ["Y","Yes","yes","y"]:
        hit_choice = input("Return Menu ? (Y) ")
    Fore.RESET
    Menu()
  
  
def main():
    filename = os.path.join("hit.txt")
    if not os.path.exists(filename):
        with open(filename, "w") as fichier:
            fichier.write("You can see your hit here :")
    Menu()
            

main()