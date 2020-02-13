# Open Notify API - Getting live data from NASA

We will use Open Notify API to get data from NASA. This data contains current coordinates of ISS, Number of Astronauts in space right now and their names.

```python
import requests
import os
request = requests.get('http://api.open-notify.org/iss-now.json')

if(request.status_code ==200):
    print('\nURL check: OK. \nEndpoint hit successful.\n')

# Convert json to a dictionary
iss_data = request.json()

print('Present Coordinates of International Space Station (ISS):')
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

# Print the number of people in space 
print('\nThere are {} astronauts in the space right now!' .format(astro_dict["number"]))

# Print the names of people in space using a for loop
print('\nList of Astronauts in Space:')
for p in astro_dict['people']:
    print(p['name'])
    
```

Here's the output of the python script:

![img](https://github.com/deepankarkotnala/PlayWithPython/blob/master/APIs_Using_Python/Images/NASA_API_Info.JPG)
