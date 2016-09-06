with open('./t.txt', 'r') as f: # with is like try ... finally f.close, become sample.
    for line in f.readlines():
        print(line.strip()) # 把末尾的'\n'删掉
