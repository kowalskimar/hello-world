#! python3

import collections
import math

def lcs(str1, str2):
    cached = collections.defaultdict(dict)
    tokens1, tokens2 = str1.split(), str2.split()
    for i in range(-1, len(tokens1)):
        for j in range(-1, len(tokens2)):
            if i == -1 or j == -1:
                cached[i][j] = [[]]
            else:
                if tokens1[i] == tokens2[j]:
                    out = [x + [(tokens1[i], j)] for x in cached[i - 1][j - 1]]
                else:
                    a, b = cached[i - 1][j], cached[i][j - 1]
                    if len(a[0]) == len(b[0]):
                        out = a + b if a[len(a) - 1] != b[len(b) - 1] else a
                    else:
                        out = a if len(a[0]) > len(b[0]) else b
                cached[i][j] = out
    return cached[len(tokens1) - 1][len(tokens2) - 1]

def seq_contiguity(subseqs, dl):
    score = 0
    
    for subseq in subseqs:
        seq = [y for x, y in subseq]
        seq1=[x for x, y in subseq]
        print(seq1)
        print(len(seq1))
        val, ent = 1, 0.
        dlugosc = 0
    
        for idx in range(0, len(seq1)):
            if seq1[idx] != "":
                dlugosc = dlugosc + len(seq1[idx])
                
        print("dlugosc:", dlugosc)
        print("dl:", dl)
        score = 2.0 * dlugosc / dl
    
        """for idx in range(1, len(seq)):
            if seq[idx] == seq[idx - 1] + 1:
                val += 1
            else:
                ent += val * math.log(val)
                val = 1
        ent += val * math.log(val)
        score = max(score, ent)"""
    return score

s1 = "can i transfer my wallet balance to my bank account\nala ma kota"
s2 = "can i transfer my bank balancee to my wallet\nala ma kota"
#s2 = "can i transfer my wallet balance to my bank account"

#s1 = "ala ma kota"
#s2 = "ala ma kota"

print(s1)
print(s2)
print(lcs(s1, s2))

print("score:",seq_contiguity(lcs(s1, s2), len(s1.replace(" ", "")) + len(s2.replace(" ", ""))))
