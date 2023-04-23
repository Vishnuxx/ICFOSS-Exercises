class MStrings:
    def __init__(_self):
        _self.string = ""

    def get_string(_self , string):
        _self.string = str(string)

    def print_string(_self):
       print((_self.string).upper())



s = MStrings()
value = str(input("Enter your string: "))
s.get_string(value)
s.print_string()