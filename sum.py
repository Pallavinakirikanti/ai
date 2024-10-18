import random
a=int(input("enter the size of passsword"))
char=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
num=["1","2","3","4","5","6","7","8","9","0"]
special=[")","(","*","&","^","%","$","@","!"]
alphabet=char+num+special
password=" "
for i in range(1,a+1):
      password=password+random.choice(alphabet)
print("password generated:",format(password))
