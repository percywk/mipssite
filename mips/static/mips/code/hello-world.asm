# Target:  MIPS ISA Simulator
# Description:  Hello World! mutation displaying the contents of a string vertically.

# store preloaded data here
.data
	message:	.asciiz "Hello World!"
	freeSpace: 	.asciiz "\n"
	endPrompt: .asciiz "\nProgram completed successfully!"

.text
.globl	main
main:	
	la $a0, message				#Load the address of our message
	addi $a1, $zero, 12			#Load the message length into $a1
	la $a2, freeSpace
	
	jal displayVertically
		
	j exitProgram				#Terminate Program

displayVertically:
	#a0 = address of string --> t7
	#a1 = length for now  --> t8
	#a2 = address of free space --> t9
	move $t7, $a0
	move $t8, $a1
	move $t9, $a2
	
	addi $t0, $zero, 0			#$t0 = loop counter
	
	li $v0, 4				#Load syscall number for printing a string
	
	loop:	
		lb $t4, 0($t7)			#Hold current byte
							
		li $v0, 11			#Load syscall for character printing
		addi $a0, $t4, 0		#Move current byte into $a0
		syscall				#Print the character
		
		li $v0, 4			#Load syscall for string printing
		move $a0, $a2			#Move freeSpace address into $a0
		syscall				#Print "\n"
		
		addi $t7, $t7, 1		#Increment to the next byte position
		addi $t0, $t0, 1 		#Increment counter
		
		slt $t1, $t0, $t8		#Set t1 to 0 if $t0 less than $t8
		bne $t1, $zero, loop		#Break Loop if counter > length

		
	jr $ra					#Return to point of call

#Exit the program
exitProgram:
	li $v0, 4				#Load syscall number for printing a string
	la $a0, endPrompt			#Load address
	syscall					#Print an end prompt (Suppossedly good manners)
	
	
	li $v0, 10				#Load the syscall for program termination			
	syscall					#End the program
