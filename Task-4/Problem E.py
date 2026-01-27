s = input().strip()
results = set()

def generate(first, final):
    if not final:
        results.add(first)
        return
    for i in range(len(final)):
        generate(first + final[i], final[:i] + final[i+1:])

generate("", s)
new_strings = sorted(results)
print(len(new_strings))
for string in new_strings:
    print(string)
