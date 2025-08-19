
# Imprimindo uma string
string = 'quem e esse'
print( string )

# Tipo de uma string.
print(type(string))

# Tamanho de uma string.
print(len(string))

# Concatenação
print(string + ' pokemon?')

# Substitui uma substring por alguma outra coisa.
substituir = string.replace('quem e esse', 'acredite no coracao das cartas') 
print(substituir)
teste = ('teste')

# A string começa com "Ola"?
print ( string.startswith('Ola') )

# A string termina com "mundo"?
print ( string.endswith('Mundo') )

# Quantas ocorrências da palavra "a" a string possui?
print ( string.count('M') )

# Capitalize - 
string_02 = ('goku')
print ( string_02.capitalize() )

# Verificar se uma string só possui numeros
string_03 = ('123456789')
string_04 = ('123456789ABC')
print( string_03.isdigit())
print( string_04.isdigit())


# Verifica se uma string é alfanumerica (só possui letras e números).
print( '12345abc'.isalnum() )

# Transforma tudo em Maiúsculo 
print( string.upper() )

# Transforma tudo em Minusculo
print( string.lower() )

# Procura algo na string
print (string.find('n') )

# Removendo espaços antes e fim da palavra
string_05 = (" Ola Mundo ")
print( string_05.strip() )

# Removendo espaços antes e fim da palavra
