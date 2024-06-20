import os
import shutil

def clear_terminal():
    # Clear command for Windows
    if os.name == 'nt':
        os.system('cls')
    # Clear command for Unix/Linux/MacOS
    else:
        try:
            _, columns = shutil.get_terminal_size()
            print("\n" * (columns if columns else 100))
        except Exception as e:
            print(e)
            os.system('clear')