#Original Problem: Add all the elements of array A and B together setting the index of A to the sum of matching indexes
#Output each sum and index along with the final total.

.data

	A:      	.word 2,4,6,8,10
	B: 		.word 2,3,5,7,11
	result_text:  	.asciiz "The final sum of array elements is: "
	cur_ind_text:  	.asciiz "The current index is: "
	cur_ele_text: 	.asciiz " The current element is: "
	newline:	.asciiz "\n"
	endPrompt:	.asciiz "\nProgram has completed successfully!"

.text
.globl	main

main:
	
	#Load the array addresses
	la $s6, A
	la $s7, B
	
	#Set counters
	add $t0, $zero, $zero			#Current counter
	addi $t1, $zero, 4			#Max array index
	
	
	
	arrayLoop:				#Point of return for loop
	
	#Find current array address
	sll $t2, $t0, 2				#Current array offset
	add $t3, $s6, $t2			#Current address of A
	lw $t3, 0($t3)				#Load current element of A
	add $t4, $s7, $t2			#Current address of B
	lw $t4, 0($t4)				#Load current element of B
	
	
	#Move interemediate results into argument registers
	add $a0, $zero, $t0
	add $a1, $t3, $t4
	
	add $t6, $t6, $a1			#Set total
	jal displayResults			#Print the result
	
	
	addi $t0, $t0, 1			#Increment the counter
	slt $t7, $t1, $t0			#Set $t7 to 1 if counter less than length
	beq $t7, $zero, arrayLoop		#Branch if 
	
	
	
	
	
	
	move $a0, $t6				#Move total into argument register
	jal displayTotal			#Display the total
	
	jal endProgram				#End the program






displayTotal:
	add $s1, $zero, $a0			#Move $a0 to temp register doesn't particularly matter

	li $v0, 4				#Load syscall number for printing an string
	la $a0, result_text			#Load the string address
	syscall					#Print the string
	
	li $v0, 1				#Load syscall number for printing an integer
	move $a0, $s1				#Load the integer
	syscall					#Print the integer
	
	jr $ra					#Return to point of call
	
displayResults:
	#Copy $a0 into $s0
	add $s0, $zero, $a0		
	
	li $v0, 4				#Load syscall number for printing an string
	la $a0, cur_ind_text			#Load the string address
	syscall					#Print the string
	
	li $v0, 1				#Load syscall number for printing an integer
	move $a0, $s0				#Load the integer
	syscall					#Print the integer
	
	li $v0, 4				#Load syscall number for printing an integer
	la $a0, cur_ele_text			#Load the string address
	syscall					#Print the string
	
	li $v0, 1				#Load syscall number for printing an integer
	move $a0, $a1				#Load the integer
	syscall					#Print the integer
	
	li $v0, 4				#Load syscall number for printing an integer
	la $a0, newline				#Load the string address
	syscall					#Print the string
	
	jr $ra					#Return to point of call
	
endProgram:
	li $v0, 4				#Load syscall number for printing an string
	la $a0, endPrompt			#Load the string address
	syscall					#Print the string
	
	li $v0, 10				#Load syscall number for ending the program
	syscall					#End the program

