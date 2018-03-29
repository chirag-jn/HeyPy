user = "b2aca159-86a0-4afa-9b22-4b720ee1957f"
passwd = "vTSl6VKjZMPA"

from watson import watson_run
from test2 import parse

got_data = watson_run(user, passwd)
# print(got_data)
parse(got_data)
