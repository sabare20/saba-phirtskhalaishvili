class Inset:
    def __init__(self):
        self.elements = []

    def insert(self, element):
        if element not in self.elements:
            self.elements.append(element)

    def member(self, element):
        return element in self.elements

    def remove(self, element):
        if element in self.elements:
            self.elements.remove(element)

    def __str__(self):
        return str(sorted(self.elements))

def main():
    inset = Inset()
    inset.insert(5)
    inset.insert(3)
    inset.insert(5)
    print(inset)  
    print(inset.member(3))  
    print(inset.member(10))  
    inset.remove(3)
    print(inset)  
    inset.remove(10)  
    
if __name__ == '__main__':
    main()