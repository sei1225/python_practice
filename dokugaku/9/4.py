import csv

data = [["トップガン", "リスキービジネス", "マイノリティリポート"],
        ["タイタニック", "ザ・レブナント", "インセプション"],
        ["トレーニングデイ","マンオンファイア","フライト"]]

with open("chinemaJapanese.csv","w",newline='',encoding="utf-8") as f:
    w = csv.writer(f,delimiter=",")
    for i in data:
        w.writerow(i)