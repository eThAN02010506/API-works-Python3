import requests as req

# This application uses FailchanceAPI created by Ethan Jiang

# It should provide a comment in the code detailing which API server your code consumes
# The application, when run, should give users the ability to access any and all information from the API
# Provide a README explaining what the software does
# Please create a separate repo for this project and submit it along with the link for the API Server you built

list_url = "http://10.6.20.246:8000/class_pass_chance"

start = input("Would you like to: \n"
              "1 - Toefl and rank of a participant\n"
              "2 - total number of participants\n"

              ">> ")
on = True

while on:
    if start == "1":
        participant_name = input("which person do you want to know?\n"
                                 ">> ")
        url = "http://10.6.20.246:8000/class_pass_chance/{participant_name}/fail_chance?api_key=060212"
        response = req.get(url=url)
        json_data = response.json()
        if "msg" in json_data:
            print(json_data["msg"])
        else:
            print(
                f"The person {json_data['name']} is rank {json_data['rank']} with a toefl score of {json_data['Toefl']} .")

    elif start == "2":
        url = "http://10.6.21.87:8000/class_pass_chance?api_key=060212"
        response = req.get(url=url)
        json_data = response.json()
        print(json_data)

    is_done = input("Is there anything else? (yes/no)\n"
                    ">> ")
    if is_done == "yes" or is_done == "Yes":
        on = False
    elif is_done == "No" or is_done == "no":
        pass
