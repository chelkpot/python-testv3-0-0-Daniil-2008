# tasks/task5.py

def solve():
# Ниже пишите решение задачи

    a=int(input())
    b=a//60//60
    c=a//60%60
    a%=60
    if a//10==0:
        a='0'+str(a)
    if c//10==0:
        c='0'+str(c)
    
    print(b, c, a, sep=':')
   
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()