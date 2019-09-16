#Original Problem:  For the following C statement, what is the corresponding MIPS assembly code? 
#Assume that the variables f, g, h, i, and j are assigned to registers $s0, $s1, $s2, $s3, and $s4, respectively. 
#Assume that the base address of the arrays A and B are in registers $s6 and $s7, respectively.
#B[8] = A[i−j];

.data
	displayNum: .asciiz "\nB[8] =  "
	firstNumPrompt: .asciiz "\nEnter a number for i =  "
	secondNumPrompt: .asciiz "\nEnter a number for j = "
		
	arrayA: .word 0, 1, 2, 3, 4, 5, 6, 7, 8, 9				#junk data
	arrayB: .word 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900 	#11 items junk data
	
.globl main
.text

main: 
	#C - Code
	#B[8] = A[i - j];
	
	#Get the numbs
	jal get_two_nums		#Get two numbers from user input
	move $s3, $v0			#Set i = $s3
	move $s4, $v1			#Set j = $s4
	sub $t4, $s3, $s4		#Calculate $t4 = i - j
	
	#Get Array Index
	add $a1, $zero, $t4		#Get the array index
	la $a0, arrayA			#Get the array location
	jal get_index_for_array		#Gets final index for the array
	move $a1, $v0			#Move into $a1
	
	#Get Array Value
	jal get_array_val		#Gets the actual value
	move $a2, $v0			#Move into $a2

	#Load Address, Index, and Value into argument registers
	la $a0, arrayB
	addi $a1, $zero, 8		#Assign to B[8]
	jal assign_array
	
	jal displayB8			#Specifically displays B[8]
	
	j endProgram
	
get_two_nums:
	li $v0, 4			#Load syscall number for printing a string
	la $a0, firstNumPrompt		#Load string address		
	syscall				#Print the string
	
	li $v0, 5			#Load syscall number for user input integer
	syscall				#Grab the int
	move $t0, $v0			#Move to temporary register
	
	li $v0, 4			#Load syscall number for printing a string
	la $a0, secondNumPrompt		#Load string address
	syscall				#Print the string
		
	li $v0, 5			#Load syscall number for user input integer
	syscall				#Grab the int
	move $t1, $v0			#Move to temporary register
	
	move $v0, $t0			#Move first integer to $v0
	move $v1, $t1			#Move second integer to $v1
	jr $ra				#Return to point of call


get_index_for_array:
	#a0 = Array address
	#a1 = Array index
	sll $a1, $a1, 2			#Index = 4 * index number
	add $v0, $a0, $a1		#True address = address + (index * 4)
	jr $ra				#Return to point of call

get_array_val:
	#$a1 = absolute address value of word
	lw  $v0, 0($a1)			#Loads the array value from some index
	jr $ra				#Return to point of call
	
assign_array:
	 #a0 = array address.
	 #a1 = index.
	 #a2 = word to store.
	 move $s7, $ra			#Save original return address
	 
	 jal get_index_for_array	#Get the true index
	 sw $a2, 0($v0)			#Store the word
	 
	 move $ra, $s7			#Restore the original return index
	 jr $ra				#Return to point of call

#Displays the contents of B[8]
displayB8:
	la $a0, arrayB			#Load the address of B
	addi $a1, $zero, 8		#Move 8 to $a1
	jal get_index_for_array		#Get the index
	
	move $a1, $v0			#Move index to $a1
	jal get_array_val		#Get the value
	
	move $a1, $v0			#Move value into $a1
	
	move $s7, $ra			#Save the original return address
	jal printNum			#Print the number

	
	move $ra, $s7			#Restore original address
	jr $ra				#Return to point of call

printNum:
	#$a1 = number to display
	li $v0, 4			#Load syscall number for printing a string
	la $a0, displayNum		#Load the string address
	syscall				#Print the string
	
	li $v0, 1			#Load syscall number for printing an integer
	move $a0, $a1			#Load $a1 into $a0
	syscall				#Print $a1

	jr $ra				#Return to point of call
	
endProgram:
	li $v0, 10			#Load syscall number for ending a program
	syscall				#End the program. :3