def reverse(strn):
    str = ""
    for i in strn:
        str = i + str
    return str
def deletestrings():
    first_char=str(input("enter first character to delete"))
    h=strn.replace(first_char, '') #deleting first entered character and sending new string to h variable
    second_char=str(input("enter second charcter to delete"))
    j=h.replace(second_char, '') #deleting second character and sending the remaining string to j variable
    return print("string after deleting two characters and reversing",reverse(j)) # printing and calling reverse function

strn = str(input("enter a string"))
print("The original intstring is : ", end="")
print(strn)
deletestrings()