import re
filename = "my-acl.txt"
output_filename = "output2.txt"
email_regex = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}'

with open(filename, "r", encoding="latin1") as f, open(output_filename, "w") as out:
    for line in f:
        line = line.replace('\\n', '\n')
        emails = re.findall(email_regex, line)
        for email in emails:
            out.write(email + "\n")