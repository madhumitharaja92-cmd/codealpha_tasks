import re

input_file = "input_emails.txt"
output_file = "extracted_emails.txt"

try:
    with open(input_file, "r", encoding="utf-8") as file:
        text = file.read()

    emails = list(dict.fromkeys(
        re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}", text)
    ))

    with open(output_file, "w", encoding="utf-8") as file:
        for email in emails:
            file.write(email + "\\n")

    print("Email addresses extracted successfully!")
    print("Total emails found:", len(emails))
    print("Saved in:", output_file)

except FileNotFoundError:
    print("ERROR: input_emails.txt must be in the same folder as this Python file.")
