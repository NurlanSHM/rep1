print("This is a calculator")
print(" ")

globalVAR = int(input("Enter a number:"))
globalVAR2 = str(input("Enter an operator: "))
globalVAR3 = int(input("Enter a second number: "))

if globalVAR2 == "*":
    localVAR2 = globalVAR
    localVAR3 = globalVAR3
    result = localVAR2 * localVAR3
    print(result)

elif globalVAR2 == "/":
    localVAR4 = globalVAR
    localVAR5 = globalVAR3
    result2 = localVAR4 / localVAR5
    print(result2)

elif globalVAR2 == "-":
    localVAR6 = globalVAR
    localVAR7 = globalVAR3
    result3 = localVAR6 - localVAR7
    print(result3)

elif globalVAR2 == "+":
    localVAR8 = globalVAR
    localVAR9 = globalVAR3
    result4 = localVAR8 + localVAR9
    print(result4)

else:
    if globalVAR3 == 0 and globalVAR2 == "/":
        print("cannot divide by 0")
