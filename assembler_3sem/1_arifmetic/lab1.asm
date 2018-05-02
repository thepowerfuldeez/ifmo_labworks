;variant 411

.MODEL	small

STACK SEGMENT PARA STACK 'stack' 
 	DB 100h DUP(?)
STACK ENDS

DATA SEGMENT PARA PUBLIC 'data'
	mas DW 5, -2, -1, 0, 18, -6, 5, 6, -3, -20, -17, 7
	res  DW 12 DUP(0)
	counter EQU 11
	len EQU 12
	second DW ?
	one EQU 2  			;величина смещения
DATA ENDS

CODE SEGMENT PARA PUBLIC 'code'
	ASSUME CS: CODE, DS: DATA, SS: STACK


;ЧАСТЬ 1: Обработка исходного массива		
START:

		MOV		AX, DATA				; получить адрес DS
		MOV		DS, AX					; установить DS
		MOV		CX, counter				; значение счетчика в CX
		MOV 	DX, mas[one]         		; сохраним второй элемент массива
		MOV 	second, DX
     		     				
FOR1:								;сортировка пузырьком с игнорированием чисел <= 0
		MOV 	AX, CX				;запоминаем счётчик внешнего цикла
		MOV 	CX, counter
		MOV		BX, OFFSET mas			; указатель текущего элемента массива
			   		 ; указатель на место вставки элемента
FOR2:
		MOV 	SI, [BX + one]
		MOV 	DX, [BX]
		CMP 	DX, 0
		JLE 	ELSE1				;goto if DX <= 0
		CMP 	DX, SI   			;DX > SI
		JLE 	ELSE1				;goto if DX <= SI
		XCHG 	SI, DX   			;swap(SI, DX)
		MOV 	[BX + one], SI
		MOV 	[BX], DX
ELSE1:
		ADD 	BX, one
		LOOP 	FOR2
		MOV 	CX, AX				;востанавливаем счётчик
		LOOP 	FOR1
		
								


;ЧАСТЬ 2: Формирование массива-результата
		MOV 	CX, len				; восстанавливаем  значение счетчика	
		XOR 	SI, SI					; обнуляем индекс начала массива 
		MOV 	DX, mas[SI]	

;Поиск минимального элемента массива, результат в DX 		
MIN:	
		CMP 	DX, mas[SI]				
		JLE		ELSE2		
		MOV 	DX, mas[SI]
ELSE2:	
		ADD		SI, one
		LOOP	MIN
		
;Вычисление среднего арефметического второго элемента и наименьшего элемента массива, DX, second
		ADD		DX, second
		SAR		DX, 1			;DX >> 1
				
;Формирование массива-результата, метод двух указателей
		XOR		SI, SI				;указатель на элемент из mas
		XOR		DI, DI				;указатель на элемент из res
		MOV		CX, len	
NEXT:	
		MOV		AX, mas[SI]	
		CMP 	DX, AX				
		JGE		ELSE3
		MOV 	res[DI], AX
		ADD		DI, one 
ELSE3:	
		ADD		SI, one
		LOOP	NEXT	
		
		
		MOV	AX, 4C00h				; the exit fuction  [4C+no error (00)]
		INT		21h						; call DOS interrupt 21h
CODE ENDS
	END START