# Cap 2 - Quando a máquina começa a tomar decisões - Lista de exercícios com Ifs
# Atividade 1
# Aluno: Afonso Heitor Favaretto Lopes
# RM94193

# Sua tarefa é criar um algoritmo que receba o tipo de assinatura do cliente
# O faturamento anual dele
# Calcule e exiba qual o valor do bônus que o cliente deve pagar

print("VERIFICAR O TIPO DE ASSINATURA DO CLIENTE");
faturamento_anual = float(input("Insira o seu faturamento anual:  \n"))
nivel_assinatura = input("Insira o seu tipo de assinatura: BASIC, SILVER, GOLD, PLATINUM : \n")

if nivel_assinatura.upper() == "BASIC":
    faturamento = faturamento_anual * 0.3
    print("O valor informado do seu faturamento anual é de R${}. Seu tipo de assinatura é {}, o valor bônus que deve pagar é de R${}".format(
                    faturamento_anual, nivel_assinatura, faturamento))

elif nivel_assinatura.upper() == "SILVER":
    faturamento = faturamento_anual * 0.2
    print("O valor informado do seu faturamento anual é de R${}. Seu tipo de assinatura é {}, o valor bônus que deve pagar é de R${}".format(
                    faturamento_anual, nivel_assinatura, faturamento))

elif nivel_assinatura.upper() == "GOLD":
    faturamento = faturamento_anual * 0.1
    print("O valor informado do seu faturamento anual é de R${}. Seu tipo de assinatura é {}, o valor bônus que deve pagar é de R${}".format(
                    faturamento_anual, nivel_assinatura, faturamento))

elif nivel_assinatura.upper() == "PLATINUM":
    faturamento = faturamento_anual * 0.05
    print("O valor informado do seu faturamento anual é de R${}. Seu tipo de assinatura é {}, o valor bônus que deve pagar é de R${}".format(
                    faturamento_anual, nivel_assinatura, faturamento))
else:
    print("Tipo de assinatura inexistente, não é possivel o verificar o bônus que deve pagar\n")


