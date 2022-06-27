# Cap 2 - Quando a máquina começa a tomar decisões - Lista de exercícios com Ifs
# Aluno: Afonso Heitor Favaretto Lopes
# RM94193

"""
2 – Os alunos da sua turma fizeram uma votação para escolher qual dia da semana é o melhor
para a realização das lives. Desenvolva um programa em que o usuário informe a
quantidade de votos que cada um dos 5 dias da semana (segunda-feira, terça-feira,
quarta-feira, quinta-feira e sexta-feira) obtiveram, verifique e exiba qual dia foi o escolhido.
"""

dias_da_semana = ['segunda-feira','terça-feira', 'quarta-feira', 'quinta-feira', 'sexta-feira']
votos = []

for x in dias_da_semana:
    informe = input(f'\ninforme quantos votos {x} ganhou: ')
    votos.append(int(informe))

for j, valor in enumerate(votos):
    if valor == max(votos):
        print(f'\n{dias_da_semana[j]} é o melhor dia para fazer Live de acordo com a turma\n')



