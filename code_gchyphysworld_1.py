mm = {'A': '-',
 'B': '-',
 'C': '-',
 'D': '-',
 'E': '-',
 'F': '-',
 'G': '-',
 'H': '-',
 'I': '-',
 'J': '-',
 'K': '-',
 'L': '-',
 'M': '-',
 'N': '-',
 'O': '-',
 'P': '-',
 'Q': '-',
 'R': '-',
 'S': '-',
 'T': '-',
 'U': '-',
 'V': '-',
 'W': '-',
 'X': '-',
 'Y': '-',
 'Z': '-',
 ' ' : ' ',
 ':' : ':'}


code = "TNVERI SMH EG ZSMRNPMUD KEPLER: M SLRN PYMP VERRNVPT M ZSMRNP PE PYN TQR THNNZT EQP NXQMS MUNMT LR NXQMS PLKNT"

def decode() :
    return "".join([mm[x] for x in list( code )])
