# Cap 2 - Quando a máquina começa a tomar decisões - Lista de exercícios com Ifs
# Aluno: Afonso Heitor Favaretto Lopes
# RM94193

"""
4 – Um grande cliente seu sofreu um ataque hacker: o servidor foi sequestrado
por um software malicioso, que criptografou todos os discos e pede a
digitação de uma senha para a liberação da máquina. E é claro que os
criminosos exigem um pagamento para informar a senha.

Ao analisar o código do programa deles, porém, você descobre
 que a senha é composta da palavra “LIBERDADE” seguida do
 fatorial dos minutos que a máquina estiver marcando no momento
 da digitação da senha (se a máquina estiver marcando 5 minutos,
 a senha será LIBERDADE120). Crie um programa que receba do usuário
 os minutos atuais e exiba na tela a senha necessária para desbloqueio.

 ATENÇÃO: seu programa não pode utilizar funções prontas para o cálculo do fatorial.
 Ele deve obrigatoriamente utilizar loop.
"""

print('\nPrograma para gerar de desbloqueio do servidor do ataque Hacker!!!\n')
print('Descobrimos que a senha é a palavra LIBERDADE + o calculo de fatorial dos minutos no seu computador.\n')
minuto = input('Digite os minutos que aparecem neste computador: ')
minuto = int(minuto)

fatorial = 1
for i in range (minuto, 0, -1):
    fatorial *= i

print(f'\nA senha que você precisa digitar é LIBERDADE{fatorial} para desbloquear o servidor.\nAtenção!!!: você tem 60 segundos validos até que a senha mude novamente!!!\n')