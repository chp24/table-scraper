from bs4 import BeautifulSoup
import requests 
import csv
from csv import writer

#setup csv to write and is now referred to as file within the code
with open('scrape.csv', 'w', newline='') as file:
    #the_writer is responsible for writing to the file
    the_writer = writer(file)
    #setting up header
    header = ['Release Number','Date','Respondents']
    #write the row 
    the_writer.writerow(header)
    #set up csv reader using urls file as our dataset
    with open('urls.csv','r') as csv_file:
        csv_reader = csv.reader(csv_file)

        #skip first line so that actual first entry is displayed
        next(csv_reader)
        for line in csv_reader:
            #now that we have the link to each page, go to each page
            page = requests.get(line[0])
            soup = BeautifulSoup(page.content,'html.parser')
            #find all row tags on page
            rows = soup.find_all('tr')
            #for every row tag
            for row in rows:
                #make a list for the row
                data = []
                #find every td tag within the row tag
                for td in row.find_all('td'):
                    info = td.text.replace('\n','')
                    data.append(info + line[1])
                #print(data)
                the_writer.writerow(data)        
print("done")