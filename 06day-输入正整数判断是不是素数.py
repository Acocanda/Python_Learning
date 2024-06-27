number=int(input('请输入一个数字：'))
i=int(number/2)+1
for j in range(2,i):
    if number%j==0:
        print('这不是素数')
        break
print('这是素数')
