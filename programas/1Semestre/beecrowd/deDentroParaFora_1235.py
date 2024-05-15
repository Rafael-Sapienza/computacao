def desembralhe(string):
    comprimento = len(string)
    s1 = string[0:comprimento//2]
    s2 = string[comprimento//2:]
    s1 = s1[::-1]
    s2 = s2[::-1]
    string = s1+s2
    print(string)

def main(n):
    for _ in range(n):
        string = input()
        desembralhe(string)

n = int(input())
main(n)