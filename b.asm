.data
type_0: .asciiz "IO"
buffer_0: .space 3
type_1: .asciiz "Bool"
buffer_1: .space 5
const_0: .asciiz "\n"
.text
.globl main
main: 
	la $t0, type_0
	move $a0, $t0
	li $a1, 0
	li $a2, 2
	la $a3, buffer_0
	jal substr
	 la $t1, buffer_0
	move $a0, $t1
	jal out_string
	la $t0, type_1
	move $a0, $t0
	li $a1, 1
	li $a2, 3
	la $a3, buffer_1
	jal substr
	 la $t1, buffer_1
	move $a0, $t1
	jal out_string
	la $a0, const_0
	jal out_string
	jr $ra
li $v0, 10
syscall
out_string: li $v0, 4 
	syscall
	jr $ra
substr: add $a0, $a0, $a1
	move $t0, $a0
	move $t1, $a3
	li $t2, 0
fill_buffer:lb $t3, 0($t0)
	sb $t3, 0($t1)
	addi $t0, $t0, 1
	addi $t1, $t1, 1
	addi $t2, $t2, 1
	bne $t2, $a2, fill_buffer

	sb $zero, 0($t1)
	move $v0, $a3
	jr $ra