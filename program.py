
#========== READ FILE TXT AND MAKE ARRAY GEJALA ============
def readFile(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines

def readText(lines):
    text = []
    for line in lines:
        line = line.replace('.', '')
        line = line.split(': ')
        text.append(line)
    return text

def makeArrGejala(text):
    gejala = []
    for gejala_ in text:
        gejala.append(gejala_)
    return gejala

def countGejala(gejala):
    c_gejala = gejala[1].split(', ')
    return len(c_gejala)

#TEST
arrGejala = makeArrGejala(readText(readFile("test.txt")))
#print(arrGejala)



#========== READ INPUT AND MAKE ARRAY INPUT ============
def readInput(string):
    input = []
    string = string.replace('.', '')
    string = string.split(', ')
    input = string
    return input


#========== ALGORITMA BOYER MOORE ============
def lastOcc(arr, c):
    n = len(arr) - 1 
    while(n != 0):
        if(arr[n] != c):
            n -= 1
        else:
            return n
    return -1


def boyerMoore(line, pattern):
    if(len(pattern) > len(line)):
        return -1
    else:
        n = len(line)
        m = len(pattern)
        i = j = m - 1
        while(i != n):
            if line[i].lower() == pattern[j].lower():
                if j == 0:
                    return i
                else:
                    i -= 1
                    j -= 1
            else:
                c = line[i]
                l = lastOcc(line, c)
                i = i + m - min(j, 1+l)
                j = m - 1 

        return -1


#========== SEARCH POSSIBLE DISEASE BY SYMPTON ============
def searchPossibleDisease(input, arrGejala):
    hasil_diagnosa = []
    for gejala in arrGejala:
        possible = True
        for p in input:
            if (boyerMoore(gejala[1], p) == -1):
                possible = False
                break
        if (possible):
            hasil_diagnosa.append(gejala)
    return hasil_diagnosa

def sortPossibleDisease(input, hasil):
    sorted_hasil = []
    for h in hasil:
        if (countGejala(h) == len(input)):
            sorted_hasil.append(h)
    for h in hasil:
        if (h not in sorted_hasil):
            sorted_hasil.append(h)
    return sorted_hasil

""" #TEST
hasil_diagnosa = sortPossibleDisease(input, searchPossibleDisease(input, arrGejala))
if (len(hasil_diagnosa) > 0):
    for h in hasil_diagnosa:
        print(h)
else:
    print("No diease have tha symptons you want")  """       


#main
print("")
print("Tools to Help Narrowing Down All Possible Diseases")
try:
    string = input("Symptons: ")
    input = readInput(string)
    #print(input)
    print("")
    hasil_diagnosa = sortPossibleDisease(input, searchPossibleDisease(input, arrGejala))
    if (len(hasil_diagnosa) > 0):
        print("Possible disease with that sympton is: ")
        k=1
        for h in hasil_diagnosa:
            print(str(k)+". "+h[0])
            k+=1
    else:
        print("No diease have tha symptons you want")  
except:
    print("Input symptons failed")