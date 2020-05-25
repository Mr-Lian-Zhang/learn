#debug--出错的时候，那行代码出错，就debug打在哪一行上面

#超继承#
#super(子类名,self).方法名()
#当子类里面的方法重写时，需要父类里面的代码，用到超继承
class MathMethond1:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        print(self.a + self.b)
    def sub(self):
        return self.a-self.b
class MathMethond2(MathMethond1):#继承
    def divide(self):
        return self.a/self.b#类的拓展
    def add(self):
        super(MathMethond2,self).add()#超继承
        print(self.a + self.b+10)#类的重写
o=MathMethond2(10,20)
o.add()