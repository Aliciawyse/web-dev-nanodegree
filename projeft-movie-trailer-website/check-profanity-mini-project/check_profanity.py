#Note, requests is not in python standard library. 
import requests

#read text from a file
def read_text():
    quotes = open(r"C:\Users\abarrett\Desktop\movie_quotes.txt")
    contents_of_file = quotes.read()
    #print(contents_of_file)
    quotes.close()
    
    check_profanity(contents_of_file)

#check text for curse words using the following website http://www.wdylike.appspot.com/?q=shot
def check_profanity(text_to_check):

    r = requests.get("http://www.wdylike.appspot.com/?q=shot" + text_to_check)

    #print(r.text)

    if "true" in r.text:
        print("Profanity alert!")
    elif "false" in r.text:
        print("This document had no curse words!")
    else:
        print("Could not scan the document.")

read_text()









