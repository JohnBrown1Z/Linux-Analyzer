


x=1
y=True
s=[]
t=("a",)
print(x==y)
print(x is y)
print(hash(x))
print(hash(y))
try:
    print(hash(s))
except:
    print("An error occured")
print(hash(t))



