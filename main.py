# AULA 1    19/10/2022

# meu primeiro projeto python 
#
# print ("") = comando de saida

print ("Alo mundo e que os deuses do python me ajudem")

# guardar uma string (frase)
# acentuação apenas entre ""

nome = "João Neves"

# guardar um numero inteiro

idade = 19

# exibir variável nome

print ("Meu nome é: " + nome)

# print "minha idade é:"
# adicionar " + e str" (por ser um número inteiro)
# ou adicionar {} dentro das aspas em seguida .format() fora das aspas

print ("Minha idade é: " + str (idade) + " anos")
print ("Minha idade é: {} anos" .format(idade))
print (f"Minha idade é: {idade} anos")

# exibir nome + idade

print("Meu nome é: {} e tenho: {} anos".format (nome, idade))

# AULA 2   26/10/2022

# comando input(): quero permitir que o usuário digite algo "in"

nome = input ("Digite o seu nome: ")
idade = int (input ("Digite a sua idade: "))

# comando input(): out
print (f"Bem vindo, {nome}")
print (f"Você tem: {idade} anos de idade")

# mostrar o dobro da idade informada

dobro = idade * 2
print (f"O dobro da sua idade é: {dobro}")
