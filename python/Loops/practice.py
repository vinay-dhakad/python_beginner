#print the no. 1 to 100
# i = 1 
# while i <= 100:
#     print (i)
#     i += 1

#print no. from 100 to 1.
# i = 100
# while i >= 1:
#     print (i)
#     i -= 1

#print multiplication table of no. n
# 1

#print the elements of following list using the loop:
# [1,4,9,16,25,36,49,64,81,100]

# nums = [1,4,9,16,25,36,49,64,81,100]

# idx = 0
# while idx < len(nums):
#     print(nums[idx])
#     idx += 1 

# traverse
# heroes = ["ironman","thor","captain","hulk","kedar jadav"]
# idx = 0
# while idx < len(heroes):
#     print(heroes[idx])
#     idx += 1


#search for no. x in this tuple using loop:
# (1,4,9,16,25,36,49,64,81,100)

nums=(1,4,9,16,25,36,49,64,81,100)


x=36

i=0
while i < len(nums):
    if(nums [i] == x):
        print("FOUND at idx",i)
  
      i += 1