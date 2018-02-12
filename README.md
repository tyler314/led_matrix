# led_matrix
Micropython library used to control Adafruit's RGB LED matrix panel.

Instructions on how to compile source code for STM32 boards
-----------------------------------------------------------

First Download the source code

    $ git clone https://github.com/micropython/micropython.git
    $ cd micropython
    $ git submodule update --init

OPTIONAL: At this point you have the opportunity to add additional custom C modules and other code to the source code.

To compile the code, you will need the ARM compiler, arm-none-eabi-gcc, found here:
https://developer.arm.com/open-source/gnu-toolchain/gnu-rm/downloads

To build for the STM32 family of boards (this includes Pyboard), run the following
commands within the source level folder (e.g. micropython/):

    $ make -C mpy-cross
    $ cd ports/stm32
    $ make BOARD=<name of board> CROSS_COMPILE=<Path where you uncompressed the toolchain>/bin/arm-none-eabi-

Note that BOARD is optional, if you do not include this in the make command, it will be
set to PYBV10 by default (Pyboard V10).
All options for BOARD can be found in folder, [micropython/ports/stm32/boards/](https://github.com/micropython/micropython/tree/master/ports/stm32/boards)

The dfu file used for flashing the board will be located at
micropython/ports/stm32/build-\<BOARD\>/firmware.dfu
