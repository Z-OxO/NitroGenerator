import os
import colorama
import string
import random
from time import *

list = list(string.ascii_letters + string.digits)


def generator():
    codes = ""
    valid_url = random.randint(1, 1000)
    valid_test = -1
    while True:
        sleep(0.3)
        codes = ""
        valid_test = random.randint(1, 1000)
        for i in range(17):
            code = random.choice(list)
            codes += code
        url = "http://discord.gift/"+codes
        print(url)
        if valid_test == valid_url:
            print("gg")
            print(url)
            break


generator()
