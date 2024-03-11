# escape sequences

weather = 'it's rainy today' 
#single quote can't be repeated or come within enclosing single quotation, so
weather = "it's rainy today"  #single quote is enclosed in double quotes here.

weather_today = "It's "too sunny" today" # before adding backslash it show's an error while adding back slash tells the compiler that it's a special character while in our case it's the string
weather_today = "It's \"too sunny\" today"
print(weather_today)

weather_today = "\tIt's \"too sunny\" today" # \t here refers to tab which adds space
weather_today = "\tIt's \"too sunny\" today \n hope you'll have a good day" # here \n is used to start from new line.
