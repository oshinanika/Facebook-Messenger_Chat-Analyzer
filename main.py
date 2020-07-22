import chat_analytics_calculations as CHAT #Import the Chat file

import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import PIL
import numpy as np
from PIL import ImageTk,Image
from tkinter import *
import gc


root = Tk()
root.title('CHAT ANALYZER')

root.geometry('{}x{}'.format(1200, 700))
root.resizable(0,0)

image2 =PIL.Image.open("gui/images/holy.jpg")
background_image =PIL.ImageTk.PhotoImage(image2)

#print(CHAT.top_10_sender_value_counts)
lrg_font=20
mid_font=12
small_font=12


# create all of the main containers
top_frame = Frame(root, bg='#A7226E', width=1300)
center = Frame(root, bg='#DCEDC2', width=1300,padx=3)
btm_frame = Frame(root, bg='#2F9599', width=1300,padx=3, pady=3)
#btm_frame2 = Frame(root, bg='#FF8C94', width=450, height=60, pady=3)

# layout all of the main containers
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

top_frame.grid(row=0, sticky="ew")
center.grid(row=1, sticky="nsew")
btm_frame.grid(row=3, sticky="ew")
#btm_frame2.grid(row=4, sticky="ew")

# create the widgets for the top frame
model_label = Label(top_frame, text=CHAT.title,compound='center', font=('Consolas', 20,'bold'),fg='#F7DB4F', bg=top_frame.cget("bg"))

# layout the widgets in the top frame
model_label.pack(fill='x')

# create the center widgets
center.grid_rowconfigure(0, weight=1)
center.grid_columnconfigure(1, weight=1)


ctr_left = Frame(center, bg='#EC2049', width=430)
ctr_mid = Frame(center, bg='#F26B38', width=430, padx=3)
ctr_right = Frame(center, bg='#F26B38', width=430)

ctr_left.grid(row=0, column=0, sticky="ns")
ctr_mid.grid(row=0, column=1, sticky="nsew")
ctr_right.grid(row=0, column=2, sticky="ns")


#left frame er top 10 list
TOP_10_heading = Label(ctr_left,text='TOP MESSAGERS',bg=ctr_left.cget("bg"),font=('Consolas', lrg_font, "bold"))
TOP_10_list = Label(ctr_left, text=CHAT.top_10_sender_value_counts.to_string(),bg=ctr_left.cget("bg"), font=('Consolas', small_font), justify=LEFT, anchor='nw',borderwidth=0,compound="center",highlightthickness = 0)


TOP_10_heading.grid(row=0, columnspan=3)
TOP_10_list.grid(row=1, columnspan=3)

#mid frame er overview
model_label = Label(ctr_mid, text='GROUP OVERVIEW',bg=ctr_mid.cget("bg"), font=('Consolas', lrg_font,'bold'))
members_label = Label(ctr_mid, text='MEMBERS',bg=ctr_mid.cget("bg"), font=('Consolas', mid_font,'bold'))
members_info = Label(ctr_mid, text=CHAT.members,bg=ctr_mid.cget("bg"), font=('Consolas', small_font))
messages_label = Label(ctr_mid, text='MESSAGES',bg=ctr_mid.cget("bg"), font=('Consolas', mid_font,'bold'))
messages_info = Label(ctr_mid, text=CHAT.messages,bg=ctr_mid.cget("bg"), font=('Consolas', small_font))
photos_label = Label(ctr_mid, text='PHOTOS',bg=ctr_mid.cget("bg"), font=('Consolas', mid_font,'bold'))
photos_info = Label(ctr_mid, text=CHAT.photos,bg=ctr_mid.cget("bg"), font=('Consolas', small_font))
videos_label = Label(ctr_mid, text='VIDEOS',bg=ctr_mid.cget("bg"), font=('Consolas', mid_font,'bold'))
videos_info = Label(ctr_mid, text=CHAT.videos,bg=ctr_mid.cget("bg"), font=('Consolas', small_font))
gifs_label = Label(ctr_mid, text='GIFS',bg=ctr_mid.cget("bg"), font=('Consolas', mid_font,'bold'))
gifs_info = Label(ctr_mid, text=CHAT.gifs,bg=ctr_mid.cget("bg"), font=('Consolas', small_font))
stickers_label = Label(ctr_mid, text='STICKERS',bg=ctr_mid.cget("bg"), font=('Consolas', mid_font,'bold'))
stickers_info = Label(ctr_mid, text=CHAT.stickers,bg=ctr_mid.cget("bg"), font=('Consolas', small_font))

