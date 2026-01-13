import time
from datetime import datetime


seconds = time.time()
seconds_format = f'{seconds:,}'
scientific_notation="{:.2e}".format(seconds)

print("Seconds since January 1, 1970: " + seconds_format + " or " + scientific_notation + " in scientific notation")

now = datetime.now()
date_time = now.strftime("%b %d %Y")

print(date_time)	
