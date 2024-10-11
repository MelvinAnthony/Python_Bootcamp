from collections import Counter

'''mylist = [1,2,3,4,5,6,5,4,3,2,1,2,3,4,5,6,5,4,3,2,3,4,3]

print(Counter(mylist))

mystring = "melvin Anthony"
print(Counter(mystring))


llm = "Large language models, also known as LLMs, are very large deep learning models that are pre-trained on vast amounts of data."

res = Counter(llm.lower().split())

print(res.most_common())

'''

#using Default Dectionary

from collections import defaultdict

'''a = {"a":10,
     "b": 20}

print(a['a'])'''

'''dict = defaultdict(lambda: 0)

dict["melvin"] = 100
dict["Anthony"] = 200

print(dict["Raj"])
print(dict["kevin"])
print(dict)

'''

from collections import namedtuple

me = namedtuple("me",["name","age","location"])

mel = (me(name="Melvin",age=23,location="Chennai"))

print(mel.age)
