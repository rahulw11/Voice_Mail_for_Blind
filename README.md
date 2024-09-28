**VOICE MAIL FOR BLIND**

This Python project allows Blind persons to send emails through voice commands. Utilizing the speech_recognition and pyttsx3 libraries, the program listens for user input, processes it into text, and sends an email via Gmail SMTP. It can be extended for further functionality, making it a useful tool for hands-free email communication.


**Features**

Voice Input: The user provides the recipient's name, email subject, and message content through voice commands using Google's Speech Recognition API.
Voice Output: The system responds back using text-to-speech (TTS) for confirmation or next actions, providing a conversational experience.
Email Sending: Sends emails via the Gmail SMTP server after successfully capturing the voice commands.
Loop Functionality: After sending one email, the system asks if the user wants to send more emails and continues accordingly.



**Technologies Used**

Python: The main language used to develop the application.
smtplib: Python’s built-in library to send emails via SMTP.
speech_recognition: Python library to recognize and convert voice commands into text.
pyttsx3: Python text-to-speech conversion library, used to give audio responses to the user.
EmailMessage: To structure and send the email.


**How It Works**

1. The system first asks for the recipient’s name using text-to-speech.
2. It listens to the user's voice input and matches the name with an entry in the email_list dictionary.
3. Next, it prompts the user for the email subject and the message content.
4. After receiving all the required information, the program uses Gmail's SMTP server to send the email.
5. Once the email is sent, the system confirms the action and asks if the user wants to send another email.
