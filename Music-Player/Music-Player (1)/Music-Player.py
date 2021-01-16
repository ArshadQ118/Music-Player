from tkinter import *
from mutagen.mp3 import MP3
import datetime
from tkinter.ttk import Progressbar
from pygame import mixer
from tkinter import filedialog

def playmusic():
    ad = audiotrack.get()
    mixer.music.load(ad)
    ProgressbarLabel.grid()
    root.mutebutton.grid()
    ProgressbarMusicLabel.grid()
    mixer.music.set_volume(0.4)
    ProgressbarVol['value'] = 40
    ProgressbarVolumeLabel['text'] = '40%'
    mixer.music.play()
    audioStatuclabel.configure(text='playing..')

    song = MP3(ad)
    totalSongLength = int(song.info.length)
    ProgressbarMusic['maximum'] = totalSongLength

    ProgressbarMusicEndTimeLabel.configure(text='{}'.format(
        str(datetime.timedelta(seconds=totalSongLength))))

    def ProgressbarMusicStick():
        CurrentSongLength = mixer.music.get_pos()//1000
        ProgressbarMusic['value'] = CurrentSongLength
        ProgressbarMusicStartTimeLabel.configure(text='{}'.format(
            str(datetime.timedelta(seconds=CurrentSongLength))))
        ProgressbarMusic.after(2, ProgressbarMusicStick)

    ProgressbarMusicStick()


def mutemusic():
    global currentvol
    root.mutebutton.grid_remove()
    root.unmutebutton.grid()
    currentvol = mixer.music.get_volume()
    mixer.music.set_volume(0)


def unmutemusic():
    global currentvol
    root.unmutebutton.grid_remove()
    root.mutebutton.grid()
    mixer.music.set_volume(currentvol)


def pausemusic():
    mixer.music.pause()
    root.PauseButton.grid_remove()
    root.ResumeButton.grid()
    audioStatuclabel.configure(text='Paused..')


def stopmusic():
    mixer.music.stop()
    audioStatuclabel.configure(text='Stoped..')


def musicurl():
    try:
        dd = filedialog.askopenfilename(initialdir='C:/Users/mohda/Downloads',
                                        title='Select Songs', filetype=(('*.mp3', '*.MP3'), ('WAV', '*.wav')))
    except:
        dd = filedialog.askopenfilename(title='Select Songs', filetype=(
            ('*.mp3', '*.MP3', '*.Mp3'), ('WAV', '*.wav')))

    audiotrack.set(dd)


def resumemusic():
    root.ResumeButton.grid_remove()
    root.PauseButton.grid()
    mixer.music.unpause()
    audioStatuclabel.configure(text='playing..')


def volup():
    vol = mixer.music.get_volume()
    mixer.music.set_volume(vol+0.05)
    ProgressbarVolumeLabel.configure(
        text='{}%'.format(int(mixer.music.get_volume()*100)))
    ProgressbarVol['value'] = mixer.music.get_volume()*100


def voldown():
    vol = mixer.music.get_volume()
    mixer.music.set_volume(vol-0.05)
    ProgressbarVolumeLabel.configure(
        text='{}%'.format(int(mixer.music.get_volume()*100)))
    ProgressbarVol['value'] = mixer.music.get_volume()*100


def createWidget():
    global audioStatuclabel, ProgressbarVolumeLabel, ProgressbarVol, ProgressbarLabel, ProgressbarMusicLabel, totalSongLength, ProgressbarMusic, ProgressbarMusicStartTimeLabel, ProgressbarMusicEndTimeLabel

    TrackLabel = Label(root, text='Select Track: ',
                       background='lightblue', font=('arial', 15, 'italic bold'))
    TrackLabel.grid(row=0, column=0, padx=20, pady=20)

    audioStatuclabel = Label(root, text='', background='lightblue', font=(
        'arial', 15, 'italic bold'), width=20)
    audioStatuclabel.grid(row=2, column=1)

    TrackLabelEntry = Entry(root, font=(
        'arial', 16, 'italic bold'), width=35, textvariable=audiotrack)
    TrackLabelEntry.grid(row=0, column=1, padx=20, pady=20)

    BrowseButton = Button(root, text='Search', bg='deeppink', font=(
        'arial', 13, 'italic bold'), width=20, bd=5, activebackground='purple4', command=musicurl)
    BrowseButton.grid(row=0, column=2, padx=20, pady=20)

    PlayButton = Button(root, text='Play', bg='green2', font=('arial', 13, 'italic bold'), width=20, bd=5,
                        activebackground='purple4', command=playmusic)
    PlayButton.grid(row=1, column=0, padx=20, pady=20)

    root.PauseButton = Button(root, text='Pause', bg='yellow', font=('arial', 13, 'italic bold'), width=20, bd=5,
                              activebackground='purple4', command=pausemusic)
    root.PauseButton.grid(row=1, column=1, padx=20, pady=20)
