nome = input('Digite seu nome:  ')

nota1 = float(input('Digite sua primeira nota:  '))
nota2 = float(input('Digite sua segunda nota:   '))
nota3 = float(input('Digite sua penúltima:      '))
nota4 = float(input('Digite sua última nota:    '))

soma = nota1 + nota2 + nota3 + nota4
media = soma / 4

print('a soma da sua média é:  ', media)

if media >= 7:
  print('Parabéns!', nome, '\nVocê foi aprovado! :)')
else:
  print('Poxa,', nome, '\nVocê foi reprovado! :(')