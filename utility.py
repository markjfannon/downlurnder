import os
from dotenv import load_dotenv
from mutagen.easyid3 import EasyID3

load_dotenv()

#Counts how many MP3 files have been uploaded as attachments, returns the value
def count_mp3(attachments):
    count = 0

    for attachment in attachments:
        if attachment.content_type == "audio/mpeg":
            count += 1

    return count

#Downloads any attachments associated with a message
async def retrieve_attachments(message, args):
    mp3_count = count_mp3(message.attachments)

    #Can't download MP3s if there aren't any given!
    if mp3_count == 0:
        await message.channel.send("No MP3 files have been provided, so not going to download")
        return

    #If the amount of alt filenames and MP3s provided do not match, downloads will go ahead but retain original filenames
    if len(args) > 0 and len(args) != mp3_count:
        await message.channel.send("Amount of alternative filenames does not match count of MP3s uploaded. For safety, the filenames and metadata of \
any attached audio files will not be changed")
        for attachment in message.attachments:
            if attachment.content_type == "audio/mpeg":
                file = os.path.join(os.getenv("SAVE_PATH")+attachment.filename)
                await attachment.save(file)

    #If no alt filenames are provided, download but retain original filenames
    elif len(args) == 0:
        for attachment in message.attachments:
            if attachment.content_type == "audio/mpeg":
                file = os.path.join(os.getenv("SAVE_PATH")+attachment.filename)
                await attachment.save(file)
    
    #If alt filenames are provided and match the amount of MP3s attached, they will be downloaded and renamed in order
    else:
        x = 0
        y = 0
        while x < len(message.attachments):
            if message.attachments[x].content_type == "audio/mpeg":
                #Checks if a .mp3 extension needs to be added to the new filename
                if args[y][-4:] == ".mp3":
                    fname = args[y]
                else:
                    fname = args[y]+".mp3"

                #Save 'n' rename
                file = os.path.join(os.getenv("SAVE_PATH")+fname)
                await message.attachments[x].save(file)
                audio = EasyID3(file)
                audio["title"] = args[y]
                audio.save()
                y += 1
            x += 1

    await message.channel.send("All files succesfully downloaded")