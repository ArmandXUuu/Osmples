# a util for file read and write


import os
import json


def json_output(in_struct, pretty=False):  # parm pretty aims to output a beautiful, readable string
    if pretty:
        print(json.dumps(in_struct, indent=4, default=str))
        return
    print(json.dumps(in_struct, default=str))