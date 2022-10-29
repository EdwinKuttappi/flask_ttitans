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
  "day": 11,
  "title": "Allen's Birthday"
})
events_list.append({
  "month": "November",
  "day": 24,
  "title": "Thanksgiving"
})
events_list.append({
  "month": "November",
  "day": 27,
  "title": "party"
})
events_list.append({
  "month": "November",
  "day": 30,
  "title": "day before december"
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