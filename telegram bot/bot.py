# coding: utf-8

import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import pandas as pd
import os
PORT = int(os.environ.get('PORT', 5000))


#importing dataset
final = pd.read_csv('https://raw.githubusercontent.com/angelinakhatiwada/Emotion-Detection-in-Song-Lyrics/main/datasets/song_lyrics_labeled_with_classifier.csv',
                    index_col = 0)
final = final.drop(columns =['text', 'label', 'artists_initial'])
list_genres = final['genre'].unique().tolist()
list_emotions = final['emotion_pred'].unique().tolist()

#bot function
def bot(phrase):
    
    phrase = phrase.replace(" ", ", ") if "," not in phrase else phrase
    phrase = phrase.split(',')
    print(phrase)
    if len(phrase) < 2:
        return "Mmm, I don't know that genre or emotion, please try again. Example: Pop, anger                 To see the list of genres and emotions, please type /start"
    elif len(phrase) > 2:
        return "Please try again and separate genre and emotion with comma. Example: Punk rock, anger                 To see the list of genres and emotions, please type /start"
    else:
        genre, emotion = phrase
        genre = genre.strip()
        emotion = emotion.strip()
        
    matching_index_genre = [genre.lower() in x.lower() for x in list_genres]
    genre = "not found" if sum(matching_index_genre) == 0 else list_genres[matching_index_genre.index(True)]
    
    matching_index_emotion = [emotion.lower() in x.lower() for x in list_emotions]
    emotion = "not found" if sum(matching_index_emotion) == 0 else list_emotions[matching_index_emotion.index(True)]
 
    if genre == "not found" or emotion == "not found":
        return "Mmm, I don't know that genre or emotion, please try again. Example: Pop, anger                 To see the list of genres and emotions, please type /start"
    
   
    df = final[(final['genre'] == genre) & (final['emotion_pred'] == emotion)]
    
    nb_sample = min(5, df.shape[0])
    
    if nb_sample == 0:
        return "No songs found for this genre and emotion. To see the list of genres and emotions, please type /start"
    else:
        df = df.sample(nb_sample).sort_values(by='emotion_score', ascending=False)
    
    list_of_lines =[]
    for i in range(df.shape[0]): 
        line = (str(df.iloc[i, 0]) + '\n' +str(df.iloc[i, 1]) + '\n' + str(df.iloc[i, 2]) + '\n' + str(df.iloc[i, 3]) + '\n' + str(df.iloc[i, 4]) + '\n' + str(df.iloc[i, 7]))
        list_of_lines.append(line)
    
    emoticon = "😄" if emotion == "joy" else "😢" if emotion == "sadness" else "😨" if emotion == "fear" else "😡" if emotion == "anger" else "??"
    
    
    return (genre.upper() + "  "+emoticon+'\n\n' + ' \n\n'.join(list_of_lines) + ' \n\n' + 'To see the list of genres and emotions, please type /start')
        

#token
TOKEN = ""

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

#defining Telegram bot function

def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text("""Hi! To get a playlist of songs, you need to type a genre and an emotion    
🎼 Genres available: 
    Pop
    Hip-hop/Rap
    Folk
    Country
    R&B/Soul
    Jazz
    Blues
    Electronic/Dance
    Reggae
    Classic Rock
    Hard Rock
    Punk Rock
    Alternative Rock/Indie
    Metal
    
🙂 Emotions (chose whether you want to hear a happy or a sad song, etc.):
    Joy
    Anger
    Fear
    Sadness
    
An example to type: Pop, anger

Please, type genre first and then emotion in a single message. Thank you and enjoy 🎧
    
""")
    
def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def run_bot(update: Update, _: CallbackContext) -> None:
    """Reply to the user message."""
    phrase = update.message.text
    answer = bot(phrase)
    update.message.reply_text(answer)
    
def error(update: Update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)
    
def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # on non command i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, run_bot))
    
    # log all errors
    dispatcher.add_error_handler(error)
    
    # Start the Bot
    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
