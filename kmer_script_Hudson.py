#!/usr/bin/env python3

import pandas as pd
import re 

def get_possible_kmers (string, k):
    '''This defined function, "get_possible_kmers", is to count possible kmers of size k from a string, where k and the string are specified as arguments. The user will need to enter in the nucleotide string by reading in a file as argument #1, argument #2 is the k value, which is the size of k the user is looking for, that is entered in manually by the user. The output for this function will be the possible kmers for a given string and k size. Reading in a file will be an integer with the possible kmers, each line has its own results and the printed output is one line per string in the file that was read in.
     '''

# If statements are used to prevent users from entering in negative integers or floating numbers before the rest of the function to produce a 0 as an output.   
# re.sub() functions stands for a substring and returns a string with replaced values.  
# It will ONLY allow the characters in the [^] brackets and will omit any other characters that are not listed in the bracket. 
# Here we are using the same variable name, 'string', so it can be used throughout my functions without having to replace all the 'string' variable names.

# length is the length of the string that is a file read into the function
# possible_kmer1 is the equation: length of the string - k size + 1, +1 to include the entire length of the string
# possible_kmer2 is the equation 4^k, 4 is for the 4 possible nucleotide options A, T, G, & C, and k represents the k size
# because the possible kmer is the minimum value from the two previously stated equations, there is an if/else statement
# if statement goes through the string and if possible_kmer1 is less than possible_kmer2, the variable "possible_kmer" gets the value of possible_kmer1
# if statement goes through the string and if possible_kmer1 is more than possible_kmer2, the variable "possible_kmer" gets the value of possible_kmer2 (the lesser of the 2 answers)
# return provides the integer that is the minimum of the two expressions provided
  


    string = re.sub("[^ATGC]","", string)
    

    #print(string)
    if k <1:
        possible_kmer = 0
        return (possible_kmer)
    if type(k) == float:
        possible_kmer = 0
        return (possible_kmer)
    
    length = len(string)
    possible_kmer1 = length - k + 1
    possible_kmer2 = 4**k

    if possible_kmer1 < possible_kmer2:
        possible_kmer = possible_kmer1
    else:
        possible_kmer = possible_kmer2
 
  
    return(possible_kmer)



#END of get_possible_kmers function 
###############################################################################################################################################

def get_observed_kmers (string, k):
    '''This defined function, "get_observed_kmers", is to count observed kmers of size k from a string, where k and the string are specified as arguments. The user will need to enter in the nucleotide string by reading in a file as argument #1, argument #2 is the k value, which is the size of k that the user is looking for that is entered in manually by the user. The output for this function will be the observed kmers for a given string and k size. Reading in a file will produce a result where each line has its own results and the printed output is one line per string in the file that was read in. 
    '''

# If statements are used to prevent users from entering in negative integers or floats before the rest of the function to produce a 0 as an output.   
# re.sub() functions stands for a substring and returns a string with replaced values.  
# It will ONLY allow the characters in the [^] brackets and will omit any other characters that are not listed in the bracket. 
# Here we are using the same variable name, 'string', so it can be used throughout my functions without having to replace all the 'string' variable names.   
# length is the length of the string that is manually entered in by the user
# count variable states that the counting starts at 0
# number_of_kmers is the variable that is the possible number of kmers 
# nuc_list is the nucleotide list that contains the 4 possible nucleotide options: A, T, G, & C.  It is outside of the 'for loop' so that it does not reset each time the loop is running
# for loop starts at i and is the variable "number_of_kmers"
# kmer variable in the loop is a string that is in the range of the start "i" and ends at the last nucleotide in the string 
# if statement goes through the string and if the nucleotide was already in the nuc_list it just continues
# else is used in case a nucleotide is not already in the nuc_list.  It is then appended to the list 
# the else count +=1, adds 1 to the count of the nucleotides that are in the nuc_list
# return provides the integer count of all the unique nucleotides in the nuc_list
    
    
    string = re.sub("[^ATGC]","", string) 
    
    #print(string)
    
    if k <1:
        observed_kmer = 0
        return (observed_kmer)
    if type(k) == float:
        observed_kmer = 0
        return (observed_kmer)
    
    length = len(string)
    count = 0
    number_of_kmers = length - k + 1
    nuc_list = []
    for i in range(number_of_kmers):
        kmer = string[i:i+k]
        
        if kmer in nuc_list:
            continue 
        else:
            nuc_list.append(kmer)
            count += 1
     
    return(count)


