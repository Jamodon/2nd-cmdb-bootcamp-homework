import sys

#k-mer counter: figure out where it is between calls to get next line
class BLASTReader(object): #has variables (properties) and functionality #Class is like a platonic ideal
    def __init__(self, file):
        self.file = file
        self.last_sid = None
    def next(self):
        if self.last_sid is None:
            line = ""#sys.stdin.readline() #read first line from file
            #assert line.startswith (">") #crashes program if first line doesn't start with >
            #sid = line[1:].rstrip("\r\n") #remove first character off string (the >) then strip off returns
            sid = ""
        else:
            sid = self.last_sid

        sequences = []
        while True:
                line = sys.stdin.readline()
                if line == "" and not sequences: #at the end of the file, stop
                    raise StopIteration
                elif line.startswith("Query="): #trying to add fly gene
                    self.last_sid1 = line[0:].rstrip("\r\n")[25:] #highly non-generalizable hardcode to remove Query=..."" text
                    break
                elif line.startswith("> N") or line == "":
                    self.last_sid = self.last_sid1 + line[1:].rstrip("\r\n")
                    break
                else:
                    sequences.append(line.strip()) #strips all white space
            
        sequence = ":".join(sequences) #join together the list using : as a delimiter
        sequence = sequence.split(":")[3]
        sequence = sequence.replace("Identities = ", "")
        sequence = sequence.replace("Gaps = ", "")
        return sid, sequence
    def __iter__(self):
        return self