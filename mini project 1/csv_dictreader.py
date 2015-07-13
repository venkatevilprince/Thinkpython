import csv

with open('names.csv', 'w') as csvfile:
    fieldnames = ['x', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'x': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'x': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'xy': 'Wonderful', 'last_name': 'Spam'})

with open('names.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['x'], row['last_name'])

