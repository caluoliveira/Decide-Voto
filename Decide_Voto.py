nome=str(input("Informe seu nome: \n"))
idade=int(input("Qual sua idade? \n"))
if (idade >= 18) and (idade < 70):
    print (nome, "seu voto é obrigatório! \n")
elif (idade >= 16) or (idade > 70):
    print (nome, "seu voto é facultativo! \n")
elif (idade < 16):
    print(nome, "você não pode votar! \n")