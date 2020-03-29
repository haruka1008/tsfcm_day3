# print(3+4)
# print(3 + 6)   # 足し算
# print(3 - 6)   # 引き算
# print(3 * 6)   # 掛け算
# print(3 / 6)   # 割り算
# print(7 % 2)   # あまりを表示
 
# # ctr + / でコメント（解除）
# print("Hello World!!")
# print('Hello World!!' * 3) #繰り返す
# print("-" * 20)
# print("hello " + "world")
# print(4 == 4)  # True
# print(4 == 3)   # False

# x = 4   # x に4を代入
# y = 3   # y に3を代入
# print(x + y)

# x = x + y
# print(x)
# y = y * y - x
# print(y)

# a = "hello " + "world"
# print(a)
# b = str(2) + "hello"
# print(b)

# lis = [2,3,-5,6]
# tup = ('鈴木','佐藤','加藤','本田')
# dic = {
#        'A001': 34,        # key: value,
#        'A002': 'Hello',   # key: value,
# }

# # list 型、tuple 型は番号を指定する
# print(lis[2])       # 3番目のデータ
# print(tup[1])        # 2番目のデータ

# # dict 型は key を指定する
# print(dic['A001'])   # A001 のデータ

# print(lis[-1])

# a = 'Hello'
# b = 3
# c = 6.0
# d = True
# lis = [1,3,5,7]
# tup = (3,5,8,1)
# dic = {'A001':34,'A002':38}

# # print(type(a))
# # print(type(b))
# # print(type(c))
# # print(type(d))
# # print(type(lis))
# # print(type(tup))
# # print(type(dic))

# print(type(lis[0]))

# x = 0
# x = x + 1
# print(x)
# x = x + 1
# print(x)
# x = x + 1
# print(x)
# x = x + 1
# print(x)
# x = x + 1
# print(x)

# for x in range(5):#:を打ったらその次は必ず空白を！”:”は”ブロック”という考え方で、ブロックごとにxの内容が決まる
#     x = x + 1
#     print(x)

# range()は中に数字を入れるとその数分実行してくれる
# for分のデフォルトはx=0

# x = 4
# if x == 3 :
#    print("xは3です") 
# else:
#    print("xは3ではない")

# x = 14 # = 代入、＝＝比較（等しいか）
# if x > 9 :
#    print("xは10以上です")
# elif x == 0:
#    print("xは0です。")
# else:
#    print("xは0より小さいです。")

# 関数の認識は"def"
# def multi(x, y):
#     return(x * y)

# # 使い方
# print(multi(3,4) )    # 結果は12
# print(multi(-2,15) )  # 結果は-30  

# class calc():
#     def __init__(self,x,y):
#         self.minus = x - y
#         self.plus = x + y
#         self.multi = x * y
#         self.divis = x / y

# # 使い方
# print(calc(3,4).multi)
# print(calc(-2,15).multi)
# print(calc(3,4).minus)
# print(calc(-2,15).plus)


# Fizz Buzz の問題にチャレンジしてみよう！

# 1~100までの数字で、
# 3で割り切れれば、「Fizz!」を表示する
# 5で割り切れれば、「Buzz!」を表示する
# 3と5で割り切れれば、「Fizz Buzz!」を表示する
# 上記以外の場合は、そのままの数字を表示する
# ヒント：for 文と if 文を組み合わせる

for i in range(1, 100):
  if i % 15 == 0:
    print("Fizz Buzz!")
  elif i % 3 == 0:
    print("Fizz!")
  elif i % 5 == 0:
   print("Buss!")
  else:
    print(i)