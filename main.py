from scipy.io import wavfile
import argparse
import numpy as np
import sys
import warnings
import os
import keyboard
os.environ['PYGAME_HIDE_SUPPORT_PROMPT']='1'
import pygame
def speedx(snd_array, factor):
    indices = np.round(np.arange(0, len(snd_array), factor))
    indices = indices[indices < len(snd_array)].astype(int)
    return snd_array[indices]
def stretch(snd_array, factor, window_size, h):
    phase = np.zeros(window_size)
    hanning_window = np.hanning(window_size)
    result = np.zeros(int(len(snd_array) / factor + window_size))
    for i in np.arange(0, len(snd_array) - (window_size + h), h*factor):
        i = int(i)
        a1 = snd_array[i: i + window_size]
        a2 = snd_array[i + h: i + window_size + h]
        s1 = np.fft.fft(hanning_window * a1)
        s2 = np.fft.fft(hanning_window * a2)
        phase = (phase + np.angle(s2/s1)) % 2*np.pi
        a2_rephased = np.fft.ifft(np.abs(s2)*np.exp(1j*phase))
        i2 = int(i/factor)
        result[i2: i2 + window_size] += hanning_window*a2_rephased.real
    result = ((2**(16-4)) * result/result.max())
    return result.astype('int16')
def pitchshift(snd_array, n, window_size=2**13, h=2**11):
    factor = 2**(1.0 * n / 12.0)
    stretched = stretch(snd_array, 1.0/factor, window_size, h)
    return speedx(stretched[window_size:], factor)
warnings.simplefilter('ignore')
fps, sound = wavfile.read('temp.py')
tones = range(-25, 25)
sys.stdout.flush()
transposed_sounds = [pitchshift(sound, n) for n in tones]
pygame.mixer.init(fps, -16, 1, 2048)
keys = list('qwertyuioplkjhgfdsazxcvbnm')
sounds = map(pygame.sndarray.make_sound, transposed_sounds)
key_sound = dict(zip(keys, sounds))
is_playing = {k: False for k in keys}
while True:
    event = pygame.event
    key = keyboard.read_key()
    if keyboard.KEY_DOWN:
        try:
            if (key in key_sound.keys()) and (not is_playing[key]):
                key_sound[key].play(fade_ms=50)
                is_playing[key] = True
        except: pass
    if key in key_sound.keys(): key_sound[key].fadeout(50)
    is_playing[key] = False
