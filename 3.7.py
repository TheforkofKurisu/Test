if __name__ == '__main__':
    Num=int(input("请输入金额："))
    Money=0
    if Num<=100000:
        Money=Num*0.1
    elif Num>100000 and Num <200000:
        Money=10000+(Num-100000)*0.075
    elif Num>200000 and Num<400000:
        Money=17500+(Num-200000)*0.05
    elif Num>400000 and Num<600000:
        Money=27500+(Num-400000)*0.03
    elif Num>600000 and Num<1000000:
        Money=39500+(Num-600000)*0.01

    print(Money)
