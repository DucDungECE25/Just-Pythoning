a = 0;
b = 0;
c = 0;
d = 0;

print("Q1) Do you like Dawn or Dusk?")
Q1 = int(input("Enter your answer (1 or 2): "))
if Q1 == 1:
  a = a + 1;
  b = b + 1;
  print("\nGryffindor and Ravenclaw both get 1 point!")
elif Q1 == 2:
  c = c + 1;
  d = d + 1;
  print("\nHufflepuff and Slytherin both get 1 point!")
else:
  print("Wrong input.")

print("\nQ2: When you're dead, what do you want people to remember you as?")
print("    1) The Good")
print("    2) The Great")
print("    3) The Wise")
print("    4) The Bold")
Q2 = int(input("Enter your answer (1-4): "))
if Q2 == 1:
  c = c + 2; 
  print("\nHufflepuff gets 2 points.")
elif Q2 == 2:
  d = d + 2;
  print("\nSlytherin gets 2 points.")
elif Q2 == 3:
  b = b + 2;
  print("\nRavenclaw gets 2 points.")
elif Q2 == 4: 
  a = a + 2; 
  print("\nGryffindor gets 2 points.")
else:
  print("\nWrong input.")

print("\nQ3: Which kind of instrument most pleases your ear?")
print("    1) The violin")
print("    2) The trumpet")
print("    3) The piano")
print("    4) The drum")
Q3 = int(input("Enter your answer (1-4): "))
if Q3 == 1:
  d = d + 4;
  print("\nSlytherin gets 4 points.")
elif Q3 == 2:
  c = c + 4; 
  print("\nHufflepuff gets 4 points.")
elif Q3 == 3:
  b = b + 4;
  print("\nRavenclaw gets 4 points.")
elif Q3 == 4: 
  a = a + 4; 
  print("\nGryffindor gets 4 points.")
else:
  print("\nWrong input.")

print("Gryffindor:", a, "points")
print("Ravenclaw:", b, "points")
print("Hufflepuff:", c, "points")
print("Slytherin:", d, "points")

# Bonus:
if a>=b and a>=c and a>=d:
  print("\n🦁 Gryffindor!")
elif b>=c and b>=d:
  print("\n🦅 Ravenclaw!")
elif c>=d:
  print("\n🦡 Hufflepuff!")
else:
  print("\n🐍 Slytherin!")