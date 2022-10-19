import streamlit

streamlit.title('My Parents New Healthy Diner')
streamlit.header('Brekfast Favourites')
streamlit.text('🥣 🥗 🐔 🥑🍞 Omega 3 & Blueberry Oatmeal')
streamlit.text('kale, Spinach & Rocket Smoothie')
streamlit.text('hard Boiled Fee-Range Egg')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


import pandas

my_fruit_list = my_fruit_list.set_index('Fruit')
#Let's put a picker here - 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
