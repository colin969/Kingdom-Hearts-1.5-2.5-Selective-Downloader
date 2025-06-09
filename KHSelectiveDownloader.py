from tkinter import Tk
from tkinter.filedialog import askdirectory
import os
import subprocess
import sys

app_id = 2552430

en_base_depot = 2552433
en_movie_depot = 2552435
en_movie_compressed_depot = 2552437
jp_base_depot = 2552432
jp_movie_depot = 2552434
jp_movie_compressed_depot = 2552436

base_regex = "^(?!Image/dt).*"
kh1_regex = "^Image/dt/kh1"
theater_regex = "^Image/dt/Theater"
com_regex = "^Image/dt/Recom"
kh2_regex = "^Image/dt/kh2"
bbs_regex = "^Image/dt/bbs"

kh1_movie_regex = "^STEAM/dt/KH1Movie"
theater_movie_regex = "^STEAM/Theater"
com_movie_regex = "^STEAM/dt/KHCReSource"
kh2_movie_regex = "^STEAM/juefigs/KH2ReSource"
bbs_movie_regex = "^STEAM/juefigs/BBSReSource"
days_movie_regex = "^STEAM/Mare/MOVIE/Days"
coded_movie_regex = "^STEAM/Mare/MOVIE/ReCoded"

appmanifest = """"AppState"
{
	"appid"		"2552430"
	"Universe"		"1"
	"LauncherPath"		"C:\\Program Files (x86)\\Steam\\steam.exe"
	"name"		"KINGDOM HEARTS -HD 1.5+2.5 ReMIX-"
	"StateFlags"		"4"
	"installdir"		"KINGDOM HEARTS -HD 1.5+2.5 ReMIX-"
	"LastUpdated"		"1724662837"
	"LastPlayed"		"0"
	"SizeOnDisk"		"77175061920"
	"StagingSize"		"77175061920"
	"buildid"		"15194255"
	"LastOwner"		"76561197960287930"
	"UpdateResult"		"0"
	"BytesToDownload"		"68382664912"
	"BytesDownloaded"		"68382664912"
	"BytesToStage"		"77175061920"
	"BytesStaged"		"77175061920"
	"TargetBuildID"		"15194255"
	"AutoUpdateBehavior"		"0"
	"AllowOtherDownloadsWhileRunning"		"0"
	"ScheduledAutoUpdate"		"0"
	"InstalledDepots"
	{
		"2552433"
		{
			"manifest"		"2946731077053901934"
			"size"		"40940685792"
		}
		"2552435"
		{
			"manifest"		"3908821002986173448"
			"size"		"36234376128"
		}
	}
	"SharedDepots"
	{
		"228989"		"228980"
		"228990"		"228980"
		"229002"		"228980"
	}
	"UserConfig"
	{
		"language"		"english"
	}
	"MountedConfig"
	{
	}
}"""

language = "en"
compressed_movies = False

