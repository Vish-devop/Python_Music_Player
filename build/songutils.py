from pygame import *
from tkinter import filedialog

songlist=[] #this is been defined for storing the songs.
songIndex=-1

# C:\Users\Vishal\PycharmProjects\Music Player\venv\Lib\site-packages\pygame\examples\data\house_lo.ogg

def loadsingle():
    global songIndex
    path=filedialog.askopenfilename()
    songlist.append(path)
    songIndex+=1
    mixer.init()
    mixer.music.load(songlist[songIndex])
    print(songIndex)
    print(songlist[songIndex])


def play():
    # in-oder to check whether the music is played for the first time, or it's already played, we need to check it position.
    # Thus, we used get_pos() -> which helped in getting the position of the music.

    '''
    now, I'll check the condition for pause - and resume of the song.
    Now, if my get_pos() is greater than 0, which means the song will be played from the position the song got paused.
    else:
    it would be played from beginning. (usually, this happens on the value-> (-1)
    '''
    if mixer.music.get_pos()>0:
        mixer.music.unpause()
    else:
        mixer.music.play()


def pause():
    mixer.music.pause()


def stop():
    mixer.music.stop()

def LoadPlaylist():
    global songIndex

    songlist.clear()
    songIndex=0
    filePaths=filedialog.askopenfilenames()
    for fileName in filePaths:
        songlist.append(fileName)
    mixer.init()
    mixer.music.load(songlist[songIndex])
    mixer.music.play()
    print(songlist)

def nextSong():
     global songIndex
     songIndex=songIndex+1
     if songIndex>=len(songlist):
         songIndex=0
     mixer.music.load(songlist[songIndex])
     mixer.music.play()
def previousSong():
    global songIndex
    songIndex = songIndex + 1
    if songIndex <0:
        songIndex=len(songlist)-1
    mixer.music.load(songlist[songIndex])
    mixer.music.play()


# if __name__ == '__main__':
#     while True:
#         print("1.Load Single 2.Play 3.Pause 4.Stop 5.Load Playlist 6. next song 7. previous song")
#         # Taking input from user
#         ch = int(input(""))
#         if ch == 1:
#             loadsingle()
#         elif ch == 2:
#             play()
#         elif ch == 3:
#             pause()
#         elif ch == 4:
#             stop()
#         elif ch==5:
#             LoadPlaylist()
#         elif ch==6:
#             nextSong()
#         elif ch==7:
#             previousSong()
