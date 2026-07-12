import streamlit as st
import pandas as pd
import joblib

# --------------------- PAGE CONFIG ----------------------
st.set_page_config(
    page_title="🚗 AI Car Price Prediction",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------- LOAD MODEL ----------------------
model = joblib.load("model.pkl")
columns = joblib.load("columns.pkl")

# --------------------- CSS ----------------------
st.markdown("""
<style>

html, body, [class*="css"]{
    font-family: 'Segoe UI', sans-serif;
}

.main{
    background-color:#F4F7FC;
}

.block-container{
    padding-top:1rem;
}

.hero{
background: linear-gradient(90deg,#0F172A,#1E40AF);
padding:35px;
border-radius:20px;
color:white;
box-shadow:0px 8px 20px rgba(0,0,0,0.25);
}

.hero h1{
font-size:45px;
margin-bottom:5px;
}

.hero p{
font-size:18px;
color:#E2E8F0;
}

.metric-card{
background:white;
padding:20px;
border-radius:15px;
text-align:center;
box-shadow:0 4px 12px rgba(0,0,0,.08);
}

.section{
background:white;
padding:25px;
border-radius:18px;
box-shadow:0 4px 10px rgba(0,0,0,.08);
margin-top:20px;
}

.result{
background:linear-gradient(135deg,#10B981,#059669);
padding:30px;
border-radius:20px;
text-align:center;
color:white;
box-shadow:0px 10px 25px rgba(0,0,0,.25);
}

.footer{
text-align:center;
color:gray;
font-size:15px;
padding-top:30px;
}

.stButton>button{
width:100%;
height:55px;
border-radius:12px;
background:#2563EB;
color:white;
font-size:20px;
font-weight:bold;
border:none;
}

.stButton>button:hover{
background:#1D4ED8;
}

</style>
""", unsafe_allow_html=True)

# --------------------- SIDEBAR ----------------------

st.sidebar.title("🚗 Dashboard")

st.sidebar.success("Model Loaded Successfully")

st.sidebar.metric("Algorithm","Random Forest")

st.sidebar.metric("Accuracy (R²)","98.27%")

st.sidebar.metric("Cars","7907")

st.sidebar.metric("Brands","30")

st.sidebar.metric("Features","46")

st.sidebar.markdown("---")

st.sidebar.info("""
### About

This project predicts the selling price of old cars using Machine Learning.

**Model**
- Random Forest Regressor

**Libraries**
- Python
- Pandas
- Scikit-Learn
- Streamlit
""")

# --------------------- HERO ----------------------

st.markdown("""
<div class="hero">

<h1>🚗 AI Used Car Price Prediction</h1>

<p>
Predict your car's resale value in seconds using Machine Learning.
</p>

</div>
""", unsafe_allow_html=True)

st.write("")

# --------------------- TOP METRICS ----------------------

m1,m2,m3,m4=st.columns(4)

with m1:
    st.markdown("""
    <div class="metric-card">
    <h2>7907</h2>
    Cars
    </div>
    """,unsafe_allow_html=True)

with m2:
    st.markdown("""
    <div class="metric-card">
    <h2>30</h2>
    Brands
    </div>
    """,unsafe_allow_html=True)

with m3:
    st.markdown("""
    <div class="metric-card">
    <h2>46</h2>
    Features
    </div>
    """,unsafe_allow_html=True)

with m4:
    st.markdown("""
    <div class="metric-card">
    <h2>98.27%</h2>
    Accuracy
    </div>
    """,unsafe_allow_html=True)

st.write("")

# --------------------- DROPDOWN DATA ----------------------

brands = [
"Ashok","Audi","BMW","Chevrolet","Daewoo","Datsun",
"Fiat","Force","Ford","Honda","Hyundai","Isuzu",
"Jaguar","Jeep","Kia","Land","Lexus","MG",
"Mahindra","Maruti","Mercedes-Benz",
"Mitsubishi","Nissan","Opel","Renault",
"Skoda","Tata","Toyota","Volkswagen","Volvo"
]

fuels = [
"CNG",
"Diesel",
"LPG",
"Petrol"
]

seller_types = [
"Dealer",
"Individual",
"Trustmark Dealer"
]

transmissions = [
"Automatic",
"Manual"
]

owners = [
"First Owner",
"Second Owner",
"Third Owner",
"Fourth & Above Owner",
"Test Drive Car"
]

# --------------------- INPUT FORM ----------------------

with st.form("prediction_form"):

    left,right=st.columns(2)

    with left:

        st.markdown("## 🚘 Vehicle Details")

        brand=st.selectbox("Brand",brands)

        fuel=st.selectbox("Fuel Type",fuels)

        seller=st.selectbox("Seller Type",seller_types)

        trans=st.selectbox("Transmission",transmissions)

        owner=st.selectbox("Owner",owners)

    with right:

        st.markdown("## ⚙️ Specifications")

        km=st.number_input(
            "KM Driven",
            0,
            500000,
            50000
        )

        mileage=st.number_input(
            "Mileage",
            0.0,
            50.0,
            20.0
        )

        engine=st.number_input(
            "Engine (CC)",
            500,
            6000,
            1200
        )

        power=st.number_input(
            "Max Power",
            10.0,
            500.0,
            80.0
        )

        seats=st.number_input(
            "Seats",
            2,
            10,
            5
        )

        age=st.number_input(
            "Age",
            0,
            50,
            5
        )

    predict = st.form_submit_button("🚀 Predict Selling Price")
    # --------------------- PREDICTION ----------------------

if predict:

    with st.spinner("🤖 AI is predicting the selling price..."):

        # Create input dictionary
        x = {c: 0 for c in columns}

        # Numerical Features
        x["km_driven"] = km
        x["mileage(km/ltr/kg)"] = mileage
        x["engine"] = engine
        x["max_power"] = power
        x["seats"] = seats
        x["age"] = age

        # Brand Encoding
        brand_col = f"brand_{brand}"
        if brand_col in x:
            x[brand_col] = 1

        # Fuel Encoding
        fuel_col = f"fuel_{fuel}"
        if fuel_col in x:
            x[fuel_col] = 1

        # Seller Type Encoding
        seller_col = f"seller_type_{seller}"
        if seller_col in x:
            x[seller_col] = 1

        # Transmission Encoding
        trans_col = f"transmission_{trans}"
        if trans_col in x:
            x[trans_col] = 1

        # Owner Encoding
        if owner != "First Owner":
            owner_col = f"owner_{owner}"
            if owner_col in x:
                x[owner_col] = 1

        # DataFrame
        input_df = pd.DataFrame([x], columns=columns)

        # Prediction
        prediction = model.predict(input_df)[0]

    st.success("Prediction Completed Successfully!")

    st.write("")

    # --------------------- RESULT CARD ----------------------

    st.markdown(
        f"""
        <div class="result">

        <h3>💰 Estimated Selling Price</h3>

        <h1>₹ {prediction:,.0f}</h1>

        <h4>Machine Learning Prediction</h4>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    # --------------------- CAR SUMMARY ----------------------

    st.subheader("🚘 Car Summary")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Brand", brand)
        st.metric("Fuel", fuel)
        st.metric("Transmission", trans)

    with col2:
        st.metric("Owner", owner)
        st.metric("Age", f"{age} Years")
        st.metric("Seats", seats)

    with col3:
        st.metric("Mileage", mileage)
        st.metric("Engine", engine)
        st.metric("KM Driven", f"{km:,}")

    st.write("")

    # --------------------- INPUT DATA ----------------------

    st.subheader("📋 Input Details")

    summary = pd.DataFrame(
        {
            "Feature": [
                "Brand",
                "Fuel",
                "Seller Type",
                "Transmission",
                "Owner",
                "KM Driven",
                "Mileage",
                "Engine",
                "Max Power",
                "Seats",
                "Age",
            ],
            "Value": [
                brand,
                fuel,
                seller,
                trans,
                owner,
                km,
                mileage,
                engine,
                power,
                seats,
                age,
            ],
        }
    )

    st.dataframe(summary, use_container_width=True)

    st.write("")

