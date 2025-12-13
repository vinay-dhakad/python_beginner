# #recursive function
# def show(n):
#     if (n == 0):
#         return
#     print(n)
#     show(n-1)

# show(5)

# def show(n):
#     if (n == -2):
#         return
#     print(n)
#     show(n-1)

# show(5)



#returns n!
# def fact(n):
#     if(n==1 or n==0):
#         return 1
#     return fact(n-1) * n
# print(fact(4))



# #recursive fn.
# write a recursive function to calculate the sum of first n natural no.

def calc_sum(n):
    if(n==0):
        return 0
    return calc_sum(n-1) + n

sum = calc_sum(10)
print(sum)


#write a recursive function to print all elements in a list.
# Hint: use list and index as parameters.
def print_list(list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)


fruits = ["mango", "litchi", "apple", "banana"]

print_list(fruits)