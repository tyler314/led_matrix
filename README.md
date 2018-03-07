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
        { MP_ROM_QSTR(MP_QSTR_derp), MP_ROM_PTR(&mp_module_derp) }, \

Adding a Function
-----------------
To add a simple function, add the following code immediately after the includes,

    #include <stdio.h>
    
    STATIC mp_obj_t derp_printy(void) {
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

Adding a Class
--------------
To create a Python class in C, we must do so using a C-struct.
In this example, we will create a class called `myLEDs` of the micropython module `derp`.
the class constructor takes in one integer, and sets it to the class's only field, `led_number `.
To follow along, add the following code in order, beginning immediately after the last
`#include` in your c file.

    // Define variable and function prototypes
    const mp_obj_type_t derp_myLEDs_type;
    mp_obj_t derp_myLEDs_make_new(const mp_obj_type_t *type, size_t n_args, size_t n_kw, const mp_obj_t *args);
    STATIC void derp_myLEDs_print(const mp_print_t *print, mp_obj_t self_in, mp_print_kind_t kind);

We must create the C-structure of our new object; it will contain some basic information
about the class, as well as fields of the class. Add the following code next.

    // this is the actual C-structure for the object "myLEDs"
    typedef struct _derp_myLEDs_obj_t {
        // base represents some basic information, like type
        mp_obj_base_t base;
        // a new member created
        uint8_t led_number;
    } derp_myLEDs_obj_t;
    
We are now able to define the methods of the class,

    // Define the constructor, and print function,
    // of the object myLEDs, respectively
    mp_obj_t derp_myLEDs_make_new(const mp_obj_type_t *type,
                                 size_t n_args,
                                 size_t n_kw,
                                 const mp_obj_t *args){
        // check the numer of arguments (min 1, max 1)
        // on an error, raise Python exception
        mp_arg_check_num(n_args, n_kw, 1, 1, true);
        // create a new object of our C-struct/myLEDs type
        derp_myLEDs_obj_t *self = m_new_obj(derp_myLEDs_obj_t);
        // give the new object a type
        self->base.type = &derp_myLEDs_type;
        // set the led_number member with the first argument of the constructor
        self->led_number = mp_obj_get_int(args[0]);
        // return the object itself
        return MP_OBJ_FROM_PTR(self);
    }
    
    STATIC void derp_myLEDs_print(const mp_print_t *print,
                                  mp_obj_t self_in,
                                  mp_print_kind_t kind) {
        // create a pointer to the C-struct of the oject
        derp_myLEDs_obj_t *self = MP_OBJ_TO_PTR(self_in);
        // print the number
        printf("LED number: (%u)", self->led_number);
    }
    
We now must create the table of global members for our class, we will add to this once we
begin adding methods to our class. For now, we leave it empty.

    // create the table of global members for the class
    STATIC const mp_rom_map_elem_t derp_myLEDs_locals_dict_table[] = { };
    STATIC MP_DEFINE_CONST_DICT(derp_myLEDs_locals_dict, derp_myLEDs_locals_dict_table);
    
We now create the class-object type. Our class needs methods, we will add a print method
(similar to `__repr__` in Python), and a constructor, called print and make_new, respectively.
These methods are "inherited" from the mp\_obj\_type\_t, and thus we do not add them to 
the local dict table we just created.

    // create the class-object type
    const mp_obj_type_t derp_myLEDs_type = {
        // inherit the type "type"
        { &mp_type_type },
        // give the type a name
        .name = MP_QSTR_myLEDsObj,
        // give the type a print function
        .print = derp_myLEDs_print,
        // give the type a constructor
        .make_new = derp_myLEDs_make_new,
        // add the global members
        .locals_dict = (mp_obj_dict_t*)&derp_myLEDs_locals_dict,
    };

Now we need to add our object to the module, by adding it into the global member dictionary
of our module:

```    
STATIC const mp_map_elem_t derp_globals_table[] = {
    { MP_ROM_QSTR(MP_QSTR___name__), MP_ROM_QSTR(MP_QSTR_derp) },
    { MP_ROM_QSTR(MP_QSTR_printy), (mp_obj_t)&derp_printy_obj },
    { MP_OBJ_NEW_QSTR(MP_QSTR_myLEDs), (mp_obj_t)&derp_myLEDs_type },
};
```

Adding a Method to Our Class
----------------------------
Adding a method only requires us to do a few things, in this example we will create a
method that does nothing, and returns the `None` object. It isn't very interesting, but it
will demonstrate what is required to add a method to our new class.

Add the following code immediately below your last class method, so in this example, it
would be below the `derp_myLEDs_print` method.

    STATIC mp_obj_t derp_myLEDs_blink(mp_obj_t self_in){
        return mp_const_none;
    }
    MP_DEFINE_CONST_FUN_OBJ_1(derp_myLEDs_blink_obj, derp_myLEDs_blink);
    
Notice how these methods always pass in a `mp_obj_t` type we call `self_in`. If you're
familiar with the intricacies of Python, you'll know that every method passes in an instance
of that class, this is what `self_in` is. This allows us to access the objects fields, or
in this case, the struct's fields. This method returns `None`, which in the C code is
`mp_const_none`, which is of type `mp_obj_t`.

We now need to add this method to the locals dict.

    STATIC const mp_rom_map_elem_t derp_myLEDs_locals_dict_table[] = {
        { MP_ROM_QSTR(MP_QSTR_blink), MP_ROM_PTR(&derp_myLEDs_blink_obj) },
    };