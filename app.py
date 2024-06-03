import streamlit as st

# Add a link to your GitHub repository at the top of the webpage
st.markdown("[GitHub Repository](https://github.com/sahiltambe/Langchain-Restaurant-Cuisine-Ideas)", unsafe_allow_html=True)
# Set the title of the Streamlit app
st.title("Intelligent AI-Powered Restaurant Name Creation")

# Create a sidebar select box for choosing a cuisine
cuisine = st.sidebar.selectbox("Pick a Cuisine", ["Indian", "Italian", "Mexican", "Arabic", "American"])

# Preloaded values for each cuisine
preloaded_values = {
    "Indian": {
        "restaurant_name": "Spice Junction",
        "menu_items": "Butter Chicken, Naan, Biryani, Pav Bhaji"
    },
    "Italian": {
        "restaurant_name": "Pasta Paradise",
        "menu_items": "Spaghetti Carbonara, Margherita Pizza, Tiramisu"
    },
    "Mexican": {
        "restaurant_name": "Salsa Fiesta",
        "menu_items": "Tacos, Burritos, Quesadillas, Guacamole"
    },
    "Arabic": {
        "restaurant_name": "Shawarma Express",
        "menu_items": "Hummus, Falafel, Shawarma, Baklava"
    },
    "American": {
        "restaurant_name": "Burger Haven",
        "menu_items": "Cheeseburger, Fries, Milkshake, Apple Pie"
    }
}

# Check if a cuisine is selected
if cuisine:
    # Display the restaurant name
    st.header(preloaded_values[cuisine]['restaurant_name'].strip())

    # Get and display the menu items
    menu_items = preloaded_values[cuisine]['menu_items'].strip().split(",")

    # Write a header for the menu items section
    st.write("**Menu Items**")

    # Loop through the list of menu items and display each one
    for item in menu_items:
        st.write(f"- {item}")


