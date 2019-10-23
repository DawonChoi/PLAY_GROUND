import time
import pyaudio
import numpy as np

# initialize sample data and get the instance of variable modules
p = pyaudio.PyAudio()
tuple_duration = [int(i) for i in input().split()]

PI = np.pi # CONST
volume = 0.5     # range [0.0, 1.0]
fs = 44100       # sampling rate, Hz, must be integer
duration = 3.0   # in seconds, may be float
f = 1000.0       # sine frequency, Hz, may be float

# not use in the current case
gap = 10

# customize the song by array
demo_song = [131, 165, 196, 131, 165, 196, 220, 220, 220, 196]

# hard coding
def settingDuration(song):
    durations = []
    for each in song:
        if each < 220:
            durations.append(2.5)
        else:
            durations.append(2)
    durations[-1] = 3.5
    return durations

def generateSong(song, durationlist):
    flagOfTempo = 0
    settingDuration(song)
    for symbol in song:
        samples = (np.sin(2*PI*np.arange(fs*durationlist[flagOfTempo])*symbol/fs)).astype(np.float32)
        flagOfTempo = flagOfTempo + 1
        stream.write(volume*samples)
        time.sleep(0.05)
        print(samples) # drivers

def generateSineWave(frequency):
    samples = (np.sin(2*PI*np.arange(fs*duration)*f/fs)).astype(np.float32)
    while frequency >= 30:
        stream.write(volume*samples)
        frequency = frequency - gap
        samples = (np.sin(2*PI*np.arange(fs*duration)*frequency/fs)).astype(np.float32)
        print(samples) # drivers

###############################################################################################
# from now on
# executive section                      ▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼
###############################################################################################

# generate samples, note conversion to float32 array
samples = (np.sin(2*PI*np.arange(fs*duration)*f/fs)).astype(np.float32)

# for paFloat32 sample values must be in range [-1.0, 1.0]
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=fs,
                output=True)

# play. May repeat with different volume values (if done interactively)
tempo = settingDuration(demo_song)
generateSong(demo_song, tempo)
# settingDuration(demo_song) -> will be used next task

stream.stop_stream()
stream.close()

p.terminate()
