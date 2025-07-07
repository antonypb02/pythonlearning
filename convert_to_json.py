import json


class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age





p1=Person("alice",30)

res = json.dumps(p1.__dict__)

print(res)