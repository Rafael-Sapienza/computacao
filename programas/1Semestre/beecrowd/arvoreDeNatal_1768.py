def desenheArvoreDeNatal(base):
    counter = 1
    while counter <= base:
        s = ''
        x = (base-counter)//2
        s += x*' '
        s += counter*'*'
        print(s)
        counter += 2
    counter2 = 1
    while counter2 <= 3:
        s = ''
        x = (base-counter2)//2
        s += x*' '
        s += counter2*'*'
        print(s)
        counter2 += 2

def solveProblem():
    while True:
        try:
            base = int(input())
            desenheArvoreDeNatal(base)
            print('')
        except EOFError:
            break

solveProblem()






