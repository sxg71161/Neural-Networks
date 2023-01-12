sentence=str(input("please enter the sentence: "))
old="python"
new="pythons"
print("sentence is :",sentence)
def replacepythonwithpythons(sentence,old,new):
    return sentence.replace(old,new)
print(replacepythonwithpythons(sentence,old,new))