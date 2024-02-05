import openai
import streamlit as st

st.header('공룡이다',
          divider=True)
st.image('/Users/gimsumin/Desktop/스크린샷 2024-01-31 오후 4.53.59.png', caption='hello')
query = st.text_input('Query : ')
if query:
    st.write('Your query is ', query)
    
button_result = st.button('PUSH ME')

if button_result:
    st.write('Thanks')