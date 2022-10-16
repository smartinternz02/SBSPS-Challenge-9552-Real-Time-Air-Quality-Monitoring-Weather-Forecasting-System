# Importing the required libraries
from datetime import datetime
import time
import requests
from calendar import monthrange
import base64
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Set Hour, Year, Month, Starting and ending day of the month
hour = 15
year = 2022
month_num = 9
start = 1
end = 0 or monthrange(year, month_num)[1]

# Naming the file in which data will be stored
file_name = f"Air_Quality_Index.csv"

# Opening the file
file = open(file_name, "a")

# Printing the column names
print('state,city,station,date,time,PM2.5,PM10,NO2,NH3,SO2,CO,OZONE,AQI,Predominant_Parameter')
print('state,city,station,date,time,PM2.5,PM10,NO2,NH3,SO2,CO,OZONE,AQI,Predominant_Parameter', file=file)


# Performs requests
response = requests.post(
    'https://app.cpcbccr.com/aqi_dashboard/aqi_station_all_india', data='e30=', verify='')

# Downloads and stores the AQI Dataset as csv file

for dataset in [day['stationsInCity'] for day in response.json()['stations']]:
    for data in dataset:
         if data['stateID'] == 'Punjab':
            id = data['id']
            for day in list(range(start, end + 1)):
                date_data = '{' + f'"station_id":"{id}","date":"{year}-{month_num}-{day}T{hour}:00:00Z"' + '}'
                date_data= base64.b64encode(date_data.encode()).decode()
                response = requests.post(
                    'https://app.cpcbccr.com/aqi_dashboard/aqi_all_Parameters', data=date_data, verify='')
                months = response.json()
                date = datetime.strptime(months['date'], "%A, %d %b %Y %I:%M %p")
                attributes = {'PM2.5': 'NA', 'PM10': 'NA', 'NO2': 'NA',
                     'NH3': 'NA', 'SO2': 'NA', 'CO': 'NA', 'OZONE': 'NA'}
                for month in months['metrics']:
                    attributes[month['name']] = str(month['max'])
                if months['aqi'] and '-' not in attributes.values():
                    print(f'{data["stateID"]},{data["cityID"]},"{data["name"]}","{date.strftime("%d/%m/%Y")}","{date.strftime("%I:%M:%S %p")}",{",".join(attributes.values())},{months["aqi"]["value"]},{months["aqi"]["param"]}')
                    print(f'{data["stateID"]},{data["cityID"]},"{data["name"]}","{date.strftime("%d/%m/%Y")}","{date.strftime("%I:%M:%S %p")}",{",".join(attributes.values())},{months["aqi"]["value"]},{months["aqi"]["param"]}', file=file)
                else:
                    print('error : No Data Available or Insufficient data for', id, data['stateID'],
                          data['cityID'], data['name'], months['title'], date)

# Closes the file
file.close()
