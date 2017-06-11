time=int(input('输入日期：'))
year=time/10000
mouth=time%10000/100
day=time%100

print('year=%d,mouth=%d,day=%d'%(year,mouth,day))
