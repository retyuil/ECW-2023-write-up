# BMPaaS

First, I attempted to request 100 flags from the server in order to perform a frequency analysis on the characters that appear.

Quickly, it became apparent that there were too many zeros. However, in a BMP file, the most common byte is the null one.

So, I decided to request 40,000 flags and examine the most frequent character at each index of the flag.

My code is in resolve.py.