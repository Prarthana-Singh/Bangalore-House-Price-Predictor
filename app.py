# import streamlit as st
# import pickle
# import pandas as pd
#
# # Load Model
# model = pickle.load(open('Bangalore_House.pkl', 'rb'))
#
# # Streamlit Page Config
# st.set_page_config(page_title="Bangalore House Price Predictor", layout="centered")
#
# # Apply Custom Styling
# st.markdown("""
#     <style>
#     .stTextInput, .stNumberInput, .stSelectbox {
#         font-size: 18px;
#     }
#     .stButton>button {
#         background-color: #4CAF50;
#         color: white;
#         font-size: 20px;
#         padding: 10px;
#         width: 100%;
#         border-radius: 10px;
#     }
#     .stButton>button:hover {
#         background-color: #45a049;
#     }
#     </style>
# """, unsafe_allow_html=True)
#
# # Title
# st.markdown("<h1 style='text-align: center; color: #4A90E2;'>🏡 Bangalore House Price Predictor</h1>",
#             unsafe_allow_html=True)
#
# # Sidebar
# st.sidebar.header("📌 Instructions")
#
# # Inputs
# location = st.text_input("📍 Enter Location", placeholder="Example: Whitefield")
# total_sqft = st.number_input("📏 Enter Total Sqft", min_value=300, max_value=10000, step=50)
# bath = st.slider("🛁 Select Number of Bathrooms", min_value=1, max_value=16, value=2)
# bhk = st.slider("🛏️ Select BHK", min_value=1, max_value=16, value=3)
#
# # Predict Button
# if st.button("💰 Predict Price"):
#     input_data = pd.DataFrame([[location, total_sqft, bath, bhk]], columns=['location', 'total_sqft', 'bath', 'bhk'])
#
#     # Make Prediction
#     pred = model.predict(input_data)[0]
#
#     # Display Result
#     st.success(f"🏠 Estimated House Price(Value of the property in lakhs): **₹ {pred:,.2f}**")
#
# # Footer
# st.markdown("<br><p style='text-align: center; color: gray;'>Developed by Prarthana 🚀</p>", unsafe_allow_html=True)


















#
#
# import streamlit as st
# import pickle
# import pandas as pd
#
# # Load Model
# model = pickle.load(open('Bangalore_House.pkl', 'rb'))
#
# # Streamlit Page Config
# st.set_page_config(page_title="Bangalore House Price Predictor", layout="centered")
#
# # Apply Custom Styling
# st.markdown("""
#     <style>
#     .stTextInput, .stNumberInput, .stSelectbox {
#         font-size: 18px;
#     }
#     .stButton>button {
#         background-color: #4CAF50;
#         color: white;
#         font-size: 20px;
#         padding: 10px;
#         width: 100%;
#         border-radius: 10px;
#     }
#     .stButton>button:hover {
#         background-color: #45a049;
#     }
#     </style>
# """, unsafe_allow_html=True)
#
# # Title
# st.markdown("<h1 style='text-align: center; color: #4A90E2;'>🏡 Bangalore House Price Predictor</h1>",
#             unsafe_allow_html=True)
#
# # Sidebar
# st.sidebar.image("https://www.grollohomes.com.au/wp-content/uploads/2020/05/Grollo-Belmore-140.jpg", width=200)  # Add an image/icon
# st.sidebar.header("➡️Instructions")
# st.sidebar.subheader("📌 How to Use")
# st.sidebar.write("""
# 1️⃣ Enter the **location** (e.g., Whitefield, Indiranagar)
# 2️⃣ Choose the **total square feet**
# 3️⃣ Select the **number of bathrooms**
# 4️⃣ Select the **BHK (bedrooms, hall, kitchen)**
# 5️⃣ Click **'Predict Price'** to see the estimated value!
# """)
#
# st.sidebar.header("📊 Bangalore Real Estate Insights")
# st.sidebar.write("""
# - 📈 **Whitefield & Koramangala** are among the costliest areas.
# - 🏠 **More BHK & Sqft** → Higher Price
# - 🔥 **Demand is rising** in Electronic City & Sarjapur
# """)
#
# st.sidebar.markdown("<hr>", unsafe_allow_html=True)
# st.sidebar.write("🚀 Developed by **Prarthana**")
#
# # Inputs
# location = st.text_input("📍 Enter Location", placeholder="Example: Whitefield")
# total_sqft = st.number_input("📏 Enter Total Sqft", min_value=300, max_value=10000, step=50)
# bath = st.slider("🛁 Select Number of Bathrooms", min_value=1, max_value=16, value=2)
# bhk = st.slider("🛏️ Select BHK", min_value=1, max_value=16, value=3)
#
# # Predict Button
# if st.button("💰 Predict Price"):
#     input_data = pd.DataFrame([[location, total_sqft, bath, bhk]], columns=['location', 'total_sqft', 'bath', 'bhk'])
#
#     # Make Prediction
#     pred = model.predict(input_data)[0]
#
#     # Display Result
#     st.success(f"🏠 Estimated House Price (in Lakhs): **₹ {pred:,.2f}**")
#
# # Footer
# st.markdown("<br><p style='text-align: center; color: gray;'>Developed by Prarthana 🚀</p>", unsafe_allow_html=True)












