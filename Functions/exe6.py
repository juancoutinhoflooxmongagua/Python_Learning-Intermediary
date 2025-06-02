

def hello(msg):
    return msg

def execute(function, msg):
    return function(msg)


variable = execute(hello, 'Buenos dias')

print(variable)