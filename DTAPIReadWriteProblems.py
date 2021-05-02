
#Utility functions:
#1. Read a metric value from Dyntrace server using RESTAPI
#2. Save data in JSON file
#3. Pick only Metric Name and values from file
#4. Check if any of the value is above defined threshold
#5. Read problem card JSON file to be sent as part of API request to 
#6. Create problem card in Dynatrace if value is above threshold (threshold input by user).
#   Problem Card JSON template included
# Note enable Trello and Slack integrations to send out notifications to corresponding teams

import json
import requests

#DT API Token
ApiTokenValue = '<your DT API Token'
#DT Tenant
tenant = "https://xxx.live.dynatrace.com"


#Step 1 GET json directly from DT server. This example is for only 1 metric
querystring = {'resolution':'10m','Api-Token':ApiTokenValue, 'metricSelector':'builtin:host.cpu.usage'}
ResponsefromDT = requests.get(tenant+"/api/v2/metrics/query", params=querystring)
print('1. JSON API Download Success-----------------')
#print(ResponsefromDT.json())
print('-----------------')

#Step 2 Save data to file on drive
with open('CPUHealth.python', 'w') as json_file:
  json.dump(ResponsefromDT.json(), json_file)
print('2. File Saved in Drive Success ------------------')

#Step 3 load json file from local directory
with open('C:\Ankur\Scripts\CPUMetric.json') as f:
  data_DICT = json.load(f)

# Step 4 Output: dt metrics format
print('3 Printing Entire File -----------------')
#print(data_DICT)

print('4 Printing Metric name & values  -----------------')
print(data_DICT["result"][0]["metricId"])
print("\n")
print(data_DICT["result"][0]["data"][0]["values"])
print('-----------------')

# Step 5 Get user input of threshold
print("\n")
userinput = input("Enter threshold value in digits: ")
thresholdvalue = int(userinput)

#Step 6 Checking all values and comparing with threshold value
for x in data_DICT['result'][0]['data'][0]['values']:
  print(x)
  if x is None:
      y = 0
  else:
      y = float(x) #converting string to float
      if y < thresholdvalue:   #if CPU is less than 75
          print('All Good')
      else:
          #value above threshold. So connect to Dynatrace and create a problem card
          print('\n 5. Need to raise alert. Now creating problem ticket in Dynatrace \n')
          
          #Read Problem Card JSON file
          with open('C:\Ankur\Scripts\ProblemCard.json') as outfile:
                problemjson_DICT = json.load(outfile)
          
          print("json data: \n")
          print(problemjson_DICT)

          print("\n 6. Sending Problem Card to Dynatrace "+tenant+"/api/v1/events/?Api-Token="+ApiTokenValue)
          posturl = tenant+"/api/v1/events?Api-Token="+ApiTokenValue
          result = requests.post(posturl, json = problemjson_DICT, headers = {"content-type": "application/json"})
          print("\n -------Problem Card Creation Status: " + result.text)
          break

print("\n Check your dynatrace dashboard here:"+ tenant)










