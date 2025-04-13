import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("exe_model.pkl")

# Page selection
st.set_page_config(page_title="Calories Burnt Predictor", layout="centered")
page = st.sidebar.selectbox("Navigate", ["🏠 Home", "📖 About", "📊 Info", "🔍 Predict"])

# Home Page
if page == "🏠 Home":
    st.title("KCAL-COUNT: Calories Burnt Prediction using XGBoost Regressor")
    st.markdown("---")

    st.subheader("Welcome!")
    st.write("""
        The **Calories Burnt Predictor App** is a smart and interactive tool designed to estimate the number of calories you burn during physical activity based on your personal and workout details.
        
        Whether you're a fitness enthusiast, an athlete, or someone just beginning their health journey — this tool helps you:
        - 🧠 Understand your body's response to exercise
        - 💪 Tailor your workout for maximum efficiency
        - 🍽️ Plan your nutrition and recovery better
    """)

    st.markdown("### 🛠️ How It Works")
    st.write("""
        This application is powered by a **Machine Learning model** (XGBoost Regressor), trained on a dataset that includes:
        - Gender
        - Age
        - Height
        - Weight
        - Workout Duration
        - Heart Rate
        - Body Temperature
        
        Using these inputs, the model predicts the total **calories burnt** with impressive accuracy!
    """)

    st.markdown("### 📍 Navigation Guide")
    st.write("""
        Use the **sidebar** on the left to access different parts of the app:
        - `Home`: You're here! Learn what the app is all about.
        - `About`: Know the tools and technologies behind this project.
        - `Info`: Understand the meaning and importance of each input.
        - `Predict`: Enter your data and get real-time calorie predictions!
    """)

    st.markdown("---")
    st.info("💡 Tip: Accurate input leads to better prediction results. Make sure you measure your data correctly.")


# About Page
elif page == "📖 About":
    st.title("📖 About This Project")
    st.markdown("---")

    st.subheader("🔧 Technologies Used")
    st.write("""
    This application has been developed using the following technologies and tools:
    - 🐍 **Python** – for backend logic and data handling
    - 📈 **Streamlit** – to build this interactive web app
    - ⚙️ **XGBoost Regressor** – the core machine learning model for prediction
    - 💾 **Joblib** – for saving and loading the trained model
    """)

    st.subheader("🧠 Model Training")
    st.write("""
    The ML model was trained using a well-structured dataset containing the following features:
    - Gender
    - Age
    - Height
    - Weight
    - Exercise Duration
    - Heart Rate
    - Body Temperature

    These features help the model learn how different physical and physiological parameters contribute to calorie burn during exercise.
    """)

    st.subheader("👨‍💻 Contributors")
    st.write("""
    This project was collaboratively developed by:
    - **KP Suhas** (1DT23CD022) – *Model Design and Implementation*
    - **Shiva Shanker** (1DT23CD047) – *Data Processing and Testing*
    - **Karunakar Reddy** (1DT23CD056) – *User Interface Development*
    - **Channa Basava** (1DT24CD400) – *Documentation and Deployment*

    Each team member contributed significantly to building, refining, and testing this smart solution.
    """)

    st.markdown("---")
    st.success("✅ We are proud to present this tool as a collaborative student effort in merging health & technology.")

# Info Page
elif page == "📊 Info":
    st.title("📊 Feature & Model Information")
    st.markdown("---")

    st.subheader("🧾 Feature Descriptions")
    st.write("""
    This model uses the following features to predict calories burnt during physical activity:

    - **Gender**: Biological sex of the individual (`Male` or `Female`). It can influence metabolic rate and energy expenditure.
    - **Age** (in years): Calorie burn tends to decrease with age due to changes in muscle mass and metabolism.
    - **Height** (in cm): Taller individuals may expend more energy during the same activity.
    - **Weight** (in kg): Heavier individuals typically burn more calories for the same duration and intensity of exercise.
    - **Duration** (in minutes): Total time spent on exercise. Longer durations usually result in higher calorie expenditure.
    - **Heart Rate** (in BPM): Indicates intensity of the workout. A higher average heart rate suggests more effort and calorie burn.
    - **Body Temperature** (in °C): Elevated body temperature during exercise is linked to metabolic rate and energy usage.
    """)

    st.markdown("---")
    st.subheader("🧠 About the Algorithm: XGBoost Regressor")
    st.write("""
    We use the **XGBoost Regressor**, a powerful and efficient machine learning algorithm based on gradient boosting. 

    ### Why XGBoost?
    - 🔥 **High performance**: Known for its speed and accuracy, especially in regression tasks.
    - 🌳 **Boosted trees**: It builds an ensemble of decision trees sequentially, where each new tree tries to correct errors from previous ones.
    - 🎯 **Handles overfitting**: Built-in regularization features prevent overfitting on training data.
    - 💡 **Interpretable**: Feature importance can be extracted to understand which variables contribute most to the prediction.

    This algorithm was chosen after testing multiple models, and XGBoost delivered the best results in terms of accuracy and generalization.
    """)

    st.markdown("---")
    st.info("💡 Understanding these features can help you input better data and interpret the predictions effectively.")


# Prediction Page
elif page == "🔍 Predict":
    st.title("Predict Calories Burnt 🔍")

    gender = st.selectbox("Gender", ["male", "female"])
    gender_encoded = 1 if gender == "male" else 0

    age = st.number_input("Age", min_value=1, max_value=100, value=25)
    height = st.number_input("Height (cm)", min_value=100, max_value=250, value=170)
    weight = st.number_input("Weight (kg)", min_value=30, max_value=200, value=65)
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=300, value=60)
    heart_rate = st.number_input("Heart Rate", min_value=40, max_value=200, value=100)
    body_temp = st.number_input("Body Temperature (°C)", min_value=35.0, max_value=45.0, value=37.0)

    if st.button("Predict"):
        input_features = np.array([[gender_encoded, age, height, weight, duration, heart_rate, body_temp]])
        prediction = model.predict(input_features)
        st.success(f"🔥 Estimated Calories Burnt: **{prediction[0]:.2f}** kcal")
