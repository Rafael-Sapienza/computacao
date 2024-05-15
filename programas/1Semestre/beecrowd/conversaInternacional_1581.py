def main(n):
    for _ in range(n):
        flag = True
        k = int(input())
        x = input()
        for i in range(k-1):
            y = input()
            if x != y:
                flag = False
        if flag:
            print(x)
        else:
            print('ingles')
        
n = int(input())
main(n)