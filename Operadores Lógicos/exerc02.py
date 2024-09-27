idade = int(input("Digite sua idade: "))
permissao = input("Você tem permissão dos pais? (sim/não): ")
if idade < 18 and permissao == "não":
    print("Você não pode participar da viagem")
else:
    print("Você pode participar da viagem")
