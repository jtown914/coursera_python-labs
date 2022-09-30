# Test List

## Let's create List 0
List0=["Michael Jackson", 10.1, 1982]
## double-check to make sure it exists, lol
print (List0)
## We'll use the .append () function to add Tuple 0 to the end of List 0;(then we'll insert another List as List 1)   
    ## First define the Tuple as Tuple 0. We want it to have a string and an integer. ***REWMINDER*** -> Tuples are immutable and use parentheses instead of square brackets
Tuple0=('A',1)
List0.append(Tuple0)
## Now let's check to make sure it updated List 0
print (List0)
## Now, let's add a List 1 to the mix. 
    ## First define List 1
List1=[1, 2]
## We will now insert the List 1 before Tuple 0 in List 0
List0.insert(3,List1)
print (List0)

# Viola! It fucking works!

