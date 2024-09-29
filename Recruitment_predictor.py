# model_integration.py
import pickle
import pandas as pd

# Function to load the model
def load_model():
    with open('Recruitment/model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

def prepare_input_data(age, gender, education_level, experience_years, previous_companies, distance_from_company, interview_score, skill_score, personality_score, recruitment_strategy):
    input_data = pd.DataFrame({
        'Age': [age],
        'Gender': [gender],
        'EducationLevel': [education_level],
        'ExperienceYears': [experience_years],
        'PreviousCompanies': [previous_companies],
        'DistanceFromCompany': [distance_from_company],
        'InterviewScore': [interview_score],
        'SkillScore': [skill_score],
        'PersonalityScore': [personality_score],
        'RecruitmentStrategy': [recruitment_strategy]
    })
    return input_data

def predict_hiring_decision(input_data):
    model = load_model()
    prediction = model.predict(input_data)
    return prediction