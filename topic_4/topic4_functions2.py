#def math_sum(a, b):
#    z = a + b
#    return z
#sum = math_sum(3,5)
#print(sum)

# function as a method for another function

def power(base, exponent):
    return base**exponent


def power_2(method, exponents):
    result = list()
    for exp in exponents:
        result.append(method(2, exp))
    return result


answers = power_2(power, [2,4,6,10,15])
print(answers)
