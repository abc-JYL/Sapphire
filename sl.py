# Sapphire programming language interpreter version 0.0.1

from var import write, read
from stdio import slin, slout
from loop import loop
from operations import add, sub, mul, div
from include import include
from sl_if import slif, slelse
import sys

code_list = []

def execute(code):
    code_list.append(code)
    try:
        argv = str(code).split()
        if len(argv) < 1:
            pass
        elif argv[0] == "write":
            content = ""
            for i in argv[2:]:
                content = content + i + " "
            write(argv[1], content)
        elif argv[0] == "read":
            print(read(argv[1]))
        elif argv[0] == "display":
            content = ""
            for i in argv[1:]:
                content = content + i + " "
            slout(content)
        elif argv[0] == "input":
            slin(argv[1])
        elif argv[0] == "loop":
            content = ""
            for i in argv[2:]:
                content = content + i + " "
            for i in loop(argv[1], content):
                execute(i)
        elif argv[0] == "add":
            add(argv[1], float(argv[2]), float(argv[3]))
        elif argv[0] == "sub":
            sub(argv[1], float(argv[2]), float(argv[3]))
        elif argv[0] == "mul":
            mul(argv[1], float(argv[2]), float(argv[3]))
        elif argv[0] == "div":
            div(argv[1], float(argv[2]), float(argv[3]))
        elif argv[0] == "include":
            for i in include(argv[1]):
                execute(i)
        elif argv[0] == "if":
            if slif(read(argv[1]), argv[2], read(argv[3])):
                content = ""
                for i in argv[4:]:
                    content = content + i + " "
                execute(content)
        elif argv[0] == "else":
            if slelse(code_list[-1]):
                content = ""
                for i in argv[1:]:
                    content = content + i + " "
                execute(content)
        else:
            print(f"Syntax Error: '{code}'")
    except Exception as e: print(e)

if len(sys.argv) < 2:
    while True:
        execute(input(">>> "))

filename = sys.argv[1]

with open(filename, "r") as file:
    for i in file:
        if i.startswith("#"):
            pass
        else:
            execute(i)
