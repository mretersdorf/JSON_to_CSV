import json
import csv

# Import JSON file -> Dict
json_file = "input_data.json"
with open(json_file, "r") as file:
    data = json.load(file)


# Export CSV file
with open('output_data.csv', 'w', newline='') as csvfile:
    fieldnames = ['Course Title', 'Course Code', 'Section Title', 'Section Code']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for row in data:
        writer.writerow({
            'Course Title': data[row]['courseTitle'],
            'Course Code': data[row]['courseCode'],
            'Section Title': data[row]['sectionTitle'],
            'Section Code': data[row]['sectionCode']
        })

csvfile.close()
