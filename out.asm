;code generated by aframe.py

BITS 64
section .data
    text db 72,101,108,108,111,44,32,87,111,114,108,100,33,10

section .bss
    x resb 8
    y resb 8
    z resb 8
    i resb 1

section .text
    global _start
    
_start:
    call _hello
    mov qword [x], 0
    mov qword [y], 1
    mov qword [z], 0

_loop:
    mov rax, [x]
    mov rbx, [y]
    add rax, rbx
    mov [x], rax
    mov qword rax, [x]
    mov qword [z], rax
    mov qword rax, [y]
    mov qword [x], rax
    mov qword rax, [z]
    mov qword [y], rax
    mov rax, [i]
    mov rbx, 1
    add rax, rbx
    mov [i], rax
    cmp byte [i], 5
    je _exit
    jmp _loop

_exit:
    mov rax, 60
    mov rdi, 0
    syscall

_hello:
    mov rax, 1
    mov rdi, 1
    mov rsi, text
    mov rdx, 14
    syscall
    ret