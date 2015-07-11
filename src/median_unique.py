"""
median_unique.py
Author:  Lin Crampton
Version:  1.0

Given a file of text strings, return a file containing running median count of unique words.  No munging, lower-casing, etc.
Checks for the existence of the hardcoded input filename, and for existence of command-line arguments.  Drops out when the input file does not exist; drops out when commandline arguments do exist.

Dependencies:
    Python 2.7 (not Python3)
    
Usage:  words_tweeted.py

ToDo:  Check for writability of output directory; give option for help

"""

import sys, os, numpy, re
#from re import split
from collections import Counter
    
#check_valid_arguments - exit unless program run without
def check_valid_arguments():
    if len(sys.argv) != 3:
        sys.exit('\nExiting - inappropriate number of arguments; input / output filenames hardcoded.\nUsage: %s' % sys.argv[0])

# check_inputfile_exists - exits if inputfile empty or otherwise unreadable
def check_inputfile_exists(file_path):   
    if not os.path.exists(file_path):
        with open(file_path) as fi:
            if not fi.read(3):  #avoid reading entire file.
                sys.exit('\nExiting - %s is empty or non-existant inputfile\n' % file_path)

# get_inputfilename returns the name of file containing tweets to be processed
def get_inputfilename():
    tweet_filename = sys.argv[1]
    check_inputfile_exists(tweet_filename)
    return(tweet_filename)

# get_outputfilename simply returns the name of the outputfilename; spec unclear as to whether not avoid clobbering existing file
def get_outputfilename():
    results_filename = sys.argv[2]
    return(results_filename)

# count_unique_words determines the number of unique words in each line of the input file and prints out the running median  
def count_unique_words(input_filename):
    running_medians = []
    unique_words_in_tweet=[]
    with open(input_filename, "rU") as f:
        for line in f:
            count=len(unique_list(line.split()))
            if not line:
                continue
            unique_words_in_tweet.append(count)
            running_medians.append(get_median_length(unique_words_in_tweet))
    return(running_medians)  

# unique_list takes an input list and returns unique entries
def unique_list(l):
    ulist=[]
    [ulist.append(x) for x in l if x not in ulist]
    return ulist

# get_median_length extracts running cumulative median from list of medians
def get_median_length(word_length):
    return numpy.median(numpy.array(word_length))

# write_running_medians outputs the running medians to a file; no error check here yet
def write_running_medians(running_medians, output_filename):
    medians_file = open(output_filename,'w')
    for median in running_medians:
        medians_file.write("%.1f\n" % median)
    medians_file.close() 
#-=-=-=-=-=-=-=-=-=-=-=-=-=-

def main():
    check_valid_arguments()
    tweet_filename = get_inputfilename()
    output_filename = get_outputfilename()
    list_of_medians = count_unique_words(tweet_filename)
    write_running_medians(list_of_medians, output_filename)

if __name__ == '__main__':
    main()
