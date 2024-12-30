# calculate the number of days between two dates
from datetime import date
date1 = date(2024,7,2)
date2 = date(2003,11,5)
diff = date1 - date2
print(diff.days)