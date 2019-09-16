#Original Problem: For the following C statement, write a minimal sequence of MIPS assembly instructions that 
#does the identical operation. Assume $t1 = A, $t2 = B, and $s1 is the base address of C.
#A = C[0] << 4;

.data
	array_C: .word 2,4,2,2,2,2,2,2,2,2,2,2		#Junk data
	displayNum: .asciiz "\nThe number is: "
	endPrompt: .asciiz "\nProgram completed successfully!"
.globl main
.text

main:
	la $t0, array_C			#Load the address of the array	
	lw $t2, 0($t0)			#Load the first entry 
	
	sll $t1, $t2, 4			#Shift the bits of the first elements 4 locations
	add $s1, $zero, $t1		#Move the register into $s1
	
	move $a1, $s1			#Copy $s1 into $a1
	jal displayInt			#Output the result
	
	j endProgram			#End the program.

#Displays an integer to the console.
displayInt:
	#$a1 = number to display
	
	li $v0, 4			#Load syscall number for printing a string
	la $a0, displayNum		#Load address
	syscall				#Print the string
	
	li $v0, 1			#Load syscall number for printing an integer
	move $a0, $a1			#Load int
	syscall				#Print the int
	
	jr $ra				#Return to point of call
	
#Ends the program
endProgram:
	li $v0, 4			#Load syscall number for printing a string
	la $a0, endPrompt		#Load address
	syscall				#Print an end prompt (Suppossedly good manners)
	
	li $v0, 10			#Ends the program.
	syscall				#See syscall documentation for more details.
