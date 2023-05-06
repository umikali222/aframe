'''
Yes, I know this code is probably the worst code that you've seen in your entire life.

'''

from sys import argv
from os import _exit, system

instructions = ('mov', 'add', 'sub', 'syscall')
registers = ['rax', 'rbx', 'rcx', 'rdx', 'cs', 'ds', 'ss', 'es', 'fs', 'gs', 'rbp', 'rsp', 'rsi', 'rdi', 'rip', 'rflags']

try:
    f = open(argv[1], 'r')
except FileNotFoundError:
    print('ERROR!\nFile not found')
    _exit()
except IndexError:
    print('ERROR!\nFile not specified')
    _exit()

def getSectionBss(asm: str):
    sections = asm.split('section ')
    bss = ""
    for i in sections:
        if i.split("\n")[0] == '.bss':
            bss = i
            break
    if bss == "":
        return bss
    bss = bss.replace('\t', '')
    bss = bss.replace('    ', '')
    bss = bss.replace('.bss\n', '')
    bss = bss.replace('\n\n', '')
    return bss

def instructionConvert(instruction:str):
    instruction = instruction.replace(',', '')
    split = instruction.split(' ')
    if split[0] == 'syscall':
        return 'syscall'
    elif split[0] == 'mov':
        out = 'mov '
        if split[1] in registers or split[2] in registers:
            if split[1] in variables:
                out += '[' + split[1] + ']'
            else:
                out += split[1]
            out += ', '
            if split[2] in variables:
                out += '[' + split[2] + ']'
            else:
                out += split[2]
        elif split[1] in variables and split[2] in variables:
            if variableSize[split[1]] == variableSize[split[2]]:
                out += variableSize[split[1]] + ' ' + split[1]
                out += ', ' + split[2]
        else:
            out += variableSize[split[1]] + ' [' 
            out += split[1] + ']' + ', ' + split[2]
        return out
    elif split[0] == 'add':
        out = '''mov rax, [xddddddddddd]
    mov rbx, [lolthisisnumber1]
    add rax, rbx
    mov [xddddddddddd], rax'''
        out = out.replace('xddddddddddd', split[1])
        out = out.replace('lolthisisnumber1', split[2])
        return out
    elif split[0] == 'sub':
        out = '''mov rax, [xddddddddddd]
    mov rbx, [lolthisisnumber1]
    sub rax, rbx
    mov [xddddddddddd], rax'''
        out = out.replace('xddddddddddd', split[1])
        out = out.replace('lolthisisnumber1', split[2])
        return out

def getAllInstructions(asm: str):
    asmc = asm.replace('    ', '')
    asmc = asmc.replace('\t', '')
    lines = asmc.split('\n')
    asmIns = []
    for i in lines:
        if i.split(' ')[0] in instructions:
            asmIns.append(i)
    newinstructions = []
    for i in asmIns:
        newinstructions.append(instructionConvert(i))
    for i in range(len(asmIns)):
        asm = asm.replace(asmIns[i], newinstructions[i])
    return asm

code = f.read()
f.close()

code = code.replace('_start:', """section .text
    global _start
    
_start:""")

variableSize = dict()
variables = []

bss = getSectionBss(code)
if bss != "":
    bss = bss.replace('\n', ' ')
    temp = bss.split(' ')

    i = 0
    while i < len(temp):
        variables.append(temp[i])
        variableSize[temp[i]] = temp[i + 1]
        i += 2

code = ';code generated by fasm.py\n\nBITS 64\n' + code

code = code.replace('qword', 'resb 8')
code = code.replace('dword', 'resb 4')
code = code.replace('word', 'resb 2')
code = code.replace('byte', 'resb 1')
             
code = getAllInstructions(code)

system('rm -f out.asm; touch out.asm')
f = open('out.asm', 'w')
f.write(code)
