<div align="center">
  <h1>🎵 Pyfy - Spotify Player</h1>
  
  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
  [![Latest Release](https://img.shields.io/github/v/release/zboni2/PyFy-Spotify-Player?label=latest%20version)](https://github.com/zboni2/PyFy-Spotify-Player/releases/latest)
  
  A lightweight, customizable Spotify player built with Python and Tkinter. Control your Spotify playback with a simple and intuitive interface.
  
  [![Download Now](https://img.shields.io/badge/Download-Now-brightgreen?style=for-the-badge&logo=github&logoColor=white)](https://github.com/zboni2/PyFy-Spotify-Player/releases/latest/download/Pyfy.exe)
</div>

## Features

- **Playback Controls** - Play, pause, skip tracks, and control volume
- **Album Art** - Displays current track's album artwork
- **Simple UI** - Clean, hover-based controls that appear when needed
- **Secure** - Uses OAuth 2.0 for secure Spotify authentication
- **Portable** - Single executable file, no installation required
- **Fast & Lightweight** - Built for performance with minimal resource usage

## Quick Start

### Prerequisites
1. **Spotify Premium** account
2. **Spotify Desktop** app installed and running
3. **.env file** with your Spotify API credentials (see setup below)

### Setup .env File
1. Create a file named `.env` in the same folder as the executable
2. Add your Spotify API credentials:
   ```
   SPOTIPY_CLIENT_ID=your_client_id_here
   SPOTIPY_CLIENT_SECRET=your_client_secret_here
   SPOTIPY_REDIRECT_URI=http://127.0.0.1:8888/callback
   ```
3. Save the file

### Running the Application
1. **Download** the latest [Pyfy.exe](https://github.com/zboni2/PyFy-Spotify-Player/releases/latest/download/Pyfy.exe)
2. **Run** the executable
3. **Authorize** with your Spotify account when prompted
4. **Enjoy** controlling your music!

> **Note**: You'll need a **Spotify Premium** account to use this application.

## System Requirements

- Windows 10/11 (64-bit)
- Spotify Desktop app installed and running
- Internet connection
- [.NET Framework 4.7.2 or later](https://dotnet.microsoft.com/download/dotnet-framework) (usually pre-installed on Windows 10/11)

## For Developers

### Prerequisites

- Python 3.8+
- pip (Python package manager)
- Git (for version control)

### For Developers

#### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git (for version control)

#### Setting Up the Development Environment

1. **Clone the repository**
   ```bash
   git clone https://github.com/zboni2/PyFy-Spotify-Player.git
   cd PyFy-Spotify-Player
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

This project is licensed under the MIT License - see the [LICENSE](https://github.com/zboni2/PyFy-Spotify-Player/blob/main/LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
