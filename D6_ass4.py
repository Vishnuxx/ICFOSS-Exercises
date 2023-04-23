import string


class Reversible:
    def __init__(_self , string):
        _self.string = str(string)

    def reverse(_self):
        strin = ""
        for i in _self.string.split(" "):
            strin = i + " " + strin
        print(strin)


name = Reversible("hello world is the thing")
name.reverse()