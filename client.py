import numpy as np
from Pyfhel import Pyfhel, PyCtxt
try:
  import requests
except ImportError:
  print("This demo requires the `requests` python module (install with pip). Exiting.")
  exit(0)

# Generate Pyfhel session
print(f"[Client] Initializing Pyfhel session and data...")
HE_client = Pyfhel(context_params={'scheme':'ckks', 'n':2**13, 'scale':2**30, 'qi':[30]*5})
HE_client.keyGen() # Generates both a public and a private key
HE_client.relinKeyGen()
HE_client.rotateKeyGen()

# Generate and encrypt data
x = np.array([1.5, 2, 3.3, 4])
cx = HE_client.encrypt(x)

# Serializing data and public context information
s_context = HE_client.to_bytes_context()
s_public_key = HE_client.to_bytes_public_key()
s_relin_key = HE_client.to_bytes_relin_key()
s_rorate_key = HE_client.to_bytes_rotate_key()
s_cx = cx.to_bytes()

print(f"[Client] sending HE_client={HE_client} and cx={cx}")
