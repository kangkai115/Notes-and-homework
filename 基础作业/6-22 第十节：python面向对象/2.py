class Jx():
    def __init__(self,long,wide):
        if isinstance(long,(int,float)) and isinstance(wide,(int,float)):
            self.long=long
            self.wide=wide
    def area(self):
        return self.long*self.wide
class Square(Jx):
    def judge(self):
        if self.long==self.wide:
            return '正方形'
        else:
            return '不是正方形'
