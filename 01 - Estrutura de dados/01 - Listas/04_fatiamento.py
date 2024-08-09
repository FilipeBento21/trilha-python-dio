lista = ["p", "y", "t", "h", "o", "n"]

# DE COMEÇO SEM FINAL E MOSTRARÁ DO INDICE O
# PASSADO ATÉ O FINAL DA LISTA;
print(lista[2:])  # ["t", "h", "o", "n"]

#PASSANDO INDICE FINAL E SERÁ ENCERRADO NO INDICE INDICADO E ELE NÃO SERÁ MOSTRADO;
print(lista[:2])  # ["p", "y"]


print(lista[1:3])  # ["y", "t"]

#3º INDICE PUXAR DE 2 EM 2
print(lista[0:3:2])  # ["p", "t"]

# CÓDIGO PARA PUXAR TODA A LISTA PASSANDO INDICES VAZIOS
print(lista[::])  # ["p", "y", "t", "h", "o", "n"]

#LISTA ESPELHADA
print(lista[::-1])  # ["n", "o", "h", "t", "y", "p"]
