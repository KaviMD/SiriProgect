''' Write '''
file = open("weather.txt", "w")
file.write("hello world in the new file")
file.close()

''' Read '''
file = open('weather.txt', 'r')
data = file.read()
file.close()
print data
