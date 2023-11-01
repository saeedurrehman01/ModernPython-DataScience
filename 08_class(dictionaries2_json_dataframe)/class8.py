from typing import Dict, Union,Optional,Any
import pprint

Key = Union[int,str] # create custom type

Value = Union[int,str,list,dict,tuple,set] # create custom type

data : Dict[Key,Value] = {"FName":"Muhammad Aslam",
                        "Name": "Muhammad Qasim",
                        "Education":"MSDS",
                        "Age": 25,
                        "abc" : [1,2,3],
                        "xyz" : {1,2,3},
                        "efg" : (1,2,3),
                        "asd" : {"a" : 1, "b" : 2}
                        #[1,2,3] : "Pakistan", # error
                        }

print(data["asd"])