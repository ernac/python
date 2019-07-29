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

# sem declarar a porção inicial

classes [:5]

# sem declarar a porção final 

classes[0:]

# Essa sintaxe permite apresentar todos os elementos a partir de qualquer ponto de sua lista até o final, independentemente do tamanho da lista.


## Índices negativos

# Exibir o último item apenas
classes[-1:]

# Exibir os dois últimos itens da lista
classes[-2:]


#%%

# Percorrendo as fatias com laços

# Exibir os nomes das classes em formato de laço

for i in classes:
    print i.title() + ' ' + 'é uma classe de D&D'
print 'Estas são todas as classes deste exemplo.'


# Tirando cópia de uma lista

# Comiga predileta

rango_1 = ['pizza', 'churrasco', 'bolo de cenoura']
rango_2 = rango_1 [:]
print rango_2

#%%

# Exercícios

# Fatias: Usando um dos programas que você escreveu neste capítulo,acrescente várias linhas no final do programa que façam o seguinte: 
# • Exiba a mensagem Os três primeiros itens da lista são: Em seguida, use uma fatia para exibir os três primeiros itens da lista desse programa. 
# • Exiba a mensagem Três itens do meio da lista são:. Use uma fatia para exibir três itens do meio da lista. 
# • Exiba a mensagem Os três últimos itens da lista são:. Use uma fatia para exibir os três últimos itens da lista. 

mult5 = [i+2 for i in range(0,10,2)]
mult5

# 3 primeiros
mult5[0:3]
# 3 do meio
mult5[1:4]
# 3 finais
mult5[-3:]

# 4.11 – Crie uma lista de pizzas favoritas com cinco sabores. Faça uma cópia da lista de pizzas e chame-a de friend_pizzas. Então faça o seguinte: 
# • Adicione uma nova pizza à lista original. 
# • Adicione uma pizza diferente à lista friend_pizzas. 
# • Prove que você tem duas listas diferentes. Exiba a mensagem Minhas pizzas favoritas são:; em seguida, utilize um laço for para exibir a primeira lista. Exiba a mensagem As pizzas favoritas de meu amigo são:; em seguida, utilize um laço for para exibir a segunda lista. Certifique-se de que cada pizza nova esteja armazenada na lista apropriada.

pizzas1 = ['calabresa','siciliana','banana','portuguesa','quatro queijos']
pizzas2 = pizzas1[:]

pizzas1.append('toscana')
pizzas1

pizzas2.append('pepperoni')
pizzas2

for i in pizzas1:
    print 'As melhores pizzas sao ' + i.title()

for j in pizzas2:
    print 'Tambem gosto de ' + j.title()

#%%

# Tuplas

# Conceito

# Uma lista cujos os itens não podem ser mudados. As tuplas são definidas com parênteses no lugar de colchetes.

# Tuplas são imutáveis...

dimensao = (100,150) # dimensões de um retângulo, altura e largura
dimensao[0]
dimensao[1]

# Tentando atribuir um valor para o índice 0:
dimensao[0] = 200 # TypeError: 'tuple' object does not support item assignment

# ...porém, podem ser sobrescritas!

dimensao=(150,400)
dimensao[:]

# Se comparada com listas, as tuplas são estruturas de dados simples. Use-as quando quiser armazenar um conjunto de valores que não deva ser alterado durante a vida de um programa.

