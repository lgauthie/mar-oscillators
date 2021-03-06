from pygame.midi import *

from marsyas import *
from marsyas_util import create
from play_melody import *

def main():

# Set up Midi Stuff
    init()
    poll = Input.poll
    read = Input.read
    midi = Input(0)

# The Maysyas stuff
    gen = ["Series/fmnet", ["APDelayOsc/waveguide","ADSR/adsr","Gain/gain","AudioSink/dest"]]
    network = create(gen)

# Set the systems sample rate
    sample_rate = 44100.0
    network.updControl( "mrs_real/israte", sample_rate)

    network.updControl("ADSR/adsr/mrs_real/aTime", 0.1)
    network.updControl("Gain/gain/mrs_real/gain", 0.6)
    network.updControl("APDelayOsc/waveguide/mrs_natural/type", 1)

# These mapping are to make the system work with play melody
    network.linkControl("ADSR/adsr/mrs_bool/noteon", "mrs_bool/noteon")
    network.linkControl("APDelayOsc/waveguide/mrs_bool/noteon", "mrs_bool/noteon")
    network.linkControl("ADSR/adsr/mrs_bool/noteoff", "mrs_bool/noteoff")

    network.linkControl("APDelayOsc/waveguide/mrs_real/frequency", "mrs_real/frequency")
    network.updControl("AudioSink/dest/mrs_bool/initAudio", MarControlPtr.from_bool(True))


    lastnote = 0
    while(True):
        if poll(midi):
            # format [[[128,  49 , 127,   0], 19633]]
            #           cc#| note| vel| n/a
            msg = read(midi, 1)
            note = msg[0][0][1]
            velocity = msg[0][0][2]
            noteon = msg[0][0][0]
            print(msg)
            if noteon == 145 or noteon == 144:
                network.updControl("mrs_real/frequency", midi2freq(note))
                network.updControl("Gain/gain/mrs_real/gain", velo2float(velocity))
                network.updControl("mrs_bool/noteon", MarControlPtr.from_bool(True))
                lastnote = note
            elif noteon == 128 or noteon == 129 and lastnote == note:
                network.updControl("mrs_bool/noteoff", MarControlPtr.from_bool(True))
                network.updControl("mrs_bool/noteon", MarControlPtr.from_bool(False))
        network.tick()

def velo2float(num):
    return num/128.0

def midi2freq(num):
    return 440 * pow(2,((num-69)/12.0))

if __name__ == "__main__":
    main()
