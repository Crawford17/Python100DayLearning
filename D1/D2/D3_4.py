import math

a = float(input('请输入第一条边长：'))
b = float(input('请输入第二条边长：'))
c = float(input('请输入第三条边长：'))

if a + b > c and a + c > b and b + c >a:
    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p -c))
    print('三角形的面积为：' , s)
else:
    print('不能构成三角形！')