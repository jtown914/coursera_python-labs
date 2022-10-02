string = 'geeks for geeks'
print(string.split())
# OUTPUT = ['geeks', 'for', 'geeks']

string0 = 'geeksforgeeks'
print(*[string0])
# OUTPUT = geeksforgeeks

string1 = 'geeksforgeeks'
print(*string1)
# OUTPUT = g e e k s f o r g e e k s

string2 = 'geeksforgeeks'
print([*string2])
# OUTPUT = ['g', 'e', 'e', 'k', 's', 'f', 'o', 'r', 'g', 'e', 'e', 'k', 's']
