# 输入三条边长，如果能构成三角形就计算周长和面积。
a=float(input('a='))
b=float(input('b='))
c=float(input('c='))
if a+b>c and a+c>b and b+c>a:
    peri=a+b+c
    print('周长：%.2f'%(peri))
    half = peri / 2
    area = (half * (half - a) * (half - b) * (half - c)) ** 0.5
    print('面积：%.2f'%area)
else:
    print('这不是三角形')
