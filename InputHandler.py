from Utilities import *

output = TerminalOutput()

class InputHandler:


    def menu(self, options:list):
        print("\n\nChoose option: ")
        for idx, option in enumerate(options):
            print(f"{idx+1}: {option}")
        choosen = False
        while not choosen:
            choice = input("Enter your choice: ")
            if not choice.isnumeric():
                output.error("Invalid choice.")
            else:
                choice = int(choice)
                if choice < 1 or choice > len(options):
                    output.error("Invalid choice.")
                else:
                    choosen = options[choice-1]
        return choosen

    def select_files(self, files:list):
        print("Choose files: (Enter 'A' for all.) ")
        for idx, f in enumerate(files):
            print(f"{idx+1}: {f}")
        choosen_files = []
        while not choosen_files:
            choice = input('Enter your choice: ')
            if choice.upper() == 'A':
                choosen_files = files
            else:
                try:
                    choice = list(map(int, choice.split(',')))
                    for c in choice:
                        if c < 1 or c > len(files):
                            raise Exception(f"Invalid index: {c}")
                    choosen_files = [files[c-1] for c in choice]
                except Exception as e:
                    output.error(f"Invalid input. {e}")
        return choosen_files

    # def input_path(self, prompt: str):
    #     path = input(prompt)
