# problem c
t = int(input())
lst = ['Division 1', 'Division 2', 'Division 3', 'Division 4']
ratings = []

for tst in range(t):
    rating = int(input())
    ratings.append(rating)
for n in ratings:
    if n < 5000 and n > -5000:
        if n >= 1900:
            print(lst[0])
        elif n >= 1600 and n <= 1899:
            print(lst[1])
        elif n >= 1400 and n <= 1599:
            print(lst[2])
        elif n <= 1399:
            print(lst[3])