#Name: Algebra Exmple
#Description: Perform some basic algebra in MIPS
.data
	returnPrompt: .asciiz "\nValue Returned: "
	endPrompt: .asciiz "\nEnding the program!"
.globl main
.text

main: 
	#Problem 1
	# X = 5			$t0
	# Y = 2 * X + 5		$t1
	
	addi $t0, $zero, 5		#Set $t0 to 5
	sll $t0, $t0, 1			#Multiply by 2 using a bit shift
	addi $t1, $t0, 5		#Add into 5
	
	add $a0, $zero, $t1		#Move the value into an argument register
	jal displayValue		#Display the value
	
	
	#Problem 2
	#X = 5
	#Y = 10
	#Z = 3 * (X + Y)
	addi $t0, $zero, 5		#Set $t0 to 5
	addi $t1, $zero, 10		#Set $t1 to 10
	
	add $t2, $t0, $t1		#Add $t0 and $t1
	addi $t3, $zero, 3		#Set multiplier to 3
	mul $t2, $t2, $t3		#Multiply result
	
	add $a0, $zero, $t2		#Move the value into an argument register
	jal displayValue		#Display the value
	
	jal EndProgram 			#End the program
	
	
	
displayValue:
	
	#Move $a0 to another location
	add $t4, $a0, $zero
	
	#Load string address
	la $a0, returnPrompt
	
	#Load syscall number
	addi $v0, $zero, 4
	
	#Print the text
	syscall
	
	
	#Move $t4 back
	add $a0, $zero, $t4
	
	#Load syscall number
	addi $v0, $zero, 1
	
	#Print the return value
	syscall
	
	#Return to point of call
	jr $ra
	
EndProgram:
	#Display the ending prompt
	la $a0, endPrompt
	li $v0, 4
	syscall
	
	#Load the syscall number
	li $v0, 10
	
	#End the program
	syscall

