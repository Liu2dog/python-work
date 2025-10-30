# 1）B
# 2) D
# 3) C
# 4) D
# 5) A

# 1.
# paper = 0.00008
# fold = 0
# while paper < 8848.13:
#     fold += 1
#     paper = paper*2
# print(fold)

# 2.
# char = input()
# num = ''
# for i in char:
#     if i.isdigit():
#         num += i
# print(num)

# 3.
# while True:
#     a = float(input('边a长：'))
#     b = float(input('边b长：'))
#     c = float(input('边c长：'))
#     if a+b>c and a+c>b and b+c>a:
#         d = a+b+c
#         print(f'你输入的三角形周长为：{d}')
#         break
#     else:
#         print('请输入正确的边长')

# 4.
# import random
# random_num = random.randint(1, 100)
# for i in range(1,5):
#     if i <= 3:
#         a = int(input('你输入的数字是：'))
#         if a == random_num:
#             print('恭喜你猜对了')
#             break
#         else:
#             print('猜错了，请重新输入')
#     else:
#         print('游戏结束')
#         break

# import random
# random_num = random.randint(1, 100)
# i = 0
# while True:
#     a = int(input('你输入的数字是：'))
#     if a == random_num:
#         print('恭喜你猜对了')
#         break
#     else:
#         print('猜错了，请重新输入')
#         i += 1
#     if i==3:
#         print('游戏结束')
#         break

# 5.
# username = 'username'
# password = 'password'
# name = '小明'
# age = '19'
# vip = 'lv.6'
# for i in range(1,5):
#     if i <= 3:
#         Username = input('请输入用户名：')
#         Password = input('请输入密码')
#         if Password == password and Username == username:
#             print('恭喜登录成功')
#             print('\t姓名',name)
#             print('\t年龄',age)
#             print('\t会员等级',vip)
#             break
#         else:
#             print('你的用户名或密码输入错误，请重试一次')
#     else:
#         print('连续三次登录失败，已强制退出')
#         break

# 6.
# a = input('您是否有车票：')
# if a == '否':
#     print('您无法上车')
# elif a == '是':
#     b = input('您是否携带危险物品：')
#     if b == '是':
#         print('您无法上车')
#     elif b == '否':
#         print('安检通过，请您上车')