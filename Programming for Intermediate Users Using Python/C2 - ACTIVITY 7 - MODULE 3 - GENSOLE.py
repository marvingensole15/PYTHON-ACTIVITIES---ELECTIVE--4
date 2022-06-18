
x = 50
if x > 100:
    raise Exception("This code will result in an error if x is bigger than 100.")

variable_1 = 'variable is not yet defined'
try:
    print(variable_1)


except:
    print("variable_1 is not yet defined")

try:
    print(12 * 6)
except:
    print("This operation can't be performed.")
else:
    print("This operation can be performed.")

for i in range(6):
    print("I'm so happy!")



best_burger = "Burger King"
number_2_burger = "McDonald's"

assert best_burger == "Burger King"
assert number_2_burger == "McDonald's"

