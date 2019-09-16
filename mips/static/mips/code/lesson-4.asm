#Purpose is to use examples for the stack
.data
	arrayMessage: .asciiz "\nArray Total: "
	endingPrompt: .asciiz "\nEnding the program!"
.globl main
.text
main: 	
	
	#Generate an array with x items 0 - x
	li $a0, 10
	jal generateArray
	
	#Move the array address into $a0
	move $a0, $v0
	#Move the total items into $a1	
	move $a1, $v1
	
	#Add the items within the array
	jal addArray
	
	#Display the result
	move $a0, $v0
	jal displayTotal
	
	#End the program
	jal endTheProgram
	
	
generateArray:
	
	add $s0, $zero, $sp			#Save the current stack pointer for returning
	addi $t0, $zero, 1			#Set counter to 1	
	move $t1, $a0				#Move $a0 to $t1
	addi $t1, $t1, 1			#Increment top by 1
	
	loopReturn:
	
	sw $t0, 0($sp)				#Store counter
	subu $sp, $sp, 4 			#Decrement the sp
	addi $t0, $t0, 1			#Increment the counter
	bne $t0, $t1, loopReturn		#Branch if counter != maxCount

	#Move into return register.
	add $v0, $zero, $s0
	add $v1, $zero, $t1
	jr $ra


addArray:
	
	move $s0, $a0				#Move the saved stack pointer
	add $t1, $a1, $zero			#Move the total items
	add $t0, $zero, $zero			#Set $t0 to zero -- counter
	add $t4, $zero, $zero			#Set $t4 to zero
	
	addArrayLoop:
	
	lw $t3, 0($s0)				#Load the item
	subu $s0, $s0, 4			#Subtract the stack pointer
	add $t4, $t4, $t3			#Add to total
	addi $t0, $t0, 1			#Increment the counter
	bne $t0, $t1, addArrayLoop		#Branch if not equal
	
	#Move into return register
	add $v0, $t4, $zero
	jr $ra
	
displayTotal:
	#Save the total in $t2
	add $t2, $a0, $zero	
	
	la $a0, arrayMessage
	li $v0, 4
	syscall
	
	add $a0, $zero, $t2
	li $v0, 1
	syscall
	
	jr $ra

#Ends the program. Explanation not necessary
endTheProgram:
	la $a0, endingPrompt
	li $v0, 4
	syscall
	
	li $v0, 10
	syscall