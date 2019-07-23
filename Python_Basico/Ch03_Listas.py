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

