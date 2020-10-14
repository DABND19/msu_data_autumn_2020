num_count = int(input())

result = list()

for i in range(0, num_count):
    num = int(input())
    if result.count(num) == 0:
        result.append(num)

for num in result:
    print(num, end=' ')
print()
print(num_count - len(result))
