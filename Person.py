class Person:
    def __init__(self):
        self.__age=0
    
    def get_age(self):
        return self.__age
    
    def set_age(self,age):
        if age>=0:
            self.__age=age
        else:
            print('yas negatif olamaz')

person=Person()
person.set_age(20)

print(person.get_age())
