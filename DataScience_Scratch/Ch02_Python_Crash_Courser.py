#%% [markdown]
### 
# # Listas Python
# Provavelmenta a estrutura mais fundamental em Python é a lista. Uma lista é simplesmente um #conjunto ordenado. É similar ao que as demais linguagens chamam de _array_.
# 
# Exemplo:
# ###

inteiro_lista = [1, 2, 3]
heterogenea_lista = ["string", 0.1, True]
lista_das_listas = [ inteiro_lista, heterogenea_lista, [] ]
lista_cumpr = len(inteiro_lista) # igual a 3
lista_soma = sum(inteiro_lista) # igual a 6
print(lista_cumpr)
print(lista_soma)


#%%
# Exemplo de listas

x = range(10) # a lista é [0, 1, ..., 9]
zero = x[0]
one = x[1]
two = x[2]
three = x[3]
four = x[4]
five = x[5]
six = x[6]
seven = x[7]
eight = x[8]
nine = x[9]

numeros = [zero, one, two, three, four, five, six, seven, eight, nine]
print(numeros[-3])

#%%
# Veficação

1 in numeros
'a' in numeros

#%%

# Concatenando listas usando a função extend

lista1 = [1,2,3]
lista1.extend([4,5,6])
lista1

# Caso não queira modificar lista1, basta adicionar mais elementos

lista3 = lista1 + [4,5,6]
lista3
