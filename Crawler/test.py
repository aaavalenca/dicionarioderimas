import csv

def append_to_file(filename, new):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        content = list(reader)[1]
        content.extend(new)
    with open(filename, 'w') as f:
        write = csv.writer(f)
        write.writerow(["palavra"])
        write.writerows([content])
        f.close()