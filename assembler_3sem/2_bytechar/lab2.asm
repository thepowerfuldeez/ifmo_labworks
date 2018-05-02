;variant 11

.MODEL	small

STACK SEGMENT PARA STACK 'stack' 
 	DB 100h DUP(?)
STACK ENDS

DATA SEGMENT PARA PUBLIC 'data'
	text DB "7890my9nI1Lw?0pWhhxSjGzNLzvrvQmAAzwvU6CRNBLA,LQsXPcrt:ZgG71YK1'c"
	rez DB 66 DUP('$')
	rez2 DB 66 DUP('$')
	bitMask DQ 1111001010101000111101100110100010111000011100010111110001011101b
			;11110010 10101000 11110110 01101000 10111000 01110001 01111100 01011101b
	len EQU 64
	counter EQU 32
	
DATA ENDS

CODE SEGMENT PARA PUBLIC 'code'
	ASSUME CS: CODE, DS: DATA, SS: STACK

.486
	
START:
		MOV		AX, DATA				; получить адрес DS
		MOV		DS, AX					; установить DS
		MOV		ES, AX
		XOR 	SI, SI
		XOR		DI, DI
		clc  							; CF = 0
		MOV 	CX, counter
				
		MOV		DX, offset text
		MOV		ah, 09h
		int 	21h
		mov		ah, 06h ;	== \n
		mov		dl, 0Ah
		int 	21h
		
;формирование первой строки
		MOV 	CX, counter
		mov 	EBX, dword ptr bitMask + 4 ;получение первых 32 бит маски
		mov 	SI, offset text
		mov		DI, offset rez
		CLD								; DF = 0
FOR1:
		shl 	EBX, 1
		
		jnc zero
		mov		ah, 06H
		mov		dl, '1'
		int		21h
		jmp		check1
		zero:
		mov		ah, 06H
		mov		dl, '0'
		int		21h
		
		check1:
		lodsb
		jnc 	nextbit1
		cmp 	al, 'a'
		jl		nextbit1
		cmp		al, 'z'
		jg		nextbit1
		stosb	
		
		nextbit1:
		
LOOP 	FOR1
		
		mov 	EBX, dword ptr bitMask	;получение вторых 32 бит маски
		MOV 	CX, counter
		CLD
FOR2:
		shl 	EBX, 1
		
		jnc zero2
		mov		ah, 06H
		mov		dl, '1'
		int		21h
		jmp		check2
		zero2:
		mov		ah, 06H
		mov		dl, '0'
		int		21h
		
		check2:
		lodsb
		jnc 	nextbit2
		cmp 	al, 'a'			;сравнение что al >= 'a' и al <= 'z'
		jl		nextbit2
		cmp		al, 'z'
		jg		nextbit2
		stosb		
		
		nextbit2:
LOOP 	FOR2
		
		mov		ah, 06h ;	== \n
		mov		dl, 0Ah
		int 	21h
		
		MOV		DX, offset rez
		MOV		ah, 09h
		int 	21h
		
		mov		ah, 06h ;	== \n
		mov		dl, 0Ah
		int 	21h
		
		
		mov 	cx, len - 1
		mov 	SI, offset text[63]
		mov		DI, offset rez2
		xor		bx, bx
		
		STD
		lodsb
		mov		bh, al
FOR3:
		STD
		lodsb
		cmp		bh, 'A'				;два подряд идущих символа АА
		jne		copy
		cmp		al, 'A'
		je		continue
		copy:
		xchg	al, bh
		CLD
		stosb
LOOP	FOR3
		mov 	al, bh
		CLD
		stosb
continue:
		
		MOV		DX, offset rez2
		MOV		ah, 09h
		int 	21h
		
		MOV		AX, 4C00h				; the exit fuction  [4C+no error (00)]
		INT		21h						; call DOS interrupt 21h
CODE ENDS
	END START