#END of get_possible_kmers function 
#########################################################################################################################################

def get_k_list(string):
    '''
    This defined function, "get_k_list", is part of four functions to create a pandas data frame containing all possible k size (based on the length of the string) and the associated number of observed and possible kmers. The user will need to enter in the nucleotide string as a file read in as the argument. The output for this function will be a list that will be combined with two other lists to create the table, each list created for the table represents a separate line of nucleotide string found within the read in file.
    '''
# re.sub() functions stands for a substring and returns a string with replaced values.  It will ONLY allow the characters in the [^] brackets and will omit any other characters that are not listed in the bracket.  Here we are using the same variable name,'string', so it can be used throughout my functions without having to replace all the 'string' variable names.
    
# In order to produce the dataframe table, first a function called "get_k_list needs to be created. 
# The same argument, the string, for the get_dataframe function will be entered in directly or a file read into the argument. 
# An empty list named "k_list" is created and is outside of the for loop so that it does not reset each time the loop is running
# n is the variable that is the length of the string 
# for loop starts at i and is in the range of the start "1" and ends at the length of the last nucleotide in the string 
# k_list is appended to the list, and adds 1 to the list  
# return provides a list of integers of a running list of numbers (1-through the length of the string)



    string = re.sub("[^ATGC]","", string) 
    

    #print(string)
    
    k_list = []
    n = len(string)
    for i in range(1, n + 1):
        k_list.append(i)
  
    return k_list


# re.sub() functions stands for a substring and returns a string with replaced values.  It will ONLY allow the characters in the [^] brackets and will omit any other characters that are not listed in the bracket.  Here we are using the same variable name,'string', so it can be used throughout my functions without having to replace all the 'string' variable names.

# In order to produce the dataframe table, a second function called "observed_kmers_list" needs to be created. 
# The same argument, the string for the get_dataframe function will be entered in directly or a file read into the argument. 
# An empty list named "observed_kmers" is created and is outside of the for loop so that it does not reset each time the loop is running
# for loop starts at i and is in the range of the start "1" and ends at the length of the last nucleotide in the string 
# observed_kmers is appended with the "get_observed_kmers" function previously created in a seperate function, the two arugments are 1)the string and 2) i, 
# return provides a list of integers of a running list of observed_kmers (1-through the length of the string)

def observed_kmers_list(string):
    '''
    This defined function, "observed_kmers_list", is part of four functions to create a pandas data frame containing all possible k and the associated number of observed and possible kmers. The user will need to enter in the nucleotide string as a file read in as the argument. The output for this function will be a list that will be comined with two other list to create the table, each list created for the table represents a seperate line of string found with in the read in file.
    '''
    

    string = re.sub("[^ATGC]","", string) 
 
    #print(string)
    
    observed_kmers = []
    for i in range(1, len(string)+1):
    
        observed_kmers.append(get_observed_kmers(string, i))
           
    return observed_kmers

#re.sub() functions stands for a substring and returns a string with replaced values.  It will ONLY allow the characters in the [^] brackets and will omit any other characters that are not listed in the bracket.  Here we are using the same variable name,'string', so it can be used throughout my functions without having to replace all the 'string' variable names.

# In order to produce the dataframe table, next a function called "possible_kmers_list" needs to be created. 
# The same argument, the string, for the get_dataframe function will be entered directly or a file read into the argument. 
# An empty list named "possible_kmers" is created and is outside of the for loop so that it does not reset each time the loop is running
# for loop starts at i and is in the range of the start "1" and ends at the length of the last nucleotide in the string 
# possible_kmers is appended with the "get_possible_kmers" function previously created in a seperate function, the two arugments are 1) the string and 2) i 
# return provides a list of integers of a running list of possible_kmers (1-through the length of the string)


