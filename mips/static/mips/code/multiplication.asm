#Original Problem:  Multiply a hardcoded register value by 26 using only shifts and a simple add 
#Shifting is fast and simple use when possible.

.data
result_text: .asciiz "The value of the multiplication is:  "

# Program body
.text
.globl	main

#Multiplying to 26
#Shifts
# 0	1	2	3	4	5
# 1	2	4	8	16	32
#26x = 32x - 6x so --> Shift orginal 5 - shift orginal 2 - shift original 1
main:
	# initilization	
	addi $s0, $0, 5				# initialize $s0 = 5  Use this value to multiple by 30

	#Multiplication Logic
	sll $s1, $s0, 5				#Multiply $s0 by 32 store $s1
	sll $s2, $s0, 2				#Multiply $s0 by 4 store $s2
	sll $s3, $s0, 1				#Multiply $s0 by 2 store $s3
	sub $t0, $s1, $s2			#Subtract $s1 (32) - $s2 (4)
	sub $t0, $t0, $s3			#Subtract $t0 (28) - $s3 (2)
	
	# Print the result
	move $a1, $t0				#Move into argument register
	jal printResult
	

	# program exit	
	li $v0, 10					#Load syscall for exiting the program.
	syscall						#End the program
	
printResult:
	li $v0, 4					#Load syscall for pinting a string
	la $a0, result_text			#Load address
	syscall						#Print the string
	
	li $v0, 1					#Load syscall for printing an integer
	move $a0, $a1				#Move $a1 into $a0
	syscall						#Print the integer
		
	jr $ra						#Return to point of call
	
