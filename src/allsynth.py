from marsyas import *
from marsyas_util import create

from pygame.midi import *

def main():
    init()
    poll = Input.poll
    read = Input.read
    midi = Input(0)

    # This sets up a number list of oscillators, only the series needs
    # to have a unique name for the series to work.
    osc_type = "BlitOsc/b"
    oscs = [["Series/osc%d" % i, [osc_type,"ADSR/adsr","Gain/gain"]] for i in range(44,52)]

    # This turns all of our system specifications and stores them in
    # a list. 
    oscs = [create(net) for net in oscs]

    osc_bank = ["Fanout/bank", oscs]
    net = ["Series/fmnet", [osc_bank,"Sum/sum", "AudioSink/dest"]]

    # Create network and intialize parameter mapping 
    network = create(net)

    # Output settings
    sample_rate = 88200.0
    network.updControl("mrs_real/israte", sample_rate)
    network.updControl("AudioSink/dest/mrs_bool/initAudio", MarControlPtr.from_bool(True))

    for osc in oscs:
        osc.updControl(osc_type + "/mrs_bool/noteon", mbool(True))
        osc.updControl("Gain/gain/mrs_real/gain", 0.6)

    # Trigs
    trigs = [(i + 44,
              net.getControl("ADSR/adsr/mrs_bool/noteon"),
              net.getControl("ADSR/adsr/mrs_bool/noteoff"),
              net.getControl(osc_type + "/mrs_real/frequency")) \
              for i, net in enumerate(oscs)]

    maj = [72,74,76,77,79,81,83,84]
    # set dem notes
    for ((_, _, _, freq), i) in zip(trigs, maj):
        freq.setValue_real(midi2freq(i))
        print(midi2freq(i))

    while(True):
        if poll(midi):
            # format [[[128,  49 , 127,   0], 19633]]
            #           cc#| note| vel| n/a
            msg = read(midi, 1)
            note = msg[0][0][1]
            noteon = msg[0][0][0]
            print(note)
            if noteon == 144:
                get_note_on(trigs, note).setValue_bool(mbool(True))
                lastnote = note
            elif noteon == 128:
                get_note_off(trigs, note).setValue_bool(mbool(True))
                lastnote = note
        network.tick()

def mbool(b):
    return MarControlPtr.from_bool(b)

def get_note_on(trigs, num):
    for (i, nton, _, _) in trigs:
        if i == num:
            return nton

def get_note_off(trigs, num):
    for (i, _, ntoff, _) in trigs:
        if i == num:
            return ntoff

def midi2freq(num):
    return 440.0 * pow(2.0,((num-69)/12.0))

if __name__ == "__main__":
    main()
