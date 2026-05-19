#PYTHON SUMMER 2026 DAY 2
#VARIABLES, EXPRESSION, AND STATEMENTS
import math
text = "Messi" #string
print(text)

num = 10 #int
print(num)

avg = 92.85 #float
print(avg)

exp1 = 2**5 #exponent
print(exp1)

#string concatenation
word1 = "Test"
word2 = "Py"
word3 = word1 + word2
print(word3)
print(f"{word1} {word2}")
print()

#EXERCISES
#VOLUME OF A SPHERE
print("Example 1")
r = 5
v = (4/3) * math.pi * r**3
print(f"Volume is {v}")
print()

print("Example 2")
coverprice = 24.95
discount = 0.4 #40%
shipping = 3 #dollars for first 3
shippingextra = .75 #cents for each additional copy
copies = 60
cost = (24.95 * 60) - ((24.95 * 60) * discount) + (3 * 1) + (shippingextra * (copies - 1))
print(f"Total cost is {cost}")
print()