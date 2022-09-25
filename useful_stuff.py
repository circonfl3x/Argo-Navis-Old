
class uo:
    def Error(text):
        print(f"\033[31mError: \033[0m {text}")
    def Warning(text):
        print(f"\033[35mWarning: \033[0m {text}")
    def Version():
        return "0.0.1 indev"
    def reserved_keywords():
        return ["string","int","array","bool","cint","cstring","carray","cbool","for","func"]