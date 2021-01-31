import csv

data = [["TopGun", "RiskyBuisiness", "MinorityReport"],
        ["Titanic", "TheRevenant", "Inception"],
        ["TraininingDay","ManonFire","Flight"]]

with open("chinema.csv","w",newline='') as f:
    w = csv.writer(f,delimiter=",")
    for i in data:
        w.writerow(i)