



import streamlit as st
import pickle

# Load model and scaler
ridge_model = pickle.load(open('ridge_model.pkl', 'rb'))
standard_scaler = pickle.load(open('scaler_model.pkl', 'rb'))

# Page Config
st.set_page_config(
    page_title="Forest Fire Prediction",
    page_icon="🔥",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
.main {
    background-color: #f5f7fa;
}

.title-box {
    background: linear-gradient(135deg, #ff6b35, #ff9f1c);
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    color: white;
    margin-bottom: 25px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.2);
}

.result-box {
    background: #ffffff;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    border-left: 8px solid #ff6b35;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
}

div.stButton > button {
    width: 100%;
    background: linear-gradient(135deg, #ff6b35, #ff9f1c);
    color: white;
    font-size: 18px;
    font-weight: bold;
    border-radius: 10px;
    border: none;
    padding: 12px;
    transition: 0.3s;
}

div.stButton > button:hover {
    transform: scale(1.03);
    background: linear-gradient(135deg, #ff5722, #ff9800);
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="title-box">
    <h1>🔥 Algerian Forest Fire Prediction</h1>
    <p>Predict Fire Weather Index (FWI) using Machine Learning</p>
</div>
""", unsafe_allow_html=True)

st.subheader("Enter Forest Parameters")

# 3 Columns Layout
col1, col2, col3 = st.columns(3)

with col1:
    Temperature = st.number_input("🌡 Temperature", value=25.0)
    RH = st.number_input("💧 Relative Humidity", value=50.0)
    Ws = st.number_input("💨 Wind Speed", value=15.0)

with col2:
    Rain = st.number_input("🌧 Rain", value=0.0)
    FFMC = st.number_input("🔥 FFMC", value=85.0)
    DMC = st.number_input("📊 DMC", value=20.0)

with col3:
    ISI = st.number_input("⚡ ISI", value=5.0)
    Classes = st.number_input("🏷 Classes", value=0.0)
    Region = st.number_input("📍 Region", value=1.0)

st.markdown("<br>", unsafe_allow_html=True)

# Predict Button
if st.button("🚀 Predict Fire Weather Index"):

    data = [[
        Temperature,
        RH,
        Ws,
        Rain,
        FFMC,
        DMC,
        ISI,
        Classes,
        Region
    ]]

    scaled_data = standard_scaler.transform(data)
    prediction = ridge_model.predict(scaled_data)

    st.markdown(f"""
    <div class="result-box">
        <h2>Prediction Result</h2>
        <h1 style="color:#ff6b35;">
            {prediction[0]:.4f}
        </h1>
        <p>Predicted Fire Weather Index (FWI)</p>
    </div>
    """, unsafe_allow_html=True)