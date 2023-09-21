from pydub import AudioSegment
from pydub.generators import Sine
def create_riddim_bassline():
    bassline = Sine(40).to_audio_segment(duration=200)


    return bassline


riddim_bassline = create_riddim_bassline() * 8

riddim_bassline.export("riddim_bassline.wav", format='wav')

print("riddim-style bassline created ands aved as 'riddim_bassline.wav'")