.text

main:
        la $a0, param0
        jal out_string
        la $a0, param1
        jal out_string
        li $v0, 10
        syscall
out_string:
        li $v0, 4
        syscall
        jr $ra
.data
        param0: .asciiz "He.
"
        param1: .asciiz "llo, world!
"
