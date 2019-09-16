#Name Loops And Jumps 

.data
	numberPrompt: .asciiz "\nNumber: "
	endingPrompt: .asciiz "\nEnding the program"
	
.globl main
.text


main: 	
	
	addi $a0, $zero, 15			#Count to 15
	jal displayNumSequence
	
	jal endProgram				#End the program
		
		
		
		
displayNumSequence:
	addi $t0, $zero, 1			#Set counter to 1
	add $t1, $zero, $a0			#Move argument register into $t0
	
	displayNumSequenceLoop:
	la $a0, numberPrompt			
	li $v0, 4
	syscall					#Display the number prompt
	
	add $a0, $zero, $t0			#Move $t0 into argument register
	li $v0, 1
	syscall					#Display the number
	
	beq $t0, $t1, displayNumSequenceReturn	#Branch to exit if equal
	addi $t0, $t0, 1			#Increment the counter
	j displayNumSequenceLoop		#Jump to top of loop
	
	displayNumSequenceReturn:		#Address to return out of loop
	jr $ra
	
	
	
	
endProgram:
	la $a0, endingPrompt
	li $v0, 4
	syscall					#Display an ending prompt
	
	li $v0, 10
	syscall					#End the program
	
	
	
