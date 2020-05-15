# 0. import required lib
import csv

# 1. opening csv file
with open (r'd:\Code\py\4-Database\output\smalldata.csv','r') as infile:
    
    # 2. define content by delimiter
    content = csv.DictReader(infile, delimiter=',')
    #print(list(content))
    # 3. reading csv line by line
    # for line in content:
    #     print(line)
    #     # 4. defining each data in a line
    #     # year = line['Year']
    #     # age = line['Age']
    #     # ethnic = line['Ethnic']
    #     # sex = line['Sex']
    #     # area= line['Area']
    #     # count= int(line['count'])

