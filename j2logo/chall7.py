
# Dada una cadena de texto que se introduce por consola, cuente y muestre el número de apariciones de cada carácter en la cadena. 
# Debes usar el tipo dict para almacenar los resultados.

tex = input("Ingresa una frase: ")
counter_dic = {}
counter_list = map(lambda x: {x: tex.count(x)}, tex)
for cl in counter_list:
    counter_dic.update(cl)
print(counter_dic)
