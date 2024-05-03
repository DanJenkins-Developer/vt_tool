import os
from dotenv import load_dotenv
import vt

load_dotenv()

vt_api_key = os.getenv('VT_API_KEY')

# client = vt.Client(
#     "f23aec89e63cdb6cb68762de1b5e10d78cdc8eace8abe4b27089c117be1d36b0")

client = vt.Client(vt_api_key)

# file attributes at https://docs.virustotal.com/reference/files
file = client.get_object("/files/44d88612fea8a8f36de82e1278abb02f")

print(file.size)

client.close()
