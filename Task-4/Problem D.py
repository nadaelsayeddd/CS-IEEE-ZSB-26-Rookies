s1 = input().strip()
s2 = input().strip()

final_position = s1.count('+') - s1.count('-')
current_position = s2.count('+') - s2.count('-')
q = s2.count('?')

def calculate(i, position):
    if i == q:
        return 1 if position == final_position else 0
    return calculate(i+1, position+1) + calculate(i+1, position-1)

print(calculate(0, current_position) / (2 ** q))
