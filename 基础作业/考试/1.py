def fun1(old_str):
        if type(old_str)==str:
            old_list=old_str.split(' ')
            new_list=[]
            for word in old_list:
                new_list.append(word.capitalize())
            return ' '.join(new_list)          
        else:
            print('您的内容输入有误，请输入字符串')
        
