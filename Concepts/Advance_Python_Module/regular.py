import re

text = "this is my phone number +91 7373 3355 58"

# using exact string to search and find
# pattern = '3355'
# reg = re.search(pattern,text)
# print(reg)
# print(text[33:37])

# find_text =  re.findall('3',text)
# print(find_text)


# for match in re.findall("3",text):
    # print(match)

#using pattern to search and find using special sqeuance

# reg = re.search("\W\d\d \d\d\d\d \d\d\d\d \d\d",text)
# print(reg)
# print(reg.group())

# reg_find = re.findall("\w",text)
# print(reg_find)


#using Metacharacters

# text = "this is my phone number +91 7373 3355 58"
# reg = re.search(r"\+91 \d{4} \d{4} \d{2}", text)
# print(reg.group())


#using compile we can seperate the group and call seperately
# compile_pattern = re.compile(r"(\+91) (\d{4}) (\d{4}) (\d{2})")
# result = compile_pattern.search(text)
# result.group()
# print(result.group(2))


#using or in search
text = "this is my phone number +91 7373 3355 58 and another number is +91 7373 1313 21" 
or_seach = re.search("....e|.3",text)
print(or_seach.group())

or_find = re.findall("....ez|^3|\d$",text)
print(or_find)