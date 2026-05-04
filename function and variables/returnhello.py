def greet(input):
    if "hello" in input:
        return "hello, there"
    else:
        return "I'm not sure what you mean by that"


greeting = greet("hello, computer")
print("hm, " + greeting + " Sam")