;variant 16

.MODEL	small

EXTRN        check:FAR

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

	public num, text
	
START:
		MOV		AX, DATA				; получить адрес DS
		MOV		DS, AX					; установить DS
		MOV		ES, AX
		
		lea 	ax, num
		push	ax
		lea		ax, text
		push	ax
		
		call 	check
		


		MOV		AX, 4C00h				; the exit fuction  [4C+no error (00)]
		INT		21h						; call DOS interrupt 21h
CODE ENDS
	END START