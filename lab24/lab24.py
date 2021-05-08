import json
with open("in.json", "r") as input_file:
    input_data = json.load(input_file)

output_data = []


def find_user_index(userID):
    for index, element in enumerate(output_data):
        if element["userId"] == userID:
            return index


id_list = []

for user in input_data:
    current_id = user["userId"]
    if current_id not in id_list:
        id_list.append(current_id)
        output_data.append({"userId": current_id, "task_completed": 0})

    if user["completed"]:
        user_index = find_user_index(current_id)
        output_data[user_index]["task_completed"] += 1

with open("out.json", "w") as output_file:
    output_file.write(json.dumps(output_data, indent=2))




