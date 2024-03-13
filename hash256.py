import hashlib

def hash_cal(input_string):

#Create the Hash object to the data
    sha256_hash = hashlib.sha256()

    #I need to update the Hash with the data

    sha256_hash.update(input_string.encode())

    #Get the hexavlaue
    hash_data = sha256_hash.hexdigest()

    print("SHA256 - Hash Value : ", hash_data)

hash_cal("Test1")

