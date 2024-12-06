class person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gen=gender
    
    def gender(self):
        print(f'I\'am {self.name} and im a {self.gen}.')
    
    def greeting(self):
        print(f'Hello everyone!. My age is {self.age}.')

ragul =person('ragul',22,'Male')
gokul=person('gokul',28,'Male')
vidya=person('vidya',52,'Female')

ragul.gender()
ragul.greeting()
print('\n')
gokul.gender()
gokul.greeting()
print('\n')
vidya.gender()
vidya.greeting()



