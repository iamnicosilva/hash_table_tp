class Node2:
    def __init__(self,key=None,element=None,next=None):
        self.key = key
        self.element = element
        self.next = next

    def __str__(self):
        return f"Producto: {self.element[0]} Cantidad: {self.element[1]}"


def hashearcodigo(codigo):
    primo = 31  # Número primo para evitar colisiones
    hash_value = 0
    string_length = len(codigo)

    for i in range(string_length):
        hash_value = (hash_value * primo + ord(codigo[i])) % 40010


    return hash_value % 40009



class HashTable:

    def __init__(self,capacity,hashFunction):
        self.m = capacity
        self.h = hashFunction
        self.T = [None] * self.m


    def stats(self):
        pass

def menu() -> None:
    print("1. Agregar")
    print("2. Buscar")
    print("3. Eliminar")
    print("4. Estado")
    print("5. Salir")


class HashTableChaining ( HashTable ):

    def insert ( self , key , element ):
        node = Node2 ( key , element )
        index = self.h(key)
        node.next = self.T[index]
        self.T[index] = node

    def search ( self , key ):
        index = self.h(key)
        nodo = self.T[index]
        if nodo is None:
            return 'No se encontro el producto'

        def buscar_por_nodos(nodo,key):

            if nodo.element[0] == key :
                return nodo
            if nodo.next == None:
                return 'No se encontro el producto'
            else:
                return buscar_por_nodos(nodo.next, key)

        return buscar_por_nodos(nodo, key)

    def delete ( self , key ):
        self.T[self.h(key)] = None
        print('Se elimino el producto')

    def stats(self):
        h = int(len(self.T))
        contador_celdas = 0
        contador_elementos = 0
        lista_larga = 0

        def contar_elementos_encadenados(nodo):
            if nodo.next == None:
                return 1
            else:
                return 1 + contar_elementos_encadenados(nodo.next)

        for i in self.T:
            if i != None:
                contador_celdas += 1
                esta_lista = contar_elementos_encadenados(i)
                contador_elementos += esta_lista
                if esta_lista > lista_larga:
                    lista_larga = esta_lista

        factor_carga = float(contador_elementos/h)

        print(f"Tamaño de tabla:        {h}")
        print(f"Celdas ocupadas:        {contador_celdas}")
        print(f"Cantidad de elementos:  {contador_elementos}")
        print(f"Lista más larga:        {lista_larga}")
        print(f"Factor de carga:        {factor_carga}")


# CODIGO PARA PRUEBAS:

import random
import string

def generate_random_string(length):
    # Generar una cadena aleatoria de caracteres alfanuméricos de longitud dada
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

if __name__ == "__main__":
    db = HashTableChaining(40009, hashearcodigo)

# Generar 40,000 registros aleatorios PARA PRUEBA
    for _ in range(40000):
        codigo = generate_random_string(10)
        cantidad = random.randint(1, 100)
        
        if db.search(codigo) == 'No se encontro el producto':
            db.insert(codigo, [codigo, cantidad])
        else:
            db.search(codigo).element[1] += cantidad



    while True:
        menu()
        choice = input("Enter choice: ")

        if choice == '1':
            print('')
            print('Insertar')
            codigo = input("Ingrese código de producto: ")
            cantidad = int(input("Ingrese cantidad: "))
            if db.search(codigo) == 'No se encontro el producto' :
                db.insert(codigo, [codigo,cantidad])
            else:
                db.search(codigo).element[1] += cantidad
            pass
        elif choice == '2':
            print('')
            print('Buscar')
            codigo = input("Ingrese código de producto: ")
            print(db.search(codigo))

            pass
        elif choice == '3':
            print('')
            print('Eliminar')
            codigo = input("Ingrese código de producto: ")
            existe = db.search(codigo)
            if existe == 'No se encontro el producto':
                print(existe)
            else:
                db.delete(codigo)

            pass
        elif choice == '4':
            print('')
            print('Estado')
            db.stats()
            pass
        elif choice == '5':

            break
        else:
            print("Opcion invalida")
        print()
