from collections import Counter
from datetime import datetime

crimes_by_month = Counter()

for item in crime_data:
    date = datetime.strptime(item[0], '%m/%d/%Y %H:%M:%S %p')
    crimes_by_month[date.month]+=1

print(crimes_by_month.most_common(3))
