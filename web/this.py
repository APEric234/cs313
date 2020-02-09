from collections import deque

class Song:
    """ Contains a credit card that has two addressess"""
    def __init__(self):
        self.title = ""
        self.artist = ""


    def display(self):
        print(f"{self.title} by {self.artist}")

    def prompt(self):
        self.title=input("Enter the title: ")
        self.artist=input("Enter the artist: ")
def main():
    print("ran main")
    que = deque()
    loop = True
    while(loop):
        print("Options: ")
        print("1. Add a new song to the end of the playlist")
        print("2. Insert a new song to the beginning of the playlist")
        print("3. Play the next song")
        print("4. Quit")
        loopvar=input("Enter selection: ")
        print("")
        valid_in =[1,2,3,4]
        if not loopvar in valid_in:
            continue
        else:
            if loopvar == 4:
                loop=False
                print("goodbye")
                break
            elif loopvar ==3:
                if len(que) <1:
                    print("The playlist is currently empty.")
                    break
                else:
                    song = que.popleft()
                    print("Playing Song")
                    song.display()
            elif loopvar == 2:
                song = Song()
                song.prompt()
                que.appendleft(song)
            elif loopvar == 1:
                song = Song()
                song.prompt()
                que.append(song)

if __name__ == "__main_":
    main()
