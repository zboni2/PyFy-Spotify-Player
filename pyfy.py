import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO
import os
import sys
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Load environment variables from .env file
load_dotenv()

# Get Spotify API credentials from environment variables
SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
SPOTIPY_REDIRECT_URI = os.getenv('SPOTIPY_REDIRECT_URI')

# Show an error message in a dialog and exit
def show_error_and_exit(message):
    try:
        import tkinter as tk
        from tkinter import messagebox
        root = tk.Tk()
        root.withdraw()  # Hide the root window
        messagebox.showerror("Error", message)
        root.destroy()
    except Exception as e:
        print(f"Error: {message}")
        print(f"Additional error showing dialog: {str(e)}")
    finally:
        sys.exit(1)

# Validate credentials
if not all([SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI]):
    error_msg = (
        "Missing Spotify API credentials in .env file\n\n"
        "Please create a .env file with the following variables:\n"
        "SPOTIPY_CLIENT_ID=your_client_id\n"
        "SPOTIPY_CLIENT_SECRET=your_client_secret\n"
        "SPOTIPY_REDIRECT_URI=your_redirect_uri"
    )
    show_error_and_exit(error_msg)

class SpotifyPlayer:
    def __init__(self, root):
        self.root = root
        self.current_track_id = None
        self.setup_spotify()
        self.setup_ui()
        self.setup_bindings()
        self.update_song()
        
    # Initialize Spotify API client from environment variables
    def setup_spotify(self):
        try:
            self.spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(
                client_id = SPOTIPY_CLIENT_ID,
                client_secret = SPOTIPY_CLIENT_SECRET,
                redirect_uri = SPOTIPY_REDIRECT_URI,
                scope="user-read-playback-state,user-modify-playback-state"
            ))
        except Exception as e:
            print(f"Error initializing Spotify client: {str(e)}")
            input("Press Enter to exit...")
            sys.exit(1)
        
    # Initialize the user interface
    def setup_ui(self):
        
        # Main window setup
        self.root.title("Pyfy - Spotify Player")
        self.root.geometry("300x300")
        self.root.resizable(False, False)

        # Canvas for album
        self.canvas = tk.Canvas(self.root, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        # Controls frame (hidden by default)
        self.setup_controls()
        
    # Initialize playback controls  
    def setup_controls(self):
        
        # Main controls container
        self.controls = tk.Frame(self.root, bg="#E6E6FA")
        
        # Button container for layout
        btn_container = tk.Frame(self.controls, bg="#E6E6FA")
        btn_container.pack(expand=True, fill='x', padx=20, pady=5)

        # Previous track button
        tk.Button(btn_container, text="⏮", command=self.prev_track, 
                 width=5).pack(side="left", padx=10)

        # Play/Pause button
        center_frame = tk.Frame(btn_container, bg="#E6E6FA")
        center_frame.pack(side="left", expand=True)
        self.play_btn = tk.Button(center_frame, text="▶️", 
                                 command=self.toggle_play_pause, width=5)
        self.play_btn.pack(side="left", padx=10)

        # Next track button
        tk.Button(btn_container, text="⏭", command=self.next_track, 
                 width=5).pack(side="right", padx=10)

    # Set up event bindings
    def setup_bindings(self):
        self.root.bind("<Enter>", self.show_controls)
        self.root.bind("<Leave>", lambda e: self.root.after(150, self.maybe_hide))

    # Toggle between play and pause
    def toggle_play_pause(self):
        try:
            current = self.spotify.current_playback()
            if current and current.get('is_playing'):
                self.spotify.pause_playback()
            else:
                self.spotify.start_playback()
        finally:
            self.root.after(500, self.update_song)

    # Skip to next track
    def next_track(self):
        self.spotify.next_track()
        self.root.after(250, self.update_song)

    # Go to previous track
    def prev_track(self):
        self.spotify.previous_track()
        self.root.after(250, self.update_song)

    # Show the controls by hovering over the window
    def show_controls(self, event=None):
        if not self.controls.winfo_ismapped():
            self.controls.pack(side="bottom", fill="x")

    # Hide the controls after a short delay
    def hide_controls(self):
        if self.controls.winfo_ismapped():
            self.controls.pack_forget()

    # Check if mouse is still over the window before hiding controls
    def maybe_hide(self):
        try:
            x, y = self.root.winfo_pointerxy()
            w = self.root.winfo_containing(x, y)
            if not w or w.winfo_toplevel() != self.root:
                self.hide_controls()
        except Exception:
            self.hide_controls()
            
    # Update the currently playing track info   
    def update_song(self):
        try:
            current = self.spotify.current_playback()
        except Exception:
            current = None

        if current and current.get('item'):
            track = current['item']
            track_id = track.get('id')
            
            # Update play/pause button
            if 'is_playing' in current:
                self.play_btn.config(text="⏸" if current['is_playing'] else "▶️")

            # Update track info if changed
            if track_id != self.current_track_id:
                self.update_track_info(track)
                self.current_track_id = track_id
        else:
            self.play_btn.config(text="▶️")

        self.root.after(2000, self.update_song)

    # Update track, title and album
    def update_track_info(self, track):
        title = track.get('name', 'Spotify')
        self.root.title(title)
        
        images = track.get('album', {}).get('images', [])
        if images:
            try:
                thumbnail_url = images[0]['url']
                response = requests.get(thumbnail_url)
                img_data = Image.open(BytesIO(response.content)).resize((300, 300))
                bg_img = ImageTk.PhotoImage(img_data)
                self.canvas.create_image(0, 0, anchor="nw", image=bg_img)
                self.canvas.bg_img = bg_img
            except Exception as e:
                print(f"Error loading image: {e}")

def main():
    root = tk.Tk()
    app = SpotifyPlayer(root)
    root.mainloop()

if __name__ == "__main__":
    main()