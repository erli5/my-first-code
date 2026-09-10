import random
# 生成1-100之间随机整数
answer = random.randint(1,100)
print("====猜数字游戏====")
print("我想好了一个1到100之间的数字,来猜猜看吧!")
count = 0 # 记录猜的次数
best =None
try:
    with open("best_score.txt","r") as f:best = int(f.read())
except:
    pass # 第一次运行，文件不存在，跳过
while True:
    # 获取用户输入
    guess_str = input("请输入你猜的数字:")

    # 判断不是数字
    if not guess_str.isdigit():
        print("请输入有效的整数!")
        continue

    guess =int(guess_str)
    count =count + 1
    if guess > answer:
        print("猜大了，再小一点!")
    elif guess < answer:
        print("猜小了，再大一点!")
    else:
        print(f"恭喜你猜对啦!答案就是{answer}")
        print(f"你一共猜了{count}次")
        if best is None or count < best:
            print("新纪录！")
            with open("best_score.txt","w") as f:
                f.write(str(count))
        else:
            print(f"历史最好的成绩是{best}次，加油！")

        break


