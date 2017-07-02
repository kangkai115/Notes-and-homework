##def encrypt(old_str):
##    if type(old_str)==str:
##        new_str=[]
##        for word in old_str:
##            new_str.append(chr(ord(word)+1))
##        return ''.join(new_str)
##    else:
##        print('输入有误，请输入字符串')
##
##def decrypt(old_str):
##      if type(old_str)==str:
##        new_str=[]
##        for word in old_str:
##            new_str.append(chr(ord(word)-1))
##        return ''.join(new_str)
##      else:
##        print('输入有误，请输入字符串')
class Encrypt(str):
    def __init__(self,string):
        super().__init__()
        self.string=string
        
    def encrypt(self):
        if isinstance(self.string,str):
            temp=''
            for i in self.string:
                if i>='a' and i<='z':
                    if i=='z':
                        temp+='a'
                    else:
                        temp+=chr(ord(i)+1)
                else:
                    temp+=i
            return temp

    def decrypt(self):
        if isinstance(self.string,str):
            temp=''
            for i in self.string:
                if i>='a' and i<='z':
                    if i=='a':
                        temp+='z'
                    else:
                        temp+=chr(ord(i)-1)
                else:
                    temp+=i
            return temp

