def power_direct(a, b):
    p = 1
    while b > 0:
        p = p * a
        b -= 1
    return p

print(f"3^2 = {power_direct(3,2)}")
print(f"3^4 = {power_direct(3,4)}")
print(f"2^8 = {power_direct(2,8)}")

def power_recursion(a,b):
    if b == 0:
        p = 1
    else:
        p = a * power_recursion(a, b - 1)
    return p

print(f"3^2 = {power_recursion(3,2)}")
print(f"3^4 = {power_recursion(3,4)}")
print(f"2^8 = {power_recursion(2,8)}")

#for clear version
def make_blanks(n):
    return "  " * n

def power(a, b, level):
    print(f"{make_blanks(level)}Level {level}: b = {b}")

    if b == 0:
        p = 1
    else:
        p = a * power(a, b - 1, level + 1)

    print(f"{make_blanks(level)}Level {level}: p={p}")
    return p

p = power(3, 2, 0)
print(f"3^2 = {p}")