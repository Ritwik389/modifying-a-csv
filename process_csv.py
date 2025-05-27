import csv

# Step 1: Read original CSV
with open('students.csv', 'r') as infile:
    reader = csv.DictReader(infile)
    rows = []

    for row in reader:
        math = int(row['math'])
        science = int(row['science'])

        # Calculate average
        average = (math + science) / 2

        # Add new field to row
        row['average'] = round(average, 2)

        rows.append(row)

# Step 2: Write to a new CSV
with open('students_modified.csv', 'w', newline='') as outfile:
    fieldnames = ['name', 'math', 'science', 'average']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(rows)

print("Modified CSV written to 'students_modified.csv'")
