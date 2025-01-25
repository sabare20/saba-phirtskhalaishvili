class Student:
    def __init__(self,name):
        self._name = name
        self._scores = []
        
    def add_score(self,score):
        if 0 <= score <= 100:
            self._scores.append(score)
        else:
            print('invalid score.entered value must be from 0 to 100')
    
    def get_average(self):
        if not self._scores:
            return 0
        else:
            return sum(self._scores) / len(self._scores)
            
    def get_score(self):
        return self._scores
    def get_name(self):
        return self._name
    
def main():
    student = Student('avto')
    student.add_score(99)
    student.add_score(96)
    student.add_score(100)
    student.add_score(98)
    print(student.get_score())
    print(student.get_average())

if __name__ == '__main__':
    main()
        