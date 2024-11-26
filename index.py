# Algoritmo para armazenar variáveis do tipo string

# Criando as variáveis de string
nome = "Renan"
profissao = "Desenvolvedor"
hobby = "Aprender programação"

# Exibindo as variáveis armazenadas
print("Informações armazenadas:")
print(f"Nome: {nome}")
print(f"Profissão: {profissao}")
print(f"Hobby: {hobby}")

# Alterando o valor de uma variável
hobby = "Praticar esportes"
print("\nNova informação atualizada:")
print(f"Hobby atualizado: {hobby}")

# Armazenando as strings em uma lista
lista_de_strings = [nome, profissao, hobby]
print("\nLista de strings armazenadas:", lista_de_strings)

# Iterando sobre a lista
print("\nIterando sobre as strings:")
for string in lista_de_strings:
    print(string)
