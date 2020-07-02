# Implementar una función llamada ordena_ciudades(ciudades) que reciba como argumento
# un diccionario con ciudades y su población y devuelva una lista con los nombres de las 
# ciudades de más de 200.000 habitantes. La lista devuelta debe estar ordenada de mayor 
# a menor según el número de habitantes de cada ciudad.
# La función se puede implementar en una sola línea de código

def order_cities(d):
    return sorted([k for k, v in d.items() if v > 200000])


d = {'Cuautitlán': 108000, 'C. México': 8800000, 'Zamora': 141000, 'Guadalupe': 673000}
print(order_cities(d))
