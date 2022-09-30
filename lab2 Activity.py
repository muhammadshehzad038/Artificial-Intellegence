
# Activity no 1
List1 = []
for i in range(5):
    n = int(input("enter a value"))
    List1.append(n)
List2 = []

for i in range(5):
    n = int(input("enter a value"))
    List2.append(n)
List = List1 + List2
print(List)


# Activity no 2:

def ispalindrome(word):
    temp = word[0::-1]
    if word.Capitalize() == temp.capitalize():
        return True
    else:
        return False


print(ispalindrome("deed"))


# Activity no 3:

def symmdiff(a, b):
    c = set()
    for v in a:
        if v not in b:
            c.add(v)

    for v in b:
        if v not in a:
            c.add(v)
            return c


set1 = {1, 2, 3, 4}
set2 = {5, 6, 7, 8}
print(symmdiff(set2, set1))
print(set1.symmetric_difference(set2))
print(set2.symmetric_difference(set1))
print(set1 ^ set2)
print(set2 ^ set1)
'''
'''
# Activity no 4:

sample = {("ali", "shehzad"): "03393748343434", ("nouman", "kamran"): "254r256352263"}
first = input("enter first name")
last = input("enter last name")

searchtuple = (first, last)
if searchtuple in sample:
    print(sample[searchtuple])
else:
    print("name not found")

# Activity no 5:
a = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
c = [[], [], []]
for indrow in range(3):
    c.append([])
    for indcol in range(3):
        c[indrow].append(0)
        for indaux in range(3):
            c[indrow][indcol] += a[indrow][indaux] * b[indcol][indaux]
print(c)


# Activity no 6:
def perimeter(listining):
    leng = len(listining)
    peri = 0
    for i in range(0, leng - 1):
        dist = ((listining[i][0] - listining[i + 1][0]) +
                (listining[i][1] + listining[i + 1][1])) ** 0.5
        peri = peri + dist
        return peri


L = [(1, 3), (2, 7), (1, 9)]
print(perimeter(L))
