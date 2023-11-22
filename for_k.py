import streamlit as st
import random
from PIL import Image

# Define the correct password
correct_password = "Zero"  # Replace with your desired password

# Define the list of questions and their correct answers
questions = {
    "What is suhaibs fav dish?": "Biryani",
    "What was the first thing we watched together?": "Anime",
    "How does suhaib like your hair?": "Straight",
    "What was the first thing suhaib was attracted to": "My voice",
}
# Colors for different roses
rose_colors = ["Correcr answer meri jaan", "YOOO getting it right", "Knew it you know me so well bro", "CRazy sooma", "Sahi jawaab muhtarma"]

def draw_heart():
    st.write("❤️💖💖💖💖")

def draw_rose(color):
    st.write(f"🌹💖❤️💖💖💖💖")

def main():
    st.title("The 23rd of Nov")
    st.image("https://th.bing.com/th/id/R.fe06ecc1fd49b9dd7b936981c05b9cad?rik=oxDNJ6iuG7cHLg&pid=ImgRaw&r=0")

    # Greet the user
    st.subheader("Hi, K!")

    # Ask for the password
    password = st.text_input("Enter the password, you would only get it if you are k:", type="password")
    st.write("hint: A secret code to stop a certain event")

    if password == correct_password:
        
        st.success("Password is correct! I knew you would know it kulsoom.")
        draw_heart()
        st.subheader("WELCOME KULSOOM")

        # Ask if it should continue
        continue_quiz = st.checkbox("Do you want to continue the quiz?")

        if continue_quiz:
            st.write("Great! Let's continue with some questions, little nugget.")
            st.write("Make sure to give one letter answer, except the last one with 'my__answer'' ")

            # Initialize a variable to keep track of the number of correct answers
            correct_answers = 0

            # Ask different questions
            for question, correct_answer in questions.items():
                user_answer = st.text_input(question)

                if user_answer.lower() == correct_answer.lower():
                    color = random.choice(rose_colors)
                    draw_rose(color)
                    st.success(f"Kulsooma! {color.capitalize()} 🌹")
                    correct_answers += 1
                elif user_answer:
                    st.error("Incorrect answer. Try again.")

                if correct_answers == 4:
                    st.empty()  # Clear the content of the current page
                    st.title("A Note of Love")
                    st.write("\n")
                    st.write("Dear Kulsoom,\n")
                    st.write("I hope you enjoyed the quiz and the roses. You're special to me, and I cherish every moment with you." )
                    st.write("I cannnot explain how much I adore you and how much I want to be with you forever and ever")
                    st.title("THANK YOU FOR THE BEST YEAR AND MANY TO COME")
                    st.write("With love,\nYour Suhaib 💕")
                    st.write("[CLICK >](https://ibb.co/zXT8kCL)")
                    st.image("https://th.bing.com/th/id/OIP.aY08iW2g3h-IzlbJ0pcqHgHaHa?w=1080&h=1080&rs=1&pid=ImgDetMain")
                    st.write(f"\nYou answered {correct_answers} questions correctly. Shukriya!")

        else:
            st.write("")

    elif password:
        st.error("Incorrect password. Please try again.")

if __name__ == "__main__":
    main()
