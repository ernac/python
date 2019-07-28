#%%

# Laço for

### O conceito de laços é importante. É uma das formas comuns usadas na automação de tarefas repetitivas. ###

names = ['Fran','Thais','Ana'] # lista em criada
for i in names: # atenção aos dois pontos após a instrução for
    print i # a opção print vem com indentação. Caso contrário, é exibido um erro.

# Concatenando texto usando for

names = ['Fran','Thais','Ana'] # lista em criada
for nome in names: # atenção aos dois pontos após a instrução for
    print nome.title() + ", que horas são?" # a opção print vem com indentação. Caso contrário, é exibido um erro.

# Listas numéricas

# Função range()

# Facilita na criação de números

for valores in range(1,10): #observar que o range é excludente na última opção de valores
    print valores

# Fazendo listas com progressão aritmética. Acrescentando um valor fixo até determinado número

# Números Pares até 12

pares = [range(2,14,2)]
print pares

# Quadrados Perfeitos de 1 a 10 - Todos os números gerados são elevados ao quadrado e armazenados numa lista chamada quadrados

quadrados = [] # lista vazia
for i in range(1,11): # como a lista deve ser de 1 a 10, coloca-se 11 pois o Python exclui a última referência
    quadrados.append(i ** 2) # Adicionando cada elemento i elevado ao quadrado à lista 'quadrados'

print quadrados # Imprime os resultados ao final, já fora do laço

#%%

# Operações simples com listas

digitos = range(1,11) # criando uma lista. Não é necessário o uso de colchetes para limitar a lista
print digitos
min(digitos) #1
max(digitos) #10
sum(digitos) #55

# List Comprehensions 

# Conceito

# É a geração de uma lista através de uma linha de código simplificada, usando o laço for

# Lista de cubos de 1 a 10 usando list comprehensions e laço for

cubos = [i**3 for i in range(1,11)]
print cubos

#%% 

# Exercícios

 # 1. Contando até vinte: Use um laço for para exibir os números de 1 a 20, incluindo-os.

for a in range(1,21):
    print a

# 2. Um milhão: Crie uma lista de números de um a um milhão e, então, use um laço for para exibir os números. (Se a saída estiver demorando demais, interrompa pressionando CTRL-C ou feche a janela de saída.)

for m in range(1,101):
    print m


# 3. Somando um milhão: Crie uma lista de números de um a um milhão e, em seguida, use min() e max() para garantir que sua lista realmente começa em um e termina em um milhão. Além disso, utilize a função sum() para ver a rapidez com que Python é capaz de somar um milhão de números.

million = range(1,1000001)
min(million)
max(million)
sum(million)

# 4. Números ímpares: Use o terceiro argumento da função range() para criar uma lista de números ímpares de 1 a 20. Utilize um laço for para exibir todos os números.

impares = range(1,20,2)
for i in impares:
    print i

# 5. Três: Crie uma lista de múltiplos de 3, de 3 a 30. Use um laço for para exibir os números de sua lista.

mult3 = range(3,30,3)
for i in mult3:
     print i


# 6. Cubos: Um número elevado à terceira potência é chamado de cubo. Por exemplo, o cubo de 2 é escrito como 2**3 em Python. Crie uma lista dos dez primeiros cubos (isto é, o cubo de cada inteiro de 1 a 10), e utilize um laço for para exibir o valor de cada cubo.

cubo1 = [k**3 for k in range(3,30,3)]
print cubo1

# 7. Comprehension de cubos: Use uma list comprehension para gerar uma lista dos dez primeiros cubos.

cubo2 = [w**3 for w in range(3,33,3)]
print cubo2


#%%

# Trabalhando com partes de uma lista

# Nesta parte vamos trabalhar com intervalos de uma lista, também chamado de fatias. Exemplo, classes de um heróis no RPG D&D Quinta Edição

classes = ['guerreiro','ladino','mago','feiticeiro','barbaro','monge','ranger','bardo']
classes.sort() #ordenando a lista em ordem alfabética
classes #lista ordenada
classes [0:4] # uma fatia de um intervalo da lista



