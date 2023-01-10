from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")


link = input("Enter the YouTube video URL: ")
choice = str(input(f"Do you want download '{YouTube(link).title}'? Y or N: "))

if choice == "Y" or choice == "y":
    Download(link)
    
else:
    print("download cancelled")
