Virtual Analog Oscillators in Marsyas
==========================================================

This repository contains examples of several Virtualy Analog Oscillators that I
have written for Marsyas.

Contents
--------

* [Prerequisites](README.md#prerequisites)
* [Playing](README.md#playing)
* [Mono-Synth](README.md#mono-synth)
* [Bandlimited Impulse Train Oscillator](README.md#bandlimited-impulse-train-oscillator)
* [Allpass Delay Oscillator](README.md#allpass-delay-oscillator)
* [Aliasing Oscillator](README.md#aliasing-oscillator)
* [Waveguide Oscillator](README.md#waveguide-oscillator)
* [Additive Oscillator](README.md#additive-oscillator)


Prerequisites
-------------
To follow this tutorial you will need:

+ Python - I'm using version 2.7, but 2.6 or 2.5 should work as well
+ PyGame - This is used for midi IO
+ Marsyas - compiled with the swig python bindings
+ marsyas_util - found in src/marsyas_python/ from the Marsyas svn repository
+ plot_spectrogram - from the same location

marsyas_util.py and plot_spectrogram.py should be placed in the same folder as
the code examples.  marsyas_util defines some Marsyas helper functions we can
use to set up MarSystems easier, and plot_spectrogram can be used to draw
spectrograms of our output.

PyGame must be compiled with midi support, on mac this can be installed via
macports with the command `sudo port install py27-game +portmidi`. On Linux it
would be easiest to build PyGame from source.  

A tutorial on installing Marsyas and swig python bindings can be found
[here](http://marsology.blogspot.ca/2011/09/installing-marsyas-with-python-bindings.html).

To use these examples you will need to most recent version of Marsyas found in
the sourceforge svn repository.
` svn co https://marsyas.svn.sourceforge.net/svnroot/marsyas/trunk marsyas `

I'm also assuming you have some experience with python.

Playing
------

For the sake of testing each of these oscillators I've prepared a file to play
the same melody on each MarSystem passed in. You could specify the melody, but
I chose to go with a default one for the demos.

### Source:

[play_melody.py]( mar-oscillators/tree/master/src/play_melody.py)

Mono-Synth
----------

This is a quick example of a real-time synth built around Marsyas, right now it is
only monophonic, but it is possible to extend this to a poly-synth.  

For simplicity I used the PyGame midi library instead of the one built into
Marsyas. This is because I'm more familiar with how it works. It shouldn't be much
harder to set up the Midi from within Marsyas.

Currently only pitch and amplitude are implemented.

### Source:

[midi.py]( mar-oscillators/tree/master/src/midi.py)

Bandlimited Impulse Train Oscillator
------------------------------------

The bandlimited impulse train oscillator work by having a phase counter that
resets each period. When the counter resets an impulse is created, and sent
though a fractional delay filter. This limits the bandwidth of the impulse. If
the system is causal (Read: Possible to implement in real time), then it is
impossible to have the impulse train perfectly bandlimited. Luckily there is
some headroom, and for the most part the aliasing wont be perceivable.

In this case a second order allpass filter was used. The amount of bandlimiting
could be increased by using b-spline interpolation, but the allpass method is
good enough in most cases and is easier to implement.  

To generate the virtual analog wave form a leaky integrator is used on the
output signal, this causes the frequency response to have an exponential decay.  

If the impulse train is unipolar (each impulse is positive and the same value),
then we will generate a full spectrum (even and odd harmonics). When the
integration is applied this will create a sawtooth waveform. 

If the impulse train is bipolar (each impulse is the oppsite polarity eg. +1 -1
+1 -1), then the spectrum will contain only odd harmonics. When this is
integrated a square wave will be generated.

This biggest challenge from this method comes from the DC offset that occurs
from an all positive impulse train. The offset can be approximated by the
formula `Frequency/Samplerate` but this approach breaks down when the pitch
must vary over time. One solution would be to lock the frequency for each
cycle, in this way you would calculate the DC offset for each cycle. This 
method also breaks down if the amount of modulation is too high, but should
work in most cases.

### Examples:

<object height="81" width="100%"> <param name="movie" value="https://player.soundcloud.com/player.swf?url=http%3A%2F%2Fapi.soundcloud.com%2Ftracks%2F55462394"></param> <param name="allowscriptaccess" value="always"></param> <embed allowscriptaccess="always" height="81" src="https://player.soundcloud.com/player.swf?url=http%3A%2F%2Fapi.soundcloud.com%2Ftracks%2F55462394" type="application/x-shockwave-flash" width="100%"></embed> </object>  <span><a href="http://soundcloud.com/lee-daniel-gauthier/blittestsaw">BlitTestSaw</a> by <a href="http://soundcloud.com/lee-daniel-gauthier">Leesifer</a></span> 

<object height="81" width="100%"> <param name="movie" value="https://player.soundcloud.com/player.swf?url=http%3A%2F%2Fapi.soundcloud.com%2Ftracks%2F55462396"></param> <param name="allowscriptaccess" value="always"></param> <embed allowscriptaccess="always" height="81" src="https://player.soundcloud.com/player.swf?url=http%3A%2F%2Fapi.soundcloud.com%2Ftracks%2F55462396" type="application/x-shockwave-flash" width="100%"></embed> </object>  <span><a href="http://soundcloud.com/lee-daniel-gauthier/blittestsquare">BlitTestSquare</a> by <a href="http://soundcloud.com/lee-daniel-gauthier">Leesifer</a></span> 

### Source:

[BlitOsc.cpp](http://marsyas.svn.sourceforge.net/viewvc/marsyas/trunk/src/marsyas/BlitOsc.cpp?revision=4803&view=markup)
|
[BlitOsc.h](http://marsyas.svn.sourceforge.net/viewvc/marsyas/trunk/src/marsyas/BlitOsc.h?revision=4803&view=markup)
|
[blit_osc.py]( mar-oscillators/tree/master/src/blit_osc.py)

Allpass Delay Oscillator
------------------------ 

This approach is similar to the BLIT approach, but instead of using a phase
counter and impulse train, a feedback delayline is used. As the signal is
fed back into the system is is run through an allpass filter. A single
impulse is then fed into the system and left to go repeatedly through the
delayline. By having the allpass as a fractional delay each time the system
feeds back the impulses spread out. The output is a perceptually harmonic
signal with zero aliasing.

Again this output is run through a leaky integrator to generate the virtual
analog waveform.

If the impulse is fed back with a positive coefficient the signal will have a
full spectrum (even and odd harmonics), when this is integrated the output will
be a sawtooth waveform. If the impulse is inverted as it is fed back, the
spectrum will contain only even harmonics, integration will lead to a square
waveform.

The saw algorithm again suffers from the same DC offset problem, and for the
case where the frequency doesn't change over time the offset can be approximated
the same way as before (Frequency/Samplerate). Unfortunately there is no easy
to deal with the case where the frequency changes over time. In some cases a DC
block might suffice, but with large modulation there will still be DC drifting.

This algorithm has a few additional problems that can be fixed with careful
tweaking. The first problem is that thought must be put in to tuning this
oscillator because the allpass coefficient and the length of the delay line
with both effect this pitch.

The other issue has to do with modulating the pitch in general, there are two
approaches, one is to change the filter coefficient overtime, I haven't play
with this method. So unfortunately I can't say if it is viable, the other
method is to adjust the length of the delay line. If you simply jump between
two pointers with different delay times, there will most likely be pops and
clicks in the output, this could possibly be fixed with two approaches. One
would be to use an interpolating delayline, and ramp the delay from one pitch
to the next. But a simpler approach is to have two pointers, at different
points in the delayline and to cross fade between them over several samples.

Despite these challenges, this is a great sounding algorithm, and could be worth
the extra effort to set up and tweak into a fully usable state.

### Examples:

<object height="81" width="100%"> <param name="movie" value="https://player.soundcloud.com/player.swf?url=http%3A%2F%2Fapi.soundcloud.com%2Ftracks%2F55462392"></param> <param name="allowscriptaccess" value="always"></param> <embed allowscriptaccess="always" height="81" src="https://player.soundcloud.com/player.swf?url=http%3A%2F%2Fapi.soundcloud.com%2Ftracks%2F55462392" type="application/x-shockwave-flash" width="100%"></embed> </object>  <span><a href="http://soundcloud.com/lee-daniel-gauthier/aptestsaw">APTestSaw</a> by <a href="http://soundcloud.com/lee-daniel-gauthier">Leesifer</a></span> 

<object height="81" width="100%"> <param name="movie" value="https://player.soundcloud.com/player.swf?url=http%3A%2F%2Fapi.soundcloud.com%2Ftracks%2F55462393"></param> <param name="allowscriptaccess" value="always"></param> <embed allowscriptaccess="always" height="81" src="https://player.soundcloud.com/player.swf?url=http%3A%2F%2Fapi.soundcloud.com%2Ftracks%2F55462393" type="application/x-shockwave-flash" width="100%"></embed> </object>  <span><a href="http://soundcloud.com/lee-daniel-gauthier/aptestsquare">APTestSquare</a> by <a href="http://soundcloud.com/lee-daniel-gauthier">Leesifer</a></span>

### Source:

[APDelayOsc.cpp](http://marsyas.svn.sourceforge.net/viewvc/marsyas/trunk/src/marsyas/APDelayOsc.cpp?revision=4803&view=markup)
|
[APDelayOsc.h](http://marsyas.svn.sourceforge.net/viewvc/marsyas/trunk/src/marsyas/APDelayOsc.h?revision=4803&view=markup) 
|
[allpass_delay_osc.py]( mar-oscillators/tree/master/src/allpass_delay_osc.py)

Aliasing Oscillator
-------------------

This is the most simple variation of a Virtual Analog oscillator. The waveforms
are perfectly calculated, and though the waveform is perfect, there is heavy
aliasing.

The saw waveform is generated by calculating the rate of change per sample to
go from -1 to +1 in one period. The value is then added to a counter starting
at -1, when the counter reaches +1 it is reset to -1, this cycle continues
indefinitely.  

The square can be calculated from this by setting the output to -1 when the saw
waveform is less than zero, and to +1 when the waveform is greater than zero. If
the middle point of this comparison is changed to a value other than zero we can
enter the realm of pulse width modulation.

Other than issues with aliasing this type of oscillator does not have many
implementation challenges, therefore modulating pitch and pulsewidth is
trivial.

As a result this was the best place to experiment with using multiple channels
of the input realvec as modulation sources. I've included one example of this
used with an adsr envelope for pitch, and another with an adsr envelope for
PWM. Though this input could be any arbitrary signal it is more clear to hear
what is happeneing when a simple envelope is used.

### Examples:

<object height="81" width="100%"> <param name="movie" value="https://player.soundcloud.com/player.swf?url=http%3A%2F%2Fapi.soundcloud.com%2Ftracks%2F55462388"></param> <param name="allowscriptaccess" value="always"></param> <embed allowscriptaccess="always" height="81" src="https://player.soundcloud.com/player.swf?url=http%3A%2F%2Fapi.soundcloud.com%2Ftracks%2F55462388" type="application/x-shockwave-flash" width="100%"></embed> </object>  <span><a href="http://soundcloud.com/lee-daniel-gauthier/aliasingtestpitch">AliasingTestPitch</a> by <a href="http://soundcloud.com/lee-daniel-gauthier">Leesifer</a></span> 

<object height="81" width="100%"> <param name="movie" value="https://player.soundcloud.com/player.swf?url=http%3A%2F%2Fapi.soundcloud.com%2Ftracks%2F55462389"></param> <param name="allowscriptaccess" value="always"></param> <embed allowscriptaccess="always" height="81" src="https://player.soundcloud.com/player.swf?url=http%3A%2F%2Fapi.soundcloud.com%2Ftracks%2F55462389" type="application/x-shockwave-flash" width="100%"></embed> </object>  <span><a href="http://soundcloud.com/lee-daniel-gauthier/aliasingtestpwm">AliasingTestPWM</a> by <a href="http://soundcloud.com/lee-daniel-gauthier">Leesifer</a></span>

<object height="81" width="100%"> <param name="movie" value="https://player.soundcloud.com/player.swf?url=http%3A%2F%2Fapi.soundcloud.com%2Ftracks%2F55462390"></param> <param name="allowscriptaccess" value="always"></param> <embed allowscriptaccess="always" height="81" src="https://player.soundcloud.com/player.swf?url=http%3A%2F%2Fapi.soundcloud.com%2Ftracks%2F55462390" type="application/x-shockwave-flash" width="100%"></embed> </object>  <span><a href="http://soundcloud.com/lee-daniel-gauthier/aliasingtestsaw">AliasingTestSaw</a> by <a href="http://soundcloud.com/lee-daniel-gauthier">Leesifer</a></span>

<object height="81" width="100%"> <param name="movie" value="https://player.soundcloud.com/player.swf?url=http%3A%2F%2Fapi.soundcloud.com%2Ftracks%2F55462391"></param> <param name="allowscriptaccess" value="always"></param> <embed allowscriptaccess="always" height="81" src="https://player.soundcloud.com/player.swf?url=http%3A%2F%2Fapi.soundcloud.com%2Ftracks%2F55462391" type="application/x-shockwave-flash" width="100%"></embed> </object>  <span><a href="http://soundcloud.com/lee-daniel-gauthier/aliasingtestsquare">AliasingTestSquare</a> by <a href="http://soundcloud.com/lee-daniel-gauthier">Leesifer</a></span>

### Source:

[AliasingOsc.cpp](http://marsyas.svn.sourceforge.net/viewvc/marsyas/trunk/src/marsyas/AliasingOsc.cpp?revision=4803&view=markup)
|
[AliasingOsc.h](http://marsyas.svn.sourceforge.net/viewvc/marsyas/trunk/src/marsyas/AliasingOsc.h?revision=4803&view=markup)
|
[aliasing_osc.py]( mar-oscillators/tree/master/src/aliasing_osc.py)


Waveguide Oscillator
--------------------

The waveguide oscillator is based off of a physical model of two waves, one
positive and the other negative. A scattering junction is used to creates an
interaction between the two waves.  

The version I implemented is a simplification of this system containing two
unit delays and one multiplication per sample in the steady state. This system
is defined as `x1 = (2 * k * x1(n-1)) - x2(n-1) | x2 = x1(n-1)` where
`k = cos(2π * frequency)`. The output is a simple sine wave.

Modulating the pitch of this system is as easy as changing the coefficient k,
with one cravat, there is amplitude scaling that goes along with a shift in
pitch. Luckily it is possible to calculate the amount of scaling and compensate
for it. I haven't added that functionality yet. Once it is added FM synthesis
should be possible using any number of these oscillators.

### Examples:

<object height="81" width="100%"> <param name="movie" value="https://player.soundcloud.com/player.swf?url=http%3A%2F%2Fapi.soundcloud.com%2Ftracks%2F55462398"></param> <param name="allowscriptaccess" value="always"></param> <embed allowscriptaccess="always" height="81" src="https://player.soundcloud.com/player.swf?url=http%3A%2F%2Fapi.soundcloud.com%2Ftracks%2F55462398" type="application/x-shockwave-flash" width="100%"></embed> </object>  <span><a href="http://soundcloud.com/lee-daniel-gauthier/waveguidetest">WaveguideTest</a> by <a href="http://soundcloud.com/lee-daniel-gauthier">Leesifer</a></span> 

<object height="81" width="100%"> <param name="movie" value="https://player.soundcloud.com/player.swf?url=http%3A%2F%2Fapi.soundcloud.com%2Ftracks%2F55462399"></param> <param name="allowscriptaccess" value="always"></param> <embed allowscriptaccess="always" height="81" src="https://player.soundcloud.com/player.swf?url=http%3A%2F%2Fapi.soundcloud.com%2Ftracks%2F55462399" type="application/x-shockwave-flash" width="100%"></embed> </object>  <span><a href="http://soundcloud.com/lee-daniel-gauthier/waveguidetestpitch">WaveguideTestPitch</a> by <a href="http://soundcloud.com/lee-daniel-gauthier">Leesifer</a></span>

### Source:

[WaveguideOsc.cpp](http://marsyas.svn.sourceforge.net/viewvc/marsyas/trunk/src/marsyas/WaveguideOsc.cpp?revision=4803&view=markup)
|
[WaveguideOsc.h](http://marsyas.svn.sourceforge.net/viewvc/marsyas/trunk/src/marsyas/WaveguideOsc.h?revision=4803&view=markup)
|
[waveguide_osc.py]( mar-oscillators/tree/master/src/waveguide_osc.py)

Additive Oscillator
-------------------

This last example is based off the waveguide, but for each sample a waveguide
is calculated for each possible harmonic of a saw wave. The saw formula is
`∑((-1)^n(cos(2π * fundamental * n)))/n`.

The problem is that the waveguide algorithm starts at zero phase, so though
the output is perceptually a sawtooth waveform, it does not look like one.

I've thought of one possible solution, and that would be to initialize the system
with the values `x1(n-1) = 0.95` and
`x2(n-1) = 0.95 * (sin( n + ((π/2) * (samplerate/n - 1))))` where `n = is the number of samples in a period`

This should cause our system to become a cosine. I haven't tested this at all,
so I could be way off the mark.  

I've found that to the ear, this is the least pleasing method of generating a
sawtooth waveform.  It is possible that this is because I don't have the phase
right, but I don't think that would make much of a difference.

### Examples:

<object height="81" width="100%"> <param name="movie" value="https://player.soundcloud.com/player.swf?url=http%3A%2F%2Fapi.soundcloud.com%2Ftracks%2F55462387"></param> <param name="allowscriptaccess" value="always"></param> <embed allowscriptaccess="always" height="81" src="https://player.soundcloud.com/player.swf?url=http%3A%2F%2Fapi.soundcloud.com%2Ftracks%2F55462387" type="application/x-shockwave-flash" width="100%"></embed> </object>  <span><a href="http://soundcloud.com/lee-daniel-gauthier/additivetestsaw">AdditiveTestSaw</a> by <a href="http://soundcloud.com/lee-daniel-gauthier">Leesifer</a></span>

### Source:

[AdditiveOsc.cpp](http://marsyas.svn.sourceforge.net/viewvc/marsyas/trunk/src/marsyas/AdditiveOsc.cpp?revision=4803&view=markup)
|
[AdditiveOsc.h](http://marsyas.svn.sourceforge.net/viewvc/marsyas/trunk/src/marsyas/AdditiveOsc.h?revision=4803&view=markup)
|
[additive_osc.py]( mar-oscillators/tree/master/src/additive_osc.py)

