file_name = 'text.txt'  
def word_count(fname):
    with open(fname) as f:
        return sum(len(line.split()) for line in f)
print("Number of words:")
print(word_count(file_name)) 