import starting_screen_gui as gui_file #the main file

import sys
import gc
import json
import objectpath
import pandas as pd
from PIL import Image
import urllib
import requests
import numpy as np
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
from nltk.corpus import stopwords



def convert_datetime(timestamp_ms):
	return pd.to_datetime(timestamp_ms,unit='ms')
def convert_date(dateo):
	return dateo.date()
def get_month(date):
	return date.month
def get_year(date):
	return date.year

#Our .json file path
path_to_file =gui_file.path_to_file
#print(path_to_file)
with open(path_to_file,encoding='utf-8') as chat_file:
    chat_history = json.load(chat_file)


#Dataframe er main keys
chat_history_keys=[]
for keys in chat_history.keys():
	chat_history_keys.append(keys)

keys=chat_history_keys

#Name of the Members
FB_participants=pd.DataFrame(chat_history['participants'])	

#Keys of the Series of Nested Dataframe
FB_messages_ORIGINAL=pd.DataFrame(chat_history['messages'])	


#Picture keys that are NULL have content=N/A. So we are removing them
FB_messages=FB_messages_ORIGINAL.dropna(subset=['content']) #picture e content nai tai oigula out hoye gesilo


#new dataframe for bangla data decoded
new_messages=pd.DataFrame()

new_participants=FB_participants['name'].apply(lambda x : x.encode('raw_unicode_escape').decode('utf-8'))

new_messages['new_sender_name']=FB_messages_ORIGINAL['sender_name'].apply(lambda x : str(x).encode('raw_unicode_escape').decode('utf-8'))
new_messages['new_content'] = FB_messages_ORIGINAL['content'].apply(lambda x : str(x).encode('raw_unicode_escape').decode('utf-8')) 
new_messages['letter_count']=FB_messages_ORIGINAL['content'].apply(lambda s : len(str(s)))
new_messages['word_count']=FB_messages_ORIGINAL['content'].apply(lambda s : len(str(s).split(' ')))
new_messages['datetime']=FB_messages_ORIGINAL['timestamp_ms'].apply(lambda x: convert_datetime(x))


new_messages['month']=new_messages['datetime'].apply(lambda x: get_month(x))
new_messages['year']=new_messages['datetime'].apply(lambda x: get_year(x))
new_messages['weekday']=new_messages['datetime'].apply(lambda s : s.day_name())
new_messages['date']=new_messages['datetime'].apply(lambda x: convert_date(x))



#Date and time conversion
start_date =FB_messages_ORIGINAL['timestamp_ms'].iloc[-1].astype(str)
end_date =FB_messages_ORIGINAL['timestamp_ms'].iloc[0].astype(str)
start_date=convert_datetime(start_date)
end_date=convert_datetime(end_date)
duration=(end_date-start_date).days



#Messege Overviews Separated
F_B_messages_overview=FB_messages_ORIGINAL.count() 
F_B_messages_members=FB_participants.count() 

title=str(chat_history['title'])
#No of members
members=F_B_messages_members['name']

#Checking if attribute is present
if 'content' not in F_B_messages_overview:
	messages=0
else:
	messages=F_B_messages_overview['content']
if 'photos' not in F_B_messages_overview:
	photos=0
else:
	photos=F_B_messages_overview['photos']
if 'videos' not in F_B_messages_overview:
	videos=0
else:
	videos=F_B_messages_overview['videos']
if 'sticker' not in F_B_messages_overview:
	stickers=0
else:
	stickers=F_B_messages_overview['sticker']
if 'gifs' not in F_B_messages_overview:
	gifs=0
else:
	gifs=F_B_messages_overview['gifs']


#TOP messegers
sender_value_counts = FB_messages['sender_name'].value_counts()
if members>10:
	top_10_sender_value_counts =sender_value_counts.head(5)
else:
	top_10_sender_value_counts =sender_value_counts.head(members) # Number of messages per author for the top 10 most active authors



#Longest MSG
longest_msg_index=new_messages[['letter_count']].idxmax()
longest_msg=new_messages[['new_sender_name','letter_count']].iloc[longest_msg_index].astype(str)
name=longest_msg['new_sender_name'].to_string()
count=int(longest_msg_index['letter_count'])


#word count & letter count highest
total_word_count_grouped_by_sender = new_messages[['new_sender_name','word_count','letter_count']].groupby('new_sender_name').sum()
sorted_total_word_count_grouped_by_sender = total_word_count_grouped_by_sender.sort_values('word_count', ascending=False)
if members>10:
	top_10_sorted_total_word_count_grouped_by_sender = sorted_total_word_count_grouped_by_sender.head(5)
else:
	top_10_sorted_total_word_count_grouped_by_sender = sorted_total_word_count_grouped_by_sender.head(members)



#Active Weekdays
active_weekday_grouped_by_sender = new_messages[['new_content','weekday']].groupby('weekday').count()
sorted_active_weekday_grouped_by_sender = active_weekday_grouped_by_sender.sort_values('new_content', ascending=False)
seven_weekday_grouped_by_sender = sorted_active_weekday_grouped_by_sender.head(7)

top_days=seven_weekday_grouped_by_sender.index.tolist()



#Timeline of Chat 
timeline = new_messages[['new_content','date']].groupby('date').count()

plt.cla()

# Clear the current figure.
plt.clf()

# Closes all the figure windows.
plt.close('all')

gc.collect()





#WORDCLOUD
text=new_messages['new_content']
#print(text)
text = str(text)
wmask = np.array(Image.open("gui/images/purple.png"))
wordcloud = WordCloud(colormap='rainbow_r',background_color='black',mask=wmask, stopwords=['download','comments','comment','www','http','https','Link','ta','hoye','dike','diye','and','the','added','er','to','etay','hok']).generate(text)
image_colors = ImageColorGenerator(wmask) #

