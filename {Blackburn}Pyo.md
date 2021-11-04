#Pyo Markdown - Kayla Blackburn 11/04/21
-
##
-
>Debugging is in fact frustrating! I have yet to figure out why I am still
receiving one error no matter what solution I try from researching.

python3 -m pip install --upgrade pip to
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" - success!

brew install liblo libsndfile portaudio portmidi - not success! :/

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

Tried this - brew install libsndfile

-bash: brew: command not found
Kaylas-MacBook-Pro:pyo kaylablackburn$  

in both error messages
