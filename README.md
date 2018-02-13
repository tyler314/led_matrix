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

Instructions on how to flash the pyboard using the `firmware.dfu` file can be found here:
https://github.com/micropython/micropython/wiki/Pyboard-Firmware-Update

Instructions on how to inject your own C code within the Micropython source code
--------------------------------------------------------------------------------

You must first create your C file in `ports/stm32`, and add references to it in several
files. Say you want to add the file titled `derp.c`, you must first add a reference to it
in the Makefile within the `ports/stm32` folder, to the list of source files in the `SRC_C`

    SRC_C = \
            main.c \
            system_stm32.c \
            stm32_it.c \
            ...
            derp.c \
            ...
        
Next, create the file `derp.c` within the `ports/stm32` folder, and add the following code

    #include "py/nlr.h"
    #include "py/obj.h"
    #include "py/runtime.h"
    #include "py/binary.h"
    #include "portmodules.h"
    
    STATIC const mp_map_elem_t derp_globals_table[] = {
        { MP_ROM_QSTR(MP_QSTR___name__), MP_ROM_QSTR(MP_QSTR_derp) },
    };
    
    STATIC MP_DEFINE_CONST_DICT (
        mp_module_derp_globals,
        derp_globals_table
    );
    
    const mp_obj_module_t mp_module_derp = {
        .base = { &mp_type_module },
        .globals = (mp_obj_dict_t*)&mp_module_derp_globals,
    };
    
This code defines a python module, using `mp_obj_module_t` type, and then initializes
some of its fields, such as the base type, the name, and the dictionary of globals for
that module. In that dictionary, it defines one variable, \_\_name\_\_, with the name of
our module in it.

Now, for this module to be available for import, we need to add it to
mpconfigport.h file to MICROPY\_PORT\_BUILTIN\_MODULES:

    extern const struct _mp_obj_module_t mp_module_derp;
    
    #define MICROPY_PORT_BUILTIN_MODULES \
        { MP_ROM_QSTR(MP_QSTR_umachine), MP_ROM_PTR(&machine_module) }, \
        ...
        { MP_ROM_QSTR(MP_QSTR_mymodule), MP_ROM_PTR(&mp_module_mymodule) }, \

Adding a Function
-----------------
To add a simple function, add the following code immediately after the includes,

    #include <stdio.h>
    
    STATIC mp_obj_t mymodule_printy(void) {
        printf("Hello world!\n");
        return mp_const_none;
    }
    STATIC MP_DEFINE_CONST_FUN_OBJ_0(derp_printy_obj, derp_printy);
    
This creates a function object `derp_printy_obj` which takes no arguments, and when it is
called, executes the C function `derp_printy`. Our function must return something, and in
this case it returns `None`. To add the function to our module, add this second line of
code within the `derp_globals_table` you already defined:

    STATIC const mp_map_elem_t derp_globals_table[] = {
        { MP_ROM_QSTR(MP_QSTR___name__), MP_ROM_QSTR(MP_QSTR_derp) },
        { MP_ROM_QSTR(MP_QSTR_printy), (mp_obj_t)&derp_printy_obj },
    };

Micropython uses the QSTR macros to define constant strings. You must add `Q(printy)` to
the end of the file `ports/stm32/qstrdefsport.h`, this will define the string `printy` for
Micropython.
