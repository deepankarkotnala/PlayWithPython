import os
import datetime
from selenium import webdriver
chrome_path = r"D:\Softwares\chromedriver80\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
driver.get("http://delhi.craigslist.com")
driver.find_element_by_xpath("""//*[@id="jjj0"]/li[25]/a""").click()
posts = driver.find_elements_by_class_name("hdrlnk")

# Changing the current working directory to Desktop
os.chdir(r"C:\Users\dkotn\Desktop")
# Getting the current working directory
cwd = os.getcwd()
print(cwd)

try:
    print("Opening file and writing data")
    with open(os.path.join(cwd,"scraped.txt"), "w") as output:
            output.write('Job Listing for Date: %s.\n' % 
            (datetime.date.today()))

    for post in posts:
        with open(os.path.join(cwd,"scraped.txt"), "a+") as output:
            output.write("\n")
            output.write(str(post.text))
    print("Job listing for date: %s successfully saved in file %s" %
    (datetime.date.today(), os.path.join(cwd,"scraped.txt")))

except:
    print("Could not write data to file. Please contact the development team.")
