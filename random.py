import random
n=random.randbytes(3)
print(n)
print(random.randrange(1,8))
print(random.randint(100,211))
mylist =["vyshu","Nandu","siri","sreeja"]
mylist1 =["vyshu","Nandu","siri","sreeja"]
print(random.choice(mylist))
#print(random.choice(mylist1))
random.shuffle(mylist)
print(mylist)
