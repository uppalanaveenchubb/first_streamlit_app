import streamlit
import requests
streamlit.title('My Parents New Healthy dite')
streamlit.header('Breakfast Favorites')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 Blueberry Oatmeal')
streamlit.text('🥗 Kale,Spinach and Rocket Smooethie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞Avocadao Toast')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)
