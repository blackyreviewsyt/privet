str = input("Введите строку   ")
str1="zzz" 
if str[0:3]=="abc" : 
    str=str.replace(str[0:3],"www") 
else : 
    str=str+str1 
print(str) 
