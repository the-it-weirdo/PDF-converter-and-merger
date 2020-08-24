from colorama import *

init(autoreset=True)

class TerminalOutput:

    def warn(self, text):
        print(f"{Fore.MAGENTA}{text}")

    def error(self, text):
        print(f"{Fore.RED}{text}")

    def success(self, text):
        print(f"{Fore.GREEN}{text}")

    def info(self, text):
        print(f"{Fore.BLUE}{text}")