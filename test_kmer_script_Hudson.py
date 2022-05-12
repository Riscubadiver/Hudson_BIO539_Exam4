from kmer_script_Hudson import *

#!/usr/bin/env python3

def test_poskmersimple():
    #Possible kmer simple
    assert get_possible_kmers("ATTTGGATT", 5) == 5

def test_poskmerneg():
    #Possible kmer negative integer
    assert get_possible_kmers("ATTTGGATT", -5) == 0, "k-value needs to be a positive integer"  
    
def test_poskmerfloat():
    #Possible kmer k value float
    assert get_possible_kmers("ATTTGGATT", 1.9) == 0, "k-value needs to be a positive integer"     

def test_poskmerWrongChar():
    #Possible kmer wrong character
    assert get_possible_kmers("ATTTGGATT;", 5) == 5   
    
#END of get_possible_kmers function Test 
############################################################################################################################################### 

def test_obskmersimple():
    #Observed kmer simple
    assert get_observed_kmers ("ATTTGGATT", 5) == 5
    
def test_obskmerneg():
    #Observed kmer negative integer
    assert get_observed_kmers ("ATTTGGATT", -5) == 0, "k-value needs to be a positive integer"  

def test_obskmerwrongchar():
    #Observed kmer wrong character
    assert get_observed_kmers("ATTTGGATT;", 5) == 5

    
#END of get_possible_kmers function Test
#########################################################################################################################################

def test_klistsimple():
    #Klist simple
    assert get_k_list("ATTTGGATT") == [1, 2, 3, 4, 5, 6, 7, 8, 9]

def test_klistsimple():
    #Klist wrong character
    assert get_k_list("ATTTGGATT;") == [1, 2, 3, 4, 5, 6, 7, 8, 9]   

def test_observlistsimple():
    #Observed list simple
    assert observed_kmers_list("ATTTGGATT") == [3, 5, 6, 6, 5, 4, 3, 2, 1]

def test_observlistwrongchar():
    #Observed list wrong character
    assert observed_kmers_list("ATTTGGATT;") == [3, 5, 6, 6, 5, 4, 3, 2, 1]
        

def test_possiblistsimple():
    #Possible list simple
    assert possible_kmers_list("ATTTGGATT") == [4, 8, 7, 6, 5, 4, 3, 2, 1]
        
def test_possiblistwrongchar():
    #Possible list wrong character
    assert possible_kmers_list("ATTTGGATT;") == [4, 8, 7, 6, 5, 4, 3, 2, 1]        
        

#def test_dataframesimple():
    #dataframe simple
    #assert get_dataframe("ATTTGGATT") == a table 




#END of get_dataframe function Test
#########################################################################################################################################

def test_ling_complexitysimple():
    #ling_complexity simple
    assert ling_complexity("ATTTGGATT") == 0.875 
    
def test_ling_complexityWrongChar():
    #ling_complexity wrong character 
    assert ling_complexity("ATTTGGATT;") == 0.875

    
#END of ling_complexity function TEst
#########################################################################################################################################