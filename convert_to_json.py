import json


class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age





name=input("enter the name")
age=input("eter your age")
p1=Person(name,age)
res = json.dumps(p1.__dict__)

print(res)