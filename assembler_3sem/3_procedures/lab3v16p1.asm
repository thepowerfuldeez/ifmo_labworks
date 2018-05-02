;variant 16

.MODEL	small

STACK SEGMENT PARA STACK 'stack' 
 	DB 100h DUP(?)
STACK ENDS

DATA SEGMENT PARA PUBLIC 'data'
	num	DD 00000000h
	text DB	"1A", 0
	
DATA ENDS

CODE SEGMENT PARA PUBLIC 'code'
	ASSUME CS: CODE, DS: DATA, SS: STACK

.486

getLenght	PROC NEAR

		xor	cx, cx
		CLD
for1:	
		lodsb
		cmp al, 0
		jz	goout
		inc cx
		jmp for1
goout:
		ret
			
getLenght	ENDP

check	PROC NEAR
			PUSHA
			CLD
			MOV BP, SP
			mov	bx, [bp + 18]
			MOV si, [BP + 18]
			call getLenght
			cmp byte ptr [bx], '-'
			jne skip
			dec cx
			jmp inrange
skip:
			cmp cx, 9
			jge	error_ch
inrange:
			STD
			dec si
			dec si
			mov ebx, 1
for2:
			lodsb
			cmp al, '0'
			jl error_ch
			cmp al, 'F'
			jg error_ch
			cmp al, '9'
			jle do1
			cmp al, 'A'
			jge do2
			jmp error_ch
do1:		
			sub al, '0'
			jmp do
do2:		sub al, 'A'
			add al, 10
do:			
			mov edi, eax
			imul edi, ebx
			add	EDX, edi
			imul ebx, 16
		loop for2
		
			mov	bx, [bp + 18]
			cmp byte ptr [bx], '-'
			jne sk
			neg EDX
sk:
			mov	bx, [bp + 20]
			mov [bx], EDX;
			jmp ok
error_ch:
			mov sp, bp
			POPA
			mov	ax, 1
			jmp return
			
ok:
			mov sp, bp
			POPA
			mov ax, 0
			
return:
			RET
check	ENDP
	
START:
		MOV		AX, DATA				; получить адрес DS
		MOV		DS, AX					; установить DS
		MOV		ES, AX
		
		;mov		ax, 55h
		;push 	ax
		
		lea 	ax, num
		push	ax
		lea		ax, text
		push	ax
		
		call 	check
		


		MOV		AX, 4C00h				; the exit fuction  [4C+no error (00)]
		INT		21h						; call DOS interrupt 21h
CODE ENDS
	END START