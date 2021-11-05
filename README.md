# Emotion-Detection-in-Song-Lyrics

### Part 1: 
**WASSA-2017 Shared Task on Emotion Intensity (EmoInt)**: training, development and test sets are combined into one dataset for model training and evaluation. \
Dataset consists of tweets with four emotion categories such as anger, fear, sadness and joy. \
*Please, see Tweets Dataset.ipynb*

### Part 2: 
**Collecting songs lyrics along with song metadata using Genius API**. 40 songs are annotated manually for emotions.\
*Please, see Song lyrics dataset with Genius API.ipynb*

### Part 3: 
**Emotion classification**: text preprocessing, feature extraction, model training, evaluation and application to the song lyrics dataset. \
Logistic Regression, Support Vector Machine, Stochastic Gradient Descent Classier, LSTM neural network classification models are applied. \
Google Colab was used to run the models. \
*Please, see Emotion_classification.ipynb*

### Part 4: 
**Telegram bot is built to provide users a playlist of 5 songs** given the input genre and emotion. Chatbot is hosted on Heroku service which makes it available 24/7.\
*Please, see telegram bot/bot.py*

To find and use the Telegram Bot, please follow the instructions:
 1.  Install and open Telegram messenger (mobile or web version);
 2.  Find  the  bot  by  username  (Botticelli  or  @botti_cielo_bot)  in  the  in-app search bar and select the bot from the list;
 3.  Start a conversation with Botticelli bot and follow the commands.






