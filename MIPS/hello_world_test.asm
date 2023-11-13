.data
  output_message: .asciiz "Hello World desde function"

.text

out_string:
  li $v0, 4
  syscall
  jr $ra
main:
  la $a0, output_message
  jal out_string

  li $v0, 10
  syscall