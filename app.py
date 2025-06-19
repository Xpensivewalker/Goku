import streamlit as st

st.set_page_config(page_title="Goku Agent Task Overview", layout="wide")
st.title("🤖 Goku: AI Healthcare Scheduling Agent")

st.markdown("""
Welcome to **Goku's Task Dashboard**. Below is a full overview of the responsibilities and capabilities designed for Goku, an AI agent that handles calls and manages healthcare appointments.
""")

st.header("📞 1. Call Handling & Voice Interaction")
st.markdown("""
- Answer inbound calls with professional greetings
- Understand patient intent (booking, rescheduling, canceling)
- Transcribe voice inputs using speech recognition
- Confirm understanding by repeating back details
- Escalate emergencies to human staff or emergency services
""")

st.header("📅 2. Appointment Scheduling")
st.markdown("""
- Access and read provider calendars
- Suggest available time slots
- Schedule based on specialty, appointment type, and insurance
- Confirm all booking details verbally and digitally
- Send automated confirmations
""")

st.header("🔄 3. Modifications & Cancellations")
st.markdown("""
- Locate existing appointments by patient data
- Offer rescheduling options
- Cancel appointments and update the calendar
- Track reasons for cancellations for follow-up
""")

st.header("🧾 4. Patient Intake & Information Collection")
st.markdown("""
- Collect and confirm:
  - Name, DOB, contact details
  - Insurance information
  - Visit reason or symptoms
- Sync data securely with EHR/CRM systems
- Identify new vs returning patients
""")

st.header("🧠 5. Pre-screening & Eligibility Checks")
st.markdown("""
- Ask relevant pre-screening questions
- Verify insurance eligibility
- Recommend best care path (in-person, telehealth, referral)
""")

st.header("💬 6. Post-call Actions & Notifications")
st.markdown("""
- Send appointment confirmations
- Trigger reminders (24-48 hours in advance)
- Log call data and appointment status
- Notify staff of any special requirements
""")

st.header("✨ Optional Enhancements")
st.markdown("""
- **Natural Language Understanding**: Flexibility in patient dialogue
- **Sentiment Detection**: Escalate frustrated or confused patients
- **Conversational Memory**: Personalize experience based on history
""")

st.success("This dashboard outlines Goku's responsibilities and flow for integration with real-time healthcare systems.")
