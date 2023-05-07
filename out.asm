;code generated by aframe.py

BITS 64
section .bss
    y resb 8
    z resb 8
    i resb 1
    x resb 2

section .data
    text db "Hello, World!",10

section .text
    global _start
    
_start:
    mov rax, [y]
    mov rbx, 1
    add rax, rbx
    mov [y], rax
    cmp qword [y], 10
    je _exit

    jmp _hello

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
    jmp _start