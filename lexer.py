from useful_stuff import uo
#import fileinput


class lexer:
    
    def variable_name_verify(string, line):
        name = string.split("=")[0].strip()
        if not str(name).isalnum():
                if not str(name).replace("_","").isalnum():
                    uo.Error(f"in line {line}. Variable names cannot contain special characters, only an underscore (_)")
                    exit()
        try:
            name[0].isnum()
            if name[0].isnum():
                uo.Error("Start of a variable name cannot be an integer")
                exit()
        except Exception as e:
            pass
        if name in uo.reserved_keywords():
            uo.Error(f"in line {line}: Variable cannot contain reserved keyword \"{name}\"")
            exit()

    def variable_assign(string, line):
        fmt = str(string).split("=")
        fmt_name = fmt[0].strip()
        fmt_content = fmt[1].split(":")[0].strip()
        try:
            fmt_type = fmt[1].split(":")[1].strip()
        except:
            fmt_type = "inherit"
            
        fstr = open(".argo_cache", "r")
        for l in fstr:
            if l.isspace():
                pass
            #print(fmt_type == l.split(",")[2])
            elif fmt_name == l.split(",")[0] or fmt_name == l.split(",")[0] and fmt_type == "inherit":
                
                if(fmt[1].count(":") > 0):
                    print(f"{fmt_type} {l.split(',')[2]}")
                    if fmt_type == str(l.split(",")[2]).strip():
                        uo.Warning(f"in line {line}: type already defined in original variable")
                    elif fmt_type != l.split(",")[2]:
                        uo.Error(f"in line {line}: New variable defined with the name of an already existing variable but a different type")
                        exit()
                #print(f"{l.split(',')[1]} {fmt_content}")
                fstr.close()
                newline = l.replace(l.split(",")[1], str(fmt_content))
                with open(".argo_cache", "r+") as f:
                    lines = f.readlines()
                    f.seek(0)
                    for i in lines:
                        if i != l:
                            f.write(i)
                    f.truncate()
                    f.write(newline)
                    

                return ""
        
        if fmt_type == "inherit":
            uo.Error(f"in line {line}: No type defined for variable")
            exit()
        if string.find(":") == -1:
            uo.Error(f"No type defined for variable in line {line}")
            exit()
        if len(string.split(":")) > 2:
            uo.Error(f"Invalid syntax on line {line} regarding \":\"")
            exit()
        
        var_type = str(string).split(":")[1].strip()
        acceptable_types = ["string", "int"]
        if var_type not in acceptable_types:
            uo.Error(f"Variable type \"{var_type}\" doesn't exist")
            exit()
        
        variable = fmt[1].split(":")[0].strip()
        #print(variable.find("\""))
        if var_type == "string" and variable.count("\"")-variable.count('\\"') != 2 and variable.find("\"") == -1 or variable.rfind("\"") == 0:
            uo.Error(f"in line {line}: defined '{fmt_type}' as a string but there is incorrect usage of \"\" ") 
            exit()
        #elif var_type == "int" and not str(variable).isnumeric():
        #    uo.Error(f"in line {line}: defined `{fmt_type}` as an integer but doesn't exclusively contain numbers")
        #    exit()
        
            
        
        #print(var_type)
        __temp = str(string).split("=")
        var_name = __temp[0].strip()
        variable = __temp[1].split(":")[0].strip()
        try:
            if var_type == "int":
                variable = eval(variable)
        except:
            uo.Error(f"in line {line}: is defined as an integer but doesn't exclusively contain numbers or is an arithmetic operation")
            exit()
        
        csv_exp = f"{var_name},{variable},{var_type}"

        fstr = open(".argo_cache", "a")
        fstr.write(f"{csv_exp}\n")
        fstr.close()
    
    def parenth_ops(string, line):
        if string.count("\"") == 2:
            pass
        if string.find("\"") > 0:
            uo.Error("invalid left hand assignment") 
            exit()
          
