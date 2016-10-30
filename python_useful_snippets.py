# string library to generate lowercase alphabets
import string
alpha= list(string.ascii_lowercase)[:10] #get list of alphabets
print alpha #['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

#zip example
numbers= range(10)
print numbers #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print zip(numbers,alpha) #[(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd'), (4, 'e'), (5, 'f'), (6, 'g'), (7, 'h'), (8, 'i'), (9, 'j')]

#zip to dictionary
dic = dict(zip(numbers,alpha))
print dic #{0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j'}

#splits the string with length of 10  or less without cutting the word
import textwrap
str = "this is abc very long text written by shruti"
print textwrap.wrap(str,10)#['this is', 'abc very', 'long text', 'written by', 'shruti']

#set operations
A = set([10,23,30,10]) #to get set from a list (no duplicates)
B = {23,34} #alternative representation
print A, type(A) #set([10, 30, 23]) <type 'set'>
print B, type(B) #set([34, 23]) <type 'set'>
#union
print A|B #set([10, 34, 30, 23])
print A.union(B) #set([10, 34, 30, 23])
#intersection
print A&B #set([23])
print A.intersection(B) #set([23])
#minus
print A-B #set([10, 30])
print A.difference(B) #set([10, 30])
print B-A #set([34])
print B.difference(A) #set([34])
#A-B union B-A
print A^B #set([34, 10, 30])
print A.symmetric_difference(B) #set([34, 10, 30])

#functional programming
def dbl(i):
	return i *2

numbers = [1,4,9]
doubles_list_comprehension = [i*2 for i in numbers] #using list comprehension #[2, 8, 18]
doubles_lambda_map = list(map(lambda i: i*2, numbers)) #map and lambda #[2, 8, 18]
doubles_function_map = list(map(dbl,numbers)) #map and function #[2, 8, 18]

sum_reduce = reduce(lambda i,j:i+j,numbers) #14

odd_filter = filter(lambda i: i%2 ==1, numbers) #[1, 9]

print doubles_list_comprehension
print doubles_lambda_map
print doubles_function_map
print sum_reduce
print odd_filter

#2nd max item from list with repeating elements
x =[12,23,45,45,34,34,23]

print sorted(list(set(x)))[-2] #using list sorting #34
z= [i for i in x if i != max(x)] #using list comprehension to remove max and then pick the max from rest
print (max(z)) #34
import heapq #using inbuilt heapq library
print heapq.nlargest(2, set(x))[1] #34
print max(filter(lambda i: i != max(x), x)) #using filter function #34

#while loop example
x = 0
while x<3:
	print x,"is less than 10"
	x += 1

#pair generation using list comprehension
a,b = 0,0
pairs = [(a,b)
          for a in range(5)
          for b in range(a+1,5)]
print pairs

#random module
print "%%%%%%%%%"
import random
four_random = [random.random() for _ in range(4)]
print four_random #4 random decimals between 0-4 #[0.5218242903121137, 0.05241558411868541, 0.02075685504174707, 0.7184501638616516]
print random.random() #regular random decimal #0.412483312598
print '$$$$$$$$$$'
random.seed(3) #generates same random numbers when the seed is reused
print random.random() #0.237964627092
print random.random() #0.544229225296
print "$$$$$$$$$"
random.seed(3)
print "*********"
print random.random() #0.237964627092
print random.random() #0.544229225296
print "*********"

up_to_ten = range(10)
random.shuffle(up_to_ten) #shuffle original list
print up_to_ten #[2, 9, 7, 1, 4, 6, 0, 8, 5, 3]
random.shuffle(up_to_ten) #shuffle originl list for different output
print up_to_ten #[6, 7, 9, 0, 5, 2, 3, 1, 8, 4]

friend = random.choice(["ali","bob","sean","pitu","hello"])
print friend #random item from list #pitu

import string, random #generate 5 random alphabets each time
alphabet = string.ascii_lowercase
print random.sample( alphabet, 5 ) #['b', 't', 'p', 'h', 'a']
print random.sample( alphabet, 5 ) #['w', 'm', 's', 'x', 'k']
print random.sample( alphabet, 5 ) #['u', 'l', 'y', 'w', 'c']