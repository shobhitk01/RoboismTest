def hidenums(num):
    nums=str(num)
    n= len(nums)-4
    ld = num%10
    sld = (num//10)%10
    tld = (num//100)%10
    fld = (num//1000)%10
    hidden="*"*n+str(fld)+str(tld)+str(sld)+str(ld)
    return hidden

number= 4865254789
print(hidenums(number))