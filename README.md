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

Make sure `DepotDownloader.exe` is downloaded and extracted next to this script
You likely want to download `DepotDownloader-windows-x64.zip` from https://github.com/SteamRE/DepotDownloader/releases

# Usage

Double click to run `KHSelectiveDownloader.py` or run it from terminal

You will be prompted for which games and movies to install, in which language and whether they are compressed or not, and where to install to.

When prompted, enter your Steam username. The script does not store this, it is just given to DepotDownloader.

DepotDownloader will ask you to enter your password the first time it runs, it will store your auth token in `.DepotDownloader` inside the install folder so it doesn't need to prompt multiple times

Delete `.DepotDownloader` from the install folder after everything has finished