## So let's say we have a merger between two (2) restaurants: A soulfood place and a Chinese joint. We have to combine the Menus from both restaurants to create a new Menu for the new, merged eatery. 

# First let's make sure we got the right items on each Menu by inputting the elements in the following sets: 
MenuA={"Rice", "Noodles", "Tea","Cookies","Chicken"}
MenuB={"Purple Drank", "Chicken", "Dirty Rice", "Cookies","Coleslaw"} 

# Now let's make sure our two (2) Menus are looking good. We should be all 'set' (see what I did there? The pun was intended)
print ('MenuA:\t',MenuA)
print ('MenuB:\t',MenuB)

# Aight so now, we're just gonna take a quick lil peek at the duplicates (if any) between between both Menus.
MenuC=MenuA&MenuB
    # Okay but WAYMENT! Before we even get into the nitty-gritty, let's first run this quick lil test just to make sure there are even duplicates between Menus. 
        # Because if *both* Menus are already unique (UNIQUE!!!), then we don't even need to mess with the union function, we can instead just concatenate them in the following. However, if the test reveals that there ARE duplicates, then we'll need to unite them (sans duplicates) in the following step. Let's see...
if MenuC in MenuA or MenuB:
    print("\n\tUh oh, we got DUPES!")
else:
    print ("\nYou're all set, babe.")
print("\tYou know what to do.\n")

# Welp, it looks like there are two (2) duplicate items found between both Menus. As a treat, let's just see what those duplicate items are.
print ('MenuC:\t',MenuC)
    #  Ah, okay, cool. Love me some good chicken! 

# We're now in the home stretch here. We only need to unite (merge) Menu B's items with Menu A's items into a new Menu D without any items appearing more than once  in Menu D (i.e. no duplicates).
MenuD=MenuA.union(MenuB)

# And viola! We now have our brand new Menu for the joint restaurant venture. Let's see how she's looking.
print('MenuD:\t',MenuD) 
    #¡Perfecto!

# To make things easier to read, we can wither rename the Menus to something more practical, *OR* we can reprint with more practical fields for names. 
    # The downside of renaming the variables would be that I'd then have to also update the variable names in all my commands, whereas the upside would be that I don't have to worry about doing it again in the future should I return back to these variables later. \
    # The downside of reprinting with updated strings for variable names would be that the underlying variable names would remain the same so reprinting would only be beneficial in this one exercise, but the very next cell with the same variables would still be named what they originally were. 
        # This could definitely cause confusion having to remember which variables were reprinted with different names, as opposed to simply renaming the variables themselves, which is more immediate work but pays off over the long term if these are variables I have to return to again in the future).  
# Just something to think about as you continue your learning. 

# Use the .issubset() funciton to see if a set is a subset of another set. For example, if we just united Menu A and Manu B into a Menu D set, then we know that Menu A is a subset of Menu D --AND-- that Menu B is a subset of Menu D.
print(MenuA.issubset(MenuD)) # Output will be TRUE
print(MenuB.issubset(MenuD)) # Output will be TRUE
print(MenuC.issubset(MenuA)) # Output will be TRUE
print(MenuC.issubset(MenuB)) # Output will be TRUE
print(MenuC.issubset(MenuD)) # Output will be TRUE
print(MenuD.issubset(MenuA)) # Output will be FALSE
print(MenuD.issubset(MenuB)) # Output will be FALSE
print(MenuD.issubset(MenuC)) # Output will be FALSE
