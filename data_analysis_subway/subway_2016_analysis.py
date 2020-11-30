import csv
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

font = fm.FontProperties(fname='./NanumBarunGothic.ttf')
data = csv.reader(open('./data/subway_2016.csv', 'r', encoding='utf-8'), delimiter=",")

num_passenger1 = []
num_passenger2 = []
station1 = '신림'
line1 = '2호선'
station2 = '강남'
line2 = '2호선'

for row in data:
    if row[1] == station1 and row[0] == line1:
        num_passenger1 = row[2:]
    if row[1] == station2 and row[0] == line2:
        num_passenger2 = row[2:]

get_on1 = num_passenger1[::2]
get_off1 = num_passenger1[1::2]

get_on2 = num_passenger2[::2]
get_off2 = num_passenger2[1::2]

get_on1 = [int(g) for g in get_on1]
get_off1 = [int(g) for g in get_off1]
get_on2 = [int(g) for g in get_on2]
get_off2 = [int(g) for g in get_off2]


labels = []
x = []
for i in range(4, 28):
    labels.append(str(i)+'시')
    x.append(i)

plt.xticks(x, labels, rotation='vertical', fontproperties=font)
plt.plot(x, get_on1, 'r', label=station1+'역 승차')
plt.plot(x, get_on2, 'b', label=station2+'역 승차')
plt.ylim(ymax=420000)

plt.xticks(x, labels, rotation='vertical')
plt.plot(x, get_off1, 'r--', label=station1+'역 하차')
plt.plot(x, get_off2, 'b--', label=station2+'역 하차')
plt.ylim(ymax=420000)

plt.title(station1+'역 승하차 인원 vs '+station2+'역 승하차 인원  \n # 2016년 6월 티머니카드 제공 데이터', fontproperties=font)
plt.legend(prop=font)

plt.savefig("image.svg", format="svg")

