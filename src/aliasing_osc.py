from marsyas import *
from marsyas_util import create

mod = ["Fanout/fo", ["ADSR/pitch","ADSR/pwm"]]
osc = ["Series/osc",[mod, "AliasingOsc/osc"]]
gen = ["Series/fmnet",[osc, "ADSR/amp", "Gain/gain", "SoundFileSink/dest2"]]
#gen = ["Series/fmnet", [["Fanout/fo", ["ADSR/adsr",osc]], "Product/mul","Gain/gain", "SoundFileSink/dest2"]]

# Create network and intialize parameter mapping 
network = create(gen)

network.updControl("Series/osc/Fanout/fo/ADSR/pwm/mrs_bool/bypass", MarControlPtr.from_bool(True))
network.updControl("Series/osc/Fanout/fo/ADSR/pwm/mrs_real/aTime", 0.7)
network.updControl("Series/osc/Fanout/fo/ADSR/pitch/mrs_bool/bypass", MarControlPtr.from_bool(True))
network.updControl("Series/osc/AliasingOsc/osc/mrs_natural/type", 1)
network.updControl("Series/osc/AliasingOsc/osc/mrs_bool/cyclicin", MarControlPtr.from_bool(True))
network.updControl("Gain/gain/mrs_real/gain", 0.7)

sample_rate = 44100.0
buffer_size = 64
device = 1

"""
Sets up the audio output for the network
"""
network.updControl( "mrs_real/israte", sample_rate)

# Set up Audio File
network.updControl( "SoundFileSink/dest2/mrs_string/filename", "AliasingTest.wav")

bufferSize = network.getControl("mrs_natural/inSamples").to_natural()
srate = network.getControl("mrs_real/osrate").to_real()
tstep = bufferSize * 1.0 / srate

pitch = 55.0
notes = [pitch, pitch * 2, (pitch * 3)/2.0, (pitch * 5)/3.0, pitch]

for note in notes:
    time = 0.0
    nton = 'on'
    network.updControl("Series/osc/AliasingOsc/osc/mrs_real/frequency", note)
    network.updControl("Series/osc/Fanout/fo/ADSR/pwm/mrs_real/nton", 1.0)
    network.updControl("Series/osc/Fanout/fo/ADSR/pitch/mrs_real/nton", 1.0)
    network.updControl("ADSR/amp/mrs_real/nton", 1.0)

    while time < 1.0:
        network.tick()

        if time > 0.7 and nton == 'on':
            network.updControl("Series/osc/Fanout/fo/ADSR/pwm/mrs_real/ntoff", 1.0)
            network.updControl("Series/osc/Fanout/fo/ADSR/pitch/mrs_real/ntoff", 1.0)
            network.updControl("ADSR/amp/mrs_real/ntoff", 1.0)
            nton = 'off'
        time = time + tstep