import streamlit as st
import pickle
import pandas as pd
import folium
from streamlit_folium import folium_static
import sklearn

#-----------------------------------------------------------------------------------
html_temp = """
        <h2 style="color: white; font-family: Arial, sans-serif; font-weight: bold; text-shadow: 0px 0px 10px rgba(255,255,255,0.8); animation: pulseShadow 2s infinite;">
    Bank Churn Prediction
</h2>

<style>
    @keyframes pulseShadow {
        0%, 100% { text-shadow: 0px 0px 10px rgba(255, 255, 255, 0.8); }
        50% { text-shadow: 0px 0px 20px rgba(255, 255, 255, 1); }
    }
</style>

    """


#----------------------------------------------------------------------------

# Load Model
model = pickle.load(open('Bangalore_House.pkl', 'rb'))

# Streamlit Page Config
st.set_page_config(page_title="Bangalore House Price Predictor", layout="centered")


#--------------------------------------------------------------------
# Apply Custom Styling
# st.markdown("""
#     <style>
#     .stApp {
#         background: linear-gradient(135deg, #f5f7fa, #c3cfe2);
#     }
#     .stTextInput, .stNumberInput, .stSelectbox {
#         font-size: 18px;
#     }
#     .stButton>button {
#         background-color: #4CAF50;
#         color: white;
#         font-size: 20px;
#         padding: 10px;
#         width: 100%;
#         border-radius: 10px;
#     }
#     .stButton>button:hover {
#         background-color: #45a049;
#     }
#     </style>
# """, unsafe_allow_html=True)

# Title
# st.markdown("<h1 style='text-align: center; color: #4A90E2;'>🏡 Bangalore House Price Predictor</h1>", unsafe_allow_html=True)


#-------------------------------------------------------------
# Apply Custom Styling
# st.markdown("""
#     <style>
#     .stApp {
#         background: linear-gradient(135deg, #f5f7fa, #c3cfe2);
#     }
#     .stTextInput, .stNumberInput, .stSelectbox {
#         font-size: 18px;
#     }
#     .stButton>button {
#         background-color: #4CAF50;
#         color: white;
#         font-size: 20px;
#         padding: 10px;
#         width: 100%;
#         border-radius: 10px;
#     }
#     .stButton>button:hover {
#         background-color: #45a049;
#     }
#     @keyframes pulseShadow {
#         0%, 100% { text-shadow: 0px 0px 10px rgba(255, 255, 255, 0.8); }
#         50% { text-shadow: 0px 0px 20px rgba(255, 255, 255, 1); }
#     }
#     .animated-title {
#         color: white;
#         font-family: Arial, sans-serif;
#         font-weight: bold;
#         text-align: center;
#         text-shadow: 0px 0px 10px rgba(255,255,255,0.8);
#         animation: pulseShadow 2s infinite;
#     }
#     </style>
# """, unsafe_allow_html=True)


