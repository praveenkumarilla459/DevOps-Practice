print("I am Learning git")
import hashlib

# Step 1: Create a string
input_string = "Hello, World!"

# Step 2: Create an MD5 hash object
md5_hash = hashlib.md5()

# Step 3: Update the hash object with the bytes representation of the string
md5_hash.update(input_string.encode('utf-8'))

# Step 4: Get the hexadecimal representation of the hash
md5_value = md5_hash.hexdigest()

# Step 5: Print the MD5 hash value
print("MD5 Hash for the string:", md5_value)
