A **decorator** is a function that takes a function as its only parameter and returns a function. This is helpful to “wrap” functionality with the same code over and over again. 

```python
# Adds a welcome message to the string 
# returned by fun(). Takes fun() as 
# parameter and returns welcome(). 
def decorate_message(fun): 
  
    # Nested function 
    def addWelcome(site_name): 
        return "Welcome to " + fun(site_name) 
  
    # Decorator returns a function 
    return addWelcome 
  
@decorate_message
def site(site_name): 
    return site_name; 
  
# Driver code 
  
# This call is equivalent to call to 
# decorate_message() with function 
# site("GeeksforGeeks") as parameter 
print(site("Data Science Universe"))
```
