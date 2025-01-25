class Person :
    def __init__(self,name,age):
        self._name = name
        self._age = age
    
    def set_name(self,n):
        self._name = n
        
    def get_name(self):
        return self._name
    
    def set_age(self,a):
        self._age = a
    
    def get_age(self):
        return self._age
    
    def get_info(self):
        return f'{self._name}, {self._age}'

def main():
    person_1 = Person('saba',20)
    print(person_1.get_info())
    
    person_2 = Person('gio',17)
    print(person_2.get_info())
    print(person_1.name)
if __name__ == '__main__':
    main()
    
    