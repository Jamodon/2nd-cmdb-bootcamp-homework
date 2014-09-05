import sys

#k-mer counter: figure out where it is between calls to get next line
class FASTAReader(object): #has variables (properties) and functionality #Class is like a platonic ideal
    def __init__(self, file):
        self.file = file
        self.last_sid = None
    def next(self):
        if self.last_sid is None:
            line = sys.stdin.readline() #read first line from file
            #assert line.startswith (">") #crashes program if first line doesn't start with >
            sid = line[1:].rstrip("\r\n") #remove first character off string (the >) then strip off returns
        else:
            sid = self.last_sid
            
        sequences = []
        while True:
                line = sys.stdin.readline()
                if line == "" and not sequences: #at the end of the file, stop
                    raise StopIteration
                elif line.startswith(">") or line == "":
                    self.last_sid = line[1:].rstrip("\r\n")
                    break
                else:
                    sequences.append(line.strip()) #strips all white space
            
        sequence = "".join(sequences) #join together the list I passed you using this string (the empty string) as a delimiter (thus effectively just concatinating)
        return sid, sequence
    def __iter__(self):
        return self