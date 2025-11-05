A = float(input("Enter the coefficient of the x^2: "))
B = float(input("Enter the coefficient of the x: "))
C = float(input("Enter the constant: "))

discriminant = B*B - 4*A*C

if discriminant > 0:
    x1 = ((-B + discriminant**0.5)/2*A)
    x2 = ((-B - discriminant**0.5)/2*A)
    x1 = round(x1, 2)
    x2 = round(x2, 2)    
    print("The equation has two real and distinct roots: ", x1, '', x2)
elif discriminant == 0:
    x1 = (-B/(2*A))
    x1 = round(x1, 2)
    print("The equation has one real root: ", x1)
else:
    print("The equation has no real roots.")