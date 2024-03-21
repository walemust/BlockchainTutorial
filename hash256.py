import hashlib
import streamlit as st


def hash_cal(input_string):

#Create the Hash object to the data
    sha256_hash = hashlib.sha256()

    #I need to update the Hash with the data

    sha256_hash.update(input_string.encode())

    #Get the hexavlaue
    hash_data = sha256_hash.hexdigest()

    st.write("SHA256 - Hash Value : ", hash_data)

#hash_cal("Test1")

st.title("SHA256")

st.text("Convert my string data to hash code")
text = st.text_area(" ")
st.button("Convert", on_click=hash_cal(text))

st.balloons()
print("my hashlib is complete")