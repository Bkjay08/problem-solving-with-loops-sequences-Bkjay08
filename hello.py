# NAME:         James Middleton
# ASSIGNMENT:   Project 1

# Example
def hello_world():
    return "Hello!"

# 1

def squared_sum(lst):

    sum_of_squares = sum(x**2 for x in lst)

    return sum_of_squares

result = squared_sum([])
print(result)

# 2
def mix(a, b):
    return ""

def main():
    print("squared sum: ", squared_sum([-3, 4]))
    print("mix:         ", mix("1234", "abcd") == "1a2b3c4d")

main()
