
n = input("Digite o nome do aluno: ")
n1 = float(input("Digite n1: "))
n2 = float(input("Digite n2: "))
n3 = float(input("Digite n3: "))

cn = ((n1+ n2 + n3) / 3)

if cn >= 6:
    print (f"O aluno {n} está com uma média {cn} e foi aprovado")

elif cn < 6 and cn >= 0:
    print(f"O aluno {n} está com média {cn} e está retido")

else:
    print("Algo deu errado")
    print("Tente novamente")