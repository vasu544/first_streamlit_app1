import streamlit
import pandas

streamlit.title('My parents new healthy diner')

streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞Avocado Toast')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Display the table on the page.
streamlit.dataframe(my_fruit_list)

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)


#New section to display Fruitvice api response
streamlit.header("Fruityvice Fruit Advice!")
import requests

#Add a Text Entry Box and Send the Input to Fruityvice as Part of the API Call
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+"kiwi")

# normalize the above data
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# print this data
streamlit.dataframe(fruityvice_normalized)


