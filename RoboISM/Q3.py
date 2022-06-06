def calc(a,opr,b):
    res=0
    if opr=="+":
        res=a+b
    elif opr=="-":
        res=a-b
    elif opr==".":
        res=a*b
    elif opr=="/":
        res=a/b
    else:
         res="invalid operator"
    return res

print(calc(4,".",6))