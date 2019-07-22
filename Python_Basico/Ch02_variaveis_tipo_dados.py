#%% [markdown]

### 
# ## Variável
# 
# > Um objeto que armazena um valor atribuído a ele
# 
# Vamos usar o exemplo para imprimir uma mensagem e depois criar uma variável contendo uma mensagem.
# 
# ###

# Exemplo

print("Hello Python")

# Agora vamos criar uma variável chamada mensagem e atribuir um valor para ela
mensagem = "Vamos aprender Python!"
print(mensagem)

### 
# ## Evitando erros com variáveis
# 
# Todo programador comete erros, e a maioria comete erros todos os dias.
# Embora bons programadores possam criar erros, eles também sabem
# responder a esses erros de modo eficiente. Vamos observar um erro que
# você provavelmente cometerá no início e vamos aprender a corrigi-lo.
# Escreveremos um código que gera um erro propositadamente. Digite o
# código a seguir, incluindo a palavra mesage com um erro de ortografia,
# conforme mostrada em negrito:
##   
# ###

message = "Hello Python Crash Course reader!"
print(mesage)

# Um traceback é um registro do ponto em que o interpretador se deparou com problemas quando tentou executar seu código. Eis um exemplo do traceback fornecido por Python após o nome da variável ter sido digitado incorretamente por engano 
#%% [markdown]
### 
# ## String
#
# Uma string é simplesmente uma série de caracteres. Tudo que estiver
# entre aspas é considerada uma string em Python, e você pode usar aspas
# simples ou duplas em torno de suas strings, assim:

"Isso é uma string." 
"Isso também é uma string."
#
#  ###

#%% [markdown]

### 
# ## Métodos de Strings
# 
# > - Palavras-chave: title(), upper(), lower()
# 
# Método é a ação que  o Python pode executar em algum dado. Abaixo um exemplo:  
# ####

# Vamos criar uma variável e atribuir a ela um nome qualquer em minúsculo

nome = "john ronald reuel tolkien"

# em seguida vamos colocar as primeiras letras em maiúsculo, utilizando o método title()

nome.title()

# assim aplicamos à variavel nome um método, através do operador de ponto "."
# [nome da variável].[nome do método] ([valor, quando necessário])

nome.upper()
nome.lower()

primeiro_nome = "J.R.R"
segundo_nome = "Tolkien"
nome_completo = primeiro_nome + " " + segundo_nome
print(nome_completo)

#%% [markdown]


