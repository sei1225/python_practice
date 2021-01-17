num1 = int(input("１つ目の数は？"))
num2 = int(input("2つ目の数は？"))

# 足し算をする
answer = num1 + num2
print(answer)

# 偶数か帰趨を判断する
if(answer % 2 == 1):  # 割り切れなければ
    print('奇数です')
else:
    print('偶数です')
