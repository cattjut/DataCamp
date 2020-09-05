# Write a regex that matches sentences with the optional words
regex_positive = r"(love|like|enjoy).+?(movie|concert)\s(.+?)\."

for tweet in sentiment_analysis:
	# Find all matches of regex in tweet
    positive_matches = re.findall(regex_positive, tweet)

    # Complete format to print out the results
    print("Positive comments found {}".format(positive_matches))



# Write a regex that matches sentences with the optional words
regex_negative = r"(hate|dislike|disapprove).+?(?:movie|concert)\s(.+?)\."

for tweet in sentiment_analysis:
	# Find all matches of regex in tweet
    negative_matches = re.findall(regex_negative, tweet)

    # Complete format to print out the results
    print("Negative comments found {}".format(negative_matches))
