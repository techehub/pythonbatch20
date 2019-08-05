data = {"111":{"name": "kumar",
                "sem1":{
                    "s1":33,
                    "s3": 44

                    },
               "sem2": {
                   "s1": 33,
                   "s3": 44

               }
               },

        "222":{"name": "seetha",
                "mark":[44,88,56]
               }
        }



for k,v in data.items():
    total = 0
    for x, y in v.items() :

        if x=="mark":
            for mark in y:
                total = total + mark
    print (k,v['name'], total )





