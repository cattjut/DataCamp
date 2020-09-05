# Write regex and scan contract to capture the dates described
regex_dates = r"Signed\son\s(\d{2})/(\d{2})/(\d{4})"
dates = re.search(regex_dates, contract)

# Assign to each key the corresponding match
signature = {
	"day": dates.group(2),
	"month": dates.group(1),
	"year": dates.group(3)
}
# Complete the format method to print-out
print("Our first contract is dated back to {data[year]}. Particularly, the day {data[day]} of the month {data[month]}.".format(data=signature))


for string in html_tags:
    # Complete the regex and find if it matches a closed HTML tags
    match_tag =  re.match(r"<(\w+)>.*?</\1>", string)

    if match_tag:
        # If it matches print the first group capture
        print("Your tag {} is closed".format(match_tag.group(1)))
    else:
        # If it doesn't match capture only the tag
        notmatch_tag = re.match(r"<(\w+)>", string)
        # Print the first group capture
        print("Close your {} tag!".format(notmatch_tag.group(1)))


    # Complete the regex to match an elongated word
regex_elongated = r"\w*(\w)\1\w*"

for tweet in sentiment_analysis:
	# Find if there is a match in each tweet
	match_elongated = re.search(regex_elongated, tweet)

	if match_elongated:
		# Assign the captured group zero
		elongated_word = match_elongated.group(0)

		# Complete the format method to print the word
		print("Elongated word found: {word}".format(word=elongated_word))
	else:
		print("No elongated word found")     	
