
hobby = input('あなたの趣味は何ですか？')

with open("hobby.txt", "w", encoding="utf-8")as f:
    f.write(hobby)
