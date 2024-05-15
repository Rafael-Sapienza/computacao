def main(n):
    for _ in range(n):
        s = input()
        x,y,z = s
        x = int(x)
        z = int(z)
        if x==z:   
            print(x*z)
        else:
            if y.isupper():
                print(z-x)
            else:
                print(z+x)
                
n = int(input())
main(n)