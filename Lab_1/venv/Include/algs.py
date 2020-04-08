def my_square(a,b,c,d):
    return (((((a+b)**(0.5))+c)**(0.5))+d)**(0.5)



def alg1(a, b, c):
    return (a/b)**3 + (c/2)**2


def alg2(a, b, c, d):

    if b>4 and c>4 and d>4: return a/b+a*b/c+a*b*c/d
    elif b<4:
        if a!=0 :
            return b/a+c*b/b+d*b*c/c
        else:
            print("Division by zero")
    elif c<4:
        if c!=0 and b!=0 and a!=0:
            return b/c+a*b/b+d*b*a/a
        else:
            print("Division by zero")

def alg3(a,b,c,d):
    if len(a)==len(b)==len(c)==len(d):
        sum = 0
        for i in range(len(a)):
            sum+=my_square(a[i],b[i],c[i],d[i])
    return sum