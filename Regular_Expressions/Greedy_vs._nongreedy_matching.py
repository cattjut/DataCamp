# Import re
import re

# Write a regex to eliminate tags
string_notags = re.sub(r"<.+?>", "", string)

# Print out the result
print(string_notags)


# Write a non-greedy regex expression
numbers_found_greedy = re.findall(r"\d+?", sentiment_analysis)

# Print out the result
print(numbers_found_greedy)


# Write a greedy regex expression
numbers_found_greedy = re.findall(r"\d+", sentiment_analysis)

# Print out the result
print(numbers_found_greedy)

# Write a greedy regex expression to match
sentences_found_greedy = re.findall(r"\(.+\)", sentiment_analysis)

# Print out the result
print(sentences_found_greedy)

# Write a lazy regex expression
sentences_found_lazy = re.findall(r"\(.*?\)", sentiment_analysis)

# Print out the results
print(sentences_found_lazy)
