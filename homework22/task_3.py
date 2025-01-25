class Stack:
    def __init__(self):
        self.elements = []

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        if self.elements:
            return self.elements.pop()
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if self.elements:
            return self.elements[-1]
        else:
            raise IndexError("Stack is empty")

    def is_empty(self):
        return len(self.elements) == 0

    def size(self):
        return len(self.elements)
    
def main():
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)
    print(s.peek())  
    print(s.pop())  
    print(s.size()) 
    print(s.is_empty()) 
    s.pop()
    s.pop()
    print(s.is_empty())  
if __name__ == '__main__':
    main()