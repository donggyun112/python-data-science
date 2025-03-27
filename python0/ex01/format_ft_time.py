import time
import datetime


print(f"Seconds since January 1, 1970: {time.time()} or {time.time():.2e}\
in scientific notation")


D = datetime.date.today()
c_data = D.strftime("%b %d %Y")
print(c_data)
