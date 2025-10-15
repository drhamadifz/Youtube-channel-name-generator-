# Youtube channel name generator t
print ("welcome to the Youtubee channel name generator")
nickname = input ("What's your nickname ?\n")
subject = input ("What's your channel about ?\n")
print ("You could name your channel: ")
patterns = [
    "{nickname}'s {subject} zone",
    "{nickname} and the world of {subject}",
    "The {subject} lab by {nickname}",
    "{nickname} talks about {subject}"
]

for pattern in patterns:
    print(pattern.format(nickname=nickname, subject=subject))
