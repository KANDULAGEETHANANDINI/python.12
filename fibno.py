t1=0
t2=1
nextterm=t1+t2
t=3
n=10
fibno=[ ]
while t <= n
    fibno.append(nextterm)
    t1=t2
    t2=nextterm
    nextterm=t1+t2
    t=t+1
print(fibno)