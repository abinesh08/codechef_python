Name="Abinesh"
length=len(Name)
print(length)
a=Name[-1]
print(a)
b=Name[2]+Name[4]
print(b)

#slicing
output=Name[2:6]
print(output)

#count and index(count:count a values and give output. Index:position of the value .only takes position of first value)
Power="this is a bookss"
print(Power.count("s"))
print(Power.index("a"))

#splitting and  joining string(split(): to delete the given value. join(): we can join any value in any line)
line="the powerfull one is a huge explosion that is heroshime nuclear bomb"
print(line.split("e"))
line2=["the","powerfull","best","big"]
line3=';'
print(line3.join(line2))
