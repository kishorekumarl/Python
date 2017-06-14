


def funct():
    # input x
    for x in [3, 10]:
        if (x < 10):
            print (x)
        else:
            print("good")


def remove_adjacent(nums):
    x = []
    for i in nums:
        if i in nums:
            x.append(i)

    print (nums)


def remove_elements(lst):
  mi=min(lst)
  ma=max(lst)
  for i in lst[:]:
    if lst==mi or lst==ma :
      lst.remove(i)
      lst.sort()
  return lst

def linear_merge(list1, list2):
    l=list1+list2
    nl=[]
    for i in l[:]:
        m=min(l)
        l.remove(m)
        nl.append(m)
    return nl

def num_freq():
   x=input('Enter the list of number : ')
   l =set(x)
   for i in l:
       print(i+"append"+x.count(i) +"times")


def dounts(counts):

    if counts>=10 :
        print ("Number of dounts"+ counts)
    else:
        #counts <10)
        print("Many dount"+ counts)



def counts():
    str = "Sort by keys and sort by values"
    count = {}
    for word in str.split():
        count[word] = count.get(word, 0) + 1
    print(word) \

def sort_print():
      sort_print({'a': 3, 'b': 2, 'c': 5})
      sort = {}
      for key in sort_print.split():
        sort[key] = sort.get(key, 0) + 1
      print(key)


def Reverselookup(strdic, strval):
    rev = []
    for k in strdic:
        if strdic[k] == strval:
            rev.append(k)
    return sorted (rev)


def invertDictionary(d):
    i = []
    for k in d:
        if d[i] == d:
            i.append(k)
            i.sort(k)
    return reverse (i)

def key():
    i ={"1":"a","4":"b","2":"c"}
    x=[i]
    print(i.sorted["1"],i.sorted["2"])

    

