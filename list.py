def remove_duplicates(nums):
    x= []
    for i in nums:
        if i not in x:
           x.append(i)
 #          x.remove(i)
 #   x.sort()
            
    x.reverse ()

    print(x)
