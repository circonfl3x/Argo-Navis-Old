from useful_stuff import uo
class base_lib:

    def stdout(f):
        while f.find("{") != -1 and f.find ("}") != -1:   
            var_name = "".join(f[f.find("{")+1:f.find("}")])
            argo_cache = open(".argo_cache", "r")
            string_retrieved = ""
            var_ret = False

            for l in argo_cache:
                var = l.split(",")[0].strip()
                if var_name == var:
                    string_retrieved = str(l).split(",")[1].strip()
                    var_ret = True

            if var_ret == False:
                uo.Error(f"\"{var_name}\" isn't a valid variable name")
                    
            f = f.replace((f[f.find("{"):f.find("}")+1]), string_retrieved)
            var_ret = False    
        print(f.replace('"', ''))
    def arithmetic(f):
        eval(f)