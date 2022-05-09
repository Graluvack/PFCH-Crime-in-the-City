import csv

CrimeTypes = {}
CT = []
count=0

with open('NYPD_Arrest_Data__Year_to_Date_.csv') as raw:
    data = csv.reader(raw)
    for row in data:
        if row[5] not in CrimeTypes:
            CrimeTypes[row[5]]=0
        CrimeTypes[row[5]]+=1
for crime in CrimeTypes:
    print(crime)
print(CrimeTypes)




