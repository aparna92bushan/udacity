from collections import defaultdict

def ff():
    return "aparna"
ddict = defaultdict(ff)
ddict['x'] = 12

# print(ddict.__missing__('xv'))
print(ddict)
def_dict = defaultdict(list)
for i in range(0, 5):
    def_dict[i].append(i)

print(type(def_dict[0]))
print(def_dict)

dd3 = defaultdict(int)
for i in range(10, 20):
    dd3[i] = i
print(dd3)