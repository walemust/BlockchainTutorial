import hashlib
import streamlit as st

print("This is a hashlib implementation")
print("--------------------------------")
data = "Hello world"

sha256_hash = hashlib.md5()

sha256_hash.update(data.encode())

hashed_data = sha256_hash.hexdigest()

print("Original data", data)
print("Derived hash", hashed_data)

#texts = input("Do you want to verify the integrity of your data? ")
#output = hashlib.md5(text.encode()).hexdigest()

st.title("SHA256")

st.text("Convert my string to hash")
text = st.text_area(" ")
output = hashlib.sha256(text.encode()).hexdigest()
st.button("Convert", on_click=output)
st.balloons()

print(output)