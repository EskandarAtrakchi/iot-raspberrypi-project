import random

#data will be just randomly generated
def getTemp():
    return round(random.uniform(20, 30), 2)

def getHumidity():
    return round(random.uniform(40, 70), 2)

def getLight():
    return random.randint(0, 1)
