import random

output = str(random.randint(0,1)) + str(random.randint(0,1)) + str(random.randint(0,1)) + str(random.randint(0,1))
listvar = ["0001","0111","1110","1000","1001","0110", "1101","1011"]

if output == "0001":
    ans = "AND"

elif output == "0111":
    ans = "OR"

elif output == "1110":
    ans = "NAND"

elif output == "1000":
    ans = "NOR"

elif output == "1001":
    ans = "EQUAL"

elif output == "0110":
    ans = "XOR"

elif output == "1101":
    ans = "IMPLY"

elif output == "1011":
    ans = "CONVERSE IMPLY"
else: 
    while output not in listvar:
        output = str(random.randint(0,1)) + str(random.randint(0,1)) + str(random.randint(0,1)) + str(random.randint(0,1))

print("output: " + output)
response = input("What is the answer? ")

if response is ans:
    print("Correct!")
else:
    print("Incorrect, answer was " + ans)