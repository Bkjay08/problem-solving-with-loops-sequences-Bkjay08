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

#2
def mix(str1, str2):
     result = ""

     min_length = min(len(str1), len(str2))
    
     for i in range(min_length):
        result += str1[i] + str2[i]
     
     if len(str1) > min_length:
        result += str1[min_length:]
     elif len(str2) > min_length:
        result += str2[min_length:]

     return result

string1 = "hello"
string2 = "there"

#print(mix(string1, string2)) 

def main():
    print("squared sum: ", squared_sum([-3, 4]))
    print("mix:         ", mix("1234", "abcd") == "1a2b3c4d")

main()
