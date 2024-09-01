import streamlit as st

st.set_page_config(page_title="Autobiography & Portfolio", layout="wide")

st.title("Welcome to Chris Marklen's Autobiography & Portfolio")

st.header("Autobiography")

st.image(r"C:\backupfiles\Pics\2x2.jpg", width=200)

st.write("""
Hello! I am **Chris Marklen A. Fernandez**. 
\n I am currently a 4th year student taking up BSIT.
\n I am particularly interested in UI/UX and frontend development.

Here is a brief overview of my journey as a student:

- **Education**: I am currently a Teknoy. I graduated from USC-TC for my SHS and completed my JHS in USC-NC. For my elementary education, I finished it in Mabolo Elementary School.
- **Experience**: I am working as my brother's assistant. I am helping him with his PowerPoint presentations, grade computations, and etc. since he worked as a law school faculty in USJR. I am also working as a social media handler for my sister's perfume business. I manage the brand's postings on social media.
- **Achievements**: I completed JHS with honors and my elementary education receiving 8th achiever.
- **Hobbies**: Outside of school, I enjoy playing badminton and volleyball.
""")

st.header("Portfolio")

st.write("""
Here are some of the projects that I have contributed on.

- **Project 1**: Wildcat Innovation Labs: Incubatee Application Review and Selection Process
  - Description: App that has a specific process for reviewing and selecting startups to join their program.

- **Project 2**: CodeTech
  - Description: An online educational course specifically made beginner-friendly.

- **Project 3**: DigiDiary
  - Description: An online diary made easy and seamless with additional feaetures such as alarm and calendar.
""")

st.header("Contact Me")

with st.form(key='contact_form'):
    st.subheader("Reach Out Anytime!")
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")
    submit_button = st.form_submit_button(label='Send')

    if submit_button:
        st.write(f"Thank you, {name}! I will get back to you at {email} soon.")

st.markdown("""
---
Made by Chris Marklen A. Fernandez
[LinkedIn](https://www.linkedin.com/in/chris-marklen-fernandez-7b06621b8/)
""")
