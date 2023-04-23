from itertools import product
from operator import truediv


class Product:
    def __init__(_self , name , price , weight , brand):
        _self.name = name
        _self.price = price
        _self.weight = weight
        _self.brand = brand
        _self._status = "onSale"
        _self._sold = False
        _self._tax = 0
    
    def display(_self):
        print("Name : " + _self.name)
        print("Price : " + _self.price)
        print("Weight : " + _self.weight)
        print("Brand : " + _self.brand)

    def status(_self , type):
        _self._status = type

    def tax(_self):
        value = int(input("Enter the tax amount: "))
        print("Price including tax is {}".format(_self.price))
    
    def sell(_self):
        _self._status = True

    def isSold(_self):
        return _self._sold



class Store:
    def __init__(_self , owner , location):
        _self.owner = owner
        _self.location = location
        _self.products = []

    def listProducts(_self):
        for i in _self.products:
            print("name: {} , price: {} , weight: {} , brand: {}".format(i.name , i.price , i.weight , i.brand))

    def addProduuct(_self , product):
        _self.products.append(product)





store = Store("Vishnu" , "Trivandrum")
store.addProduuct(Product("banana" , 30 , 1 , "organic"))
store.addProduuct(Product("juice" , 50 , 2 , "tropicana"))
store.addProduuct(Product("biscuit" , 20 , 3 , "britania"))
store.addProduuct(Product("cake" , 300 , 4 , "blackforest"))
store.listProducts()