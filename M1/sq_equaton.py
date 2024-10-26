eq = input()

eq = eq.replace(' ','').replace('+','').replace('(','').replace(')','')
ap = eq.find('x^2')

a = int(eq[:ap])
print('a =',a)

eq = eq[ap+3:]
bp = eq.find('x')

b = int(eq[:bp])
print('b =',b)

eq = eq[bp+1:]
cp = eq.find('=')

c = int(eq[:cp])
print('c =',c)

x1 = int((-b+(b**2-4*a*c)**(1/2))/(2*a))
x2 = int((-b-(b**2-4*a*c)**(1/2))/(2*a))

print('x1 =',x1)
print('x2 =',x2)