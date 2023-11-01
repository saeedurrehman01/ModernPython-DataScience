from typing import Dict, Union,Optional
import pprint

Key = Union[int,str] # create custom type
Value = Union[int,str,list,dict,tuple,set] # create custom type

data : Dict[Key,Value] = {"FName":"Muhammad Aslam",
                        "Name": "Muhammad Qasim",
                        "Education":"MSDS",
                        "Age": 25}

data["Name"] = "Muhammad Ali"

pprint.pprint(data)
print(data["Name"])

print(data["Age"])

[i for i in dir(data) if "__" not in i]