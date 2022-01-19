from typing import List

def convert_from_dec(to_type: str, data_list: List[int]):
    
    result_list: List[str] = list()
    for data in data_list:
        if to_type == "bin":
            result_list.append(str(bin(data)))
        elif to_type == "oct":
            result_list.append(str(oct(data)))
        elif to_type == "hex":
            result_list.append(str(hex(data)))

    response_data = (
            {
                'isResult' : True,
                'code' : 'SUCCESS',
                'data' : {
                    'output': result_list
                }
            }, 200
        )
    
    return response_data


def convert_from_bin(to_type: str, data_list: List[bin]):
    
    result_list: List[str] = list()
    for data in data_list:
        if to_type == "dec":
            result_list.append(int(data, 2))
        elif to_type == "oct":
            result_list.append(oct(int(data, 2)))
        elif to_type == "hex":
            result_list.append(hex(int(data, 2)))

    response_data = (
            {
                'isResult' : True,
                'code' : 'SUCCESS',
                'data' : {
                    'output': result_list
                }
            }, 200
        )
    
    return response_data


def convert_from_oct(to_type: str, data_list: List[oct]):
    
    result_list: List[str] = list()

    for data in data_list:
        if to_type == "bin":
            result_list.append(int(data, 8))
        elif to_type == "dec":
            result_list.append(int(data, 8))
        elif to_type == "hex":
            result_list.append(int(data, 8))

    response_data = (
            {
                'isResult' : True,
                'code' : 'SUCCESS',
                'data' : {
                    'output': result_list
                }
            }, 200
        )
    return response_data


def convert_from_hex(to_type: str, data_list: List[hex]):
    
    result_list: List[str] = list()
    for data in data_list:
        if to_type == "bin":
            result_list.append(bin(int(data, 16)))
        elif to_type == "oct":
            result_list.append(oct(int(data, 16)))
        elif to_type == "dec":
            result_list.append(int(data, 16))

    response_data = (
            {
                'isResult' : True,
                'code' : 'SUCCESS',
                'data' : {
                    'output': result_list
                }
            }, 200
        )
    
    return response_data
