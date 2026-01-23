#problem A
# Health of monster is H
# health after attack = H - A
# serval wins when monster's health becomes 0 or below 
# number of attacks serval needs before winning  == how many times to subtract until H becomes 0 or below 

H, A = map(int, input().split())
no_of_attacks = (H + A - 1) // A
print(no_of_attacks)
