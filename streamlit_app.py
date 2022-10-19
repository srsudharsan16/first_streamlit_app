import streamlit

streamlit.title('My Parents New Healthy Diner')
streamlit.header('Brekfast Favourites')
streamlit.text('🥣 🥗 🐔 🥑🍞 Omega 3 & Blueberry Oatmeal')
streamlit.text('kale, Spinach & Rocket Smoothie')
streamlit.text('hard Boiled Fee-Range Egg')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


import pandas
my_fruit_list = pandas.csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
