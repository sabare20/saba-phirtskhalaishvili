class Queue:
    def __init__(self):
        self.elements = []

    def insert(self, element):
        self.elements.append(element)

    def pop(self):
        if self.elements:
            return self.elements.pop(0)
        else:
            raise IndexError("Queue is empty")

def main():
    q= Queue()
    q.insert(1)
    q.insert(2)
    q.insert(3)
    print(q.pop()) 
    print(q.pop())  
    print(q.pop())  
if __name__ == '__main__':
    main()