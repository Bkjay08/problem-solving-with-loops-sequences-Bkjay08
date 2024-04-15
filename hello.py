# NAME:        by James Middleton
# ASSIGNMENT:   Project 1

# Example
def hello_world():
    return "Hello!"
print(hello_world)
# 1
def squared_sum(lst):
    total = 0
    for num in lst:
        total += num ** 2
    return total

# Test Cases
print(squared_sum([]))
print(squared_sum([5, -2, 3]))
print(squared_sum([-3, 4]))
print(squared_sum([7, -1, 15, 0]))


# 2
def mix(str1, str2):
    result = ''
    min_len = min(len(str1), len(str2))
    for i in range(min_len):
        result += str1[i] + str2[i]

    result += str1[min_len:] + str2[min_len:]
    return result

print(mix("hello", "there"))
print(mix("1234", "abcd"))
print(mix("12", "abcd"))
print(mix("1234", "ab"))

def main():
    print("squared sum: ", squared_sum([-3, 4]))
    print("mix:         ", mix("1234", "abcd") == "1a2b3c4d")

main()
