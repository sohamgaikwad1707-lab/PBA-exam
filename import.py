import re

text = "The exam dates are 15-03-2026,25-04-2026,and 05-06-2026.The invalid date format is 2026/07/10."
pattern = r'\b\d {2} - \d{2} - \d{4} \b'

dates = re . findall (pattern , text)

print ("Dates Found:")
for date in dates:
    print (date)