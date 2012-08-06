from marsyas import *
from marsyas_util import create

gen = ["Series/fmnet",["ADSR/pitch","WaveguideOsc/sin","ADSR/env","Gain/gain","SoundFileSink/dest2"]]

# Create network and intialize parameter mapping 
network = create(gen)

#network.updControl("Fanout/fo/AliasingOsc/saw/mrs_real/frequency", 440.0)
network.updControl("ADSR/pitch/mrs_real/aTime", 0.7)
network.updControl("ADSR/pitch/mrs_bool/bypass", MarControlPtr.from_bool(True))
network.updControl("Gain/gain/mrs_real/gain", 0.7)

sample_rate = 44100.0
buffer_size = 128
device = 1
"""
Sets up the audio output for the network
"""
network.updControl( "mrs_real/israte", sample_rate)

# Set up Audio File
network.updControl("SoundFileSink/dest2/mrs_string/filename", "WaveguideTest.wav")

bufferSize = network.getControl("mrs_natural/inSamples").to_natural()
srate = network.getControl("mrs_real/osrate").to_real()
tstep = bufferSize * 1.0 / srate

pitch = 440.0
notes = [pitch, pitch * 2, (pitch * 3)/2.0, (pitch * 5)/3.0, pitch]

for note in notes:
    time = 0.0
    nton = 'on'
    network.updControl("WaveguideOsc/sin/mrs_real/frequency", note)
    network.updControl("ADSR/env/mrs_real/nton", 1.0)
    network.updControl("ADSR/pitch/mrs_real/nton", 1.0)

    while time < 1.0:
        network.tick()

        if time > 0.7 and nton == 'on':
            network.updControl("ADSR/env/mrs_real/ntoff", 1.0)
            network.updControl("ADSR/pitch/mrs_real/ntoff", 1.0)
            nton = 'off'
        time = time + tstep
