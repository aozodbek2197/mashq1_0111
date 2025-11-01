# 1-mashq
numbers = tuple(map(int, input("son kirit: ").split()))
print(numbers)

# 2-mashq
numbers = input("Tuple kirit: ")
t = tuple(map(int, numbers.split(',')))
print("Eng katta element:", max(t))

# 3-mashq
tuple1 = input("Tuple1 kirit: ")
tuple2 = input("Tuple2 kirit: ")

tuple = tuple1 + tuple2
print("Birlashtirilgan tuple", tuple)

# 4-mashq
tuple = tuple(map(int, input("Tuple kirit: ").split(',')))
juft_sonlar = []

for x in tuple:
    if x % 2 == 0:
        juft_sonlar.append(x)

print('juft_sonlar:', juft_sonlar)

# 5-mashq
t = tuple(map(int, input("Tuple kirit: ").split(',')))
teskari = t[::-1]
print(teskari)
