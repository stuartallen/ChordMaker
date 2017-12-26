notesSharps = ['C', "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
notesFlats = ['C', "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]
majorkeysteps = [0,2,2,1,2,2,2,1]
minorkeysteps = [0,2,1,2,2,1,2,2]
chordSteps = {
    "triad": "0 2 4".split(),
    "seventh":"0 2 4 6".split(),
    "dominant seventh":"0 2 4 6b".split(),
    "augmented triad":"0 2 4#".split(),
    "diminished triad":"0 2 4b".split(),
    "half diminished seventh":"0 2 4b 6".split(),
    "fully diminished seventh":"0 2 4b 6b".split()}

def findkeySharps(root, tonic):
    #root is not found
    rootfound = False
    #place is a counter when going through the notes lists
    place = 0
    #scale is the actual notes of the scale
    scale = []
    #number of the list the root is
    rootnum = 0
    for note in notesSharps:
            if root == note:
                #key is how the root of the scale is found
                key = root
                rootfound = True
            if root != note and rootfound == False:
                #rootnum now the correct number
                rootnum = rootnum + 1
    if tonic.lower() == "major":
            #ONLY WORKS FOR OCTOTONIC SCALES
            for i in range(0,len(majorkeysteps)-1):
                place = place + majorkeysteps[i]
                scale.append(notesSharps[(rootnum + place) % len(notesSharps)])
            return scale
    elif tonic.lower() == "minor":
            for i in range(0,len(minorkeysteps)-1):
                place = place + minorkeysteps[i]
                scale.append(notesSharps[(rootnum + place) % len(notesSharps)])
            return scale
        
def findkeyFlats(root,tonic):
    #root is not found
    rootfound = False
    #place is a counter when going through the notes lists
    place = 0
    #scale is the actual notes of the scale
    scale = []
    #number of the list the root is
    rootnum = 0
    for note in notesFlats:
        if root == note:
            #key is how the root of the scale is found
            key = root
            rootfound = True
        if root != note and rootfound == False:
            #rootnum now the correct number
            rootnum = rootnum + 1
    if tonic.lower() == "major":
        #ONLY WORKS FOR OCTOTONIC SCALES
        for i in range(0,len(majorkeysteps)-1):
            place = place + majorkeysteps[i]
            scale.append(notesFlats[(rootnum + place) % len(notesSharps)])
        return(scale)
    elif tonic.lower() == "minor":
        for i in range(0,len(minorkeysteps)-1):
            place = place + minorkeysteps[i]
            scale.append(notesFlats[(rootnum + place) % len(notesSharps)])
        return scale

def findkey(root,tonic):
    scaleTypes = ["major","minor"]
    if tonic.lower() in scaleTypes:
        if root[0].upper() in notesSharps or root[0].upper() in notesFlats:
            goodkeysharps = True
            goodkeyflats = True
            for i in range(len(findkeySharps(root,tonic))):
                if findkeySharps(root,tonic)[i][0] == findkeySharps(root,tonic)[i-1][0]:
                    goodkeysharps = False
            for i in range(len(findkeyFlats(root,tonic))):
                if findkeyFlats(root,tonic)[i][0] == findkeyFlats(root,tonic)[(i-1)][0]:
                    goodkeyflats = False
            if len(root) == 2:
                if root[1] == 'b':
                    return findkeyFlats(root,tonic)
                elif root[1] == '#':
                    return findkeySharps(root,tonic)
                else:
                    return findkeySharps("C","major")
            if goodkeyflats == True and goodkeysharps == False:
                return findkeyFlats(root,tonic)
            if goodkeysharps == True and goodkeyflats == False:
                return findkeySharps(root,tonic)
            if goodkeysharps == True and goodkeyflats == True:
                return findkeyFlats(root,tonic)
                return findkeySharps(root,tonic)
        else:
            return findkeySharps("C","major")
    else:
        return findkeySharps("C","major")

def chord(scale,degree):
    if degree in chordSteps.keys():
        print("chord %s %s"%(scale,degree))
        chordNotes = []
        for note in chordSteps[degree]:
            if len(note) == 1:
                note = int(note)
                tone = scale[note % len(scale)]
                chordNotes.append(tone)
            elif note[1] == "#":
                fix = int(note[0])
                if len(scale[fix]) == 1:
                    chordNotes.append(scale[fix] + "#")
                if len(scale[fix]) != 1 and scale[fix][1] == "b":
                    chordNotes.append(scale[fix][0])
                if len(scale[fix]) != 1 and scale[fix][1] == "#":
                    place = 0
                    for note in notesSharps:
                        if scale[fix] != note:
                            place += 1
                        else:
                            chordNotes.append(notesSharps[place + 1])
            elif note[1] == "b":
                fix = int(note[0])
                if len(scale[fix]) == 1:
                    chordNotes.append(scale[fix] + "b")
                if len(scale[fix]) != 1 and scale[fix][1] == "#":
                    chordNotes.append(scale[fix][0])
                if len(scale[fix]) != 1 and scale[fix][1] == "b":
                    place = 0
                    for note in notesFlats:
                        if scale[fix] != note:
                            place += 1
                        else:
                            chordNotes.append(notesFlats[((place - 1) + len(notesFlats)) % len(notesFlats)])
        for count, note in enumerate(chordNotes):
            if note == "Fb":
                chordNotes[count] = "E"
            if note == "Cb":
                chordNotes[count] = "B"
            if note == "E#":
                chordNotes[count] = "F"
            if note == "B#":
                chordNotes[count] = "C"
        return chordNotes
    else:
        return chord(findkey("C","major"),"triad")

def findnotetab(lowest,desinote):
    lcounter = 0
    dcounter = 0
    if len(lowest) == 1 or lowest[1] == "#":
        for note in notesSharps:
            if note != lowest:
                lcounter += 1
            else:
                lowcount = lcounter
    elif len(lowest) != 1 and lowest[1] == "b":
        for note in notesFlats:
            if note != lowest:
                lcounter += 1
            else:
                lowcount = lcounter
    if len(desinote) == 1 or desinote[1] == "#":
        for note in notesSharps:
            if note != desinote:
                dcounter += 1
            else:
                desicount = dcounter
    if len(desinote) != 1 and desinote[1] == "b":
        for note in notesFlats:
            if note != desinote:
                dcounter += 1
            else:
                desicount = dcounter
    if desicount < lowcount:
        desicount += 12
    tab = desicount - lowcount
    return tab

instrumentStrings = {
    "guitar":["E","A","D","G","B","E"],
    "dropd":["D","A","D","G","B","E"],
    "mandolin":["G","D","A","E"],
    "viola":["C","G","D","A"],
    "bass":"E A D G".split(),
    "ukulele":"G C E A".split(),
    "banjo":"G D G B D".split()
    }

def findtab(chord,strings):
    for string in strings:
        inv = 0
        allTabString = []
        for note in chord:
            possibleTabString = [findnotetab(string,note),inv]
            octavepossibleTabString = [findnotetab(string,note) + 12,inv]
            allTabString.append(possibleTabString)
            allTabString.append(octavepossibleTabString)
            inv += 1
        print(str(string) + " can be " + str(allTabString))
