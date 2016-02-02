#!/usr/bin/python
import math
import decimal

P = raw_input("P Pressure of the atm: ")
yita = raw_input("Viscosity of the air(Temperature related, find in graph): ")
b = 8.2*(10**(-3))
rou = 866
vf = raw_input("vf Downward velocity: ")
vr = raw_input("vr Rising velocity: ")
d = raw_input("d Distance between plates: ")
V = raw_input("V the votage that used: ")

P = float(P)
yita = float(yita)
vf = float(vf)
vr = float(vr)
d = float(d)
V = float(V)

a =math.sqrt(((b/2*P)**2) + (9*yita*vf/(2*9.8*rou)))-(b/(2*P))
print "Radius a = %.3E "%decimal.Decimal(a)
m = 4*3.141592653*(a**3)*rou/3
print "Mass m = %.3E "%decimal.Decimal(m)
q =m*9.8*d*(vr+vf)/(V*vf)
print "Charge q = %.3E "%decimal.Decimal(q)

#'%.2E' % Decimal('40800000000.00000000000000')
