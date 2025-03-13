import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Load the models
# kidney_model = pickle.load(open('kidney_model.sav', 'rb'))
# liver_model = pickle.load(open('liver_model.sav', 'rb'))
# parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))

# Sidebar Menu
with st.sidebar:
    selected = option_menu(
        'Multiple Disease Prediction System',
        ['Home', 'Kidney Prediction', 'Liver Prediction', 'Parkinsons Prediction'],
        menu_icon='hospital-fill',
        icons=['house-door', 'heartbeat', 'liver', 'brain'],
        default_index=0
    )
 # Main content based on sidebar selection   
if selected == 'Home':
    st.title('Welcome to the Multiple Disease Prediction System')
    st.write("This system allows you to predict the likelihood of diseases based on symptoms and medical data.")   
elif selected == 'Kidney Prediction':
    st.title('Kidney Disease Prediction')
    st.write("Enter the relevant details for kidney disease prediction.") 
elif selected == 'Liver Prediction':
    st.title('Liver Disease Prediction')
    st.write("Enter the relevant details for liver disease prediction.")
elif selected == 'Parkinsons Prediction':
    st.title('Parkinsons Disease Prediction')
    st.write("Enter the relevant details for Parkinsons disease prediction.")
    

# Set the background image
def set_bg_image(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{image_url}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Example usage
set_bg_image("https://www.humanitas.net/content/uploads/2017/10/medical-care.jpg")

if selected == "Home":
    with st.expander('Kidney Disease Symptoms'):
       st.title("Symptoms of Kidney Disease")
       st.write("""
            1. **Tiredness**: Feeling tired or weak
            2. **Blood in the Urine**: Blood in the urine
            3. **Itchy Skin**: Dry, itchy skin
            4. **Nausea and Vomiting**: Feeling sick or being sick
            5. **Difficulty Sleeping**: Trouble falling or staying asleep
            6. **Frequent Urination**: Needing to urinate more often, especially at night
            7. **Swelling in the Legs or Ankles**: Puffiness or swelling due to fluid retention
        """)

    with st.expander('Liver Disease Symptoms'):
        st.title("Symptoms of Liver Disease")
        st.write("""
            1. **Bleeding and Bruising**: Bleeding easily or bruising more than normal
            2. **Weakness and Muscle Wasting**: Loss of muscle mass or strength
            3. **Swelling in the Legs/Ankles/Feet**: Edema caused by liver dysfunction
            4. **High Temperature and Shivering**: Common symptoms with liver inflammation
            5. **Yellowing of the Skin and Eyes (Jaundice)**: A yellow tint in the skin and/or eyes
            6. **Loss of Appetite**: Decreased interest in food or difficulty eating
            7. **Dark Urine**: Urine may appear darker than usual, sometimes resembling cola
        """)

    with st.expander('Parkinson\'s Disease Symptoms'):
        st.title("Symptoms of Parkinson's Disease")
        st.write("""
            1. **Posture Instability**: Stooping or hunching over
            2. **Loss of Smell**: A noticeable reduction or loss of your sense of smell
            3. **Tremors**: Shaking in the hands, arms, legs, jaw, or head
            4. **Impaired Balance**: Leading to an increased risk of falls
            5. **Slowed Movement (Bradykinesia)**: Slower physical movements and difficulty with initiating movement
            6. **Muscle Rigidity**: Stiffness and difficulty moving muscles, especially in the arms and legs
            7. **Changes in Speech**: Soft or slurred speech, or difficulty articulating words clearly
        """)

# Kidney Prediction
if selected == "Kidney Prediction":
    st.title('Kidney Disease Prediction')
    
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        age = st.text_input('Age', placeholder='Enter age in years')

    with col2:
        bp = st.text_input('Blood Pressure', placeholder='Enter blood pressure')

    with col3:
        al = st.text_input('Albumin', placeholder='Enter albumin level')

    with col4:
        su = st.text_input('Sugar', placeholder='Enter sugar level')

    with col5:
        rbc = st.text_input('RBC Count', placeholder='Enter RBC count')
    with col1:
       pc = st.text_input('Pus Cells Count', placeholder='Enter pus cells count')

    with col2:
       pcc = st.text_input('Pus Cells Casts', placeholder='Enter pus cells casts count')

    with col3:
       ba = st.text_input('Bacterial Agglutination', placeholder='Enter bacterial agglutination level')

    with col4:
        bgr = st.text_input('Blood Glucose Ratio', placeholder='Enter blood glucose ratio')

    with col5:
       bu = st.text_input('Blood Urea (mg/dL)', placeholder='Enter blood urea level in mg/dL')
    with col1:
        sc = st.text_input('Serum Creatinine (mg/dL)', placeholder='Enter serum creatinine level in mg/dL')

    with col2:
       pot = st.text_input('Potassium (mEq/L)', placeholder='Enter potassium level in mEq/L') 

    with col3:
       wc = st.text_input('White Blood Cell Count (cells/µL)', placeholder='Enter white blood cell count')

    with col4:
       htn = st.text_input('Hypertension (Yes/No)', placeholder='Enter Yes if hypertensive, No otherwise')

    with col5:
       dm = st.text_input('Diabetes (Yes/No)', placeholder='Enter Yes if diabetic, No otherwise')

    with col1:
        cad = st.text_input('Coronary Artery Disease (Yes/No)', placeholder='Enter Yes if the person has coronary artery disease, No otherwise')

    with col2:
       pe = st.text_input('Pedal Edema (Yes/No)', placeholder='Enter Yes if the person has pedal edema, No otherwise')

    with col3:
       ane = st.text_input('Anemia (Yes/No)', placeholder='Enter Yes if the person has anemia, No otherwise')

    # Additional input fields for kidney disease prediction
    # ... (rest of the fields go here) 

    if st.button("Kidney Test Result"):
        user_input = [age, bp, al, su, rbc,
                        pc, pcc, ba,bgr, bu, sc, pot,
                        wc, htn, dm, cad, pe, ane]
        user_input = [float(x) if x else 0.0 for x in user_input]  # Ensure all inputs are numeric
        
        if len(user_input) == 5:
            # Simulate prediction with kidney model
            # kidney_prediction = kidney_model.predict([user_input])

            # For now, we'll mock the prediction
            kidney_prediction = [1]  # Assume prediction returns 1 for kidney disease

            if kidney_prediction[0] == 1:
                kidney_diagnosis = "The person has kidney disease"
            else:
                kidney_diagnosis = "The person does not have kidney disease"

            st.success(kidney_diagnosis)
        else:
            st.error("Please ensure all fields are filled correctly.")

# Liver Prediction
if selected == "Liver Prediction":
    st.title('Liver Disease Prediction')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        total_bilirubin = st.text_input('Total Bilirubin')

    with col3:
        direct_bilirubin = st.text_input('Direct Bilirubin')
    with col1:
        Alkaline_Phosphotase = st.text_input('Alkaline_Phosphotase')

    with col2:
        Alamine_Aminotransferase = st.text_input('Alamine_Aminotransferase')

    with col3:
        Aspartate_Aminotransferase = st.text_input('Aspartate_Aminotransferase')
    with col1:
        Total_Protiens = st.text_input('Total_Protiens')

    with col2:
        Albumin = st.text_input('Albumin')

    with col3:
        Albumin_and_Globulin_Ratio = st.text_input('Albumin_and_Globulin_Ratio')
    with col1:
        Gender_Male = st.text_input('Gender_Male')

    # Add other liver-related input fields
    # ...

    if st.button("Liver Test Result"):
        user_input = [age, total_bilirubin, direct_bilirubin, Alkaline_Phosphotase, Alamine_Aminotransferase,
                      Aspartate_Aminotransferase,Total_Protiens, Albumin,Albumin_and_Globulin_Ratio,Gender_Male]
        user_input = [float(x) if x else 0.0 for x in user_input]  # Ensure all inputs are numeric
        
        if len(user_input) == 3:
            # Simulate prediction with liver model
            # liver_prediction = liver_model.predict([user_input])

            # For now, we'll mock the prediction
            liver_prediction = [1]  # Assume prediction returns 1 for liver disease

            if liver_prediction[0] == 1:
                liver_diagnosis = "The person has liver disease"
            else:
                liver_diagnosis = "The person does not have liver disease"

            st.success(liver_diagnosis)
        else:
            st.error("Please ensure all fields are filled correctly.")

# Parkinson's Prediction
if selected == "Parkinsons Prediction":
    st.title("Parkinson's Disease Prediction")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
    with col1:
        RAP = st.text_input('MDVP:RAP')

    with col2:
        PPQ = st.text_input('MDVP:PPQ')

    with col3:
        DDP = st.text_input('Jitter:DDP')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')
    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')  
    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')       
 
    # Add other Parkinson's-related input fields
    # ...

    if st.button("Parkinson's Test Result"):
        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]
        user_input = [float(x) if x else 0.0 for x in user_input]  # Ensure all inputs are numeric

        if len(user_input) == 5:
            # Simulate prediction with Parkinson's model
            # parkinsons_prediction = parkinsons_model.predict([user_input])

            # For now, we'll mock the prediction
            parkinsons_prediction = [1]  # Assume prediction returns 1 for Parkinson's disease

            if parkinsons_prediction[0] == 1:
                parkinsons_diagnosis = "The person has Parkinson's disease"
            else:
                parkinsons_diagnosis = "The person does not have Parkinson's disease"

            st.success(parkinsons_diagnosis)
        else:
            st.error("Please ensure all fields are filled correctly.")
