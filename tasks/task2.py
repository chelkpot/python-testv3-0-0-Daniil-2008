# tasks/task2.py

def solve():
# Ниже пишите решение задачи

   a=int(input())
   if a//1440!=0:
      print(a%1440//60, 59)
   else:
      print(a//60, a%60)

   
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()