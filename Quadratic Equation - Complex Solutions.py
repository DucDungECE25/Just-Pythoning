import cmath
A = float(input("Enter the coefficient of the x^2: "))
B = float(input("Enter the coefficient of the x: "))
C = float(input("Enter the constant: "))

discriminant = B*B - 4*A*C

# Calculate the two solutions using the quadratic formula
x1 = ((-B + cmath.sqrt(discriminant)))/(2*A)
x2 = ((-B - cmath.sqrt(discriminant)))/(2*A)

if discriminant > 0:
    print("The equation has two real and distinct solutions:", x1.real, "and", x2.real)
elif discriminant == 0:
    print("The equation has one real solution:", x1.real)
else:
    print("The equation has two complex solutions:", x1, "and", x2)



