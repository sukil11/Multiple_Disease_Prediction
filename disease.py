import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
kidney_model = pickle.load(open('kidney_model.sav', 'rb'))
liver_model = pickle.load(open('liver_model.sav', 'rb'))
loaded_model = pickle.load(open('parkinsons_model.sav', 'rb'))
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',

                           ['Home','Kidney Prediction',
                            'Liver Prediction',
                            'Parkinsons Prediction'],
                           menu_icon='hospital-fill',
                           icons=['Home','activity', 'heart', 'person'],
                           default_index=0)
    

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
set_bg_image("https://cdn.wallpapersafari.com/33/95/0Czm58.jpg")

#Home page
if selected == "Home":
    with st.expander('**Kidney**'):
        st.title('Symptoms and Remedies for Kidney disease')
        st.image("C:\\Users\\SukilPriya\\Pictures\\kidney.jpeg")
        st.write("""
            1. **Tiredness**: Feeling tired or weak.
               - **Remedy**: Ensure you get enough rest and manage stress. Consider increasing your intake of iron-rich foods and consult with a doctor for any underlying issues. 
            2. **Blood in the Urine**: Blood in the urine.
               - **Remedy**: This may indicate a serious issue such as kidney stones or infection. It’s important to consult a healthcare provider immediately. 
            3. **Itchy Skin**: Dry, itchy skin.
               - **Remedy**: Use a good moisturizer and avoid hot showers that can dry out the skin. For persistent itching, a healthcare provider may recommend medications to help manage the symptoms.
            4. **Nausea and Vomiting**: Feeling sick or being sick.
               - **Remedy**: Stay hydrated, avoid heavy meals, and eat light, bland foods. If the symptoms persist, contact your doctor for a more accurate diagnosis. 
            5. **Difficulty Sleeping**: Trouble falling or staying asleep.
               - **Remedy**: Try establishing a bedtime routine, reduce caffeine intake, and limit screen time before bed. If difficulty sleeping continues, it may be a sign of kidney problems and should be evaluated.  
            6. **Frequent Urination**: Needing to urinate more often, especially at night.
               - **Remedy**: Avoid drinking too many fluids before bedtime and reduce intake of caffeinated drinks. If frequent urination continues, it’s best to speak with a healthcare provider. 
            7. **Swelling in the Legs or Ankles**: Puffiness or swelling due to fluid retention.
               - **Remedy**: Elevate your legs when sitting, limit salt intake, and try wearing compression stockings. If swelling persists, see a doctor to rule out kidney or heart issues. 
        """)
    with st.expander('**Liver**'):
        st.title('Symptoms and Remedies for Liver disease')
        st.image("C:\\Users\\SukilPriya\\Pictures\\liver.jpeg")
        st.write("""
            1. **Bleeding and Bruising**: Bleeding easily or bruising more than normal.
               - **Remedy**: Ensure a balanced diet rich in vitamin K and avoid medications that may increase bleeding risks. If you notice frequent or severe bruising, consult with a healthcare professional.
            2. **Weakness and Muscle Wasting**: Loss of muscle mass or strength.
               - **Remedy**: Engage in light exercises or physical therapy to maintain muscle strength. Eating a protein-rich diet may help in rebuilding muscle mass. Always consult a doctor before starting an exercise routine. 
            3. **Swelling in the Legs/Ankles/Feet**: Edema caused by liver dysfunction.
               - **Remedy**: Elevate the legs, reduce salt intake, and avoid standing for prolonged periods. Diuretics may be prescribed by your doctor to reduce fluid retention. 
            4. **High Temperature and Shivering**: Common symptoms with liver inflammation.
               - **Remedy**: Rest and stay hydrated. If fever persists, consider taking acetaminophen (under medical guidance) or consult a healthcare provider to identify and treat the underlying cause.  
            5. **Yellowing of the Skin and Eyes (Jaundice)**: A yellow tint in the skin and/or eyes.
               - **Remedy**: Seek medical attention immediately, as jaundice can indicate serious liver problems. Treatment may include medications, lifestyle changes, and in some cases, a liver transplant.  
            6. **Loss of Appetite**: Decreased interest in food or difficulty eating.
               - **Remedy**: Eat smaller, frequent meals and try high-protein snacks. If you struggle with eating, talk to a nutritionist or healthcare provider to manage your diet effectively. 
            7. **Dark Urine**: Urine may appear darker than usual, sometimes resembling cola.
               - **Remedy**: Increase water intake to stay hydrated. Dark urine can indicate dehydration or liver issues, so if it persists, see a healthcare provider for a proper diagnosis. 
        """)

    with st.expander('**Parkinson\'s**'):
        st.title('Symptoms and Remedies for Parkinsons disease')
        st.image("C:\\Users\\SukilPriya\\Pictures\\brain.jpeg")
        st.write("""
            1. **Posture Instability**: Stooping or hunching over.
               - **Remedy**: Practice good posture techniques and engage in regular physical therapy to strengthen muscles and improve posture. A physical therapist can teach specific exercises to improve balance.  
            2. **Loss of Smell**: A noticeable reduction or loss of your sense of smell.
               - **Remedy**: While there's no direct remedy for loss of smell, maintaining a healthy diet and managing Parkinson's symptoms with medications can help slow progression. It's also beneficial to consult with a specialist about olfactory training.
            3. **Tremors**: Shaking in the hands, arms, legs, jaw, or head.
               - **Remedy**: Medications like levodopa or dopamine agonists may help manage tremors. Regular exercise, such as yoga or tai chi, may also aid in improving motor control and reducing tremors. 
            4. **Impaired Balance**: Leading to an increased risk of falls.
               - **Remedy**: Engage in balance training exercises, such as physical therapy or certain yoga and Pilates exercises. Consider using mobility aids if recommended by a healthcare provider. Occupational therapy can help modify the environment to reduce fall risks. 
            5. **Slowed Movement (Bradykinesia)**: Slower physical movements and difficulty with initiating movement.
               - **Remedy**: Regular physical exercise and movement-focused therapies, such as dance or boxing classes designed for Parkinson’s, can help improve motor function. Medications like levodopa can also help improve movement speed and initiation.
            6. **Muscle Rigidity**: Stiffness and difficulty moving muscles, especially in the arms and legs.
               - **Remedy**: Stretching, massage, and physical therapy can reduce muscle stiffness. Medications like dopamine agonists or muscle relaxants may be prescribed to reduce rigidity. Heat or cold therapy might also provide relief. 
            7. **Changes in Speech**: Soft or slurred speech, or difficulty articulating words clearly.
               - **Remedy**: Speech therapy can be highly beneficial for improving vocal strength and clarity. Practicing speaking out loud, engaging in vocal exercises, and using speech amplification devices can also help manage speech difficulties.  
        """)
