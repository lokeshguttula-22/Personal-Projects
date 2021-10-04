from xml.etree import ElementTree
import os
import csv
import pandas as pd

tree=ElementTree.parse('employee.xml')

employee_data=open('employee.csv','w',newline='',encoding='utf-8')
csvwriter=csv.writer(employee_data)

col_names=['id','name','email','password']
csvwriter.writerow(col_names)

root = tree.getroot()

for eventData in root.findall('eventData'):
    event_data=[]
    event=eventData.find('row')

    event_id=event.find('id')
    if event_id!=None:
        event_id=event_id.text
    event_data.append(event_id)

    event_name=event.find('name')
    if event_name!=None:
        event_name=event_name.text
    event_data.append(event_name)

    event_email=event.find('email')
    if event_email!=None:
        event_email=event_email.text
    event_data.append(event_email)

    event_password=event.find('password')
    if event_password!=None:
        event_password=event_password.text
    event_data.append(event_password)
    csvwriter.writerow(eventData)

employee_data.close()
dataframe=pd.read_csv('employee.csv')
print(dataframe.shape)