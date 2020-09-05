# Complete the f-string
print(f"Data science is considered {field1 !r} in the {fact1}st century")

# Complete the f-string
print(f"About {fact2 :e} of {field2} in the world")

# Complete the f-string
print(f"{field3} create around {fact3 :.2f}% of the data but only {fact4 :.1f}% is analyzed")

# Include both variables and the result of dividing them
print(f"{number1} tweets were downloaded in {number2} minutes indicating a speed of {number1/number2 :.1f} tweets per min")

# Replace the substring https by an empty string
print(f"{string1.replace('https', '')}")

print(f"Only {len(list_links)*100/120 :.2f}% of the posts contain links")

# Access values of date and price in east dictionary
print(f"The price for a house in the east neighborhood was ${east['price']} in {east['date']:%m-%d-%Y}")

# Access values of date and price in west dictionary
print(f"The price for a house in the west neighborhood was ${west['price']} in {west['date']:%m-%d-%Y}.")
