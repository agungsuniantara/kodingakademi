name = "Rani"
age = 13

name = input("What is your name? ")
print("Hello,", name)

age = int(input("How old are you? "))
if age < 13:
    print("Wow, you are still young!")
else:
    print("Keep up the spirit to learn!")

name = input("What is your name? ")
print("Hello,", name, "! Welcome to the Simple Chatbot.")

hobby = input("What is your hobby? ")
print("Wow,", hobby, "is an interesting hobby!")

name = input("What is your name? ")
if name.lower() == "agung":
    print("Hello, admin!")
else:
    print("Hello,", name)
    
name = input("Hello! What is your name? ")
print("Hi,", name, "! I am a simple chatbot.")
message = input("Is there anything you want to ask? ")
if message.lower() == "how are you":
    print("I'm good, thank you for asking!")
elif message.lower() == "what is your name":
    print("My name is SMP Chatbot.")
else:
    print("Sorry, I don't understand that question yet.")
    





