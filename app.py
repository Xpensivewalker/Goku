import streamlit as st

def get_age_description(age):
    if age < 1:
        return "Infant – Requires specialized pediatric care and vaccinations."
    elif 1 <= age <= 3:
        return "Toddler – Key developmental stage with frequent wellness checks."
    elif 4 <= age <= 12:
        return "Child – Important years for growth, schooling, and immunizations."
    elif 13 <= age <= 19:
        return "Teenager – Hormonal changes, mental health, and lifestyle guidance matter."
    elif 20 <= age <= 35:
        return "Young Adult – Focus on fitness, career stress, and reproductive health."
    elif 36 <= age <= 55:
        return "Adult – Career-peak years, regular checkups, and stress management advised."
    elif 56 <= age <= 75:
        return "Senior Adult – Age-related screenings become more critical."
    else:
        return "Elderly – Support with mobility, memory, and chronic condition management."

# Streamlit App UI
st.set_page_config(page_title="Goku Age Description Tool", layout="centered")
st.title("🧠 Goku's Age Insight Assistant")

st.write("Enter your age, and Goku will provide a short description tailored to your stage of life.")

age_input = st.number_input("Enter age", min_value=0, max_value=120, value=30)

if st.button("Get Description"):
    description = get_age_description(age_input)
    st.success(description)
