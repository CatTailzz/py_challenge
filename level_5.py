from urllib.request import urlopen
import pickle

data = pickle.load(urlopen('http://www.pythonchallenge.com/pc/def/banner.p'))
print(data)

for line in data:
    print("".join(k * v for k, v in line))

# channel
