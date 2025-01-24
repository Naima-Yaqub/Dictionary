import json 
import streamlit as st 
from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

try:
 data= json.load(open("data.json",'r'))
except:
   st.error("The file not found!")
   data={}
st.title('Dictionary :)')
entry = st.text_input('Enter the word you want to know the meaning of: ')
entry= entry.lower().strip()

keys= list(data.keys())
values= list(data.values())

value= []
if entry and data:
 for key in keys:
     
     if entry==key:
        value= values[keys.index(key)]
     elif similar(key,entry)>=0.85:
        st.write(f"Similar key found: '{key}' with similarity {similar(key,entry):.2f}")
        value= values[keys.index(key)]
 if isinstance(value,list):
    formatted_definitions= "\n".join([f"{val}" for val in value])
    st.text_area(label='Output Data', value=f'The meanings of {entry} are:\n {formatted_definitions }', height= 200)            
 elif value:
  st.text_area(label=f'Output Data the meaning of {entry} is:', value=f'{value }', height= 200)
 else:
  st.text_area(label='Output Data', value='No match found!')
else:
    if not entry:
        st.text_area(label='Output Data', value='Please enter a word!')
