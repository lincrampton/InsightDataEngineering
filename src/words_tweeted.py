"""
words_tweeted.py
Author:  Lin Crampton
Version:  1.0

Given a file of text strings, return a file containing word counts.  No munging, lower-casing, etc.
Checks for the existence of the hardcoded input filename, and for existence of command-line arguments.  Drops out when the input file does not exist; drops out when commandline arguments do exist.

Dependencies:
    Python 2.7 (not Python3)
    
Usage:  words_tweeted.py

ToDo:  Check for writability of output directory; give option for help

"""

import sys, os
from re import split
from collections import Counter
    
TWEET_FILE_IN = '../tweet_input/tweets.txt'
TWEET_COUNT_FILE = '../tweet_output/ft1.txt'

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

# count_words - uses Python Counter to calculate and return word frequencies in input filename
def count_words(filename):
    counter = Counter()
    with open(filename, "rU") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            counter.update(x for x in line.split() if x)
    return counter

#format_and_print takes Counter list input, alpha sorts, formats, and prints to outputfile
def format_and_print(counter, output_filename):
    tweet_list = counter.items()
    tweet_list.sort()
    template = "{0:45}{1:5}\n" 
    f = open(output_filename,'w')
    for tweet in tweet_list: 
        f.write(template.format(*tweet))
    f.close() 
#-=-=-=-=-=-=-=-=-=-=-=-=-=-

def main():
    check_valid_arguments()
    tweet_filename = get_inputfilename()
    tweet_count = count_words(tweet_filename)
    output_filename = get_outputfilename()
    format_and_print(tweet_count, output_filename)

if __name__ == '__main__':
    main()