def run():
  print("Kingdom Hearts 1.5 + 2.5 Selective Downloader")
  print("=" * 40)

  # Make sure DepotDownloader exists
  if not os.path.exists('DepotDownloader.exe'):
    print("✗ DepotDownloader.exe not found. Please download it from https://github.com/SteamRE/DepotDownloader/releases")
    return
  
  # Language selection
  print("\nSelect language:")
  print("1. English (en)")
  print("2. Japanese (jp)")
  lang_choice = input("Enter choice (1-2): ").strip()
  language = "en" if lang_choice == "1" else "jp"

  # Compressed movies selection
  print("\nUse compressed movies?")
  print("1. Yes (Steam Deck Versions, Saves ~1GB per Game and ~4GB per Movie)")
  print("2. No (Full Quality)")
  compress_choice = input("Enter choice (1-2): ").strip()
  compressed_movies = compress_choice == "1"

  games = {
    "1": ("Kingdom Hearts 1           (10.3 GB Full / 9 GB    Compressed)", "kh1"),
    "2": ("KH1 Theater Mode           (10.1 GB Full / 3.4 GB  Compressed)", "theater"),
    "3": ("Re:Chain of Memories       (10.3 GB Full / 5.3 GB  Compressed)", "com"),
    "4": ("Kingdom Hearts 2           (16.7 GB Full / 15.8 GB Compressed)", "kh2"),
    "5": ("Birth by Sleep             ( 8.0 GB Full / 6.4 GB  Compressed)", "bbs"),
    "6": ("358/2 Days (Movie Only)    ( 6.0 GB Full / 1.6 GB  Compressed)", "days"),
    "7": ("Re:Coded (Movie Only)      ( 6.4 GB Full / 2 GB    Compressed)", "coded")
  }

  print("\nSelect games to download (comma-separated, e.g., 1,3,4):")
  for key, (name, _) in games.items():
      print(f"{key}. {name}")

  game_choices = input("Enter choices: ").strip().split(",")
  selected_games = [games[choice.strip()][1] for choice in game_choices if choice.strip() in games]

  if not selected_games:
    print("No valid games selected. Exiting...")
    input("Press any key to exit...")
    return
  
  # Install directory selection
  print(f"\nSelect steamapps directory to install to:")
  steamapps_dir = askdirectory(mustexist=True)
  common_dir = os.path.join(steamapps_dir, 'common')
  appmanifest_path = os.path.join(steamapps_dir, 'appmanifest_2552430.acf')
  install_dir = os.path.join(steamapps_dir, 'common', 'KINGDOM HEARTS -HD 1.5+2.5 ReMIX-')

  if not os.path.exists(common_dir):
    print("✗ Invalid steamapps directory selected, no common folder found. Exiting...")
    return

  username = input("\nEnter Steam username: ").strip()

  print(f"\nDownloading with settings:")
  print(f"Language: {language}")
  print(f"Compressed movies: {compressed_movies}")
  print(f"Selected games: \n\t{"\n\t".join([games[k][0] for k, v in games.items() if v[1] in selected_games])}")
    
  base_depot = en_base_depot if language == "en" else jp_base_depot
  download_depot("Base Install", base_depot, install_dir, base_regex, username)

  movie_depot = en_movie_compressed_depot if compressed_movies else en_movie_depot
  if language == "jp":
    movie_depot = jp_movie_compressed_depot if compressed_movies else jp_movie_depot

  # Download selected games
  for game in selected_games:
    if game == "kh1":
      download_depot("Kingdom Hearts 1 Install", base_depot, install_dir, kh1_regex, username)
      download_depot("Kingdom Hearts 1 Movies",movie_depot, install_dir, kh1_movie_regex, username)
      
    elif game == "theater":
      download_depot("KH1 Theater Install", base_depot, install_dir, theater_regex, username)
      download_depot("KH1 Theater Movies", movie_depot, install_dir, theater_movie_regex, username)
      
    elif game == "com":
      download_depot("Re:Chain of Memories Install", base_depot, install_dir, com_regex, username)
      download_depot("Re:Chain of Memories Movies", movie_depot, install_dir, com_movie_regex, username)
      
    elif game == "kh2":
      download_depot("Kingdom Hearts 2 Install", base_depot, install_dir, kh2_regex, username)
      download_depot("Kingdom Hearts 2 Movies", movie_depot, install_dir, kh2_movie_regex, username)
        
    elif game == "bbs":
      download_depot("Birth By Sleep Install", base_depot, install_dir, bbs_regex, username)
      download_depot("Birth By Sleep Movies", movie_depot, install_dir, bbs_movie_regex, username)
      
    elif game == "days":
      download_depot("358/2 Days Movie", movie_depot, install_dir, days_movie_regex, username)
        
    elif game == "coded":
      download_depot("Re:Coded Movie", movie_depot, install_dir, coded_movie_regex, username)

  print(f"\nSetting up app manifest...")
  with open(appmanifest_path, 'w') as manifest:
    manifest.write(appmanifest)

  print("✓ Downloads completed.")

def download_depot(name, depot_id, dest, regex, username):
  print(f"\nDownloading {name} from depot {depot_id} with filter: {regex}")

  with open("filelist.txt", "w") as f:
    f.write(f"regex:{regex}")
  
  cmd = [
    "DepotDownloader.exe",
    "-app", str(app_id),
    "-depot", str(depot_id),
    "-username", username,
    "-remember-password",
    "-validate",
    "-dir", f'"{dest}"',
    "-filelist", "filelist.txt"
  ]
  
  try:
    cmd_str = " ".join(cmd)
    process = subprocess.Popen(f'start /wait cmd /c "{cmd_str}"', shell=True)
    process.wait()
    print(f"✓ Successfully downloaded depot {depot_id}")
  except FileNotFoundError:
    print("✗ DepotDownloader not found. Make sure it's in the current directory.")
    sys.exit(1)

if __name__ == "__main__":
  try:
    run()
  except KeyboardInterrupt:
    print("\n✗ Download cancelled by user.")
    input("\nPress any key to exit...")
    sys.exit(1)
  input("\nPress any key to exit...")