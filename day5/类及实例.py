


class Student(object):
    count = 0
    def __init__(self,name):
        self._score = None
        self.name =name
        #类属性的访问方式
        Student.count +=1

    @property
    def score(self):
        return self._score
    @score.setter
    def score(self,value):
        if value>100:
            raise ValueError('score must between 0-100!')
        self._score = value

stu1 = Student('jack')
stu1.score=999
print(stu1.score)
