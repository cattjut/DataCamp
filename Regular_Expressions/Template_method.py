# Import Template
from string import Template

# Create a template
wikipedia = Template("$tool is a $description")

# Substitute variables in template
print(wikipedia.substitute(tool=tool1, description=description1))
print(wikipedia.substitute(tool=tool2, description=description2))
print(wikipedia.substitute(tool=tool3, description=description3))


# Import template
from string import Template

# Select variables
our_tool = tools[0]
our_fee = tools[1]
our_pay = tools[2]

# Create template
course = Template("We are offering a 3-month beginner course on $tool just for $$$fee ${pay}ly")

# Substitute identifiers with three variables
print(course.substitute(tool=our_tool, fee=our_fee, pay=our_pay))


# Import template
from string import Template

# Complete template string using identifiers
the_answers =Template("Check your answer 1: $answer1, and your answer 2: $answer2")

# Use substitute to replace identifiers
try:
    print(the_answers.substitute(answers))
except KeyError:
    print("Missing information")


# Import template
from string import Template

# Complete template string using identifiers
the_answers = Template("Check your answer 1: $answer1, and your answer 2: $answer2")

# Use safe_substitute to replace identifiers
try:
    print(the_answers.safe_substitute(answers))
except KeyError:
    print("Missing information")
