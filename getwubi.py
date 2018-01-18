import sys

fo1 = open("Encode/cl_utf8.txt","r")
dic_wubi = dict()

while 1:
    line = fo1.readline()

    if not line:
        break

    line = line.split()
    word = line[0]
    wubi = line[2]
    dic_wubi[word] = wubi

fo1.close()

fo2 = open("pre_chars_for_w2v.txt","r")
fo3 = open("pre_wubi_for_w2v.txt","a")

total_lines = len(fo2.readlines())
lines = 0
fo2.close()

fo2 = open("pre_chars_for_w2v.txt","r")

while 1:
    line = fo2.readline()
    line = line.split()

    lines = lines + 1
    progress = float(lines) / total_lines * 100.00
    sys.stdout.write("Progress: %.2f%%      \r" % (progress))
    sys.stdout.flush()

    for word in line:
        if(dic_wubi.has_key(word)):
            fo3.write(dic_wubi[word])
        else:
            fo3.write(word)
        fo3.write(' ')

    fo3.write('\n')

    if lines==total_lines:
        break

fo2.close()
fo3.close()

train_char = ["Corpora/pku/train-all.txt","Corpora/cityu/train-all.txt","Corpora/msr/train-all.txt","Corpora/ctb/train-all.txt"]

train_wubi = ["Corpora/pku/train-all_wubi.txt","Corpora/cityu/train-all_wubi.txt","Corpora/msr/train-all_wubi.txt","Corpora/ctb/train-all_wubi.txt"]

for i in range(4):
    fo2 = open(train_char[i],"r")
    fo3 = open(train_wubi[i],"a")

    total_lines = len(fo2.readlines())
    lines = 0
    fo2.close()

    fo2 = open(train_char[i],"r")

    while 1:
        line = fo2.readline()
        line = line.split()

        lines = lines + 1
        progress = float(lines) / total_lines * 100.00
        sys.stdout.write("Progress of "+train_wubi[i]+": %.2f%% \r" % (progress))
        sys.stdout.flush()

        for word in line:
            if(dic_wubi.has_key(word)):
                fo3.write(dic_wubi[word])
            else:
                fo3.write(word)
            fo3.write(' ')

        fo3.write('\n')

        if lines==total_lines:
            break

    fo2.close()
    fo3.close()

