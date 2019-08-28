
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

#%% Instruções If-Else

# Estrutura usada quando da análise de duas condições
# Abaixo verificando quais jogos são permitidos segundo a idade - usando a classificação da PSN.

if age0 >=18:
    print "Já pode jogar jogos de classificação M"
else:
    print "Apenas jogos com classificação abaixo de M são permitidos"

#%% Instrução If-Elif-Else

# Estrutura usada quando se pretende avaliar mais de duas condições para validação

# Considere que uma loja de games dê descontos distintos para grupos etários diferentes

# Jogos para clientes menores de 6 anos tem 50% de desconto
# Jogos para clientes com idade entre 7-18 tem 40% de desconto
# Acima de 18 anos o desconto é de 30%

age = 77

if age < 6:
    print "Seu desconto é de 50%"
elif age < 18:
    print "Seu desconto é de 40%"
else:
    print "Seu desconto é de 30%"

#%% Vários Blocos Elif

# Caso na situação haja um desconto de 80% para maiores de 50 anos

age = 77

if age < 6:
    print "Seu desconto é de 50%"
elif age < 18:
    print "Seu desconto é de 40%"
elif age <50:
    print "Seu desconto é de 30%"
else:
    print "Seu desconto é de 80%"

#%% Omitindo o bloco Else

age = 77

if age < 6:
    print "Seu desconto é de 50%"
elif age < 18:
    print "Seu desconto é de 40%"
elif age <50:
    print "Seu desconto é de 30%"
elif age>=65: # usando a condição elif e omitindo o else: maior confiança no código
    print "Seu desconto é de 80%"

### O bloco else é uma instrução que captura tudo. Ela corresponde a qualquer condição não atendida por um teste if ou elif específicos e isso, às vezes, pode incluir dados inválidos ou até mesmo maliciosos. Se você tiver uma condição final específica para testar, considere usar um último bloco elif e omitir o bloco else. Como resultado, você terá mais confiança de que seu código executará somente nas condições corretas.
###

#%%  Testando várias condições

### A cadeia if-elif-else é eficaz, mas é apropriada somente quando você quiser que apenas um teste passe. Assim que encontrar um teste que passe, o interpretador Python ignorará o restante dos testes. Esse comportamento é vantajoso, pois é eficiente e permite testar uma condição específica. Às vezes, porém, é importante verificar todas as condições de interesse. Nesse caso, você deve usar uma série de instruções if simples, sem blocos elif ou else. Essa técnica faz sentido quando mais de uma condição pode ser True e você quer atuar em todas as condições que sejam verdadeiras.###

# Vamos reconsiderar o exemplo da pizzaria. Se alguém pedir uma pizza com dois ingredientes, será necessário garantir que esses dois ingredientes sejam incluídos em sua pizza:

pedidos = ['queijo', 'cogumelos']

if 'queijo' in pedidos:
    print "Queijo adicionado!"
if 'cogumelos' in pedidos:
    print 'Cogumelos adicionados!'
if 'calabresa' in pedidos:
    print 'Calabresa adicionada!'

print 'Pizza terminada!'

#%% Instruções if com listas

### As pessoas pedirão de tudo, em especial quando se tratar de ingredientes para uma pizza. E se um cliente realmente quiser batatas fritas em sua pizza? Podemos usar listas e instruções if para garantir que o dado de entrada faça sentido antes de atuar sobre ele. Vamos prestar atenção em solicitações de ingredientes incomuns antes de prepararmos uma pizza. O exemplo a seguir define duas listas. A primeira é uma lista de ingredientes disponíveis na pizzaria, e a segunda é a lista de ingredientes que o usuário pediu. ###

disponivel = ['cogumelos', 'azeitonas', 'pimentao', 'pepperoni', 'abacaxi', 'queijo']

solicitados = ['cogumelos', 'batata frita', 'queijo']

for disponivel in solicitados:
    if disponivel in solicitados:
         print("Adicionando " + solicitados + ".")
    else: 
         print("Lamento não temos" + solicitados + ".")
        
#%% 

available_toppings = ['mushrooms', 'olives', 'green peppers','pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings: 
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else: 
        print("Sorry, we don't have " + requested_topping + ".")

print("\nFinished making your pizza!")