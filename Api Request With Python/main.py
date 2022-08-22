import requests
#  In this project, I used python in order to fetch my repositories from github
response= requests.get("https://api.github.com/users/arsenhh-byte/repos")
my_projects = response.json()

#Looping through the list in order to find get each item in the repository
# print(response.json())
for project in my_projects:
    print (f"Project Name: {project['name']}, \n Project Url: {project['svn_url']} \n" )  