wordslist = []

input = input("Enter file name: ")
fileopen = open(input)

for line in fileopen:
	for word in line.split():
		if word not in wordslist:
			wordslist.append(word)

wordslist.sort()
print (wordslist)

file = input("Enter a file name.")

fhand = open(file)

count = 0 

for line in fhand:
  words = line.split()
  if len(words) == 0 : continue
  if words[0] != 'From' : continue
  print(words[1])
  if words[0] == 'From' : 
    count = count + 1

print ("There were " + str(count) + " lines in the file with From as the first word.")

values = []
Still_Going = True

while Still_Going:
  newIn = input("Enter a number: \n")
  if newIn == "done":
    break
  else: 
    newIn = int(newIn)
    values.append(newIn)
    
print("The maximum value is: " + str(max(values)))
print("The minimum value is: " + str(min(values)))

numbers=[7,123]
numbers[1]=5
print(numbers)

a=[1,2,3]
b=[4,5,6]
c=a+b
print(c)

a=[0] * 4
print(a)

b=[1,2,3] * 3
print(b)

t=[1,2,3,4,5,6,7]
t[1:3]
print(t)

r=['a','b','c']
r.append('d')
print(r)

s=[3,6,8,2,6,5,9]
s.sort()
print(s)

d=[1,3,4,6,8,9]
del d[2]
print(d)



#Ex.8.1
def chop(lst):
    """
    Takes a list, modifies it, removing the first and last elements, and
    returns None.
    Input:  lst -- a list
    Output: None
"""
    del lst[0]                          # Removes the first element
    del lst[-1]                         # Removes the last element


def middle(lst):
    """
    Takes a list and returns a new list that contains all but the first and
    last elements.
    Input: lst -- a list
    Output: new -- new list with first and last elements removed
    """
    new = lst[1:]                       # Stores all but the first element
    del new[-1]                         # Deletes the last element
    return new


my_list = [1, 2, 3, 4]
my_list2 = [1, 2, 3, 4]

chop_list = chop(my_list)
print(my_list)                          # Should be [2,3]
print(chop_list)                        # Should be None

middle_list = middle(my_list2)
print(my_list2)                         # Should be unchanged
print(middle_list)                      # Should be [2,3]


#Ex.8.2
fhand = open('exercise8_2.txt')
for line in fhand:
    words = line.split()

    if len(words) < 3:
        continue
    if words[0] != 'From':
        continue
    print(words[2])


#Ex.8.3
fhand = open('exercise8_2.txt')
for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    print(words[2])



#Ex8.4
my_list = []
fhand = open('romeo.txt')
for line in fhand:
    words = line.split()                # Splits line into array of words
    for word in words:
        if word in my_list:
            continue                    # Discards duplicates
        my_list.append(word)            # Updates the list
print(sorted(my_list))                  # Alphabetical order

#Ex.8.5
fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    print(words[1])
    count += 1
print('There were %d lines in the file with From as the first word' % count)

#Ex.8.6
my_list = []                        # Initialize array
while True:
    number = 0.0
    input_number = input('Enter a number: ')
    if input_number == 'done':
        break

    try:
        number = float(input_number)
    except ValueError:
        print('Invalid input')
        quit()

    my_list.append(input_number)

print('Maximum: ', max(my_list))
print('Minimum: ', min(my_list))
