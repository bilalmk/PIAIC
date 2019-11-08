
#import locale
#print(locale.getpreferredencoding())
a = "foo"
#print(a.count("o"))
#print(a.capitalize())
#getattr(a,'split')

def isIterateable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False

#print(isIterateable('a string'))
#print(isIterateable([1,2,3,4]))
#print(isIterateable(53434))
#template = "{0:.2f} {1:s} are worth US$ {2:d}"
#print(template.format(4.5666,"Argentine Pesos",1000))

#val = "کیس کا ٹرائل چینلز پر لائیو دکھایا جائے، شاہد خاقان"
#alphabet = 'αβγδεζηθικλμνξοπρςστυφχψ'
#print(alphabet)
#print(len(val.encode("utf-8")))
#val_uni = val.encode('utf-8')
#print(val_uni.decode('utf-16'))

#string = "hello"
#print(string[::-1])
#print(string[2:4])
#print(string[-5:-2])

#seq1 = ["foo","bar","zoo"]
#seq2 = ["one","tow","three"]
#seq3 = [True,False]
#zipped = zip(seq1,seq2,seq3)
#print(list(zipped))
#for i,(a,b) in enumerate(zip(seq1,seq2)):
#    print("{0}:{1},{2}",i,a,b)

#key_list = ['mon','tue','wed','thu']
#value_list = [20,30,40]
#dic = {}

#for i,key in enumerate(key_list):
#    dic[key] = value_list[i]

#print(dic)

#for key,val in zip(key_list,value_list):
#    dic[key]=val

#key="wed"
#print(dic[key])
#if key in dic:
#    print(dic[key])
#else:
#    print("not found")

#print(dic.get(key))
#print(dic.pop(key))
#print(dic)


words = ["apple","bat","bar","atom","book"]
by_letter = {}
for word in words:
    letter = word[0]
    if(letter not in by_letter):
        by_letter[letter] = [word]
    else:
        by_letter[letter].append(word)
#print(by_letter)

by_letter = {}

for word in words:
    letter = word[0]
    by_letter.setdefault(letter,[]).append(word)    
#print(by_letter)

from collections import defaultdict
by_letter = {}
by_letter = defaultdict(list)
for word in words:
    by_letter[word[0]].append(word)

#print(by_letter)

#print(hash([1,2]))
temp = set([1,2,2,3,4,5,5])
#print(temp)

a = {1,2,3,4,5}
b = {3,4,5,6,7,8}
#print(a.union(b))
#print(b.union(a))
#print(a|b)
#print(a.intersection(b))
#print(a & b)
#a.add(7)
#print(a)
#a.update(b)
#print(a)

strings = ["a",'as',"bat","car","dov","python"]

#print([x.upper() for x in strings if len(x)>2])
unique_set = {len(x) for x in strings}
#print(unique_set)
#print(set(map(len,strings)))
loc_map = {val:index for index ,val in enumerate(strings)}
#print(loc_map)

all_data = [["john","Emily","Michael","Mary","Steven"],["Maria","John","Javier","Natalia","Pilar"]]
names_of_interest=[]
for names in all_data:
    extract_name = [name for name in names if name.count('a')>=2]
    names_of_interest.extend(extract_name)
#print(names_of_interest)

#print([name for names in all_data for name in names if name.count('a')>=2])

some_tuples = [(1,2,3),(4,5,6),(7,8,9),(10,11,12)]
flatten = [x for tup in some_tuples for x in tup]
#print(flatten)
flatten = [[x for x in tup] for tup in some_tuples]
#print(flatten)
import re
states = ["      Albama  ","Georgia!",  "Georgia ", "georgia","FloRidA", "south   carolina##",  "West virginia?"]

def clean_state(states):
    result = []
    for state in states:
        state = state.strip()
        state = re.sub('[!?#]','',state)
        state = state.title()
        result.append(state)
    return result

#print(clean_state(states))

def remove_punctuations(value):
    return re.sub('[!?#]','',value)

clean_ops = [str.strip,remove_punctuations,str.title]

def clean_strings(states,ops):
    result=[]
    for state in states:
        for function in ops:
            state = function(state)
        result.append(state)
    return result

#print(clean_strings(states,clean_ops))
#for x in map(remove_punctuations,states):
#    print(x)

def apply_to_list(some_list,f):
    return [f(x) for x in some_list]

ints = [4,0,1,5,6]
lambdaFun = lambda x:x*2
#print(apply_to_list(ints,lambdaFun))
#print([x*2 for x in ints])

strings = ['foo', 'card', 'bar', 'aaaa', 'abab']
strings.sort(key=lambda x:len(set(list(x))),reverse=True)
#print(strings)


#for x in strings:
#    print(len(set(list(x))))

def add_numbers(x,y):
    return x+y

add_five = lambda y:add_numbers(5,y)
#print(add_five(15))

from functools import partial
add_five = partial(add_numbers,5)
#print(add_five(50))

#=============Generators=====================
some_dict = {"a":1,"b":2,"c":3}
#for key in some_dict:
#    print(key)

dict_iter = iter(some_dict)
#print(dict_iter)

#print(list(dict_iter))

def squres(n=10):
    print("generate squres from 1 to {0}".format(n**2))
    for i in range(1,n+1):
        yield i**2

gen = squres()
#print(list(gen))
#for i in gen:
#    print(i,end=" ")

gen = (x**2 for x in range(100))
#print(gen)
#print(sum(gen))
#print(min(gen))
#print(max(gen))

#print(sum(x**2 for x in range(100)))

gen = ((i,i**2) for i in range(5))
#print(dict(gen))
#print(list(gen))

gen = dict((i,i**2) for i in range(5))
#print(gen)

import itertools
names = ['Alan', 'Adam', 'Wes', 'Will', 'Albert', 'Steven']
first_letter = lambda x:x[0]
iterObj = itertools.groupby(names,first_letter)

#for letter,name in iterObj:
#    print(letter,list(name))

ints = [1,2,3,4,5,6,7]
#it = iter(ints)
#total = next(it)
#print(total)

#print(list(itertools.accumulate(ints,lambda x,y:x+y)))

chain = [1,2,3],[4,5,6],[7,8,9]
chainGen = itertools.chain(chain)

#for i in chainGen:
#    print(i)

chain = [1,2,3],[4,5,6],[7,8,9]
chainList = list(itertools.chain([1,2,3],[4,5,6],[7,8,9]))
#print(chainList)
#for i in itertools.chain([1,2,3],[4,5,6],[7,8,9]):
#    print(i)


#for i in iterObj:
#    print(i)

#test = lambda x,y:x+1+y
#print(test(2,3))

test = 'ABCD'
#pool = tuple(test)
#indices = list(range(2))
#print(tuple(pool[i] for i in indices))
#for i in reversed(range(2)):
#    print(i)

#for i in tuple(itertools.combinations('ABCD',2)):
#print(tuple(itertools.combinations('ABCD',2)))
#print(list((itertools.count(10,20))))

permList = ['A','B','C','A']
perm = itertools.permutations(permList,4)
perm = itertools.permutations(permList,2)
#print((list(perm)))
comb = itertools.combinations(permList,2)
print(list(comb))
