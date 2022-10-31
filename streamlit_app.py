import streamlit

streamlit.title('My Parents New Healthy Diner')
streamlit.header('Brekfast Favourites')
streamlit.text('🥣 🥗 🐔 🥑🍞 Omega 3 & Blueberry Oatmeal')
streamlit.text('kale, Spinach & Rocket Smoothie')
streamlit.text('hard Boiled Fee-Range Egg')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

#Setting Index
my_fruit_list = my_fruit_list.set_index('Fruit')
#Let's put a picker here - 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

#new Section to Display FruityVice Advice

streamlit.header("Fruityvice Fruit Advice!")

import requests

fruit_choice = streamlit.text_input('What fruit would you like informatin about?', 'kiwi')
streamlit.write('The user entered', fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ fruit_choice)
streamlit.text(fruityvice_response.json())


#take the json version of the response and normalize it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#output it the screen as a table
streamlit.dataframe(fruityvice_normalized)

