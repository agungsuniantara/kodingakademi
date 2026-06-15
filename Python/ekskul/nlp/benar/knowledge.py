# put KNOWLEDGE_BASE in here

def get_response(input):
    if input in KNOWLEDGE_BASE:
        return KNOWLEDGE_BASE[input]
    else:
        return "Sorry, I don't have information about that"

user = "what is an airplane"
response = get_response(user)

print("user : ", user)
print("bot : ", response)