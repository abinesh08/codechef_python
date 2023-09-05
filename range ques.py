#Write code to create a list of integers from 0 through 52 and assign that list to the variable numbers. You should use the Python range function and don’t forget to covert the result to a list – do not type out the whole list yourself.
numbers=range(0,53)
for i in numbers:
    print(i)

#Count the number of characters in string str1. Do not use len(). Save the number in variable numbs.
str1 = "I like nonsense, it wakes up the brain cells. Fantasy is a necessary ingredient in living."
nums=0
for i in str1:
    nums+=1
print(nums)



#Write one for loop to print out each element of the list several_things. Then, write another for loop to print out the TYPE of each element of the list several_things. To complete this problem you should have written two different for loops, each of which iterates over the list several_things, but each of those 2 for loops should have a different result.
several_things = ["hello", 2, 4, 6.0, 7.5, 234352354, "the end", "", 99]
print("elements")
for i in several_things:
    print(i)
print("TYPE")
for i in several_things:
    print(type(i))

#Write code that uses iteration to print out the length of each element of the list stored in str_list.
str_list = ["hello", "", "goodbye", "wonderful", "I love Python"]
for i in str_list:
    length=len(i)
    print(length)
