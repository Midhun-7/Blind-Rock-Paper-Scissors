from gtts import gTTS
import pygame
import speech_recognition as sr
import random
import time
import os

# Voice output function using gTTS + pygame
def speak(text):
    print(f"SPEAKING: {text}")
    tts = gTTS(text=text, lang='en')
    filename = "temp.mp3"
    tts.save(filename)

    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

    pygame.mixer.quit()
    os.remove(filename)

# Voice input function
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 6500
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        command = r.recognize_google(audio, language='en-in')
        print(f"You said: {command}")
    except Exception:
        speak("Sorry, I could not understand. Please say that again.")
        return "none"
    return command.lower()

# Game logic
speak("Welcome to Voice Controlled Rock Paper Scissors!")
choice_list = ["rock", "paper", "scissor"]
computer_score = 0
player_score = 0
rounds_played = 0

while rounds_played < 3:
    speak("Rock Paper Scissors, shoot!")
    computer_move = random.choice(choice_list)
    player_move = take_command()

    if player_move not in choice_list:
        if player_move != "none":
            speak("Invalid move. Please say rock, paper, or scissor.")
        continue

    speak(f"You chose {player_move}.")
    speak(f"Computer chose {computer_move}.")

    if player_move == computer_move:
        speak("It's a draw!")
    elif (player_move == "rock" and computer_move == "scissor") or \
         (player_move == "paper" and computer_move == "rock") or \
         (player_move == "scissor" and computer_move == "paper"):
        player_score += 1
        speak("You win this round!")
    else:
        computer_score += 1
        speak("Computer wins this round!")

    rounds_played += 1
    speak(f"Current score. You: {player_score}. Computer: {computer_score}.")

# Final result
if player_score > computer_score:
    speak("Congratulations! You win the game!")
elif computer_score > player_score:
    speak("Sorry! Computer wins the game.")
else:
    speak("The game is a draw.")
