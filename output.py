# Just the print beauty
from colorama import init, Fore, Style
import os

def success(msg):
    print(Fore.LIGHTGREEN_EX + '[*] ' + Style.RESET_ALL + msg)
def warning(msg):
    print(Fore.LIGHTYELLOW_EX + '[!] ' + Style.RESET_ALL + msg)
def error(msg):
    print(Fore.LIGHTRED_EX + '[-] ' + Style.RESET_ALL + msg)
def info(msg):
    print(Fore.LIGHTCYAN_EX + '[-] ' + Style.RESET_ALL + msg)
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def banner():
    print("    ____              ____                    __")
    print("   / __ \   __  __   / __ \  __  __  _____   / /__")
    print("  / /_/ /  / / / /  / / / / / / / / / ___/  / //_/")
    print(" / ____/  / /_/ /  / /_/ / / /_/ / / /__   / ,<")
    print("/_/       \__, /  /_____/  \__,_/  \___/  /_/|_|")
    print("         /____/\n")
    print("  \x1B[3mby ThoughtfulDev | github.com/ThoughtfulDev\x1B[23m\n")
    print(" \x1B[3mGet your USB Rubber Ducky up and running faster\x1B[23m")
    print(Fore.WHITE + " \t\t  Version " + Fore.MAGENTA + "1.1.0\n")
