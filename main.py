import os
from dotenv import load_dotenv
import vt

from testing import file_test

load_dotenv()

hashes = file_test.get_hash_list()
query_string = "/files/" + hashes[1]

print(query_string)

vt_api_key = os.getenv('VT_API_KEY')

client = vt.Client(vt_api_key)

# file attributes at https://docs.virustotal.com/reference/files
file = client.get_object(query_string)

print(file.names)

client.close()
