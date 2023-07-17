import streamlit

import pandas
import pandas
import requests
import snowflake.connector
streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)

streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
#import requests
#import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" +fruit_choice)


# JSON response
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output of json response
streamlit.dataframe(fruityvice_normalized)


#import snowflake.connector
#import snowflake.connector

streamlit.header("The fruit load list contains:")
#snowflake-related functions
def get_fruit_load_list();
with my_cnx.cursor() as my_cur
my_cur.execute("SELECT * from fruit_load_list")
retun my_cur.fetchall()

#add a button to load the fruit
if streamlit.button('Get Fruit Load List');
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_data_rows = get_fruit_load_list()
streamlit.dataframe(my_data_row)
#dont run anything past here while we troubleshoot
streamlit.stop()

add_my_fruit= streamlit.text_input('What fruit would you like to add?','jackfruit')
streamlit.write('Thanks for adding ', add_my_fruit)
#This will not work correctly ,but just go with it for now 
my_cur.execute("insert into fruit_load_list values('from streamlit')")
