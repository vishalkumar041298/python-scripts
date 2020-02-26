def argss(*args):
    for i in args:
        print(i)
    print (sum(args)*0.05)
argss(40,60,60)

def kwargss(**kwargs):
    print(kwargs)
    if "hi" in kwargs:
        print(kwargs["hi"])
    else:
        print("no hi")
kwargss(hiii=1,hii=2)

def combined(*a,**b):
    print("len of args:",len(a))
    for i in a:
        print (i)
    print("len of kwargs:",len(b)) 
    for i in b:
        print(b[i])

combined(1,2,3,l="hello",m="world")