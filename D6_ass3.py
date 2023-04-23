from tkinter import W


class Rectangle:
    def __init__(_self , width , height):
        _self.width = int(width)
        _self.height = int(height)

    def calculate_area(_self):
        return _self.width * _self.height




rect = Rectangle(10 , 20)
print(rect.calculate_area())