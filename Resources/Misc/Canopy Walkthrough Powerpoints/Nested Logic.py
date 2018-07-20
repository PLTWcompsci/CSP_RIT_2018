from __future__ import print_function
import random


def code_test():
    houseColor = 'Blue'
    print ('I love the color of my house', houseColor)

def logic_check(houseColor, colorPreference):
    if houseColor == colorPreference:
        print ("I want to buy this house because it is ", houseColor)
    else:
        print ("I do not want to buy this house. I would prefer to buy a house that is", colorPreference)
        
def nested_check(grade):
    if grade >=90:
        print ('You have a grade of', grade, '. This is an A!')
    elif grade>=80:
        print ('You have a grade of', grade, '. This is a B!')
    elif grade>=70:
        print ('You have a grade of', grade, '. This is a C!')
        
def nested_check2(grade):
    if grade >=90:
        print ('You have a grade of', grade, '. This is an A!')
    else:
        if grade>=80:
            print ('You have a grade of', grade, '. This is a B!')
        else:
            if grade>=70:
                print ('You have a grade of', grade, '. This is a C!'        )
        
def name_in_list(name, list1):
    if name in list1:
        print ('The name', name, 'is in the list.')
    else:
        print ('The name', name, 'is NOT in the list.')
        
def f(x):
    if int(x)==x:
        if x%2==0:
            if x%3==0:
                print (x,'is a multiple of 6')
            else:
                print (x,'is even')
        else:
            print (x, 'is even odd')
    else: 
        print (x,'is not an integer')
        
        