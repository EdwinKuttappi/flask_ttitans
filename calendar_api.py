from flask import Blueprint, jsonify, request

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
  "id": 0,
  "month": "November",
  "day": 3,
  "title": "3 \n N@TM!"
})

events_list.append({
  "id": 1,
  "month": "November",
  "day": 11,
  "title": "11 \n NO SCHOOL"
})

events_list.append({
  "id": 2,
  "month": "November",
  "day": 24,
  "title": "24 \n Thanksgiving"
})



@api_bp.route("/events", methods=["GET"])
def events():
    return jsonify(events_list)

@api_bp.route("/events/add", methods=["POST"])
def add_event():

  event_dict={
    "id": len(events_list),
    "month": request.form["month"],
    "day": int(request.form["day"]),
    "title": request.form["title"]
  }
  events_list.append(event_dict)
  return jsonify(event_dict)



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
