# functions more deeply
z = 10
print(f"1st_z: {z}")
z = 5 + 8
print(f"2nd_z: {z}")

# till here scope is global
# below enclosing scope

def math_sum(a, b):
    z = a + b
    print(f"3rd_z: {z}")

print(math_sum(10,8))

# here exit from enclosed scope back to global

print(f"4th_z: {z}")