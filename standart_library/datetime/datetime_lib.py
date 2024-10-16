import datetime
# NAME
#     datetime - Fast implementation of the datetime type.

from datetime import date
now = date.today()
print(now)

# support dates calendar aritmetik

ultah = date(2006,9,13)
umur = now - ultah
print(umur.days)
