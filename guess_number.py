import random
best = None
try:
    with open("best_score.txt","r") as f:
        best = int(f.read())
except:
    pass # 文件不存在跳过

while True:
    answer = random.randint(1,100)
    count = 0

    print("\n"+"="*20)
    print("猜数字游戏")
    print("="*20)
    print("我想好了一个1到100之间的数字，来猜猜看吧")

    while True: # 内层：控制一局里猜几次
          guess_str = input("请输入你猜的数字:")

          if not guess_str.isdigit():
              print("请输入有效的整数！")
              continue

          guess = int(guess_str)
          count += 1

          if guess > answer:
              print("猜大了，再小点！")
          elif guess < answer:
              print("猜小了，再大点！")
          else:
              print(f"恭喜你猜对啦！答案就是{answer}")
              print(f"你一共猜了{count}次")

              if best is None or count < best:
                  print("新纪录！")
                  with open("best_score.txt","w") as f:
                      f.write(str(count))
                  best = count # 同步更新内存里记录
              else:
                  print(f"历史最好的成绩是{best}次")

              break # 跳出内层，这局结束

    again = input("再来一局？(y/n):")
    if again != "y":
          print("谢谢游玩！再见！")
          break # 跳出外层，游戏结束
