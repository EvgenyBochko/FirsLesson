from termcolor import cprint

colors = ["red", "yellow","green", "blue", "cyan" , "magenta"]
text = "Hello world!"
for i in range(len(text)):
    letter = text[i]
    color = colors[i%len(colors)]
    cprint(letter, color, end = "")
print()