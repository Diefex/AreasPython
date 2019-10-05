
class store:
    def __init__(self, name):
        pass
    def addProduct(self, product):
        pass
class product:
    def __init__(self, name, price):
        pass

class sale:
    def __init__(self, id, products):
        pass
    def addtoCar(self, product):
        pass

    def calcDiscount(self):
        pass

    def calcPrice(self):
        pass


class storeType (store):
    def __init__ (self, name):
        self.name=name
        self.products={}
    def addProduct(self, product):
        self.products.update({product.name:product})

class productType (product):
    def __init__(self, name, price):
        self.name=name
        self.price=price



class saleType(sale):
    def __init__(self, id):
        self.id=id
        self.products={}
        self.price=0


    def addtoCar(self, product, quantity):
        if(product.name in self.products.keys()):
            self.products.update({product.name:(self.products.get(product.name))+quantity})
            self.price+=product.price*quantity
        else:
            self.products.update({product.name:quantity})
            self.price+=product.price*quantity

    def calcDiscount (self):
        val=0
        for i in self.products.values():
            val=i+val
        if (val>=10):
            self.discount=(val-5)//5
        else:
            self.discount=0
        return self.price*self.discount / 100

    def calcPrice(self):
        return self.price - self.calcDiscount()


store1=storeType("Tienda 1")

product1=productType("Producto 1", 200)
product2=productType("Producto 2", 300)
product3=productType("Producto 3", 400)
product4=productType("Producto 4", 450)

store1.addProduct(product1)
store1.addProduct(product2)
store1.addProduct(product3)
store1.addProduct(product4)

sale1=saleType("001")

client=True

text="Seleccione un producto para incluir al carro: \nNombre del producto       Precio\n"
cod=0
for item in store1.products.values():
    cod+=1
    text+=str(cod)+". "+item.name+ "                      "+ str(item.price)+"\n"

text+="0. Terminar Compra"

while(client):

    product=int(input(text))

    if(product == 0):
        client=False
    else:
        p="Producto "+str(product)

        cant=int(input("Seleccione la cantidad de %s" %p))

        sale1.addtoCar(store1.products.get(p), cant)



    car= "Carrito: \nProducto           Cantidad\n"

    for p,c in sale1.products.items():
        car+="%s            %s \n"%(p,c)

    car+="\nPrecio Neto:      "+ str(sale1.price)+"\n"+"Valor de Descuento:       "+str(round(sale1.calcDiscount()))+" \n"+"Precio Total:      "+str(round(sale1.calcPrice()))

    input("%s\nPresione una tecla para continuar..."%car)




