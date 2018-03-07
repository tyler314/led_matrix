#include "py/nlr.h"
#include "py/obj.h"
#include "py/runtime.h"
#include "py/binary.h"
#include "portmodules.h"
#include <stdio.h>
#include <led.h>


// CLASS BEGIN
// Define variable and function prototypes
const mp_obj_type_t derp_myLEDs_type;
mp_obj_t derp_myLEDs_make_new(const mp_obj_type_t *type, size_t n_args, size_t n_kw, const mp_obj_t *args);
STATIC void derp_myLEDs_print(const mp_print_t *print, mp_obj_t self_in, mp_print_kind_t kind);

// this is the actual C-structure for the object "myLEDs"
typedef struct _derp_myLEDs_obj_t {
    // base represents some basic information, like type
    mp_obj_base_t base;
    // LED number
    pyb_led_t led_number;
} derp_myLEDs_obj_t;

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
//     self->led_number = mp_obj_get_int(args[0]);
    switch(mp_obj_get_int(args[0])) {
        case 1:
            self->led_number = PYB_LED_RED;
            break;
        case 2:
            self->led_number = PYB_LED_GREEN;
            break;
        case 3:
            self->led_number = PYB_LED_YELLOW;
            break;
        case 4:
            self->led_number = PYB_LED_BLUE;
            break;
        default:
            self->led_number = PYB_LED_RED;
    }
    // return the object itself
    return MP_OBJ_FROM_PTR(self);
}

STATIC void derp_myLEDs_print(const mp_print_t *print,
                              mp_obj_t self_in,
                              mp_print_kind_t kind) {
    // create a pointer to the C-struct of the oject
    derp_myLEDs_obj_t *self = MP_OBJ_TO_PTR(self_in);
    // print the number
    printf("LED number: %u", self->led_number);
}

STATIC mp_obj_t derp_myLEDs_blink(mp_obj_t self_in){
    derp_myLEDs_obj_t *self = MP_OBJ_TO_PTR(self_in);
    led_toggle(self->led_number);
    return mp_const_none;
}
MP_DEFINE_CONST_FUN_OBJ_1(derp_myLEDs_blink_obj, derp_myLEDs_blink);

// create the table of global members for the class
STATIC const mp_rom_map_elem_t derp_myLEDs_locals_dict_table[] = {
    { MP_ROM_QSTR(MP_QSTR_blink), MP_ROM_PTR(&derp_myLEDs_blink_obj) },
};
STATIC MP_DEFINE_CONST_DICT(derp_myLEDs_locals_dict, derp_myLEDs_locals_dict_table);
          
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
// CLASS END             
STATIC mp_obj_t derp_printy(void){
    printf("Tyler is the coolest.\n");
    return mp_const_none;
}
STATIC MP_DEFINE_CONST_FUN_OBJ_0(derp_printy_obj, derp_printy);

STATIC const mp_map_elem_t derp_globals_table[] = {
    { MP_ROM_QSTR(MP_QSTR___name__), MP_ROM_QSTR(MP_QSTR_derp) },
    { MP_ROM_QSTR(MP_QSTR_printy), (mp_obj_t)&derp_printy_obj },
    { MP_OBJ_NEW_QSTR(MP_QSTR_myLEDs), (mp_obj_t)&derp_myLEDs_type },
};

STATIC MP_DEFINE_CONST_DICT (
    mp_module_derp_globals,
    derp_globals_table
);

const mp_obj_module_t mp_module_derp = {
    .base = { &mp_type_module },
    .globals = (mp_obj_dict_t*)&mp_module_derp_globals,
};
