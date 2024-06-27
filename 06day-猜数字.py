import random
num=random.randint(1,100)
counter=0
while True:
    answer=int(input('请输入数字：'))
    if num >answer:
        print('小了')
    elif num<answer:
        print('大了')
    else:
        print('对了！')
        break