# Kidney Prediction      
if selected == "Kidney Prediction":
    st.title('Kidney Prediction')
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
       age = st.text_input('age')

    with col2:
       bp = st.text_input('blood pressure(bp)')

    with col3:
       al = st.text_input('albumin level(al)')

    with col4:
       su = st.text_input('sugar level(su)')

    with col5:
       rbc = st.text_input('RBC')

    with col1:
       pc = st.text_input('pus cells(pc)')

    with col2:
       pcc = st.text_input('pus cells casts(pcc)')

    with col3:
       ba = st.text_input('bacterial agglutination(ba)')

    with col4:
        bgr = st.text_input('blood glucose ratio(bgr)')

    with col5:
       bu = st.text_input('blood urea(bu)')

    with col1:
        sc = st.text_input('serum creatinine(sc)')
        
    with col2:
       pot = st.text_input('potassium(pot)')  

    with col3:
       wc = st.text_input('white blood cell(wc)')

    with col4:
       htn = st.text_input('hypertensive(htn)',placeholder='Enter Yes if hypertensive, No otherwise')

    with col5:
       dm = st.text_input('diabetic(dm)',placeholder='Enter Yes if diabetic, No otherwise')
 
    with col1:
        cad = st.text_input('coronary artery disease(cad)',placeholder='Enter Yes if the person has coronary artery disease, No otherwise')

    with col2:
       pe = st.text_input('pedal edema(pe)',placeholder='Enter Yes if the person has pedal edema, No otherwise')

    with col3:
       ane = st.text_input('anemia(ane)',placeholder='Enter Yes if the person has anemia, No otherwise')

    kidney_diagnosis = ''

    if st.button("kidney Test Result"):
        user_input = [age, bp, al, su, rbc,
                        pc, pcc, ba,bgr, bu, sc, pot,
                        wc, htn, dm, cad, pe, ane]
        
        user_input = [float(x) for x in user_input]

        Kidney_Prediction = kidney_model.predict([user_input])

        if Kidney_Prediction[0] == 1:
                kidney_diagnosis = "The person has kidney disease"
        else:
                kidney_diagnosis = "The person does not have kidney disease"

        st.success(kidney_diagnosis)

# Liver Prediction
if selected == "Liver Prediction":
    st.title('Liver Prediction')

    col1,col2,col3 = st.columns(3)

    with col1:
        age = st.text_input('age')

    with col2:
        Total_Bilirubin = st.text_input('Total_Bilirubin')

    with col3:
        Direct_Bilirubin = st.text_input('Direct_Bilirubin')

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

    liver_diagnosis = ''

    if st.button("Liver Test Result"):
       user_input = [age, Total_Bilirubin, Direct_Bilirubin, Alkaline_Phosphotase, Alamine_Aminotransferase,
                      Aspartate_Aminotransferase,Total_Protiens, Albumin,Albumin_and_Globulin_Ratio,Gender_Male]
       
       user_input = [float(x) for x in user_input]

       liver_Prediction = liver_model.predict([user_input])

       if liver_Prediction[0] == 1:
            liver_diagnosis = "The person has liver disease"
       else:
            liver_diagnosis = "The person does not have liver disease"

       st.success(liver_diagnosis)

# Parkinson's Prediction 
if selected == "Parkinsons Prediction":
    st.title("Parkinson's Prediction")
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

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = loaded_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)
