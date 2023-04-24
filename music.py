from tkinter import *
from tkinter import messagebox
import mysql.connector


# Create a connection to the database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="test",
  database="music"
)

# Create the songs table if it doesn't exist
cursor = mydb.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS songs (id INT AUTO_INCREMENT PRIMARY KEY, song_name VARCHAR(255), artist_name VARCHAR(255), album_name VARCHAR(255), length VARCHAR(255))")

# Create the playlists table if it doesn't exist
cursor.execute("CREATE TABLE IF NOT EXISTS playlists (id INT AUTO_INCREMENT PRIMARY KEY, playlist_name VARCHAR(255))")

# Create the playlist_songs table if it doesn't exist
cursor.execute("CREATE TABLE IF NOT EXISTS playlist_songs (id INT AUTO_INCREMENT PRIMARY KEY, playlist_id INT, song_id INT, FOREIGN KEY (playlist_id) REFERENCES playlists(id), FOREIGN KEY (song_id) REFERENCES songs(id))")

# Create the window
window = Tk()
window.title("Song Manager")

# Create labels and entry fields for adding songs
song_name_label = Label(window, text="Song Name:")
song_name_label.grid(row=0, column=0)
song_name_entry = Entry(window)
song_name_entry.grid(row=0, column=1)

artist_name_label = Label(window, text="Artist Name:")
artist_name_label.grid(row=1, column=0)
artist_name_entry = Entry(window)
artist_name_entry.grid(row=1, column=1)

album_name_label = Label(window, text="Album Name:")
album_name_label.grid(row=2, column=0)
album_name_entry = Entry(window)
album_name_entry.grid(row=2, column=1)

# Create function to add songs to the database
def add_song():
    song_name = song_name_entry.get()
    artist_name = artist_name_entry.get()
    album_name = album_name_entry.get()
    length = length_entry.get()

    cursor = mydb.cursor()
    sql = "INSERT INTO songs (song_name, artist_name, album_name, length) VALUES (%s, %s, %s, %s)"
    values = (song_name, artist_name, album_name, length)
    cursor.execute(sql, values)
    mydb.commit()
    messagebox.showinfo("Success", "Song added to database successfully")

# Create function to remove songs from the database
def remove_song():
    song_name = remove_song_entry.get()

    cursor = mydb.cursor()
    sql = "DELETE FROM songs WHERE song_name = %s"
    value = (song_name,)
    cursor.execute(sql, value)
    mydb.commit()

    if cursor.rowcount == 0:
        messagebox.showerror("Error", "Song not found in database")
    else:
        messagebox.showinfo("Success", "Song removed from database successfully")
        
def display_all_songs():
    # get all the songs from the database
    cursor = mydb.cursor()
    cursor.execute("SELECT song_name, artist_name FROM songs")
    all_songs = cursor.fetchall()
    
    # display each song in a message box
    songs_text = ""
    for song in all_songs:
        songs_text += f"{song[0]} by {song[1]}\n"
    if songs_text:
        messagebox.showinfo("All Songs", songs_text)
    else:
        messagebox.showwarning("No Songs", "There are no songs in the database.")

def print_playlists():
    # fetch all the playlists from the database
    cursor.execute("SELECT * FROM playlists")
    playlists = cursor.fetchall()
    # iterate over the playlists
    for playlist in playlists:
        print(f"\n{playlist[1]}:")
        # fetch all the songs in the playlist
        cursor.execute(f"SELECT * FROM songs WHERE playlist_id={playlist[0]}")
        songs = cursor.fetchall()
        # iterate over the songs and print them as bullet points
        for song in songs:
            print(f"• {song[1]}")

# function to check for duplicate playlists and songs
def check_duplicates(playlist_name, song_name):
    # check if the playlist already exists
    cursor.execute(f"SELECT * FROM playlists WHERE name='{playlist_name}'")
    playlist = cursor.fetchone()
    if playlist:
        print(f"Playlist '{playlist_name}' already exists.")
        return True
    # check if the song already exists in the same playlist
    cursor.execute(f"SELECT * FROM songs WHERE name='{song_name}' AND playlist_id={playlist[0]}")
    song = cursor.fetchone()
    if song:
        print(f"Song '{song_name}' already exists in the '{playlist_name}' playlist.")
        return True
    return False

# Create function to create playlists in the database
def create_playlist(name):
    if check_duplicates(name, ""):
        return
    # insert the new playlist into the database
    sql = "INSERT INTO playlists (name) VALUES (%s)"
    val = (name,)
    cursor.execute(sql, val)
    mydb.commit()
    print(f"Playlist '{name}' added successfully.")

    messagebox.showinfo(f"Playlist '{name}' added successfully.")
    
# Create function to add songs to playlists in the database
def add_to_playlist():
    song_name = add_to_playlist_entry.get()
    playlist_name = playlist_name_entry.get()

    cursor = mydb.cursor()

    # Get the song ID
    sql = "SELECT id FROM songs WHERE song_name = %s"
    value = (song_name,)
    cursor.execute(sql, value)
    song_id = cursor.fetchone()[0]

    # Get the playlist ID
    sql = "SELECT id FROM playlists WHERE playlist_name = %s"
    value = (playlist_name,)
    cursor.execute(sql, value)
    playlist_id = cursor.fetchone()[0]

    # Check if the song is already in the playlist
    sql = "SELECT * FROM playlist_songs WHERE song_id = %s AND playlist_id = %s"
    values = (song_id, playlist_id)
    cursor.execute(sql, values)
    if cursor.fetchone():
        messagebox.showerror("Error", "Song already in playlist")
        return

    # Add the song to the playlist
    sql = "INSERT INTO playlist_songs (playlist_id, song_id) VALUES (%s, %s)"
    values = (playlist_id, song_id)
    cursor.execute(sql, values)
    mydb.commit()
    messagebox.showinfo("Success", "Song added to playlist successfully")

length_label = Label(window, text="Length:")
length_label.grid(row=3, column=0)
length_entry = Entry(window)
length_entry.grid(row=3, column=1)

add_song_button = Button(window, text="Add Song", command=add_song)
add_song_button.grid(row=4, column=0)

# Create labels and entry fields for removing songs
remove_song_label = Label(window, text="Song Name:")
remove_song_label.grid(row=5, column=0)
remove_song_entry = Entry(window)
remove_song_entry.grid(row=5, column=1)

remove_song_button = Button(window, text="Remove Song", command=remove_song)
remove_song_button.grid(row=6, column=0)

# Create labels and entry fields for creating playlists
playlist_name_label = Label(window, text="Playlist Name:")
playlist_name_label.grid(row=7, column=0)
playlist_name_entry = Entry(window)
playlist_name_entry.grid(row=7, column=1)

create_playlist_button = Button(window, text="Create Playlist", command=create_playlist)
create_playlist_button.grid(row=8, column=0)

# Create labels and entry fields for adding songs to playlists
add_to_playlist_label = Label(window, text="Song Name:")
add_to_playlist_label.grid(row=9, column=0)
add_to_playlist_entry = Entry(window)
add_to_playlist_entry.grid(row=9, column=1)

add_to_playlist_label = Label(window, text="Playlist Name:")
add_to_playlist_label.grid(row=10, column=0)
add_to_playlist_entry_2 = Entry(window)
add_to_playlist_entry_2.grid(row=10, column=1)

add_to_playlist_button = Button(window, text="Add to Playlist", command=add_to_playlist)
add_to_playlist_button.grid(row=11, column=0)

display_all_songs_button = Button(window, text="Display All Songs", command=display_all_songs)
display_all_songs_button.grid(row=12, column=0)



# Run the window
window.mainloop()

