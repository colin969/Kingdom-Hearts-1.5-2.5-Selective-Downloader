# Kingdom Hearts 1.5 + 2.5 Selective Downloader (Steam)

Python script which uses Depot Downloader to download only the games or movies from the collection you wish to use:

| Game      | w/ Full Quality Movie Size | w/ Compressed Movie Size |
| ------------- | ------------- | ------------- |
| Kingdom Hearts 1 | 10.3 GB | 9 GB |
| Re:Chain of Memories | 10.3 GB | 5.3 GB |
| Kingdom Hearts 2 | 16.7 GB | 15.8 GB |
| Birth By Sleep | 8 GB | 6.4 GB |

| Movie      | Full Quality | Compressed |
| ------------- | ------------- | ------------- |
| KH1 Theater Mode | 10.1 GB | 3.4 GB |
| 358/2 Days Movie | 6 GB | 1.6 GB |
| Re:Coded Movie | 6.4 GB | 2 GB |

**NOTE: You must own the collection on Steam for this to work**

# Setup

Download the EXE from the releases page, build it yourself, or just execute the script manually when required

Make sure `DepotDownloader.exe` is downloaded and extracted next to the EXE.
You likely want to download `DepotDownloader-windows-x64.zip` from https://github.com/SteamRE/DepotDownloader/releases

# Usage

Make sure Steam is closed.

Run the EXE and follow the prompts to configure your install.

When prompted to select a folder, select the `steamapps` folder you wish to install to. (By default this would be `C:\Program Files (x86)\Steam\steamapps`)

Wait for the install to finish. You will get several terminals opening as it downloads each games set of files, but these will close automatically.

# Build

`pip install -r requirements.txt`

`pyinstaller --onefile 'KHSelectiveDownloader.py'`
