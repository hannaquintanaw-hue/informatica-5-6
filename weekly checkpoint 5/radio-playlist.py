def main():
    playlist = ["Boston", "Dracula", "I Knew It, I Knew You", "hate that i made you love me", "Risk It All"]
    playlist.append("Be By You")

    playlist.insert(0,"Bohemian Rhapsody")

    playlist.pop(4)
    print(playlist)
    print(playlist.index("Risk It All"))
    print(f"Number of sings in playlist: {len(playlist)}")
    playlist.reverse()
    print(playlist)
    playlist.sort()
    print(playlist)

    #challenge
    repeat = len(playlit)
    while repeat > 0:
        print(playlist)
        song = playlist[0]
        playlist.pop(0)
        playlist.append(song)
        repeat -=1
        time.sleep(3)

if __name__ == "__main__":
    main()
