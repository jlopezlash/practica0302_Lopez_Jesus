'''Añadir una clase Pedido que tiene como atributos:
    - lista de productos
    - lista de cantidades
Añade las siguiente funcionalidad:
    - total_pedido: muestra el precio final del pedido
    - mostrar_productos: muestra los productos del pedido
'''
class Producto:

    def __init__(self, codigo, nombre, precio):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = precio

    @property
    def codigo(self):
        return self.__codigo
    @codigo.setter
    def nombre(self, valor):
        self.__codigo = valor
    
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    @property
    def precio(self):
        return self.__precio
    @precio.setter
    def precio(self, valor):
        self.__precio = valor

    def calcular_total(self, cantidad):
        return self.__precio * cantidad
    
    def __str__(self):
        return 'Codigo ' + str(self.__codigo) + ', nombre: ' + self.__nombre + ', precio: ' + str(self.__precio)

class Pedidio:
    def __init__(self, productos, cantidades):
        self.__productos = productos
        self.__cantidades = cantidades
    def total_pedido(self):
        total = 0

        for (p,c) in zip(self.__productos, self.__cantidades):
            total = total + p.calcular_total(c)

        return total
    
    def mostrar_predido(self):
        for (p,c) in zip(self.__productos, self.__cantidades):
            print('Producto -> ', p.nombre, ', Cantidad: ' + str(c))   

p1 = Producto(1,'Producto 1', 7)
p2 = Producto(2,'Producto 2', 20)
p3 = Producto(3,'Producto 3', 60)

print(p1)
print(p2)
print(p3)

print(p1.calcular_total(4))
print(p2.calcular_total(7))
print(p3.calcular_total(10))

Productos = [p1, p2, p3]
cantidades = [5, 13, 8]

Pedidio = Pedidio(Productos, cantidades)

print('Total pedido: ' + str(Pedidio.total_pedido()))

Pedidio.mostrar_predido()