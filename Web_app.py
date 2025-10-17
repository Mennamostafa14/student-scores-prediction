# e:\python312\python.exe -m streamlit run Web_app.py
import numpy as np
import pickle
import streamlit as st
import pandas as pd
import pathlib

st.set_page_config(
    page_title="🎓 Student Score Predictor",
    page_icon="🎯",
    layout="centered",
    initial_sidebar_state="expanded"
)
# loading the saved model
# استخدمي Path بدل __file__
current_dir = pathlib.Path(__file__).parent if "__file__" in locals() else pathlib.Path.cwd()
model_path = current_dir / "trained_model.sav"

with open(model_path, "rb") as file:
    loaded_model = pickle.load(file)

# ✅ CSS لتجميل الواجهة
st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #e0f7fa 0%, #fffde7 100%);
    }

    .main-card {
        background-color: #ffffffcc;
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }

    div.stButton > button:first-child {
        background: linear-gradient(to right, #42a5f5, #478ed1);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.6rem 1.3rem;
        font-size: 1rem;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    div.stButton > button:hover {
        background: linear-gradient(to right, #1e88e5, #1565c0);
        transform: scale(1.03);
    }

    h1, h2, h3 {
        text-align: center;
        color: #0d47a1;
        font-family: 'Segoe UI', sans-serif;
    }

    </style>
""", unsafe_allow_html=True)

# creating a function for Prediction

def predict_exam_score(input_data):
    # نحول ل numpy array من غير تغيير نوع البيانات
    #input_data_as_numpy_array = np.asarray(input_data, dtype=object).reshape(1, -1)
    prediction = loaded_model.predict(input_data)
    return f"🎯 Predicted Exam Score: {prediction[0]:.2f}"

  
    
  
def main():
    
    
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.title('🎓 Student Score Prediction App')
    st.write("Enter student details below and get the predicted exam score instantly!")

    st.header("📋 Student Information")
    
    Hours_Studied = st.number_input("Hours Studied", min_value=0, step=1)
    Attendance = st.number_input("Attendance (%)", min_value=0, max_value=100, step=1)
    Parental_Involvement = st.selectbox("Parental Involvement", ["Low", "Medium", "High"])
    Access_to_Resources = st.selectbox("Access to Resources", ["Low", "Medium", "High"])
    Extracurricular_Activities = st.selectbox("Extracurricular Activities", ["Yes", "No"])
    Sleep_Hours = st.number_input("Sleep Hours", min_value=0, max_value=12, step=1)
    Previous_Scores = st.number_input("Previous Scores", min_value=0, max_value=100, step=1)
    Motivation_Level = st.selectbox("Motivation Level", ["Low", "Medium", "High"])
    Internet_Access = st.selectbox("Internet Access", ["Yes", "No"])
    Tutoring_Sessions = st.number_input("Tutoring Sessions", min_value=0, step=1)
    Family_Income = st.selectbox("Family Income", ["Low", "Medium", "High"])
    Teacher_Quality = st.selectbox("Teacher Quality", ["Low", "Medium", "High"])
    School_Type = st.selectbox("School Type", ["Public", "Private"])
    Peer_Influence = st.selectbox("Peer Influence", ["Negative", "Neutral", "Positive"])
    Physical_Activity = st.number_input("Physical Activity ", min_value=0, step=1)
    Learning_Disabilities = st.selectbox("Learning Disabilities", ["Yes", "No"])
    Parental_Education_Level = st.selectbox("Parental Education Level", ["High School", "College", "Postgraduate"])
    Distance_from_Home = st.selectbox("Distance from Home", ["Near", "Moderate", "Far"])
    Gender = st.selectbox("Gender", ["Male", "Female"])

    # 

    input_data = pd.DataFrame({
    "Hours_Studied": [Hours_Studied],
    "Attendance": [Attendance],
    "Parental_Involvement": [Parental_Involvement],
    "Access_to_Resources": [Access_to_Resources],
    "Extracurricular_Activities": [Extracurricular_Activities],
    "Sleep_Hours": [Sleep_Hours],
    "Previous_Scores": [Previous_Scores],
    "Motivation_Level": [Motivation_Level],
    "Internet_Access": [Internet_Access],
    "Tutoring_Sessions": [Tutoring_Sessions],
    "Family_Income": [Family_Income],
    "Teacher_Quality": [Teacher_Quality],
    "School_Type": [School_Type],
    "Peer_Influence": [Peer_Influence],
    "Physical_Activity": [Physical_Activity],
    "Learning_Disabilities": [Learning_Disabilities],
    "Parental_Education_Level": [Parental_Education_Level],
    "Distance_from_Home": [Distance_from_Home],
    "Gender": [Gender]
})
    
    # code for Prediction
    
    
    # creating a button for Prediction
    
    if st.button('Predict Exam Score'):
        
        result=predict_exam_score(input_data)
        st.success(result)
    st.markdown('</div>', unsafe_allow_html=True)
    
    
    
    
if __name__ == '__main__':
    main()

    









