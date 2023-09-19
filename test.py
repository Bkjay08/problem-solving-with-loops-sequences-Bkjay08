def squared_sum(lst):
    sum_of_squares = sum(x**2 for x in lst)
    return sum_of_squares

result = squared_sum([])
print(result)