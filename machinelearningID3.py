# https://medium.com/@lope.ai/decision-trees-from-scratch-using-id3-python-coding-it-up-6b79e3458de4
import pprint
import numpy as np
import pandas as pd
eps = np.finfo(float).eps
from numpy import log2 as log

outlook = 'overcast,overcast,overcast,overcast,rainy,rainy,rainy,rainy,rainy,sunny,sunny,sunny,sunny,sunny'.split(',')
temp = 'hot,cool,mild,hot,mild,cool,cool,mild,mild,hot,hot,mild,cool,mild'.split(',')
humidity = 'high,normal,high,normal,high,normal,normal,normal,high,high,high,high,normal,normal'.split(',')
windy = 'FALSE,TRUE,TRUE,FALSE,FALSE,FALSE,TRUE,FALSE,TRUE,FALSE,TRUE,FALSE,FALSE,TRUE'.split(',')
play = 'yes,yes,yes,yes,yes,yes,no,yes,no,no,no,no,yes,yes'.split(',')

dataset ={'outlook':outlook,'temp':temp,'humidity':humidity,'windy':windy,'play':play}
df = pd.DataFrame(dataset,columns=['outlook','temp','humidity','windy','play'])
print(df)
##1. claculate entropy o the whole dataset
def find_entropy(df):
    Class = df.keys()[-1]   #To make the code generic, changing target variable class name
    entropy = 0
    values = df[Class].unique() #Unique objects - 'Yes', 'No'
    for value in values:
        fraction = df[Class].value_counts()[value]/len(df[Class])
        entropy += -fraction*np.log2(fraction)
    return entropy
  
print('Entropija celog skupa podataka: ',find_entropy(df))
  
def find_entropy_attribute(df,attribute):
   #print("df[attribute]: ")
   #print(df[attribute]) # vraca sve moguce vrednosti jednog atributa
   Class = df.keys()[-1]   #To make the code generic, changing target variable class name
   target_variables = df[Class].unique()  #This gives all 'Yes' and 'No' tj. izlaz: ['yes' 'no']
   variables = df[attribute].unique()    #This gives different features in that attribute (like 'Hot','Cold' in Temperature)
   entropy2 = 0
   for variable in variables:
       entropy = 0
       for target_variable in target_variables:
           '''print("*-*")
           print(df[attribute][df[attribute]==variable][df[Class] ==target_variable])
           print("*-*")
           print(df[attribute][df[attribute]==variable])'''
           num = len(df[attribute][df[attribute]==variable][df[Class] ==target_variable])
           den = len(df[attribute][df[attribute]==variable])
           fraction = num/(den+eps)
           entropy += -fraction*log(fraction+eps) 
       fraction2 = den/len(df)
       entropy2 += -fraction2*entropy
   return abs(entropy2)


def find_winner(df):
    Entropy_att = []
    IG = []
    for key in df.keys()[:-1]:
        Entropy_att.append(find_entropy_attribute(df,key))
        IG.append(find_entropy(df)-find_entropy_attribute(df,key))
    return df.keys()[:-1][np.argmax(IG)]
  
  
def get_subtable(df, node,value):
    return df[df[node] == value].reset_index(drop=True)


def buildTree(df,tree=None): 
    Class = df.keys()[-1]   #To make the code generic, changing target variable class name
    
    #Here we build our decision tree

    #Get attribute with maximum information gain
    node = find_winner(df)
    
    #Get distinct value of that attribute e.g Salary is node and Low,Med and High are values
    attValue = np.unique(df[node])
    
    #Create an empty dictionary to create tree    
    if tree is None:                    
        tree={}
        tree[node] = {}
    
   #We make loop to construct a tree by calling this function recursively. 
    #In this we check if the subset is pure and stops if it is pure. 
    print(attValue)
    print('----------')
    for value in attValue:
        
        subtable = get_subtable(df,node,value)
        print(subtable)
        print('****************')
        clValue,counts = np.unique(subtable['play'],return_counts=True)                        
        print(" ----clValue,counts----- ",clValue," ",counts)
        if len(counts)==1:#Checking purity of subset
            tree[node][value] = clValue[0]                                                    
        else:        
            tree[node][value] = buildTree(subtable) #Calling the function recursively 
                   
    return tree

t = buildTree(df)
pprint.pprint(t)
