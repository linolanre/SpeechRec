import speech_recognition as sr
import nltk
from nltk.chat.util import Chat
import streamlit as st

# Load the chatbot algorithm
pairs = [
    [
        r"my name is (.*)",
        ["Hello AI, How are you today?",]
    ],
    [r"How do I set up an OPay merchant account?",
    ["It's really easy! Go to Google Play and download OPay. Then, follow the instructions to register your account."]],

    [r"What documents are required to complete my registration?",
     ["BVN,UTILITY BILLS,NIN AND 1 PASSPOSRT"]],

    [r"What do I do after registering as an OPay merchant?",["Start Sending and Receiving Money"]],
    [r"Is there a limit on the maximum transaction amount for a merchant?",["You can receive and send up to 5 million Naira daily as an OPay merchant."]],
    [r"bye|Goodbye",["Goodbye! Have a great day!"]],
    [r"How are you?",["Am doing great, How may i be of service to you Today!"]],
    [r"What is the largest land animal?",["The African Elephant is the largest land animal."]],
    [r"How many continents are there?",["There are seven continents: Africa, Antarctica, Asia, Europe, North America, Australia (Oceania), and South America."]],
    [r"What is the largest ocean in the world?", ["The Pacific Ocean is the largest ocean in the world."]],
    [r" How many planets are there in our solar system?", ["There are eight planets in our solar system: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, and Neptune."]],
    [r"What is the tallest mountain in the world?", ["Mount Everest is the tallest mountain in the world."]],
    [r"Who painted the Mona Lisa?", ["The Mona Lisa was painted by Leonardo da Vinci."]],
    [r"What is the national bird of Australia?", ["The national bird of Australia is the Emu."]],
    [r"What is the speed of light?", ["The speed of light in a vacuum is approximately 299,792 kilometers per second (186,282 miles per second)."]],




    # Add more patterns and responses here
]

chatbot = Chat(pairs)

# Function to transcribe speech into text using speech recognition
def transcribe_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Listening...")
        audio = r.listen(source)
    try:
        st.write("Transcribing...")
        text = r.recognize_google(audio)
        st.write("You said:", text)
        return text
    except sr.UnknownValueError:
        st.write("Sorry, I could not understand your speech.")
    except sr.RequestError:
        st.write("Sorry, there was an issue with the speech recognition service.")

# Function to generate a response from the chatbot
def get_chatbot_response(user_input):
    return chatbot.respond(user_input)

# Streamlit app
def main():
    st.title("Speech-Enabled ChatBot By LinoLanre")
    st.sidebar.image("pngwing.com (3).png")
    st.markdown('''<style> [theme] base="dark"primaryColor="#b39696" backgroundColor="#27374D" textColor="#26dc40" font="serif"</style> ''', unsafe_allow_html=True)


    # User input method selection
    input_method = st.radio("Select input method:", ("Text", "Speech"))

    if input_method == "Text":
        user_input = st.text_input("User Input:")
        if st.button("Submit"):
            response = get_chatbot_response(user_input)
            st.text_area("Chatbot Response:", value=response)

    elif input_method == "Speech":
        st.write("Please ensure you have a microphone connected to your device.")
        if st.button("Start Recording"):
            user_input = transcribe_speech()
            response = get_chatbot_response(user_input)
            st.text_area("Chatbot Response:", value=response)

if __name__ == "__main__":
    nltk.download("punkt")  # Download the necessary NLTK data
    main()