st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #f5f7fa, #c3cfe2);
    }
    .stTextInput, .stNumberInput, .stSelectbox {
        font-size: 18px;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 20px;
        padding: 10px;
        width: 100%;
        border-radius: 10px;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }

    /* Animated Text */
    @keyframes pulseShadow {
        0%, 100% { text-shadow: 0px 0px 10px rgba(30, 144, 255, 0.8); }
        50% { text-shadow: 0px 0px 20px rgba(30, 144, 255, 1); }
    }

    .animated-title {
        color: #4A90E2;
        font-family: Arial, sans-serif;
        font-weight: bold;
        text-shadow: 0px 0px 10px rgba(30, 144, 255, 0.8);
        animation: pulseShadow 2s infinite;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Animated Title
st.markdown("<h2 class='animated-title'>🏡 Bangalore House Price Predictor</h2>", unsafe_allow_html=True)




# st.markdown(html_temp,unsafe_allow_html=True)


# Header Image
st.image("img2.png", width=150)

# Sidebar
st.sidebar.image("https://www.grollohomes.com.au/wp-content/uploads/2020/05/Grollo-Belmore-140.jpg", width=200)
st.sidebar.header("➡️Instructions")
st.sidebar.subheader("📌 How to Use")
st.sidebar.write("""
1️⃣ Enter the **location** (e.g., Whitefield, Indiranagar)  
2️⃣ Choose the **total square feet**  
3️⃣ Select the **number of bathrooms**  
4️⃣ Select the **BHK (bedrooms, hall, kitchen)**  
5️⃣ Click **'Predict Price'** to see the estimated value!  
""")

st.sidebar.header("📊 Bangalore Real Estate Insights")
st.sidebar.write("""
- 📈 **Whitefield & Koramangala** are among the costliest areas.  
- 🏠 **More BHK & Sqft** → Higher Price  
- 🔥 **Demand is rising** in Electronic City & Sarjapur  
""")

st.sidebar.markdown("<hr>", unsafe_allow_html=True)
st.sidebar.write("🚀 Developed by **Prarthana**")

# Inputs

st.markdown("""
    <style>
    .stTextInput label {
        color: red; /* Change this to any color you like */
        font-size: 20px; /* Optional: Change font size */
        font-weight: bold; /* Optional: Make the text bold */
    }
    </style>
""", unsafe_allow_html=True)

location = st.text_input("📍 Enter Location", placeholder="Example: Whitefield", help="Enter the locality in Bangalore")
# total_sqft = st.number_input("📏 Enter Total Sqft", min_value=300, max_value=10000, step=50, help="Total area in square feet")
# bath = st.slider("🛁 Select Number of Bathrooms", min_value=1, max_value=16, value=2, help="Number of bathrooms")
# bhk = st.slider("🛏️ Select BHK", min_value=1, max_value=16, value=3, help="Number of bedrooms, hall, and kitchen")
st.markdown("""
    <style>
    /* Style for all input labels */
    .stNumberInput label, .stSlider label {
        color: #4A90E2; /* Blue color */
        font-size: 18px; /* Adjust font size */
        font-weight: bold; /* Optional: Make the text bold */
    }
    </style>
""", unsafe_allow_html=True)

# Input Fields
total_sqft = st.number_input("📏 Enter Total Sqft", min_value=300, max_value=10000, step=50, help="Total area in square feet")
bath = st.slider("🛁 Select Number of Bathrooms", min_value=1, max_value=16, value=2, help="Number of bathrooms")
bhk = st.slider("🛏️ Select BHK", min_value=1, max_value=16, value=3, help="Number of bedrooms, hall, and kitchen")

#---------------------------------------------------------
# # Predict Button
# if st.button("💰 Predict Price"):
#     with st.spinner("Predicting..."):
#         input_data = pd.DataFrame([[location, total_sqft, bath, bhk]], columns=['location', 'total_sqft', 'bath', 'bhk'])
#         pred = model.predict(input_data)[0]
#         # st.success(f"🏠 Estimated House Price (in Lakhs): **₹ {pred:,.2f}**")
#         st.success(f"🏠 **Estimated House Price (in Lakhs): ₹ {pred:,.2f}**")

#-------------------------------------------------------

if st.button("💰 Predict Price"):
    with st.spinner("Predicting..."):
        input_data = pd.DataFrame([[location, total_sqft, bath, bhk]], columns=['location', 'total_sqft', 'bath', 'bhk'])
        pred = model.predict(input_data)[0]
        st.markdown(f"""
            <div style="
                border: 2px solid #4CAF50;
                border-radius: 10px;
                padding: 15px;
                background-color: #E8F5E9;
                color: #1B5E20;
                font-size: 20px;
                text-align: center;
                box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.2);
            ">
                🏠 <strong>Estimated House Price (in Lakhs): ₹ {pred:,.2f}</strong> 🎉
            </div>
        """, unsafe_allow_html=True)
# Footer
st.markdown("""
    <hr>
    <p style='text-align: center; color: gray;'>
        Developed by Prarthana 🚀 | 
        <a href="https://github.com/Prarthana-Singh" target="_blank">GitHub</a> | 
        <a href="https://www.linkedin.com/in/prarthanasingh/" target="_blank">LinkedIn</a>
    </p>
""", unsafe_allow_html=True)