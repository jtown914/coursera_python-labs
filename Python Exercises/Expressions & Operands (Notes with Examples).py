# Expressions & Operands (Python Notes)

# set i equal to a number
i=2

#Logical Test:
    # == is used to mean "is equal to", and the output is a TRUE or FALSE answer.
i=2
i==5
    # != is used to mean "is NOT equal to" and the output is a TRUE or FALSE answer.
i=3
i!=4

# Branching
    # IF statement Logic: If statements are like an excclusive nightclub that every condition wants to get into. Only the true ones can gain entrance. 
        # Hence, IF the statement is true, THEN the program will run. 
    ##Syntax: 
    # {
    #   if (condition):
    #        print ("What appears if TRUE")
    #        print ("What appears if FALSE")
    # }

# first we set age = 19, then define our conditions. 
age=19
# note: PAY ATTENTION TO THE INDENTATIONS HERE! A tab/indent is required for the 'print()' commands following the "if:" and "else:" conditions.
if (age>18):
    print("You may Enter, kind sir.")#this will run if the variable meedts the first condition.
else:
    print ("Back of the line, pal!")
    #this (AFTER "else:) " will run if the variable does not meet the condition.
print("It's gonna be a long night, so buckle up.") 
#this (NOT after "else:") will run regardless of whether any other condition is met, and does not require a tab/indent.

# The "elif: statement (short for "else if") allows us to check additional conditions if the preceding condition is false. If the condition is true, the alternate expressions will be run.
age=12
if(age>=19):
    print("You may attend the AC/DC Showing")
elif(age==18):
    print("You can attend Pink Floyd's performance but not AC/DC's performance")
else:
    print("You should be in line for the Goofy-Goobers in Concert.")
print("Okay, move on now. Thank you, next!")

# Logic Operators
## This is a poor example, but it technically works (just not intuitively). A better example would be setting a=false. Then using "if not(a=true): print(False)" and vice-versa
        a = False

        if not a:
          print('a is false.')
age=20
## NOT —> if the input is TRUE, then a "not(TRUE)" statement will output a FALSE result
if not(age>=21):
    print("You gotta be 21 to ride that ride, babe!")
## NOT —> if the input is FALSE, then "not(FALSE)" statement will output a TRUE result
if not(age<21):
    print("You can sip some Henny.")



# An OR statement is only False if *all* the Boolean values are False.... SO if A and B are Booleans (i.e.: if (A condish is true) or (B condish is true): print (TRUE if either A is true, or B is true, or both A and B are true) else: print (FALSE if both A is false and also B is false).

# EXAMPLE of an "OR" Operator Statement:
album_year=1990
if(album_year<1980) or (album_year>1989):
    print("It was made int he '70s or '90s")
else:
    print("It was maade in the '80s")


# An AND statement is only TRUE if *all* the Boolean values are TRUE.... SO if A and B are Booleans (i.e.: if (A condish is true) and (B condish is true): print (TRUE) since they're both true. Otherwise the result will always be false since at leasrt one (or more) booleans are false

album_year=1983
if(album_year>1979) and (album_year<1990: #meaning AFTER 1979 *AND ALSO* BEFORE 1990 -> would therefore have to be 1980-1989, and thus is from the '80s
    print("It's an '80s Classic! You don't know nothin' about that, young blood! This is ~real~ Grown Folks Music")
else:
    print ("It's not an '80s era banger.")

