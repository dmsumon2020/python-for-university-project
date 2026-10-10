Dict1 = { 0: 'Zero', 1 : "One", 2 : 'Two', 3 : 'Three' }

print(Dict1)

for key in Dict1.keys():
    print(key, Dict1.get(key))