#Name: Literal Hellow World
#Description: Just Hello World in MIPS
.data
	#Place for ascii strings
	HelloPrompt: .asciiz "\nHello World!"
	
.globl main
.text
main:
	#Load the string address into the argument register
	la $a0, HelloPrompt
	
	#Load the syscall code into $v0 indicating we wish to print a message
	li $v0, 4
	
	#Call syscall to print a message
	syscall
	
	
	#Load the syscall code into $v0 indicating the end of the program
	li $v0, 10
	
	#Call syscall to end the program
	syscall
	
	
	
