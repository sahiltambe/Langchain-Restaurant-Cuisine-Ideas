import streamlit as st
import langchain_helper

# Add a link to your GitHub repository at the top of the webpage
st.markdown("[GitHub Repository](https://github.com/sahiltambe/Langchain-Restaurant-Cuisine-Ideas)", unsafe_allow_html=True)

# Set the title of the Streamlit app
st.title("Intelligent AI-Powered Restaurant Name Creation")

# Create a sidebar select box for choosing a cuisine
cuisine = st.sidebar.selectbox("Pick a Cuisine", ["Indian", "Italian", "French", "Chinese", "Japanese", "Thai", "Mexican", "Arabic", "American", "Afghan", "German", "Greek"])

# Check if a cuisine is selected
if cuisine:
    # Generate restaurant name and menu items based on the selected cuisine
    response = langchain_helper.generate_restaurant_name_and_items(cuisine)

    # Display the restaurant name
    st.header(response['restaurant_name'].strip())

    # Get and display the menu items
    menu_items = response['menu_items'].strip().split(",")
    
    # Write a header for the menu items section
    st.write("**Menu Items**")
    
    # Loop through the list of menu items and display each one
    for item in menu_items:
        st.write(f"- {item}")