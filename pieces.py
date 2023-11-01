#!env Python3.11

from icecream import ic
import numpy as np

ORIENTATION_D = {
    'red': 'right',
    'orange': 'left',
    'white': 'bottom',
    'yellow': 'top',
    'blue': 'front',
    'green': 'back'
}

#positive means the orientation go away from the observer
# red, blue and yellow are positives
# orange, green and white are negatives
# [x,-x,y,-y,z,-z]

COLOR_AMPLYFIER = {
    'no': 1,
    'white': 2,
    'yellow': 3,
    'red': 4,
    'orange': 5,
    'green': 6,
    'blue': 7
}
COLOR_ID = ['', 'no', 'white', 'yellow', 'red', 'orange', 'green', 'blue']

# whit the cube solved and whit standard orientation the yellow-red-blue corner
corner = [1,7,4,1,3,1]

upper_layer = [
    [6,1,1,5,3,1],[6,1,1,1,3,1],[6,1,4,1,3,1],
    [1,1,1,5,3,1],[1,1,1,1,3,1],[1,1,4,1,3,1],
    [1,7,1,5,3,1],[1,7,1,1,3,1],[1,7,4,1,3,1]
]

def array_to_dict(array):
    translated = {
        'x': COLOR_ID[array[0]],
        '-x': COLOR_ID[array[1]],
        'y':COLOR_ID[array[2]],
        '-y': COLOR_ID[array[3]],
        'z': COLOR_ID[array[4]],
        '-z': COLOR_ID[array[5]],
    }
    return translated


def layer_to_array_of_dict(layer=upper_layer):
    r_array = ['upper_layer']
    for array in layer:
        tr = array_to_dict(array)
        r_array.append(tr)
    return r_array

upper_layer_dict = layer_to_array_of_dict()

def visuazilize(layer=upper_layer_dict):

    fol = {
        'b1': layer[1]['x'],
        'b2': layer[2]['x'],
        'b3': layer[3]['x'],
        'l1': layer[1]['-y'],
        'l2': layer[4]['-y'],
        'l3': layer[7]['-y'],
        'r1': layer[3]['y'],
        'r2': layer[6]['y'],
        'r3': layer[9]['y'],
        'f1': layer[7]['-x'],
        'f2': layer[8]['-x'],
        'f3': layer[9]['-x'],
        'u1': layer[1]['z'],
        'u2': layer[2]['z'],
        'u3': layer[3]['z'],
        'u4': layer[4]['z'],
        'u5': layer[5]['z'],
        'u6': layer[6]['z'],
        'u7': layer[7]['z'],
        'u8': layer[8]['z'],
        'u9': layer[9]['z']
        }
    
    five1 = f'|invis|{fol["b1"]}|{fol["b2"]}|{fol["b2"]}|invis|\n'
    five2 = f'|{fol["l1"]}|{fol["u1"]}|{fol["u2"]}|{fol["u3"]}|{fol["r1"]}|\n'
    five3 = f'|{fol["l2"]}|{fol["u4"]}|{fol["u5"]}|{fol["u6"]}|{fol["r1"]}|\n'
    five4 = f'|{fol["l3"]}|{fol["u7"]}|{fol["u8"]}|{fol["u9"]}|{fol["r1"]}|\n'
    five5 = f'|invis|{fol["f1"]}|{fol["f2"]}|{fol["f3"]}|invis|\n'
    
    returned = five1 + five2 + five3 + five4 + five5

    return returned


if __name__ == "__main__":
    ic(upper_layer)
    ic(upper_layer_dict)
    ic(visuazilize())




