import os
from dotenv import load_dotenv
load_dotenv()

first_flag = os.getenv("FLAG_1")
print(first_flag)