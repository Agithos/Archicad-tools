from archicad import ACConnection

# Pairnei lista apo elem-Zones kai allazei Onoma
# Kanei print ta letters pou xrisimopoiei
# shiftNode gia na girnane numbers giro giro, startNode gia na ksekinaei apo pio megalo arithmo
def changeNumber(zones, prefix="", startNode=0, letters=False, shiftNode=0, array=None):
    nodeNum = len(zones)
    lettersList = ["Α", "Β", "Γ", "Δ", "Ε", "Ζ", "Η", "Θ", "Ι", "Κ", "Λ", "Μ", "Ν", "Ξ", "Ο", "Π", "Ρ",
    "Σ", "Τ", "Υ", "Φ", "Χ", "Ψ", "Ω"]
    prop = acu.GetBuiltInPropertyId('Zone_ZoneNumber')

    nodeCounter = startNode + 1
    if letters:
        nodeCounter = (nodeCounter-1)
        counter = lettersList[nodeCounter]
    else:
        counter = nodeCounter
    
    if shiftNode:
        shiftNode %= nodeNum
        newZones = zones[shiftNode:] + zones[:shiftNode]
        zones = newZones
    else:
        newZones = zones
    changes = []
    for elem in newZones:
        changedProp = act.ElementPropertyValue(elem.elementId, prop, act.NormalStringPropertyValue(prefix + str(counter)) )
        if array != None:
            array.append(prefix + str(counter))

        nodeCounter = nodeCounter+1
        if letters:
            counter = lettersList[nodeCounter%24]
            if nodeCounter>=24:
                counter += "'"
        else:
            counter = nodeCounter
        changes.append(changedProp)
    acc.SetPropertyValuesOfElements(changes)

def printNodes(nodeArray):
    nodeArray.sort()
    for node in nodeArray:
        print(node)

if __name__ == '__main__':
    conn = ACConnection.connect()
    assert conn

    acc = conn.commands
    act = conn.types
    acu = conn.utilities

    zones = acc.GetElementsByType('Zone')
    zones2 = zones[17:]

    myArray = []
    # changeNumber(zones[:17], letters=True, shiftNode=-1, array=myArray, starNode = posa proigithikan)
    changeNumber(zones2,startNode=17, letters=True, array=myArray)


    printNodes(myArray)
