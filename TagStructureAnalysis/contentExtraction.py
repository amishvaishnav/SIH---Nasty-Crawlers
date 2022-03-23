from bs4 import BeautifulSoup
import os, os.path
# import pprint/

def extract(path):
    # assign directory
    directory = 'marketplaces'

    resultFile = open("result.txt", "w")
    resultData = ""

    # iterate over files inthat directory
    # for filename in os.listdir(directory):
    #     file = os.path.join(directory, filename)
    #     # checking if it is a file
    #     if os.path.isfile(file):

    file = path
    soup = BeautifulSoup(open(file, "r"), "lxml")


    extractTag = ['h1', 'h2', 'p', 'h3', 'a', 'h4', 'h5', 'h6', 'span']
    data = ""

    # match = soup.find('div')
    # for i in extractTag:
    # result = soup.find_all(extractTag)
    resultData = soup.get_text(" ")

    # for x in range (len(result)):

    resultFile.write(resultData)        

