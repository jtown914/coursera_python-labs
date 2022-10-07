# Practicing with dictionaries.

        # Dict={"A":1,"B":"2","C":[3,3,3],"D":(4,4,4),'E':5,'F':6}
        # print(Dict["E"])
        ## Get into the habit of creating dictionary keys with double quotes "" instead of apostrophes ''


## CONCEPT:    The key is a singular piece of info, and the value(s) can be multiple pieces of info in a list that corresponds to its key. EXAMPLE: in a flat file (or tabular relational database) you might have rows of Celebrities named Jennifer and each column with a category/attribute that corresponds to that Jennifer. So the rows would be Jennifer Hudson, Jennifer Lewis, Jennifer Lopez, Jennifer Love Hewitt, etc. Then there'd be a column for race and another column for birth year. So if Jennifer Hudson is Black and born in 1970, and Jennifer Lewis is Black and born in 1940, and Jennifer Lopez is White Latina and born in 1982, and Jennifer Love Hewitt is white and both in 1985, then the Python Dictionary for out Jenny Table would look like the following: DICT_Jenny={"Jennifer Hudson": ['Black',1970], "Jennifer Lewis":['Black',1940], "Jennifer Lopez": ['White Latina',1982], "Jennifer Love Hewitt":['White',1985]}


## Creating our own dictionary
DICT_Jenny={"Jennifer Hudson":['Black',1970], "Jennifer Lewis":['Black',1940], "Jennifer Lopez":['White Latina',1982], "Jennifer Love Hewitt":['White',1985]}

print(DICT_Jenny["Jennifer Lopez"]) #Recalls the values for the corresponding key

    # Let's add some more entries to the dictionary
DICT_Jenny["Jennifer Aniston"]=['White',1970]
DICT_Jenny["Jennifer Lawrence"]=['White',1990]
DICT_Jenny["Jennifer Garner"]=['White',1988]

del(DICT_Jenny["Jennifer Garner"]) # deletes the entry from our dictionary

print("Jennifer Garner" in DICT_Jenny) #checks to make sure the entry isn't (or is, if we want it to be) in our dictionary

print(DICT_Jenny.keys()) # Returns the list of keys in our dictionary
print(DICT_Jenny.values()) # Returns the list of values in our dictionary

