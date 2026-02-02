s1={1,23,43,34}
s2={32,44,32,64}

print(s1.union(s2))

print(s1.intersection(s2))

print({23,43}.issubset(s2))

print(s1.issuperset(s2))