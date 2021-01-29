corList = [1, 3, 5, 7, 9]
cnt = 1
while (True):
    ans = input("数字を入力してください.qで終了します.\n")
    if(ans == "q"):
        break
    else:
        try:
            ans = int(ans)
            if(ans in corList):
                print("正解です！あなたは{}回目で正解しました。".format(cnt))
                break
            else:
                print("不正解です")
                if(cnt > 2):
                    print("ヒント:奇数")
                cnt += 1
        except ValueError:
            print("数字もしくはqを入力してください")
