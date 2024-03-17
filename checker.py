import requests
import time
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
import base64
from helpers import account_volume


public_key = input("Enter your public key: ")
private_key = Ed25519PrivateKey.from_private_bytes(
            base64.b64decode(input("Enter your secret key: ")))
instruction = "fillHistoryQueryAll"
timestamp = int(time.time() * 1e3)

params = {"limit": 999}
sign_str = f"instruction={instruction}&limit=999&timestamp={timestamp}&window=5000"
signature_bytes = private_key.sign(sign_str.encode())
encoded_signature = base64.b64encode(signature_bytes).decode()

headers = {
            "X-API-Key": public_key,
            "X-Signature": encoded_signature,
            "X-Timestamp": str(timestamp),
            "X-Window": str(5000),
            "Content-Type": "application/json; charset=utf-8",
}

r = requests.get("https://api.backpack.exchange/wapi/v1/history/fills", headers=headers, params=params)
volume, fee_volume = account_volume(r.json())
print(f"Volume of your account: {volume}\nUSDC spent for fees: {fee_volume}")
