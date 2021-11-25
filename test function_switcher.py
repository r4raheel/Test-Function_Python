

def testFunction(data):
    # Has to be implemented without IF/ELSE
    switcher = {
        "add": data['val1'] + data['val2'],
        "sub": data['val1'] - data['val2'],
        "mul": data['val1'] * data['val2'],
        "div": data['val1'] / data['val2'],
    }
    
    return switcher.get(data['command'], 1)

testset = [{
    "i": {"command":"add", "val1":1, "val2":2},
    "o": 3
},
    {
        "i" : {"command":"sub", "val1":3, "val2":9},
        "o": -6
    }
    ,
        {
        "i" : {"command":"mul", "val1":3, "val2":9},
        "o": 27
    },
        {
        "i" : {"command":"div", "val1":9, "val2":3},
        "o": 3
    }
]


for test in testset:
    result = testFunction(test["i"])
    if result != test["o"]:
        raise Exception(f'Wrong Result {result} for {test["i"]}')
    print(f'Correct Result: {result} for test {test["i"]}')
