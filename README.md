# Pyfy - Spotify Player

A lightweight, customizable Spotify player built with Python and Tkinter. Control your Spotify playback with a simple and intuitive interface.

![Pyfy Screenshot](https://via.placeholder.com/300x300?text=Pyfy+Player+Screenshot)

## Features

- Play/Pause, Next, and Previous track controls
- Album art display
- Hover-based controls that appear when needed
- Custom application icon
- Secure API credential handling
- Single executable file for easy distribution

## Prerequisites

Before using Pyfy, you'll need:

1. A Spotify Premium account
2. Spotify Desktop app installed and running
3. Internet connection

## Getting Started

### For End Users

1. Download the latest `Pyfy.exe` from the [releases page](https://github.com/your-username/pyfy/releases)
2. Run the executable
3. The first time you run it, you'll be redirected to Spotify's authorization page
4. Log in to your Spotify account and approve the permissions
5. The app will automatically connect to your Spotify client

### For Developers

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git (for version control)

### Setting Up the Development Environment

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/pyfy.git
   cd pyfy
   ```

2. **Create and activate a virtual environment** (recommended)
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate
   
   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   - Create a `.env` file in the project root
   - Add your Spotify API credentials:
     ```
     SPOTIPY_CLIENT_ID=your_client_id
     SPOTIPY_CLIENT_SECRET=your_client_secret
     SPOTIPY_REDIRECT_URI=http://127.0.0.1:8888/callback
     ```
   - Replace `your_client_id` and `your_client_secret` with your actual Spotify Developer credentials

### Running the Application

```bash
python pyfy.py
```

### Building the Executable

To create a standalone executable:

1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```

2. Build the executable:
   ```bash
   pyinstaller --onefile --windowed --icon=pyfy.ico --name "Pyfy" pyfy.py
   ```

3. The executable will be created in the `dist` directory

### Project Structure

```
Pyfy/
├── pyfy.py           # Main application code
├── pyfy.ico          # Application icon
├── requirements.txt  # Python dependencies
└── README.md         # This file
```

## Acknowledgments

- [Spotipy](https://spotipy.readthedocs.io/) - The Spotify Web API wrapper for Python
- [Tkinter](https://docs.python.org/3/library/tkinter.html) - Python's standard GUI library
- [Pillow](https://python-pillow.org/) - Python Imaging Library

## Usage

- Hover over the application to show the control buttons
- Click the play/pause button to toggle playback
- Use the next/previous buttons to navigate tracks
- The window title shows the current track name
- The application automatically updates when the track changes
- The window title shows the current track name
- The application automatically updates when the track changes

## Troubleshooting

- **App won't start**: Make sure Spotify Desktop is running
- **Authentication issues**: Check your internet connection and API credentials
- **Missing features**: Ensure you've granted all necessary permissions during the first run

## Security Note

This application uses OAuth 2.0 for secure authentication with Spotify. Your credentials are never stored or transmitted to any server other than Spotify's.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
