;hand-tlanslated assembly

BITS 64
section .bss
    text resb 4
    y resb 8
    z resb 8
    i resb 1
    x resb 2

section .text
    global _start

_start:
    mov qword [y], 9
    mov qword [z], 10
    mov word [x], 21

    mov rax, [y]
    mov rbx, [x]
    add rax, rbx
    mov [y], rax

    mov rax, 60
    mov rdi, 0
    syscall