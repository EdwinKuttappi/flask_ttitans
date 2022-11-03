from flask import Blueprint, jsonify

api_bp = Blueprint(
    "calendar-api",
    __name__,
    url_prefix="/calendar-api",
    static_folder="static",
    static_url_path="static/calendar-api"
)

# url = "https://public-holiday.p.rapidapi.com/2022/US"

# headers = {
# 	"X-RapidAPI-Key": "48e23c6bf3msh9a6baf3e68d9a4ep14546ajsn1a39e98c4ad5",
# 	"X-RapidAPI-Host": "public-holiday.p.rapidapi.com"
# }

# response = requests.request("GET", url, headers=headers)

# print(response.text)

events_list=[]
events_list.append({
  "month": "November",
  "day": 3,
  "title": "3 \n N@TM!"
})
events_list.append({
  "month": "November",
  "day": 7,
  "title": "7 \n Finals Week Starts. Yay!"
})
events_list.append({
  "month": "November",
  "day": 8,
  "title": "8 \n Finals Period 5!"
})
events_list.append({
  "month": "November",
  "day": 9,
  "title": "9 \n Finals Period 1 and 2!"
})
events_list.append({
  "month": "November",
  "day": 10,
  "title": "10 \n Finals Period 3 and 4!"
})
events_list.append({
  "month": "November",
  "day": 11,
  "title": "11 \n NO SCHOOL"
})
events_list.append({
  "month": "November",
  "day": 24,
  "title": "24 \n Thanksgiving"
})
events_list.append({
  "month": "November",
  "day": 29,
  "title": "29 \n Tri 2 Begins!",
})
events_list.append({
  "month": "November",
  "day": 30,
  "title": "30 \n December Eve!",
})

@api_bp.route("/events")
def events():
    return jsonify(events_list)

# event = ""
# while(event != "N"):
#     dictionary = {}
#     dictionary["Event"] = input("Enter the name of the Event: ")
#     dictionary["Date"] = input("Enter a date: ")
#     dictionary["Start time"] = input("Enter a start time: ")
#     dictionary["End time"] = input("Enter a end time: ")
#     events_lists.append(dictionary)
#     flag = input("Continue adding events?: ")
#     if flag == "N":
#         break
#     else:
#         continue

# print(events_list)


''' delete after 
x = 1
for i in range():
    create(button(onclick: function, id = "x")

'''
