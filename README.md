# JSONAPI
Python utlity to Read metric values from Dynatrace Cluster, parse JSON to read metric values, check values and create problem card in Dynatrace based in user input.

Included files:
1. python code
2. JSON format downloaded using rest api from Dynatrace server
3. JSON format required for uploading using rest api to Dynatrace server

Utility functions:
1. Read a metric value from Dyntrace server using RESTAPI
2. Save data in JSON file
3. Pick only Metric Name and values from file
4. Check if any of the value is above defined threshold
5. Read problem card JSON file to be sent as part of API request to 
6. Create problem card in Dynatrace if value is above threshold (threshold input by user).
#   Problem Card JSON template included
# Note enable Trello and Slack integrations to send out notifications to corresponding teams

What you will need
1. python 3.6 or above installed
2. Dynatrace tenant URL
3. Dynatrace API token with access to write events


