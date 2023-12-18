with open("subjects.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

subjects_dict = {}

for line in lines:
    parts = line.split(":")
    subject = parts[0].strip()
    activities = parts[1].split()
    total_lectures = total_practicals = total_labs = 0

    for activity in activities:
        if "(л)" in activity:
            total_lectures += int(activity.split("(л)")[0])
        elif "(пр)" in activity:
            total_practicals += int(activity.split("(пр)")[0])
        elif "(лаб)" in activity:
            total_labs += int(activity.split("(лаб)")[0])

    total_activities = total_lectures + total_practicals + total_labs

    subjects_dict[subject] = total_activities

print(subjects_dict)
