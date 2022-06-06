def intsum(string):
    i=0
    sum=0
    while i < len(string):
        if string[i]=="1" or string[i]=="2" or string[i]=="3" or string[i]=="4" or string[i]=="5" or string[i]=="6" or string[i]=="7" or string[i]=="8" or string[i]=="9" or string[i]=="0":
            sum= sum + int(string[i])
        i=i+1
    return sum

print(intsum("shobhit28water17"))