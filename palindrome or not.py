my_str='aIbohPhoBi'
my_str=my_str.casefold()
rev_str=reversed(my_str)

if list(my_str)==list(rev_str):
    print("palindrome")
else:
    print("not a palindrome")