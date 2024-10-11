import csv

#file read

# example_file = open("example.csv",encoding="utf-8")

# csv_example_file = csv.reader(example_file)

# display_example_data = list(csv_example_file)

# #print(display_example_data)
# for item in display_example_data:
    # print(item)
# print(len(display_example_data))

#file write

write_csv_file = open('to_csv_file.csv', mode="w", newline='')
csv_write = csv.writer(write_csv_file, delimiter=',')

# Write the header
csv_write.writerow(['a', 'b', 'c', 'd'])

# Write multiple rows using writerows()
csv_write.writerows([[1, 2, 3, 4], [5, 6, 7, 8]])

# Close the file
write_csv_file.close()

# To verify the content, you would need to read it back
with open('to_csv_file.csv', mode='r') as read_csv_file:
    csv_reader = csv.reader(read_csv_file)
    for row in csv_reader:
        print(row)