def possible_kmers_list(string):
    '''
    This defined function, "possible_kmers_list", is part of four functions to create a pandas data frame containing all possible k and the associated number of observed and possible kmers. The user will need to enter in the nucleotide string as a file read in as the argument. The output for this function will be a list that will be combined with two other lists to create the table, with each list created for the table representing a separate line of string found within the read in file.
    '''
   
    string = re.sub("[^ATGC]","", string) 
   
    #print(string)
    
    possible_kmers = []
    
    for i in range(1, len(string)+1):
        possible_kmers.append(get_possible_kmers(string, i))
           
    return possible_kmers

# In order to produce the dataframe table, lastly, the function "get_dataframe" was produced. 
# The same argument for the get_dataframe function will be entered in directly or as file read into the argument. 
# Outside of the function the Pandas function was imported
# A variable "k_list" was created by using the function get_k_list(string)
# A variable "observed_kmers" was created by using the function observed_kmers_list(string)
# A variable "possible_kmers" was created by using the function possible_kmers_list(string)
# A dictionary, "dict" was created by providing the name of the column followed the appropriate variable, this was done for each the three columns/variables
# A variable "df" was created using the pandas function for a DataFrame, the argument was the dictionary that was just created
# return provides a table of integers from the functions/variables previously mentioned


def get_dataframe(string):
    '''
    The purpose of this defined function, "get_dataframe_kmers", is to create a pandas data frame containing all possible k sizes and the associated number of observed and expected kmers. The user will need to enter in the nucleotide string as a file read in as the argument. The output for this function will be a table that has the 3 columns (alongside a generic Python row number column), where the column names are 'k', 'Observed kmers'and 'Possible kmers'.  Each table represents a seperate line of string found within the read in file.
    '''
   
    string = re.sub("[^ATGC]","", string) 
    
    #print(string)

    k_list = get_k_list(string)
    observed_kmers = observed_kmers_list(string)
    possible_kmers = possible_kmers_list(string)

    dict = {'k' : k_list, 'Observed kmers' : observed_kmers, 'Possible kmers': possible_kmers}
   
   
    #data = {'k':[a], 'Observed kmers':[b], 'Possible kmers':[c]}
    
    df = pd.DataFrame(dict)
    #display(df)
    return (df)




#END of get_dataframe function 
#########################################################################################################################################

def ling_complexity(string):
  
    '''
    This defined function, "ling_complexity", is used to calculate linguistic complexity. The user will need to enter in the nucleotide string by reading in a file as argument #1. The output for this function will be the linguistic complexity from the dataframe created from the "get_dataframe" function. The output of reading in a file will be a float that represents the linguistic complexity, and each line within the file will have its own results in the printed output.
    '''

# re.sub() functions stands for a substring and returns a string with replaced values.  It will ONLY allow the characters in the [^] brackets and will omit any other characters that are not listed in the bracket.  Here we are using the same variable name, 'string', so it can be used throughout my functions without having to replace all the 'string' variable names.
# A variable "observed" was created by using the function observed_kmers_list(string), the argument is the same as the input from the user for the function 
# A variable "possible" was created by using the function possible_kmers_list(string), the argument is the same as the input from the user for the function 
# A sum_observed variable was created and starts the counting at 0
# A sum_possible variable was created and starts the counting at 0
# the first for loop starts at i and allows the sum of the observed list to be calculated
# the second for loop starts at i and allows the sum of the possible list to be calculated
# A varible "ling_complex was created; this is the output of the varible sum_obsereved divided by the sum_possible variable  
# return provides the float that is the linguistic complexity from the functions/variables previously mentioned

   
    


    string = re.sub("[^ATGC]","", string) 
    

    #print(string)

    observed = observed_kmers_list(string)
    possible = possible_kmers_list(string)
    
    sum_observed = 0
    sum_possible = 0
    for i in observed:
        sum_observed += i

    for i in possible:
        sum_possible +=i

   
    ling_complex = sum_observed / sum_possible
    #print("The linguistic complexity of this nucleotide is", ling_complex)
    
    return(ling_complex)


#only run this print if you're running the script
if __name__== '__main__':
    string1 = open("sampledna.txt.txt", "r")
    string = (string1.readlines())
    
    for i in string:
        print(get_dataframe(i))
        print("The linguistic complexity is: ",  ling_complexity(i))

        
#END of ling_complexity function 
#########################################################################################################################################

