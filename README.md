# How To Use
Download `bf2c.py`, create a python script called whatever,
import `bf2c.py` in your python script
```py
import bf2c
```
and transpile your code using the `transpile` function:
```py
bf2c.transpile("brainfuck code here")
```
bf2c exports into `main.c`, if you have a c script you don't want to be replaced, remember to change its name.
# Transpile a file
You can easily take a bf file `main.bf` and transpile it into a c file using the script below
```py
import bf2c
with open("main.bf", "r") as f:
	bf2c.transpile(f.read())
```
