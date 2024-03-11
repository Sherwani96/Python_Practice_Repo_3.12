import re
# password validation

# at least 8 characters long
# contain any sort letters, numbers $%#@
# has to end with number

# regex for email
regex_email = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
# regex for password
regex_pwd = re.compile(r"[A-Za-z0-9$%#@]{8,}[0-9]")

email = 'abc@gmail.com'
password = 'password@$#10'

validate_email = regex_email.search(email)
validate_pwd = regex_pwd.fullmatch(password)

print(validate_email)
print(validate_pwd)
