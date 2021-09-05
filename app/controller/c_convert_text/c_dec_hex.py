from typing import List

def convert_decimal_to_hex(dec_list: List[int]):
    hex_list: List[hex] = list()
    for dec in dec_list:
        hex_list.append(hex(dec))

    response_data = (
            {
                'isResult' : True,
                'code' : 'SUCCESS',
                'data' : {
                    'output': hex_list
                }
            }, 200
        )
    
    return response_data

def convert_hex_to_decimal(hex_list: List[hex]):
    dec_list: List[int] = list()
    for hex_element in hex_list:
        dec_list.append(int(hex_element, 16))
    
    response_data = (
            {
                'isResult' : True,
                'code' : 'SUCCESS',
                'data' : {
                    'output': dec_list
                }
            }, 200
        )
    
    return response_data