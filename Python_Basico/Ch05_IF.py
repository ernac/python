
### 
# Com frequência, a programação envolve analisar um 
# conjunto de condições e decidir qual ação deve ser 
# executada de acordo com essas condições. A instrução if 
# de Python permite analisar o estado atual de um 
# programa e responder de forma apropriada a esse estado.###

#%% Exemplo 1 - Carros

# o else deve estar alinhado com o if

carros = ['audi','bmw','subaru', 'toyota']

for i in carros:
    if i == 'bmw':
        print i.upper()
    else:
            print i.title()


#%% Verificando a diferença

item1 = 'bmw' # Atribuição de valores. Deste modo item1 recebe o valor de 'bmw' como variável.
item1 == 'bmw' # Sinal duplo é comparativo de igualdade

item2 = 'toyota'
item1 != item2 # diferente de 


#%% Comparações numéricas

idade = 18
idade == 18

if idade < 21:
    print ("Programação não permitida para a faixa etária")


#%% Usando AND para comparação de várias condições

# Duas idades atribuídas
age0 = 21
age1 = 18

# Idades comparadas a duas situações usando AND
age0 >=14 and age1 <=25 # para que seja verdade ambas as situações tem que ser TRUE
age0 >=50 and age1 <=99





