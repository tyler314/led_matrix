#include "py/nlr.h"
#include "py/obj.h"
#include "py/runtime.h"
#include "py/binary.h"
#include "portmodules.h"
#include "pin.h"

// Define variable and function prototypes
const mp_obj_type_t led_matrix_LEDMatrix_type;
mp_obj_t led_matrix_LEDMatrix_make_new(const mp_obj_type_t *type, size_t n_args, size_t n_kw, const mp_obj_t *args);

// this is the actual C-structure for the object "LEDMatrix"
typedef struct _led_matrix_LEDMatrix_obj_t {
    // base represents some basic information, like type
    mp_obj_base_t base;
    // Pin objects from pin.h
    pin_obj_t R1;
    pin_obj_t R2;
    pin_obj_t B1;
    pin_obj_t B2;
    pin_obj_t G1;
    pin_obj_t G2;
    pin_obj_t A;
    pin_obj_t B;
    pin_obj_t C;
    pin_obj_t D;
    pin_obj_t OE;
    pin_obj_t LAT;
    pin_obj_t CLK;
    // boolean
    mp_obj_t smallBoard;
} led_matrix_LEDMatrix_obj_t;

// Define the constructor, functions & methods,
mp_obj_t led_matrix_LEDMatrix_make_new(const mp_obj_type_t *type,
                             size_t n_args,
                             size_t n_kw,
                             const mp_obj_t *args){
    // check the numer of arguments
    // on an error, raise Python exception
    mp_arg_check_num(n_args, n_kw, 1, 1, true);
    // create a new object of our C-struct/myLEDs type
    led_matrix_LEDMatrix_obj_t *self = m_new_obj(led_matrix_LEDMatrix_obj_t);
    // give the new object a type
    self->base.type = &led_matrix_LEDMatrix_type;
    // Set the fields
    
    // set smallBoard with the first argument of the constructor
    self->smallBoard = mp_obj_new_bool(mp_obj_get_int(args[0]));
    // return the object itself
    return MP_OBJ_FROM_PTR(self);
}

STATIC mp_obj_t led_matrix_LEDMatrix_set_RGB_pins(size_t n_args, const mp_obj_t *args) {
    led_matrix_LEDMatrix_obj_t *self = args[0]; // MP_OBJ_TO_PTR(self_in);
    // TODO: make new "object", call constructor
    self->R1 = *((pin_obj_t*) &args[1]);
    self->R2 = *((pin_obj_t*) &args[2]);
    self->B1 = *((pin_obj_t*) &args[3]);
    self->B2 = *((pin_obj_t*) &args[4]);
    self->G1 = *((pin_obj_t*) &args[5]);
    self->G2 = *((pin_obj_t*) &args[6]);
    return mp_const_none;
}
STATIC MP_DEFINE_CONST_FUN_OBJ_VAR_BETWEEN(led_matrix_LEDMatrix_set_RGB_pins_obj, 7, 7, led_matrix_LEDMatrix_set_RGB_pins);

STATIC mp_obj_t led_matrix_LEDMatrix_set_row_select_pins(size_t n_args, const mp_obj_t *args){
    led_matrix_LEDMatrix_obj_t *self = args[0];
    // TODO: make new "object", call constructor
    self->A = *((pin_obj_t*) &args[1]);
    self->B = *((pin_obj_t*) &args[2]);
    self->C = *((pin_obj_t*) &args[3]);
    self->D = *((pin_obj_t*) &args[4]);
    return mp_const_none;
}
STATIC MP_DEFINE_CONST_FUN_OBJ_VAR_BETWEEN(led_matrix_LEDMatrix_set_row_select_pins_obj, 5, 5, led_matrix_LEDMatrix_set_row_select_pins);

STATIC mp_obj_t led_matrix_LEDMatrix_set_control_pins(size_t n_args, const mp_obj_t *args){
    led_matrix_LEDMatrix_obj_t *self = args[0];
    // TODO: make new "object", call constructor
    self->LAT = *((pin_obj_t*) &args[1]);
    self->OE = *((pin_obj_t*) &args[2]);
    self->CLK = *((pin_obj_t*) &args[3]);
    return mp_const_none;
}
STATIC MP_DEFINE_CONST_FUN_OBJ_VAR_BETWEEN(led_matrix_LEDMatrix_set_control_pins_obj, 4, 4, led_matrix_LEDMatrix_set_control_pins);

// create the table of global members for the class
STATIC const mp_rom_map_elem_t led_matrix_LEDMatrix_locals_dict_table[] = { 
    { MP_ROM_QSTR(MP_QSTR_set_RGB_pins), MP_ROM_PTR(&led_matrix_LEDMatrix_set_RGB_pins_obj) },
    { MP_ROM_QSTR(MP_QSTR_set_row_select_pins), MP_ROM_PTR(&led_matrix_LEDMatrix_set_row_select_pins_obj) },
    { MP_ROM_QSTR(MP_QSTR_set_control_pins), MP_ROM_PTR(&led_matrix_LEDMatrix_set_control_pins_obj) },
};
STATIC MP_DEFINE_CONST_DICT(led_matrix_LEDMatrix_locals_dict, led_matrix_LEDMatrix_locals_dict_table);

// create the class-object type
const mp_obj_type_t led_matrix_LEDMatrix_type = {
    // inherit the type "type"
    { &mp_type_type },
    // give the type a name
    .name = MP_QSTR_LEDMatrixObj,
    // give the type a constructor
    .make_new = led_matrix_LEDMatrix_make_new,
    // add the global members
    .locals_dict = (mp_obj_dict_t*)&led_matrix_LEDMatrix_locals_dict,
};

STATIC const mp_map_elem_t led_matrix_globals_table[] = {
    { MP_ROM_QSTR(MP_QSTR___name__), MP_ROM_QSTR(MP_QSTR_led_matrix) },
    { MP_ROM_QSTR(MP_QSTR_LEDMatrix), (mp_obj_t)&led_matrix_LEDMatrix_type },
};

STATIC MP_DEFINE_CONST_DICT (
    mp_module_led_matrix_globals,
    led_matrix_globals_table
);

const mp_obj_module_t mp_module_led_matrix = {
    .base = { &mp_type_module },
    .globals = (mp_obj_dict_t*)&mp_module_led_matrix_globals,
};