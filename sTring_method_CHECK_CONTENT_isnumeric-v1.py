mars_temperature = "The highest temperature on Mars is about 30.54 C"
for item in mars_temperature.split():
    print(item)
    if item.isdecimal():
        print(" ************** Si hay un al menos un DECIMAL ************** ")
        print(item)
        