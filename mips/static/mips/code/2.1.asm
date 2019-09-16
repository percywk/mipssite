#Original Problem: For the following C statement, what is the corresponding MIPS assembly code? 
#Assume that the variables f, g, h, and i are given and could be considered 32-bit integers as 
#declared in a C program. Use a minimal number of MIPS assembly instructions.
#f = g + (h − 5);

.data
	displayNum: .asciiz "\nF =  "
	getNumPrompt: .asciiz "\nEnter a number for H =  "
	getAddNumPrompt: .asciiz "\nEnter a number for G = "
	endPrompt: .asciiz "\nProgram completed successfully!"
.globl main
.text

main: 
	#f = g + (h - 5);
	#f = $v0
	#g = $a1
	#h = $a2
	
	jal get_two_nums
	move $a1, $v0			#Move results into argument registers
	move $a2, $v1			#Move results into argument registers
	
	jal perform_algebra 		#Performs f = g + (h - 5)
	move $a1, $v0			#Move the result into an argument register
	
	jal display_number		#Display the number
	
	j end_program			#End the program
					#Due to the structure of the code the program must be ended before it spills through
	
get_two_nums:
	li $v0, 4			#Load syscall number for printing a string
	la $a0, getNumPrompt		#Load address
	syscall				#Print the string
	
	li $v0, 5			#Load syscall number for reading an integer
	syscall				#Read the integer
	move $t0, $v0			#Move to tempory register for other syscalls.
	
	li $v0, 4			#Load syscall number for printing a string
	la $a0, getAddNumPrompt		#Load address
	syscall				#Print the string
	
	li $v0, 5			#Load syscall number for reading an integer
	syscall				#Read the integer
	move $t1, $v0			#Move to tempory register for other syscalls.
	
	move $v0, $t0			#Store results
	move $v1, $t1			#Store results
	jr $ra				#Return to point of call
	
perform_algebra:
	#a1 = g
	#a2 = h
	sub $t0, $a2, 5			#Subtracts 5 from a2 stores in $t2
	add $v0, $a1, $t0		#Adds result to $a1
					#$v0 = $a1 + ($a2 - 5)
	jr $ra				#Return to point of call
	
display_number:
	#$a1 = number to display
	li $v0, 4			#Load syscall number for printing a string
	la $a0, displayNum		#Load address
	syscall				#Print "\nF =  "
	
	li $v0, 1			#Load syscall number for printing a number
	move $a0, $a1			#Load number
	syscall				#Print $a1
	
	jr $ra				#Return to point of call

end_program:
	li $v0, 4			#Load syscall number for printing a string
	la $a0, endPrompt		#Load address
	syscall				#Print an end prompt (Suppossedly good manners)
	
	li $v0, 10			#Ends the program.
	syscall				#See syscall documentation for more details.
	
	
