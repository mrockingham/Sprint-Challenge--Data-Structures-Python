import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
#for name_1 in names_1:
 #   for name_2 in names_2:
  #      if name_1 == name_2:
   #         duplicates.append(name_1)

class BSTN:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTN(value)
            else:
                self.left.insert(value)
        elif value >= self.value:
            if self.right is None:
                self.right = BSTN(value)
            else:
                self.right.insert(value)

    def contains(self, list_name):
        if self.value == list_name:
            return True
        elif self.value > list_name:
            if self.left is None:
                return False
            else:
                return self.left.contains(list_name)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(list_name)

names = None
for name in names_1:
    if names is None:
        names = BSTN(name)
    else:
        names.insert(name)

for name in names_2:
    if names.contains(name):
        duplicates.append(name)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
