from useful_stuff import uo
class base_lib:

    def stdout(f):
        while f.find("{") != -1 and f.find ("}") != -1:   #interpolate into curly braces to replace with variables
            var_name = "".join(f[f.find("{")+1:f.find("}")]) # find the variable name
            argo_cache = open(".argo_cache", "r") 
            string_retrieved = ""
            var_ret = False

            for l in argo_cache:
                var = l.split(",")[0].strip()# interpolate through variable names
                if var_name == var:
                    type_var = ""
                    if "\"" in l:
                        type_var = l.split("\"",2)[2].replace(",","")
                        #print(type_var)
                    #else:
                    #    type_var = l.split(",")[3]
                    #    print(type_var)
                        string_retrieved = str(l).split(",",1)[1].replace(f",{type_var}","")
                    else:
                        string_retrieved = str(l).split(",")[1]
                    #print(string_retrieved)
                    var_ret = True

            if var_ret == False:
                uo.Error(f"\"{var_name}\" isn't a valid variable name")
            #print(f)
            f = f.replace((f[f.find("{"):f.find("}")+1]), string_retrieved) 
            var_ret = False    
        print(f.replace('"', ''))
    def arithmetic(f):
        eval(f) #how convenient