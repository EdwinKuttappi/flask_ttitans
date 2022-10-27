import requests

url = "https://public-holiday.p.rapidapi.com/2022/US"

headers = {
	"X-RapidAPI-Key": "48e23c6bf3msh9a6baf3e68d9a4ep14546ajsn1a39e98c4ad5",
	"X-RapidAPI-Host": "public-holiday.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.text)

events_lists=[]
event = ""
while(event != "N"):
    dictionary = {}
    dictionary["Event"] = input("Enter the name of the Event: ")
    dictionary["Date"] = input("Enter a date: ")
    dictionary["Start time"] = input("Enter a start time: ")
    dictionary["End time"] = input("Enter a end time: ")
    events_lists.append(dictionary)
    flag = input("Continue adding events?: ")
    if flag == "N":
        break
    else:
        continue

print(events_lists)

# Planning to delete this file, done in Python 
