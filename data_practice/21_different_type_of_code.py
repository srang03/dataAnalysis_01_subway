personinfo = [
    "김유리,23,대전,여",
    "김현민,26,서울,남",
    "이현우,23,부산,남"
]

#1 일반적인 함수
print("1. 일반적인 함수")
def get_name(row):
    split = row.split(',')
    return split[0]

for row in personinfo:
    print(get_name(row))

print("2. list comprehension")
#2 list Comprehension
name_list = [get_name(row) for row in personinfo]
print(name_list)

print("3. map")
#3  map 
name_map = map(get_name, personinfo)
for i in name_map:
    print(i)

print("4. map with lambda")
#4 map with lambda
name_map_lambda = map(
    lambda row: row.split(',')[0], personinfo
)

for i in name_map_lambda:
    print(i)
