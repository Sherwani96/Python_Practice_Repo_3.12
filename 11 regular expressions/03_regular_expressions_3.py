import re
# regex
# use case of regex
# when you're collecting emails, may be you're creating a startup, this startup wants to collect the emails of interested customers
# now we want to ensure that whoever interested in our startup enters proper email address, because we don't want our database to be filled with improper random words
#  regex is a great thing and is used for validation

# regex helps us match different things

regex = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")  # here dollar means it's the end of the line

val = 'abc@gmail.com'

mail = regex.search(val)
print(mail)