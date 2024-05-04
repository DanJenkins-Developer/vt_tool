import os
from dotenv import load_dotenv
import vt

from testing import file_test

load_dotenv()

file_test.get_hash_list()

# vt_api_key = os.getenv('VT_API_KEY')

# client = vt.Client(vt_api_key)

# # file attributes at https://docs.virustotal.com/reference/files
# file = client.get_object("/files/44d88612fea8a8f36de82e1278abb02f")

# print(file.size)

# client.close()
