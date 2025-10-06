# tasks/task2.py

def solve():
# Ниже пишите решение задачи

   a=int(input())
   if a>=2400:
      print(23, 59)
   elif a>1400:
      print(a//60-24, a%60)
   else:
      print(a//60, a%60)

   
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()