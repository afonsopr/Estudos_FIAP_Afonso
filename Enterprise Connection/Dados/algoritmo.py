

lista = [

    [[2006, 7, 15], 'Yahoo', 'senha', 'ajuda de senha', 'telefone', 'nome', 'email'],
    [[2000, 6, 11], 'Shoppe', 'senha', 'ajuda de senha', 'telefone', 'nome'],
    [[1999, 1, 6], 'Microsoft', 'senha', 'ajuda de senha', 'telefone', 'email'],
    [[1999, 11, 4], 'Claro', 'senha', 'ajuda de senha', 'email'],
    [[1994, 9, 10], 'Discord', 'senha', 'ajuda de senha', 'email'],
    [[1997, 3, 21], 'Google', 'ajuda de senha', 'telefone', 'nome', 'email'],
    [[2012, 10, 7], 'Amazon', 'telefone'],
    [[1990, 2, 1], 'Tesla', 'nome'],
]

lista_prioridade = ['senha', 'ajuda de senha', 'telefone', 'nome', 'email']

linha = 0
ordem = []
for indice, valor_prioridade in enumerate(lista_prioridade):

    print(indice,valor_prioridade, sep='--> ')
    
    contador = len(lista_prioridade)
    while contador > 0:
        
            if linha >= len(lista):
                linha = 0

            ordena_data = []
            while linha < len(lista):
                
                if lista[linha][2] == valor_prioridade and len(lista[linha]) - 2 == contador - indice:

                    ordena_data.append(lista[linha])
                    ordena_data.sort(reverse=True)
                    linha += 1
                    
                else:
                    linha += 1
                    
            contador -= 1
            
            for valor_linha in ordena_data:
                ordem.append(valor_linha)
                    

for i in lista:
    print(i)

print()

for j in ordem:
    print(j)
