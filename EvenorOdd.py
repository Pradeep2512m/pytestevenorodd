def Check_EvenorOdd(a):
    if a%2==0:
        return True
    else:
        return False
if __name__=="__main__":
    a=int(input("enter the number"))
    result=Check_EvenorOdd(a)
    print(result)