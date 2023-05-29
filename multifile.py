import os
import re

folder_path = "folder path"
email_regex = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}'

for filename in os.listdir(folder_path):
    input_file = os.path.join(folder_path, filename)
    output_file = os.path.join(folder_path, "output_" + filename)
    with open(input_file, "r", encoding="latin1") as f, open(output_file, "w") as out:
        for line in f:
            line = line.replace('\\n', '\n')
            emails = re.findall(email_regex, line)
            for email in emails:
                out.write(email + "\n")
