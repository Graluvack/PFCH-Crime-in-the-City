import requests
import json
import csv

AllData = []
acnt = 0
#Fetching crime categories
with open('CrimeCategories.json', 'r') as f:
    Crimes = json.load(f)
    for CT in Crimes:
        print(CT)
        #Create and reset the teporary data storage
        TempData = []
        count = 0
        for crime in Crimes[CT]:
            #Get data from API
            r = requests.get(f'https://data.cityofnewyork.us/resource/uip8-fykc.csv?ofns_desc={crime}&$limit={Crimes[CT][crime]}')
            decoded_content = r.content.decode('utf-8')
            cr = csv.reader(decoded_content.splitlines(), delimiter=',')
            my_list = list(cr)
            #Only keep the hedder once
            if count == 0:
                TempData.append(my_list[0])
                count+=1
                if acnt == 0:
                    AllData.append(my_list[0])
                    acnt+=1

            #append all the data
            for row in my_list[1:]:
                TempData.append(row)
                AllData.append(row)
            print(crime)      
            print("-------------------------------------------------")
        #Write to CSV
        with open(f'Final Data/{CT}Data.csv', 'w') as out:
            writer = csv.writer(out)
            writer.writerows(TempData)
        with open('Final Data/AllData.csv', 'w') as out:
            writer = csv.writer(out)
            writer.writerows(AllData)