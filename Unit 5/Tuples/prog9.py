T1 = ((10, 'A'), (20, 'B'), (30, 'C'))

T2, T3 = zip(*T1)

print(T2)
print(T3)

T4 = zip(*T1)
print(T4)