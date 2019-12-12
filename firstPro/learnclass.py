std1 = {'name':'yuzhengjun','score':100}
std2 = {'name':'jiangjunjun','score':88}

def print_score(std):
    print('%s:  %s' % (std1['name'],std1['score']))

class Student():
    __name = None
    __gender = None

    def __init__(self,name,gender):
        self.__name = name
        self.__gender = gender

    def set_name(self,name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_gender(self,gender):
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def print_score(self):
        print('%s: %s' %(self.name,self.score))


# 测试:
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')

