import json

student1 = {
    'first name': 'Greg',
    'last name': 'Dean',
    'scores': [70, 80, 90],
    'description': 'Good job, Greg',
    'certificate': True
}

student2 = {
    'first name': 'Wirt',
    'last name': 'Wood',
    'scores': [80, 80.2, 80],
    'description': 'Nicely done',
    'certificate': True
}

data = [student1, student2]
data_json = json.dumps(data, indent=4, sort_keys=True)
data_again = json.loads(data_json)
print(sum(data_again[0]['scores']))


print(json.dumps(data, indent=4, sort_keys=True))
with open('students_example.json') as myfile:
    json.dump(data, myfile, indent=4, sort_keys=True)

# with open('students_example.json') as myfile:
#    data_again = json.load(myfile)
#    print(sum(data_again[1]['scores']))
