import random
best = None
try:
    with open("best_score.txt","r")as f:
        best = int(f.read())
except:
    pass
while True: # 控制玩几局
    answer = random.randint(1,100) # 每局不同答案
    count = 0 # 每局重新计数
    print("\n====猜数字游戏====")
    print("我想好了一个1到100之间的数字，来猜猜看吧！")
    while True: # 控制一局猜几次
        guess_str = input("请输入你猜的数字")
        if not guess_str.isdigit():
            print("请输入有效整数！")
            continue
        guess = int(guess_str)
        count +=1
        if guess > answer:
            print("猜大了，再小一点！")
        elif guess < answer:
            print("猜小了，再大一点！")
        else:
            print(f"恭喜你猜对啦！答案就是{answer}")
            print(f"你一共猜了{count}次")
            if best is None or count < best:
                print("新纪录!")
                with open("best_score.txt","w")as f:
                    f.write(str(count))
                best = count
            else:
                    print(f"历史最好的成绩是{best}次")
            break
        
            again = input("\n再来一局？(y/n):") # 一局结束问要不要再来
            if again != "y":
                print("谢谢游玩，再见！")
                break # 游戏结束
