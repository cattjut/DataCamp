# Import the re module
import re

# Write the regex
regex = r"@robot\d\W"

# Find all matches of regex
print(re.findall(regex, sentiment_analysis))

# Write a regex to obtain user mentions
print(re.findall(r"User_mentions:\d", sentiment_analysis))

# Write a regex to obtain number of likes
print(re.findall(r"likes:\s\d", sentiment_analysis))

# Write a regex to obtain number of retweets
print(re.findall(r"number\sof\sretweets:\s\d", sentiment_analysis))

# Write a regex to match pattern separating sentences
regex_sentence = r"\W\dbreak\W"

# Replace the regex_sentence with a space
sentiment_sub = re.sub(regex_sentence, " ", sentiment_analysis)

# Write a regex to match pattern separating words
regex_words = r"\Wnew\w"

# Replace the regex_words and print the result
sentiment_final = re.sub(regex_words, " ", sentiment_sub)
print(sentiment_final)
