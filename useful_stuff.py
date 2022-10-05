
import platform



os_name = platform.uname().system
if os_name == "Windows":
    try:
        from colorama import Fore, Style
        import colorama
    except:
        print("Error: couldn't import module colorama, try installing it from PyPi")
#print(os_name == "Windows")
class uo:

    #def Error(text):
    #   print(f"\033[31mError: \033[0m {text}")
    def Error(text):# handles the error message
        if os_name == "Windows":
            colorama.init() # has to have this to work on Windwos
            print(Fore.RED+f"Error: " + Fore.WHITE + f"{text}")
            print(Style.RESET_ALL)
        else:
            print(f"\033[31mError: \033[0m {text}") # *nix Operating systems allow printing out to terminal colour directly, but not windows, so for now i'll use the module colorama

    def Warning(Text): # Handles the warning message, similar to error message
        print(Fore.RED+f"Warning {text}")
        print(Style.RESET_ALL)
    #def Warning(text):
    #    print(f"\033[35mWarning: \033[0m {text}")
    def Version():
        return "0.0.1 indev"
    def reserved_keywords():
        return ["string","int","array","bool","cint","cstring","carray","cbool","for","func"]
        # only string and int are implemented as of now