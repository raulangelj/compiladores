.text

main:
	la $a0, param0
	jal out_string
	li $v0, 10
	syscall
out_string:
	li $v0, 4
	syscall
	jr $ra
.data
	param0: .asciiz "Hello, world!"