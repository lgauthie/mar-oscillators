Virtual Analog Oscillators in Marsyas
==========================================================

This repository contains examples of several Virtualy Analog Oscillators that I
have written for Marsyas.

Contents
--------

* [Prerequisites](README.md#prerequisites)
* [Bandlimited Impulse Train Oscillator](README.md#bandlimited-impulse-train-oscillator)
* [Allpass Delay Oscillator](README.md#allpass-delay-oscillator)
* [Aliasing Oscillator](README.md#aliasing-oscillator)
* [Additive Oscillator](README.md#additive-oscillator)
* [Waveguide Oscillator](README.md#waveguide-oscillator)

Prerequisites
-------------
To follow this tutorial you will need:

+ Python - I'm using version 2.7, but 2.6 or 2.5 should work as well
+ Marsyas - compiled with the swig python bindings
+ marsyas_util - found in src/marsyas_python/ from the Marsyas svn repository
+ plot_spectrogram - from the same location

marsyas_util.py and plot_spectrogram.py should be placed in the same folder as
the code examples.  marsyas_util defines some Marsyas helper functions we can
use to set up MarSystems easier, and plot_spectrogram can be used to draw
spectrograms of our output.

A tutorial on installing Marsyas and swig python bindings can be found
[here](http://marsology.blogspot.ca/2011/09/installing-marsyas-with-python-bindings.html).

To use these examples you will need to most recent version of Marsyas found in
the sourceforge svn repository.

I'm also assuming you have some experience with python.

Bandlimited Impulse Train Oscillator
------------------------------------
[BlitOsc.cpp](http://marsyas.svn.sourceforge.net/viewvc/marsyas/trunk/src/marsyas/BlitOsc.cpp?revision=4803&view=markup)
|
[BlitOsc.h](http://marsyas.svn.sourceforge.net/viewvc/marsyas/trunk/src/marsyas/BlitOsc.h?revision=4803&view=markup)

<object height="81" width="100%"> <param name="movie" value="https://player.soundcloud.com/player.swf?url=http%3A%2F%2Fapi.soundcloud.com%2Ftracks%2F55462394"></param> <param name="allowscriptaccess" value="always"></param> <embed allowscriptaccess="always" height="81" src="https://player.soundcloud.com/player.swf?url=http%3A%2F%2Fapi.soundcloud.com%2Ftracks%2F55462394" type="application/x-shockwave-flash" width="100%"></embed> </object>  <span><a href="http://soundcloud.com/lee-daniel-gauthier/blittestsaw">BlitTestSaw</a> by <a href="http://soundcloud.com/lee-daniel-gauthier">Leesifer</a></span> 

<object height="81" width="100%"> <param name="movie" value="https://player.soundcloud.com/player.swf?url=http%3A%2F%2Fapi.soundcloud.com%2Ftracks%2F55462396"></param> <param name="allowscriptaccess" value="always"></param> <embed allowscriptaccess="always" height="81" src="https://player.soundcloud.com/player.swf?url=http%3A%2F%2Fapi.soundcloud.com%2Ftracks%2F55462396" type="application/x-shockwave-flash" width="100%"></embed> </object>  <span><a href="http://soundcloud.com/lee-daniel-gauthier/blittestsquare">BlitTestSquare</a> by <a href="http://soundcloud.com/lee-daniel-gauthier">Leesifer</a></span> 

Allpass Delay Oscillator
------------------------
[APDelayOsc.cpp](http://marsyas.svn.sourceforge.net/viewvc/marsyas/trunk/src/marsyas/APDelayOsc.cpp?revision=4803&view=markup)
|
[APDelayOsc.h](http://marsyas.svn.sourceforge.net/viewvc/marsyas/trunk/src/marsyas/APDelayOsc.h?revision=4803&view=markup)

<object height="81" width="100%"> <param name="movie" value="https://player.soundcloud.com/player.swf?url=http%3A%2F%2Fapi.soundcloud.com%2Ftracks%2F55462392"></param> <param name="allowscriptaccess" value="always"></param> <embed allowscriptaccess="always" height="81" src="https://player.soundcloud.com/player.swf?url=http%3A%2F%2Fapi.soundcloud.com%2Ftracks%2F55462392" type="application/x-shockwave-flash" width="100%"></embed> </object>  <span><a href="http://soundcloud.com/lee-daniel-gauthier/aptestsaw">APTestSaw</a> by <a href="http://soundcloud.com/lee-daniel-gauthier">Leesifer</a></span> 

<object height="81" width="100%"> <param name="movie" value="https://player.soundcloud.com/player.swf?url=http%3A%2F%2Fapi.soundcloud.com%2Ftracks%2F55462393"></param> <param name="allowscriptaccess" value="always"></param> <embed allowscriptaccess="always" height="81" src="https://player.soundcloud.com/player.swf?url=http%3A%2F%2Fapi.soundcloud.com%2Ftracks%2F55462393" type="application/x-shockwave-flash" width="100%"></embed> </object>  <span><a href="http://soundcloud.com/lee-daniel-gauthier/aptestsquare">APTestSquare</a> by <a href="http://soundcloud.com/lee-daniel-gauthier">Leesifer</a></span>

Aliasing Oscillator
-------------------
[AliasingOsc.cpp](http://marsyas.svn.sourceforge.net/viewvc/marsyas/trunk/src/marsyas/AliasingOsc.cpp?revision=4803&view=markup)
|
[AliasingOsc.h](http://marsyas.svn.sourceforge.net/viewvc/marsyas/trunk/src/marsyas/AliasingOsc.h?revision=4803&view=markup)

<object height="81" width="100%"> <param name="movie" value="https://player.soundcloud.com/player.swf?url=http%3A%2F%2Fapi.soundcloud.com%2Ftracks%2F55462388"></param> <param name="allowscriptaccess" value="always"></param> <embed allowscriptaccess="always" height="81" src="https://player.soundcloud.com/player.swf?url=http%3A%2F%2Fapi.soundcloud.com%2Ftracks%2F55462388" type="application/x-shockwave-flash" width="100%"></embed> </object>  <span><a href="http://soundcloud.com/lee-daniel-gauthier/aliasingtestpitch">AliasingTestPitch</a> by <a href="http://soundcloud.com/lee-daniel-gauthier">Leesifer</a></span> 

<object height="81" width="100%"> <param name="movie" value="https://player.soundcloud.com/player.swf?url=http%3A%2F%2Fapi.soundcloud.com%2Ftracks%2F55462389"></param> <param name="allowscriptaccess" value="always"></param> <embed allowscriptaccess="always" height="81" src="https://player.soundcloud.com/player.swf?url=http%3A%2F%2Fapi.soundcloud.com%2Ftracks%2F55462389" type="application/x-shockwave-flash" width="100%"></embed> </object>  <span><a href="http://soundcloud.com/lee-daniel-gauthier/aliasingtestpwm">AliasingTestPWM</a> by <a href="http://soundcloud.com/lee-daniel-gauthier">Leesifer</a></span>

<object height="81" width="100%"> <param name="movie" value="https://player.soundcloud.com/player.swf?url=http%3A%2F%2Fapi.soundcloud.com%2Ftracks%2F55462390"></param> <param name="allowscriptaccess" value="always"></param> <embed allowscriptaccess="always" height="81" src="https://player.soundcloud.com/player.swf?url=http%3A%2F%2Fapi.soundcloud.com%2Ftracks%2F55462390" type="application/x-shockwave-flash" width="100%"></embed> </object>  <span><a href="http://soundcloud.com/lee-daniel-gauthier/aliasingtestsaw">AliasingTestSaw</a> by <a href="http://soundcloud.com/lee-daniel-gauthier">Leesifer</a></span>

<object height="81" width="100%"> <param name="movie" value="https://player.soundcloud.com/player.swf?url=http%3A%2F%2Fapi.soundcloud.com%2Ftracks%2F55462391"></param> <param name="allowscriptaccess" value="always"></param> <embed allowscriptaccess="always" height="81" src="https://player.soundcloud.com/player.swf?url=http%3A%2F%2Fapi.soundcloud.com%2Ftracks%2F55462391" type="application/x-shockwave-flash" width="100%"></embed> </object>  <span><a href="http://soundcloud.com/lee-daniel-gauthier/aliasingtestsquare">AliasingTestSquare</a> by <a href="http://soundcloud.com/lee-daniel-gauthier">Leesifer</a></span>

Additive Oscillator
-------------------
[AdditiveOsc.cpp](http://marsyas.svn.sourceforge.net/viewvc/marsyas/trunk/src/marsyas/AdditiveOsc.cpp?revision=4803&view=markup)
|
[AdditiveOsc.h](http://marsyas.svn.sourceforge.net/viewvc/marsyas/trunk/src/marsyas/AdditiveOsc.h?revision=4803&view=markup)

<object height="81" width="100%"> <param name="movie" value="https://player.soundcloud.com/player.swf?url=http%3A%2F%2Fapi.soundcloud.com%2Ftracks%2F55462387"></param> <param name="allowscriptaccess" value="always"></param> <embed allowscriptaccess="always" height="81" src="https://player.soundcloud.com/player.swf?url=http%3A%2F%2Fapi.soundcloud.com%2Ftracks%2F55462387" type="application/x-shockwave-flash" width="100%"></embed> </object>  <span><a href="http://soundcloud.com/lee-daniel-gauthier/additivetestsaw">AdditiveTestSaw</a> by <a href="http://soundcloud.com/lee-daniel-gauthier">Leesifer</a></span>

Waveguide Oscillator
--------------------
[WaveguideOsc.cpp](http://marsyas.svn.sourceforge.net/viewvc/marsyas/trunk/src/marsyas/WaveguideOsc.cpp?revision=4803&view=markup)
|
[WaveguideOsc.h](http://marsyas.svn.sourceforge.net/viewvc/marsyas/trunk/src/marsyas/WaveguideOsc.h?revision=4803&view=markup)

<object height="81" width="100%"> <param name="movie" value="https://player.soundcloud.com/player.swf?url=http%3A%2F%2Fapi.soundcloud.com%2Ftracks%2F55462398"></param> <param name="allowscriptaccess" value="always"></param> <embed allowscriptaccess="always" height="81" src="https://player.soundcloud.com/player.swf?url=http%3A%2F%2Fapi.soundcloud.com%2Ftracks%2F55462398" type="application/x-shockwave-flash" width="100%"></embed> </object>  <span><a href="http://soundcloud.com/lee-daniel-gauthier/waveguidetest">WaveguideTest</a> by <a href="http://soundcloud.com/lee-daniel-gauthier">Leesifer</a></span> 

<object height="81" width="100%"> <param name="movie" value="https://player.soundcloud.com/player.swf?url=http%3A%2F%2Fapi.soundcloud.com%2Ftracks%2F55462399"></param> <param name="allowscriptaccess" value="always"></param> <embed allowscriptaccess="always" height="81" src="https://player.soundcloud.com/player.swf?url=http%3A%2F%2Fapi.soundcloud.com%2Ftracks%2F55462399" type="application/x-shockwave-flash" width="100%"></embed> </object>  <span><a href="http://soundcloud.com/lee-daniel-gauthier/waveguidetestpitch">WaveguideTestPitch</a> by <a href="http://soundcloud.com/lee-daniel-gauthier">Leesifer</a></span>

