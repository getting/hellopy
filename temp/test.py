class Person():
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.getter
    def name(self):
        return self.__name + 'jj'

    @name.setter
    def name(self, value):
        self.__name = value + 'kk'


if __name__ == '__main__':
    p = Person('jim', 20)
    p.name = 'jj'
    print(p.name)