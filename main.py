from time import sleep
from pynput.keyboard import Key, Controller
import discord


keyboard = Controller()



client = discord.Client()



TOKEN = "TYPE YOUR TOKEN HERE"#--------------------------------------------------------------------------------------


client.user = input("What is the name of the person that is using the bot (without tag and spaces) ")
client.usersname = "======[ ", client.user , "'s Adventure ]======"



@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))




@client.event
async def on_message(message):
    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel.name)



    if message.author == client.user:
        return

    if username == "DiscordRPG#0366":
#!adv
        if message.channel.name == "discord-rpg-1": #discord rpg deciding heal or pheal or adv
            print(user_message)
            if user_message[3] == "d":
                if user_message.split("!")[1] == client.usersname:

                    client.pethp = ""
                    client.petmaxhp = ""
                    client.index1 = 0
                    client.index2 = 0

                    client.playermaxhp = ""
                    client.playerhp = ""

                    #pet max hp
                    client.index1 = user_message.index("HP left")
                    client.index2= user_message.index("/")
                    for i in range(client.index2 + 1, client.index1):
                        if user_message[i] != ",":
                            client.petmaxhp = client.petmaxhp + user_message[i]
                    #pet max hp
                    #-----------------------------------
                    #pethp
                    client.index1 = user_message.index("/")
                    client.index2 = user_message.index("+ Pet Rock has ")
                    for i in range(client.index2 + 15, client.index1):
                        if user_message[i] != ",":
                            client.pethp = client.pethp + user_message[i]
                    #pethp
                    #---------------------------------------------------------------------------------------------
                    #playermaxhp
                    client.index1 = user_message.index("HP left.")
                    client.index2 = user_message.index("/",user_message.index("/")+2)
                    for i in range(client.index2 + 1, client.index1):
                        if user_message[i] != ",":
                            client.playermaxhp = client.playermaxhp + user_message[i]
                    #playermaxhp
                    # -----------------------------------
                    #playerhp
                    client.index1 = user_message.index("/", user_message.index("/") + 2)
                    client.index2 = user_message.index("o has ") +6
                    for i in range(client.index2, client.index1):
                        if user_message[i] != ",":#!adv

                            client.playerhp = client.playerhp + user_message[i]
                    #playerhp
                    await message.channel.send(f"{client.playerhp} = playerhp")
                    await message.channel.send(f"{client.playermaxhp} = playermaxhp")
                    await message.channel.send(f"{client.pethp} = pethp")
                    await message.channel.send(f"{client.petmaxhp} = petmaxhp")
                    print(user_message)







                    sleep(15)

                    if int(client.pethp) <= int(client.petmaxhp)/2: #pheal
                        sleep(7)
                        keyboard.press("#")
                        keyboard.release("#")

                        keyboard.press("!")
                        keyboard.release("!")

                        keyboard.press("p")
                        keyboard.release("p")

                        keyboard.press("h")
                        keyboard.release("h")

                        keyboard.press("e")
                        keyboard.release("e")

                        keyboard.press("a")
                        keyboard.release("a")

                        keyboard.press("l")
                        keyboard.release("l")

                        keyboard.press(" ")
                        keyboard.release(" ")

                        keyboard.press("5")
                        keyboard.release("5")

                        keyboard.press(Key.enter)
                        keyboard.release(Key.enter)


                    if int(client.playerhp) <= int(client.playermaxhp)/2:
                        sleep(7)

                        keyboard.press("#")
                        keyboard.release("#")

                        keyboard.press("!")
                        keyboard.release("!")

                        keyboard.press("h")
                        keyboard.release("h")

                        keyboard.press("e")
                        keyboard.release("e")

                        keyboard.press("a")
                        keyboard.release("a")
    #!adv

                        keyboard.press("l")
                        keyboard.release("l")

                        keyboard.press(" ")
                        keyboard.release(" ")

                        keyboard.press("5")#!forage

                        keyboard.release("5")

                        keyboard.press(Key.enter)
                        keyboard.release(Key.enter)



                    keyboard.press("#")
                    keyboard.release("#")

                    keyboard.press("!")
                    keyboard.release("!")

                    keyboard.press("a")
                    keyboard.release("a")

                    keyboard.press("d")
                    keyboard.release("d")

                    keyboard.press("v")
                    keyboard.release("v")

                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)





client.run(TOKEN)