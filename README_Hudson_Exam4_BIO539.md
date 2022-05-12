README
This Readme file is for Robbie Hudson's BIO539 Exam 4 May 11, 2022

Python 3.6.8 (default, Nov 16 2020, 16:55:22) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.4.0 -- An enhanced Interactive Python. Type '?' for help.

Uploaded to GitHub for this project are 4 files:
1) README.md
2) Python script = kmer_script_Hudson.py
3) Python test script = kmer_testScript_Hudson.py
4) Data file = sampledna.txt.txt


1)README.md - Thank you for reading this document first. This will include instructions how to use this code. 

The scripts produced for this exam are to:
1. Define a function to count possible kmers of size k from a string, where k and the string are specified as arguments.
2. Define a function to count observed kmers of size k from a string, where k and the string are specified as arguments.
3. Define a function to create a pandas data frame containing all possible k and the associated number of observed and expected kmers (see above table).
4. Define a function to calculate linguistic complexity.
5. The main function of the script is to produce a data frame that displays the kmer size, observed kmers and possible kmers based upon the sample data file that contains strings of nucleotides 


2)Python script: kmer_script_Hudson.py file has all the functions required for this exam including docstrings and comments about the script. The Docstrings for each function include what the function is, what the function does, input type and the anticipated output. The comments explain the purpose of each part of the script.

To run the code, you will need to navigate to the folder in which you download this file (kmer_script_Hudson.py) and the sampledna.txt file. On the command line, enter: $ python3 kmer_script_Hudson.py. This will generate 3 dataframes and the associated lingustic complexity of each string of nucleotides,and one table for each line of script within the sampledna.txt file.
  
3)Python test script: kmer_testScript_Hudson.py is a .py file is used to test the functions created in the kmer_script_Hudson.py file. 

To run the code you will need to navigate to the folder in which you download this file, the kmer_script_Hudson.py file and the sampledna.txt file. On the command line, enter: $ py.test. This will generate a test session output, that contains 14 test scripts within this file.

4) The Data file "sampledna.txt.txt" was provided to the class for this exam. This file will need to be read into the functions, and it contains 3 seperate strings. 


Any questions about these documents that are part of my BIO539 Exam4, please contact me at rhudson@uri.edu 

Thank you


