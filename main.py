import queue
import random

# Inisialisasi playlist dan antrian lagu
songs_queue = queue.Queue()
playlist = []

def add_song(song):
    songs_queue.put(song)
    playlist.append(song)

def play_next_song():
    if not songs_queue.empty():
        next_song = songs_queue.get()
        print(f"Playing: {next_song}")
        playlist.remove(next_song)
    else:
        print("Playlist is empty")

def display_playlist():
    if playlist:
        print("Playlist:")
        for i, song in enumerate(playlist, start=1):
            print(f"{i}. {song}")
    else:
        print("Playlist is empty")

# def shuffle_playlist():
#     random.shuffle(playlist)

def fisher_yates_shuffle(playlist):
    n = len(playlist)
    for i in range(n - 1, 0, -1):
        j = random.randint(0, i)  # Pilih elemen secara acak
        playlist[i], playlist[j] = playlist[j], playlist[i]  # Tukar elemen

def shuffle_playlist():
    fisher_yates_shuffle(playlist)  # Menggunakan Fisher-Yates shuffle

def remove_song(song_name):
    if song_name in playlist:
        playlist.remove(song_name)
        print(f"Removed: {song_name}")
    else:
        print(f"{song_name} not found in the playlist")

def search_song(song_name):
    found_songs = [song for song in playlist if song_name.lower() in song.lower()]
    if found_songs:
        print(f"Found Songs:")
        for i, song in enumerate(found_songs, start=1):
            print(f"{i}. {song}")
    else:
        print(f"No songs found with '{song_name}' in the title.")

def main():
    while True:
        print("====================================")
        print(" ")
        display_playlist()
        print(" ")
        print("====================================")
        print("Options:")
        print("1. Add a song to the playlist")
        print("2. Play next song")
        print("3. Shuffle playlist")
        print("4. Remove a song from the playlist")
        print("5. Search for a song")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            song = input("Enter the song name: ")
            add_song(song)
            print(" ")
        elif choice == "2":
            play_next_song()
            print(" ")
        elif choice == "3":
            shuffle_playlist()
            print(" ")
        elif choice == "4":
            song_name = input("Enter the name of the song to remove: ")
            remove_song(song_name)
            print(" ")
        elif choice == "5":
            song_name = input("Enter the name of the song to search for: ")
            search_song(song_name)
            print(" ")
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()