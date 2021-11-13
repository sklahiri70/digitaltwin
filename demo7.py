


# 1 --- first and foremost, we import the necessary libraries
import pandas as pd
import streamlit as st

import plotly.express as px
#######################################

# 2 --- you can add some css to your Streamlit app to customize it
# TODO: Change values below and observer the changes in your app


st.markdown(
        f"""
<style>
    .reportview-container .main .block-container{{
        max-width: 90%;
        padding-top: 5rem;
        padding-right: 1rem;
        padding-left: 1rem;
        padding-bottom: 5rem;
    }}
    img{{
    	max-width:40%;
    	margin-bottom:40px;
    }}
</style>
""",
        unsafe_allow_html=True,
    )


#######################################

# 3 --- build the structure of your app


# Streamlit apps can be split into sections


# container -> horizontal sections
# columns -> vertical sections (can be created inside containers or directly in the app)
# sidebar -> a vertical bar on the side of your app


# here is how to create containers
header_container = st.container()
stats_container = st.container()	
#######################################



# You can place things (titles, images, text, plots, dataframes, columns etc.) inside a container
with header_container:

	# for example a logo or a image that looks like a website header
	#st.image('sandiplogo.png')

	# different levels of text you can include in your app
	st.title("A cool new Streamlit app")
	st.header("Welcome!")
	st.subheader("This is a great app")
	st.write("check it for yourself, if you don't believe me")

