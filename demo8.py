


# 1 --- first and foremost, we import the necessary libraries
import pandas as pd
import streamlit as st

import plotly.express as px
from PIL import Image
#######################################




####################################


# 2 --- you can add some css to your Streamlit app to customize it
# TODO: Change values below and observer the changes in your app





#######################################

# 3 --- build the structure of your app


# Streamlit apps can be split into sections


# container -> horizontal sections
# columns -> vertical sections (can be created inside containers or directly in the app)
# sidebar -> a vertical bar on the side of your app


# here is how to create containers
#header_container = st.container()
#stats_container = st.container()	
#######################################



# You can place things (titles, images, text, plots, dataframes, columns etc.) inside a container


	# for example a logo or a image that looks like a website header
	#st.image('sandiplogo.png')

	# different levels of text you can include in your app
	#st.title("Digital Twin Application")
	#st.header("Developed By Scientific Design Company Inc")
	#st.subheader("This is a great app")
	#st.write("check it for yourself, if you don't believe me")

# 4 --- You import datasets like you always do with pandas
	# 		if you'd like to import data from a database, you need to set up a database connection
	### --- LOAD DATAFRAME
excel_file = 'sandipdata.xlsx'
sheet_name = 'Sheet1'

df = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='A:F',
                   header=3)

col1, col2,col3 = st.columns(3)


selectbox = st.sidebar.selectbox(
    "Please select from dropdown menu",
    ["Bar", "Line","Matrix"]
)
st.write(f"You selected {selectbox}")


# radio button
# first argument is the title of the radio button
# second argument is the options for the ratio button
#status = st.radio("Select trend: ", ('Bar', 'Line', 'Matrix'))
 
# conditional statement to print
# Male if male is selected else print female
# show the result using the success function




if (selectbox == 'Bar'):
   # --- PLOT BAR CHART
	 bar_chart = px.bar(df,
                  	    x='x',
                            y='y',
                            text='x',
                            color_discrete_sequence = ['#F63366']*len(df),
                            template= 'plotly_white')
#st.plotly_chart(bar_chart)
	 col1.plotly_chart(bar_chart)


#write this code in command prompt
#C:\Users\sk_la>cd C:\Users\sk_la\Desktop\my streamlit project\StreamlitTemplate\streamlit template

#C:\Users\sk_la\Desktop\my streamlit project\StreamlitTemplate\streamlit template>streamlit run sandipdemo.py
elif (selectbox == 'Line'):
	#plotly line chart
     fig = px.line(df, x="x", y="y")
#fig.show()
	#st.plotly_chart(fig)
     col1.plotly_chart(fig)

else:
#if (selectbox == 'Matrix'):
    fig1 = px.scatter_matrix(df, dimensions=["x", "y", "z", "a"])
    col1.plotly_chart(fig1)

