#Pyo Markdown - Kayla Blackburn 11/04/21
-
##
-
>Debugging is in fact frustrating! I have yet to figure out why I am still
receiving one error no matter what solution I try from researching.

>I am able to start the steps and able to get through the initial instructions
in the Debugging Markdown.

python3 -m pip install --upgrade pip to
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" - success!

>This is the point at which I start running into errors.

brew install liblo libsndfile portaudio portmidi - not success! :/

>These are the two error messages I get despite trying all the soutions I had
researched, what was suggested in class, and what was on the developer's Github.

include/servermodule.h:31:10: fatal error: 'sndfile.h' file not found
#include "sndfile.h"
         ^~~~~~~~~~~
1 error generated.
error: command '/usr/bin/gcc' failed with exit code 1
Kaylas-MacBook-Pro:pyo kaylablackburn$


include/ad_portaudio.h:25:10: fatal error: 'portaudio.h' file not found
#include "portaudio.h"
         ^~~~~~~~~~~~~
1 error generated.
error: command '/usr/bin/gcc' failed with exit code 1
Kaylas-MacBook-Pro:pyo kaylablackburn$

>This is what was on the developer's Github that still did not fix my error.

Tried this - brew install libsndfile

-bash: brew: command not found
Kaylas-MacBook-Pro:pyo kaylablackburn$  

in both error messages
