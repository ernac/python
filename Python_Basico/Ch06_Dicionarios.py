#%% Introdução

### Neste capítulo aprenderemos a usar dicionários Python, que permitem conectar informações relacionadas. Veremos como acessar as informações depois que elas estiverem em um dicionário e modificá-las. Pelo fato de os dicionários serem capazes de armazenar uma quantidade quase ilimitada de informações, mostraremos como percorrer os dados de um dicionário com um laço. Além disso, aprenderemos a aninhar dicionários em listas, listas em dicionários e até mesmo  dicionários em outros dicionários.
# 
# Entender os dicionários permite modelar uma diversidade de objetos do mundo real de modo mais preciso. Você será capaz de criar um dicionário que representa uma pessoa e armazenar quantas informações quiser sobre ela. Poderá armazenar o nome, a idade, a localização, a profissão e qualquer outro aspecto de uma pessoa que possa ser descrito. Você será capaz de armazenar quaisquer duas informações que possam ser combinadas, por exemplo, uma lista de palavras e seus significados, uma lista de nomes de pessoas e seus números favoritos, uma lista de montanhas e suas altitudes, e assim por diante.
# ###

#%% Um dicionário simples

# Considere um jogo com alienígenas que possam ter cores e valores de pontuação diferentes. O dicionário simples a seguir armazena informações sobre um alienígena em particular:

alien_0 = {'raça': 'vedrano', 'energia': 5}
print alien_0 ['raça']
print alien_0 ['energia']


#%% Trabalhando com dicionários

# Um dicionário em Python é uma coleção de pares chave-valor. Cada chave é conectada a um valor, e você pode usar uma chave para acessar o valor associado a ela. O valor de uma chave pode ser um número, uma string, uma lista ou até mesmo outro dicionário. De fato, podemos usar qualquer objeto que possa ser criado em Python como valor de um dicionário.

# Um par chave-valor é um conjunto de valores associados um ao outro. Quando fornecemos uma chave, Python devolve o valor associado a essa chave. Toda chave é associada a seu valor por meio de dois-pontos, e pares chave-valor individuais são separados por vírgulas. Podemos armazenar quantos pares chave-valor quisermos em um dicionário.

