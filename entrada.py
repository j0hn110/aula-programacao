nome = input("Digite seu nome de usuário: ")
senha = input("Digite sua senha: ")
dominio = input("Qual seria o domínio? ")
print("Olá ", nome, ", seja bem vindo ao meu mundo")
print("Sua senha é: ", senha)
print("O seu domínio é: ", dominio)


email = usuario +"@" + dominio
print("Seu e-mail é: ", email)

palavra = "jaca"
#colocar a string como toda maiúscula
print("Colocando o texto em maiúscula: ", palavra.upper())

PALAVRA = "JACA"
#colocar a string como toda minúscula
print("Colocando o texto em minúsculo: ", PALAVRA.lower())

#contar caracter da string
palavra_contar = "banana"
print("Contar a letra b: ", palavra_contar.count("b"))
print("Contar a letra a: ", palavra_contar.count("a"))
print("Contar a letra n: ", palavra_contar.count("n"))

#exercício, gerar senha automaticamente:
print("Senha gerada automaticamente: ")
print("a"+str(email.count("a"))+"e"+str(email.count("e"))+"i"+str(email.count("i"))+"o"+str(email.count("o"))+"u"+str(email.count("u")))

print(email)
a = email.count("a")
e = email.count("e")
i = email.count("i")
o = email.count("o")
u = email.count("u")
nova_senha = "a" + str(a) + "e" + str(e) + "i" + str(i) + "o" + str(o) + "u" + str(u)
print(nova_senha)