d_label = Label(ctr_mid, text='CHAT DURATION',bg=ctr_mid.cget("bg"), font=('Consolas', lrg_font,'bold'))
d_info = Label(ctr_mid, text=str(CHAT.duration)+" DAYS",bg=ctr_mid.cget("bg"), font=('Consolas', mid_font))


model_label.grid(row=0, columnspan=3)
members_label.grid(row=1, column=0)
members_info.grid(row=2, column=0)
messages_label.grid(row=1, column=1)
messages_info.grid(row=2, column=1)
photos_label.grid(row=1, column=2)
photos_info.grid(row=2, column=2)
videos_label.grid(row=4, column=0)
videos_info.grid(row=5, column=0)
gifs_label.grid(row=4, column=1)
gifs_info.grid(row=5, column=1)
stickers_label.grid(row=4, column=2)
stickers_info.grid(row=5, column=2)

d_label.grid(row=7, columnspan=3)
d_info.grid(row=8, column=1)


#wordcloud
wordc=plt.figure(figsize=(5,4), dpi=100)
wordc.patch.set_facecolor('xkcd:mint green')
#image coloring
plt.imshow(CHAT.wordcloud, interpolation="bilinear")
canvas = FigureCanvasTkAgg(wordc, ctr_right)
canvas.get_tk_widget().pack(fill='x')
plt.tight_layout(pad=0)
plt.axis("off")
plt.margins(x=0,y=0)
plt.title("WordCloud")
canvas.draw()
#plt.savefig('gui/images/www.png', bbox_inches='tight')


#graphs
my_colors = ['#A7226E','#EC2049','#F26B38','#F7DB4F']
graph_font_size='x-small'

#BAR
figure2 = plt.Figure(figsize=(4,4), dpi=100)
figure2.patch.set_facecolor(btm_frame.cget("bg"))
ax2 = figure2.add_subplot(111)
line2 = FigureCanvasTkAgg(figure2, btm_frame)
line2.get_tk_widget().pack(side=LEFT, fill='x')
CHAT.top_10_sorted_total_word_count_grouped_by_sender.plot(kind='bar', 
	ax=ax2, 
	color=my_colors,
	legend=False)
ax2.set_title('Word & Letter Count')
ax2.set_xlabel('Senders',rotation=90,fontsize=graph_font_size)
ax2.set_ylabel('Number of Words & Number of Letter',fontsize=graph_font_size, labelpad=16)
ax2.tick_params(axis ='x', rotation = 45,labelsize=graph_font_size)
ax2.set_facecolor('#F7DB4F')





#STICK
figure3 = plt.Figure(figsize=(4,4), dpi=100)
figure3.patch.set_facecolor(btm_frame.cget("bg"))
ax3 = figure3.add_subplot(111)
scatter3 = FigureCanvasTkAgg(figure3, btm_frame) 
scatter3.get_tk_widget().pack(side=RIGHT, fill='x')
ax3.legend() 
CHAT.timeline.plot(kind='bar', 
	legend=False, 
	ax=ax3,align='center', 
	width=1,color='#F26B38')
ax3.set_title('Timeline')
ax3.set_xlabel('Date',fontsize=graph_font_size)
ax3.tick_params(axis ='x', rotation=45)
ax3.locator_params(nbins=10, axis='x')
ax3.set_ylabel('Activity',fontsize=graph_font_size)
ax3.set_facecolor('#F7DB4F')




#PIE
figure4 = plt.Figure(figsize=(4,4), dpi=100)
figure4.patch.set_facecolor(btm_frame.cget("bg"))
ax4 = figure4.add_subplot(111)
line4 = FigureCanvasTkAgg(figure4, btm_frame)
line4.get_tk_widget().pack(side=RIGHT, fill='x')
my_explode = (0.1, 0, 0,0,0,0,0)
CHAT.seven_weekday_grouped_by_sender.plot.pie(subplots=True, 
	autopct='%1.1f%%', 
	startangle=15, 
	legend=False, 
	ax=ax4, 
	shadow = True, 
	colors=my_colors, 
	explode=my_explode)
ax4.set_title('Active Days of the Week')
ax4.set_ylabel("")
#ax4.set_xlabel('Weekdays',fontsize=graph_font_size)
ax4.axis('equal')


# Closes all the figure windows.
plt.close('all')


gc.collect()
root.mainloop()

''' A7226E   EC2049   F26B38   F7DB4F   2F9599'''


#A8E6CE   DCEDC2   FFD3B5   FFAAA6   FF8C94 

# FE4365   FC9D9A   F9CDAD   C8C8A9   83AF9B 