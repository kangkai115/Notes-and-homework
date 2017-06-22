def fun(*tup,**dic):
    dic_keys=list(dic.keys())
    new_dic={}
    for i in range(len(tup)):
        new_dic[dic_keys[i]]=tup[i]
    return new_dic
    
