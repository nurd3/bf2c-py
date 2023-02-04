# horrible code made by the amazing me (Nurdle)
# completely open for free use

def transpile_f(src, output = "") -> str:
	'''
 	Transpiles brainfuck code from file path
  	
 	:param src: The brainfuck file you wish to transpile
  	:type src: str
  	:param output: The name of the exported C file (leave blank if you don't want it to make a C file)
   	:type output: str or None
 	'''
	with open(src, "r") as f:
		return transpile(f.read(), output)

def transpile(code, output = "") -> str:
	'''
 	Transpiles brainfuck code from string
  	
 	:param code: The brainfuck code you wish to transpile
  	:type code: str
  	:param output: The name of the exported C file (leave blank if you don't want it to make a C file)
   	:type output: str or None
 	'''
	tokens = [
		"+",
		"-",
		">",
		"<",
		"[",
		"]",
		",",
		"."
	]
	comment = ""
	script = []
	for i in code:
		if i in tokens:
			if comment != "":
				script.append(comment.replace("*/", "*\/").replace("\n", " "))
				comment = ""
			script.append(i)
		elif comment != "" and i == "\n":
			script.append(comment.replace("*/", "*\/").replace("\n", " "))
			comment = ""
		else:
			comment += i
	i = 0
	out = "char t[30000] = {0}; char *p = t;\nint main() {\n"
	balance = 1
	while i < len(script):
		x = script[i]
		tabs = "\t" * balance
		out += tabs
		if x in tokens:
			if x == "+":
				y = 0
				while i < len(script) and script[i] == "+":
					i += 1
					y += 1
				if y == 1: out += "++*p;\n"
				else: out += "*p += {0};\n".format(y)
				continue
			elif x == "-":
				y = 0
				while i < len(script) and script[i] == "-":
					i += 1
					y += 1
				if y == 1: out += "--*p;\n"
				else: out += "*p -= {0};\n".format(y)
				continue
			elif x == ">":
				y = 0
				while i < len(script) and script[i] == ">":
					i += 1
					y += 1
				if y == 1: out += "++p;\n"
				else: out += "p += {0};\n".format(y)
				continue
			elif x == "<":
				y = 0
				while i < len(script) and script[i] == "<":
					i += 1
					y += 1
				if y == 1: out += "--p;\n"
				else: out += "p -= {0};\n".format(y)
				continue
				
			elif x == "[":
				out += "while (*p) {\n"
				balance += 1
			elif x == "]":
				out = out[:-1]
				out += "}\n"
				balance -= 1
			elif x == ".":
				out += "putchar(*p);\n"
			elif x == ",":
				out += "*p = getchar();\n"
		else:
			out += "/* {0} */\n".format(x)
		i += 1
	if balance != 1:
		print("err: unmatched square bracket")
		return None
	out += "\treturn 0;\n}"
	if output != "": 
		with open(output, "w") as f:
			f.write(out)
	return out
