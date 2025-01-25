class ExtendedList(list):
    def min(self):
        if not self:
            raise ValueError("The list is empty")
        return min(self)

    def max(self):
        if not self:
            raise ValueError("The list is empty")
        return max(self)
def main():
    el = ExtendedList([3, 1, 4, 1, 5])
    print(el.min())
    print(el.max())  
    el.append(10)
    print(el.min()) 
    int(el.max())
if __name__ == '__main__':
    main()
     