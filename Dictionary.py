import json 
import streamlit as st 
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
     if entry[0]==key[0]:
         if entry==key:
             value= values[keys.index(key)]
 if isinstance(value,list):
    formatted_definitions= "\n".join([f"{val}" for val in value])
    st.text_area(label='Output Data', value=f'The meanings of {entry} are:\n {formatted_definitions }', height= 200)            
 elif value:
  st.text_area(label='Output Data', value=f'The meaning of {entry} is:\n {value }', height= 200)
 else:
  st.text_area(label='Output Data', value='No match found!')
else:
    if not entry:
        st.text_area(label='Output Data', value='Please enter a word!')