# Warning
I am not working on this anymore, though I may rewrite Argo-Navis one day in C/C++ or Rust


# Argo-Navis
Small and completely useless interpreter written in python. This project isn't meant to write anything serious, just a fun little adventure for myself. I'm not that good at programming in python or in OOP so my code is hideous as well...

## Command flags


`python3 main.py [filename.an / -v(--version)]}`

## Features available
- Writing out to stdout using parentheses i.e. `"This will be output to stdout"`
- Basic variable definition with 2 types: **int and string**:

**Syntax**: 

`variable_name = variable : type` i.e. 

`number = 72:int`

`str = "Hello world":string`

**If a variable is already defined, you don't need to specify its type, rather, you shouldn't, as a different type will throw an error**.i.e.

`number = 72:int`
`number = 48`
`"{number}"`
-This will print out 48 to output. While it is allowed to write `number = 48: int` (it'll only throw a warning), writing something like `number = 48:string` will cause a panic

- Including variable printing in output using `{}` .i.e.

`number = 48: int`

`"the number is {number}"`



# How the interpreter works
- ### The interpreter is fairly rudimentary and has a few hard-coded features and there are some problems:
- print function is built into the base library
- Upon finding a variable, it is exported into a cache file (.argo_cache) and it is split up into a csv. 1 part containing the name, the other the content, and the last the variable itself **(Yes, this makes the language very unsafe as values can be changed at runtime)**
- Retrieval of a file is simple as the line just needs to be imported back in its 3 parts but is slow due to having to go through all of them without any kind of searching/sorting algorithm
- Reinitialisation of a variable is also slow as the whole file needs to be flushed and rewritten **(can't imagine how efficient this'll be with large projects)**
- The file names of the interpreter are really mixed up relative to their functions so they'll be refactored later
