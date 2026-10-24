import random
import string
import time
from datetime import datetime, timezone

section_one = ''.join(random.choices(string.ascii_lowercase + string.digits, k=4))
section_two = ''.join(random.choices(string.ascii_lowercase + string.digits, k=4))
section_three = ''.join(random.choices(string.ascii_lowercase + string.digits, k=4))

random_string = f'{section_one}-{section_two}-{section_three}'
while True:
    timestamp = datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z")

    print(f'{timestamp}: {random_string}')
    time.sleep(5)