# ------------------------------------
    root.ResumeButton = Button(root, text='Resume', bg='yellow', font=('arial', 13, 'italic bold'), width=20, bd=5,
                               activebackground='purple4', command=resumemusic)
    root.ResumeButton.grid(row=1, column=1, padx=20, pady=20)
    root.ResumeButton.grid_remove()
# ------------------------------------
    root.mutebutton = Button(root, text='Mute', width=10, bg='yellow',
                             activebackground='purple4', bd=5, command=mutemusic)
    root.mutebutton.grid(row=3, column=3)
    root.mutebutton.grid_remove()

    root.unmutebutton = Button(root, text='UnMute', width=10, bg='yellow',
                               activebackground='purple4', bd=5, command=unmutemusic)
    root.unmutebutton.grid(row=3, column=3)
    root.unmutebutton.grid_remove()
# ------------------------------------
    VolumeUpButton = Button(root, text='VolumeUp', bg='blue', font=('arial', 13, 'italic bold'), width=20, bd=5,
                            activebackground='purple4', command=volup)
    VolumeUpButton.grid(row=1, column=2, padx=20, pady=20)

    StopButton = Button(root, text='Stop', bg='red', font=('arial', 13, 'italic bold'), width=20, bd=5,
                        activebackground='purple4', command=stopmusic)
    StopButton.grid(row=2, column=0, padx=20, pady=20)

    VolumeDownButton = Button(root, text='VolumeDown', bg='blue', font=('arial', 13, 'italic bold'), width=20, bd=5,
                              activebackground='purple4', command=voldown)
    VolumeDownButton.grid(row=2, column=2, padx=20, pady=20)

    ProgressbarLabel = Label(root, text='', bg='red')
    ProgressbarLabel.grid(row=0, column=3, rowspan=3, padx=20, pady=20)
    ProgressbarLabel.grid_remove()

    ProgressbarVol = Progressbar(
        ProgressbarLabel, orient=VERTICAL, mode='determinate', value=0, length=190)
    ProgressbarVol.grid(row=0, column=0, ipadx=5)

    ProgressbarVolumeLabel = Label(
        ProgressbarLabel, text='0%', bg='lightgray', width=3)
    ProgressbarVolumeLabel.grid(row=0, column=0)

# ------------------------------------------------------------------------
    ProgressbarMusicLabel = Label(root, text='', bg='red')
    ProgressbarMusicLabel.grid(row=3, column=0, columnspan=3, padx=20, pady=20)
    ProgressbarMusicLabel.grid_remove()

    ProgressbarMusicStartTimeLabel = Label(
        ProgressbarMusicLabel, text='0:00:0', bg='red', width=5)
    ProgressbarMusicStartTimeLabel.grid(row=0, column=0)

    ProgressbarMusicEndTimeLabel = Label(
        ProgressbarMusicLabel, text='0:00:0', bg='red')
    ProgressbarMusicEndTimeLabel.grid(row=0, column=2)

    ProgressbarMusic = Progressbar(
        ProgressbarMusicLabel, orient=HORIZONTAL, mode='determinate', value=0)
    ProgressbarMusic.grid(row=0, column=1, ipadx=350, ipady=3)

# ------------------------------------------------------------------------


root = Tk()
root.geometry('1100x500+50+50')
root.title('Music-Player')
root.iconbitmap('m.ico')
root.resizable(False, False)
root.configure(bg='lightblue')
ss = 'Music-Player'
audiotrack = StringVar()
currentvol = 0
count = 0
text = ''
totalSongLength = 0
SliderLabel = Label(root, text=ss, bg='lightblue',
                    font=('arial', 30, 'italic bold'))
SliderLabel.grid(row=4, column=0, padx=20, pady=20, columnspan=3)


def IntroLabel():
    global count, text
    if(count >= len(ss)):
        count = -1
        text = ''
        SliderLabel.configure(text=text)
    else:
        text = text+ss[count]
        SliderLabel.configure(text=text)
    count += 1
    SliderLabel.after(200, IntroLabel)


IntroLabel()
mixer.init()
createWidget()
root.mainloop()
