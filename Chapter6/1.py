a = 3
print("a = ", a)
print("type(a) = ", type(a) )
a = 'spam'
print("a = ", a)
print("type(a) = ", type(a) )
a = 1.23
print("a = ", a)
print("type(a) = ", type(a) )

a = 3
b = a
a = 'spam'

print("a = ", a)
print("b = ", b)

a = 3
b = a
a = a + 2

print("a = ", a)
print("b = ", b)

L1 = [2, 3, 4]
L2 = L1
L1[0] = 24

print("L1 = ", L1)
print("L2 = ", L2)

L1 = [2, 3, 4]
L2 = L1[:]
L1[0] = 24

print("L1 = ", L1)
print("L2 = ", L2)
