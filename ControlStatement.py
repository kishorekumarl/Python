def sort_print(d):
    #Iterate thru all the sorted keys one at a time and print the key and the corresponding value.
    print("sorted by keys:")
    for n in sorted(d.keys()):
        print (n, d[n])

    #Iterate thru all the sorted values and print the value and the corresponding key.
    #Convert the list of values to a set to get rid of duplicates, and then sort
    print("sorted by values:")
    for n in sorted(set(d.values())):
        #To get the corresponding key of a particular value, loop thru all the keys. This is the inner for loop
        for k in d.keys():
            if d[k] == n:
                print(k,d[k])


def reverselookup(d, val):

    l = [] #The list which will contain the keys whose
    # values match the supplied 'val'

    #Iterate thru the dictionary, if a value matches
    #val, append the key to l.
    for key in d.keys():

        if d[key] == val:

            l.append(key)
    l.sort()
    return l

def invertDictionary(d):

    new_d = {}

    #Iterate thru all the values of the dictionary.
    for val in d.values():
        new_d[val] = []
        #Iterate thru all the keys and find the keys whose value is equal to the value we are iterating above.
        for key in d.keys():
            if d[key] == val:
                new_d[val].append(key)

    return new_d

def convertVector(l):

    d = {}

    index = 0

    #Iterate thru all the elements of the list.
    for value in l:

        #If the element is non-zero, add its index and the element to the dictionary.
        if value != 0:

            d[index] = value

        index = index + 1

    return d


def convertDictionary(d):

    l = []
    index = 0
    keys = list(d.keys())
    keys.sort()

    #Iterate thru the sorted list of keys
    for key in keys:

        #If the key is equal to the index, append the key's value to the list.
        #OTherwise, append 0s to the list until the index becomes equal to the key.
        if key == index:
            l.append(d[key])
            index = index + 1
        else:
            while (index < key):
                l.append(0)
                index = index + 1
            l.append(d[key])
            index = index + 1

    return l


def convertDictionary1(d):
  """Another way to solve this"""

  if not d:
    return []

  l = []
  keys=list(d.keys())
  keys.sort()

  for i in range(keys[-1]+1):
    if i in keys:
      l.append(d[i])
    else:
      l.append(0)




def hr_db():
  """HR database"""

  db={}
  while True:
    s = input("Please enter employee number and name (type END when done):")
    if s == 'END':
      break
    split_s=s.split(None,1)
    db[int(split_s[0])] = split_s[1]
  print (db)
  print ("List sorted by num")
  nums = sorted(list(db.keys()))
  for num in nums:
    print (num,db[num])

  print ("List sorted by name")
  names = sorted(list(db.values()))
  for name in names:
    for n in db.keys():
      if db[n]==name:
        print (n,name)

def dice():
  d = {}

  for sum in [2,3,4,5,6,7,8,9,10,11,12]:
    d[sum] = []
    for i in [1,2,3,4,5,6]:
      for j in [1,2,3,4,5,6]:
        if sum == i+j:
          d[sum].append((i,j))
  print(d)


def rot13():
  s = input("Please enter the string:")
  for i in s:
    if i.islower():
      i = ord(i)+13
      #if i is greater than 122 ('z'), then rotate
      if i > 122:
        i = i - 26
      print(chr(i),end='')
    elif i.isupper():
      i = ord(i)+13
      #if i is greater than 90 ('Z'), then rotate
      if i > 90:
        i = i - 26
      print(chr(i),end='')
    else:
      print(i,end='')
  print("")


def has_duplicates():
  import ast
  l = ast.literal_eval(input("Please enter list of integers: "))
  return len(l) != len(set(l))
