if __name__ == '__main__':
    for i in range(100,1000):
        a=i//100
        b=(i//10)-a*10
        c=i-a*100-b*10

        if a**3+b**3+c**3 == i:
            print(i)