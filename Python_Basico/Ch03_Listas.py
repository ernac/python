#%% [markdown]
### 
# # Listas
# ## Definição
# 
# > Coleção de itens numa ordem em particular. Em Python, colchetes [] indicam uma lista e vírgulas separam seus elementos.
# 
# Exemplo:

# ###

bicicletas = ['moutain','tracker','cross','monociclo']
print bicicletas

## Acessando os elementos de uma lista

# É usado uma posição ou índice para informar qual item da lista será acessado.
# Em Python os índices começam em zero
bicicletas [0]

#%%

# Acrescentando, removendo e alterando elementos em uma lista

# Modificando os elementos de uma lista

cores = ['azul', 'branco', 'preto', 'rosa']
cores[0] = 'carmin'
print cores

# Acrescetando elementos numa linha - método append()

cores.append('laranja')
print cores

# Inserindo elementos numa lista - método insert()

cores.insert(0,'roxo') # essa instrução vai inserir roxo no índice 0, deslocando os demais elementos adiante
print cores

# Removendo elementos de uma lista - del[]

del cores[0] # deletando a cor roxo
print cores

# Os dados removidos com del não podem mais ser acessados
#%%
# Usando o método pop() para remover os itens de uma lista

# O método pop() remove o último item de uma lista, porém permite que você trabalhe com ele após a remoção.

cores = ['azul', 'branco', 'preto', 'rosa']
print cores

# vamos usar o método pop() para remover o item da lista

cor_removida = cores.pop()
print cores
print cor_removida

# para remover qualquer item da lista basta indicar com o índice

cor_indice = cores.pop(2)
print cor_indice

#%%

# removendo o item de acordo com o valor - método remove()

frutas = ['laranja', 'pera', 'uva', 'abacaxi']
print frutas


#%%
# Ordenando listas de forma permanente

nomes = ['Jo','Lu','Nic','Au','Bru','Gabi']
nomes.sort()
nomes.sort(reverse= True)
print nomes

# Ordenando as listas de forma temporária usando sorted()

print (sorted(nomes, reverse=True))
print nomes

#%%

# para imprimir uma lista em ordem contrária usamos reverse() de forma permanente

bare_bears = ['Panda', 'Polar','Pardo']
bare_bears.reverse()
print bare_bears

# Para retornar ao padrão anterior, basta aplicar novamente o método

#%%

# Descobrindo o tamanho de uma lista com a função len()

sala = ['cadeiras','mesa','sofa','tv']

sala.__len__() 





