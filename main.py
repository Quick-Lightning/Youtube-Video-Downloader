import tkinter
import pytube
from pytube import YouTube
root=tkinter.Tk()
root.geometry("426x254")
root.resizable(False, False)
root.title("Youtube Video Downloader")
yotube = tkinter.PhotoImage(file="youtube.png")
ytb = tkinter.Label(root, image=yotube)
ytb.place(x=4, y=4)

urltxt = tkinter.Text(root, height=2, width=14, font=('montserrat', 11))
urltxt.place(x=256, y=29)
urltxt.insert(1.0, "Video URL")
dwntxt = tkinter.Text(root, height=2, width=14, font=('montserrat', 11))
dwntxt.place(y=76, x=256)
dwntxt.insert(1.0, "Download Path")


def downloadVideo():
    vurl = urltxt.get("1.0", "end-1c")
    youtube = pytube.YouTube(vurl)
    youtube.streams.get_highest_resolution().download(dwntxt.get("1.0", "end-1c"))


down = tkinter.Button(root, text="Download Video", command=lambda: downloadVideo(), padx=5, pady=3,  width=11)
down.place(y=144, x=150)
root.mainloop()
