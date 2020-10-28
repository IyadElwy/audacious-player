import subprocess
import logging

logger = logging.getLogger(__name__)

# Run a command line command and returns stdout
def _run(command):
	result = subprocess.run(command, check=True, stdout=subprocess.PIPE, text=True)
	result.stdout = result.stdout[:-1]
	return result.stdout

def is_playing():
	result = subprocess.run(["audtool", "playback-status"], stdout=subprocess.PIPE, text=True)
	logger.debug(result.stdout)
	if result.returncode == 0 and result.stdout is not None and result.stdout != "stopped":
		return True
	return False

def status():
	return _run(["audtool", "playback-status"])

# Get current song
def get_current_song():
	return _run(["audtool", "current-song"])

# Skip to next song
def next():
	_run(["audtool", "playlist-advance"])
	_run(["audtool", "playback-play"])

def prev():
	_run(["audtool", "playlist-reverse"])
	_run(["audtool", "playback-play"])

def volume(amount):
	_run(["audtool", "set-volume", amount])

def playpause():
	_run(["audtool", "playback-playpause"])

# Display all songs in current playlist
def display_songs():
	lines = _run(["audtool", "playlist-display"]).splitlines()
	lines.pop() # Removes last item, whe don't need that
	lines.pop(0) # We also don't need the first item
	songs = []
	for line in lines:
		[pos, name, length] = line.split(" | ")
		pos = pos.lstrip()
		name = name.rstrip()
		songs.append({"name": name, "pos": pos, "length": length})
	return songs

def jump(pos):
	_run(["audtool", "playlist-jump", pos])