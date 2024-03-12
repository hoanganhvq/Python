# #Normal Agruments
# def  add(n1):
#     print(n1)
#
# add(n1 = 2)
# #*Agrus
# def add(*args):
#     result = 0
#     for number in args:
#         result = result+  number
#     return result
#
# print(add(1,2,3,4,5))

#**kwargs
def caculate(n,**kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    n +=kwargs["add"]
    n *=kwargs["multiple"]
    print(n)
caculate(2,add =3, multiple=2)

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.seat = kwargs.get("seats")
        self.color = kwargs.get("color")


my_car = Car(make="Ford")
print(my_car.model)