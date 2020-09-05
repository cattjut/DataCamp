# Write a regex to match text file name
regex = r"^[aeiouAEIOU]{2,3}.+txt"

for text in sentiment_analysis:
	# Find all matches of the regex
	print(re.findall(regex, text))

	# Replace all matches with empty string
	print(re.sub(regex, "", text))


# Write a regex to match a valid email address
regex =r"[a-zA-Z0-9!#%&*$.]+@\w+\.com"

for example in emails:
  	# Match the regex to the string
    if re.match(regex, example):
        # Complete the format method to print out the result
      	print("The email {email_example} is a valid email".format(email_example=example))
    else:
      	print("The email {email_example} is invalid".format(email_example=example))


# Write a regex to match a valid password
regex = r"[a-zA-Z0-9*#$%!&.]{8,20}"

for example in passwords:
  	# Scan the strings to find a match
    if re.match(regex, example):
        # Complete the format method to print out the result
      	print("The password {pass_example} is a valid password".format(pass_example=example))
    else:
      	print("The password {pass_example} is invalid".format(pass_example=example))  
