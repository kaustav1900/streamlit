 
import pickle
import streamlit as st
 
# loading the trained model
pickle_in = open('classifier1.pkl', 'rb') 
classifier = pickle.load(pickle_in)
 
@st.cache()
  
# defining the function which will make the prediction using the data which the user inputs 
def prediction(is_a_grate_bank, sense_of_achievement, feel_valued_for_the_work_I_do, age):   
 
    # Pre-processing user input    
    if is_a_grate_bank == "Agree":
        is_a_grate_bank = 1
    elif is_a_grate_bank == "Tend to Agree":
        is_a_grate_bank = 2
    elif is_a_grate_bank == "Neutral":
        is_a_grate_bank = 3
    elif is_a_grate_bank == "Tend to Disagree":
        is_a_grate_bank = 4
    elif is_a_grate_bank == "Disagree":
        is_a_grate_bank = 5
 

    if feel_valued_for_the_work_I_do == "Agree":
        feel_valued_for_the_work_I_do = 1
    elif feel_valued_for_the_work_I_do == "Tend to Agree":
        feel_valued_for_the_work_I_do = 2
    elif feel_valued_for_the_work_I_do == "Neutral":
        feel_valued_for_the_work_I_do = 3
    elif feel_valued_for_the_work_I_do == "Tend to Disagree":
        feel_valued_for_the_work_I_do = 4
    elif feel_valued_for_the_work_I_do == "Disagree":
        feel_valued_for_the_work_I_do = 5


    if sense_of_achievement == "Agree":
        sense_of_achievement = 1
    elif sense_of_achievement == "Tend to Agree":
        sense_of_achievement = 2
    elif sense_of_achievement == "Neutral":
        sense_of_achievement = 3
    elif sense_of_achievement == "Tend to Disagree":
        sense_of_achievement = 4
    elif sense_of_achievement == "Disagree":
        sense_of_achievement = 5
        
        
    if age == "18 years or under":
        age = 1
    elif age == "19-24 years":
        age = 2
    elif age == "25-34 years":
        age = 3
    elif age == "35-44 years":
        age = 4
    elif age == "45-59 years":
        age = 5
    elif age == "60+ years":
        age = 6


    
     # Making predictions 
    prediction = classifier.predict([[is_a_grate_bank, sense_of_achievement, feel_valued_for_the_work_I_do, age]])
     
    if prediction == 0:
        pred = 'Not Churn'
    else:
        pred = 'Churn'
    return pred
      
  
# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:blue;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Streamlit Churn Prediction</h1>
    <img src="Tivian.png" alt="Tivian" width="100" height="150">
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # following lines create boxes in which user can enter data required to make prediction 
    is_a_grate_bank = st.selectbox('I feel that this is a great bank',("Agree","Tend to Agree", "Neutral", "Tend to Disagree", "Disagree"))
    feel_valued_for_the_work_I_do = st.selectbox('I feel valued for the work that I do',("Agree","Tend to Agree", "Neutral", "Tend to Disagree", "Disagree"))
    sense_of_achievement = st.selectbox('I get a sense of achievement from my work',("Agree","Tend to Agree", "Neutral", "Tend to Disagree", "Disagree"))
    age = st.selectbox('I belong to the age group',("18 years or under","19-24 years", "25-34 years", "35-44 years", "45-59 years", "60+ years"))
    result =""
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(is_a_grate_bank, sense_of_achievement, feel_valued_for_the_work_I_do, age)
        st.success('This employee is a {}'.format(result))
     
if __name__=='__main__': 
    main()
