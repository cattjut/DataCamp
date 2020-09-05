# Positive lookahead
look_ahead = re.findall(r"\w+(?=\spython)", sentiment_analysis)

# Print out
print(look_ahead)

# Positive lookbehind
look_behind = re.findall(r"(?<=[Pp]ython\s)\w+", sentiment_analysis)

# Print out
print(look_behind)

for phone in cellphones:
	# Get all phone numbers not followed by optional extension
	number = re.findall(r"\d{3}-\d{4}-\d{6}(?!-\d{2})", phone)
	print(number)

for phone in cellphones:
	# Get all phone numbers not preceded by area code
	number = re.findall(r"(?<!\d{3}-)\d{4}-\d{6}-\d{2}", phone)
	print(number)
