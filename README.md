# DownlURNder
Python-based Discord tool to allow downloading and automatic renaming of MP3 files submitted

## Purpose
This was designed for [Univeristy Radio Nottingham (URN)](https://urn1350.net), hence the silly punny name. Allows ident tracks to be easily submitted via Discord and automatically saved into the correct directory for playout. It also allows renaming of these tracks, which is carried out by both renaming the file and the id3 metadata. 

## Setup
Run `pip3 install -r requirements.txt
Run `python3 main.py`

## Operation
Bot token, prefix and save path info should be stored in a .env file and set to the user's needs.

Only one command currently exists - the main download tool which is just called `d`. This should be called in a message containing attachments of .mp3 file type for it to work properly. If no other arguments are provided, the file(s) will be downloaded to the preset path and have the same name as the original file. If the user desires to **rename** the files, then alternative filenames can be provided in the order of the attachments. The download function has been created in such away that allows the alternative filenames to be provided with or without the .mp3 extension on the end - either way it'll save as a .mp3. If no attachments at all have been provided, a message will be sent back highlighting this. The same will happen if only non-mp3 attachments are given. 

If the download is complete, a success message gets sent back.

## To do
- Better logging!
- Better help/debugging
- Perhaps support for a wider range of formats
