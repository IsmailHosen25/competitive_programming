#  !!! Diff_2

# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

# Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

 

# Example 1:

# Input: num1 = "2", num2 = "3"
# Output: "6"
# Example 2:

# Input: num1 = "123", num2 = "456"
# Output: "56088"
 

# Constraints:

# 1 <= num1.length, num2.length <= 200
# num1 and num2 consist of digits only.
# Both num1 and num2 do not contain any leading zero, except the number 0 itself.

# sol

x = input('Enter the num1 as String x: ')
y = input('Enter the num2 as String y: ')

def multiplys(sx, sy):
    if (sx=="0" or sy=="0"):
        return "0"
    mul = []
    lst1 = list(sx)
    lst2 = list(sy)

    l1 = []
    l2 = []
    for i in lst1:
        l1.append(ord(i)-48)

    for i in lst2:
        l2.append(ord(i)-48)
   
    num1 = 0
    num2 = 0

    while len(l1):
        F = l1.pop(0)
        num1 = (num1*10)+F
        

    while len(l2):
        F2 = l2.pop(0)
        num2 = (num2*10)+F2
    product = num1 * num2

    while product:
        rem = product%10
        mul.append(chr(48+rem))
        product = product // 10
    
    return ''.join(mul[::-1])


    
print(multiplys(x,y))
