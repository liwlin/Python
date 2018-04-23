
from datetime import datetime
import pytz

utc = pytz.utc # utc is Coordinated Universal Time
ist = pytz.timezone('Asia/Kolkata') #IST is Indian Standard Time

now = datetime.now(tz=utc) # this is the current time in UTC
ist_now = now.astimezone(ist) # this is the current time in IST.
print(pytz.utc)
print(ist)
print(now)
print(ist_now)