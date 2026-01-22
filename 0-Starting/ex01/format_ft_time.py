import time
from datetime import datetime

seconds = time.time()
seconds_format = f"{seconds:,.4f}"
scientific_notation = f"{seconds:.2e}"

print(
    f"Seconds since January 1, 1970: {seconds_format} or "
    f"{scientific_notation} in scientific notation"
)

now = datetime.now()
date_time = now.strftime("%b %d %Y")

print(date_time)
