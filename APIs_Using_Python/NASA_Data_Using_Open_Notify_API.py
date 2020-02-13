import requests
import os
request = requests.get('http://api.open-notify.org/iss-now.json')

if(request.status_code ==200):
    print('\nURL check: OK. \nEndpoint hit successful.')

# Convert json to a dictionary
iss_data = request.json()

# Function to recursively iterate elements of a nested dictionary
def iterdict(d):
  for k,v in d.items():        
     if isinstance(v, dict):
         iterdict(v)
     else:            
         print (k,":",v)

# Print the elements of iss_data dictionary
iterdict(iss_data)

people = requests.get('http://api.open-notify.org/astros.json')

# Convert json to a dictionary 
astro_dict = people.json()
print('\nThere are {} astronauts in the space right now!' .format(astro_dict["number"]))

