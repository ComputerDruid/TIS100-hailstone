Hailstone for TIS-100
=====================

This is a hailstone problem for TIS-100 (a [game] by Zachtronics). 

[More about hailstone numbers][hailstone].

[hailstone]: https://en.wikipedia.org/wiki/Collatz_conjecture
[game]: http://www.zachtronics.com/tis-100/

Problem specification
---------------------

    > READ A VALUE FROM IN
    > IF EVEN, HALVE THE VALUE
    > IF ODD, TRIPLE THE VALUE AND ADD 1
    > REPEAT UNTIL VALUE IS 1
    > WRITE THE REPETITION COUNT TO OUT
