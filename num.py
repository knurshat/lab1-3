x = 1     # int
y = 2.8   # float
z = 1j    # complex
print(type(x),", ", type(y),", ", type(z))



x = 1
y =12345679081232435475769879
z = -123565768
print(type(x),", ", type(y),", ", type(z))


x = 35e3
y = 12E4
z = -87.7e100

print(type(x),", ", type(y),", ", type(z))

x = 3+5j
y = 5j
z = -5j

print(type(x),", ", type(y),", ", type(z))

x = 1     # int
y = 2.8   # float  
z = 1j    # complex 

a = float(x)
b = int(y)
c = complex(z)

print(a, b, c)
print(type(a), ", ", type(b), ", ", type(c) )