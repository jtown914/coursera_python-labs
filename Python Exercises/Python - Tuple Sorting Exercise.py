# Sort the tuple

    ## NOTE: Even though our Ratings sequence is a Tuple (not a List), using the sorted function in our "SortedRatings=sorted(Ratings)" command will BY DEFAULT produce output that is a sorted LIST (and *not* a sorted TUPLE) despite our original sequence being a Tuple.
    ## To account for the output now being changed to a list, we must convert it back to a tuple by re-defining the "RatingsSorted" output as a Tuple using "="
print('\n\t The Hard Way')
Ratings = (0, 9, 6, 5, 10, 8, 9, 6, 2) 
print('Unsorted Tuple:\t',Ratings) # Ratings = (Tuple) -- unsorted
RatingsSorted = sorted(Ratings)
print('Sorted List:\t',RatingsSorted) # RatingsSorted = [List]
Ratings=tuple(RatingsSorted) # redefines the original Ratings tuple as a tuple of the sorted RatingsSorted list
print('Sorted Tuple:\t',Ratings) # Ratings = (Tuple) -- sorted
Ratings = (0, 9, 6, 5, 10, 8, 9, 6, 2) 

    ## Easier way to do the above operations is to simply make the RatingsSorted list a tuple to begin with by using the tuple() command on the sorted(tuple) command. Essentially making Python auto-convert the default output as a tuple instead of the default list output.
print('\n\t The Easy Way')
Ratings = (0, 9, 6, 5, 10, 8, 9, 6, 2) 
print('Unsorted Tuple:\t',Ratings) # Ratings = (Tuple) -- unsorted
RatingsSorted = tuple(sorted(Ratings))
print('Sorted Tuple:\t',RatingsSorted) # RatingsSorted = (Tuple) -- sorted

# And viola, it works!