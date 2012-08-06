Synthesizing trumpet tones with Marsyas using FM synthesis
==========================================================

We are going to emulate a trumpet tone according to the two operator method
described by Dexter Morrill in the first edition of the computer music journal.

Contents
--------

* [Prerequisites](README.md#prerequisites)

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

I'm also assuming you have some experience with python.

