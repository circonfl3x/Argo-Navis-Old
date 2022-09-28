try:
    from colorama import Fore, Style
except:
    print("Error: cannot import module 'colorama'")
import platform
os_name = platform.uname().system
class uo:

    #def Error(text):
    #   print(f"\033[31mError: \033[0m {text}")
    def Error(text):
        if os_name != "Windows":
            print(f"\033[31mError: \033[0m {text}")
        else:
            print(Fore.RED+f"Error: " + Fore.WHITE + f"{text}")
            print(Style.RESET_ALL)
    def Warning(Text):
        print(Fore.RED+f"Warning {text}")
        print(Style.RESET_ALL)
    #def Warning(text):
    #    print(f"\033[35mWarning: \033[0m {text}")
    def Version():
        return "0.0.1 indev"
    def reserved_keywords():
        return ["string","int","array","bool","cint","cstring","carray","cbool","for","func"]