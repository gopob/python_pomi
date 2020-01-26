counter = {}
string = ''

f = open("input.txt", "r")

string = f.readline()

for word in string:
    counter[word] = counter.get(word, 0) + 1

for key in counter:
    print(key+' -> '+str(counter[key]))