# About
bf2c-py is a python module that was poorly written by Nurdle (me).
It outputs C code and optionally C files, it tries to maintain comments (still looks a little messy) and has some very useless attempts at optimization
# How To Use
Download `bf2c.py`, create a python script called whatever,
import `bf2c.py` in your python script
```py
import bf2c
```
### transpile(`code: str`, `output: str = ""`)
+ `file` - the brainfuck code to transpile<br>
+ `output` - the name of the c file to output to (leave blank to just return string)
### transpile_f(`file: str`, `output: str = ""`)
+ `file` - the name of the brainfuck file to transpile<br>
+ `output` - the name of the c file to output to (leave blank to just return string)
# Example scripts
take a bf file `main.bf` and export a C file `main.c`
```py
import bf2c

bf2c.transpile("main.bf", "main.c")
```
