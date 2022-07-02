lista = ['Hamburguer', 'Suco', 'Pizza', 'Picolé']
print(lista)

#Para adicionar alguma coisa:
lista = ['Hamburguer', 'Suco', 'Pizza', 'Picolé']
lista.append('Sushi')

#Para adicionar alguma coisa, em determinado lugar:
lista.insert(0,'Hot Dog')

#para deletar alguma coisa
del lista[3]
#ou
lista.pop(3)
#para deletar pelo nome
lista.remove('Pizza')

#So vou remover o objeto, SE o objeto estiver na lista
if 'Pizza' in lista:
    lista.remove('Pizza')

#Criando listas atravez de Ranges
valores = list(range(4, 11))

#Colocando em ordem os valores
valores = [8, 5, 4, 7, 0, 3, 4]
valores.sort()
#ou em ordem contraria
valores.sort(reverse=True)

#Criar uma copia sem ligaçao
a = [3, 4, 6, 7]
b = a[:]
b[2]= 8
print(f'Lista A{a}')
print(f'Lista B{b}')