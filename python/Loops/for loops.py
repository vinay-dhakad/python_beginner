# nums = [1 ,2 ,3 ,4 ,5 ]
# for val in nums:
#     print(val)


# cars = ["lamborgini" , "nano" , "swift"]
# for val in cars:
#     print(val)


# tup = (1 ,2 ,3 ,4 ,5 )
# for num in tup:
#     print(num)


# str = "vijay shankar"
# for char in str:
 
#     print(char)
# else:
#     print("END")



# str = "vijay shankar"
# for char in str:
#     if(char == 'y'):
#         print("y found")
#         break
#     print(char)
# else:
#     print("END")



# print the elements of following list using the loop:
# [1,4,9,16,25,36,49,64,81,100]

# nums =[1,4,9,16,25,36,49,64,81,100]
# for val in nums:
#     print(val)


# search for no. x in this tuple using loop:
# (1,4,9,16,25,36,49,64,81,100)

nums = [1,4,9,16,25,36,49,64,81,100,64]
x = 49

idx = 0
for el in nums :
    if(el == x):
        print("num found at idx", idx)
        idx +=1 
