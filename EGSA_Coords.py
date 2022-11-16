# Morph thelei
gdl = """
!
!   Name     : 2.gdl
!   Date     : Δευτέρα, 14 Νοεμβρίου 2022
!   Version  : 24.00
!   Written by ARCHICAD 
!

bms_53 = 0
r = REQUEST{2} ("Building_Material_info", "02 ARCHITECTURAL _ WALL EXTERIOR 1.50", "gs_bmat_surface", bms_53)

body    -1
model solid
resol       36
GLOB_SCRIPT_TYPE =      3
GLOB_CONTEXT =      3
GLOB_VIEW_TYPE =      3
GLOB_SCALE =    200
GLOB_NORTH_DIR =           90
GLOB_PROJECT_LONGITUDE = 23.73333333333
GLOB_PROJECT_LATITUDE =           38
GLOB_DRAWING_BGD_PEN =    154
GLOB_FRAME_NR =     -1
GLOB_EYEPOS_X = 2.830703228749
GLOB_EYEPOS_Y = 32.41612840056
GLOB_EYEPOS_Z = 31.93915515389
GLOB_TARGPOS_X = 1.359075822606
GLOB_TARGPOS_Y = 18.86284331633
GLOB_TARGPOS_Z = 25.81620931833
GLOB_SUN_AZIMUTH = 271.3531919538
GLOB_SUN_ALTITUDE =           40
!!TR - 031 B8CFA555-355A-4552-972B-CE3DEDADB432
group 	"group_C7977365_E51C_4B6E_BFD2_74489C2947A1"
    pen     40
    set building_material "02 ARCHITECTURAL _ WALL EXTERIOR 1.50", 113, 133
    sect_attrs{2} 93, ind(LINE_TYPE,"Solid Line")
vert{2}	-12.86080373818, -6.020151508972,            0, 1	!	#1   VertId=0
vert{2}	-9.413550152327, -4.421263512224,            0, 1	!	#2   VertId=0
vert{2}	-15.89573048701, 0.5232473844662,            0, 1	!	#3   VertId=0
vert{2}	-11.99693249873, 2.336916821077,            0, 1	!	#4   VertId=0
vert{2}	-11.12772190684, 0.4628713103011,            0, 1	!	#5   VertId=0
vert{2}	-8.180321924447, -7.080143077299,            0, 1	!	#6   VertId=0
vert{2}	-5.458982322831, -5.817944871262,            0, 1	!	#7   VertId=0
vert{2}	-2.14671927024, 4.628395307809,            0, 1	!	#8   VertId=0
vert{2}	-6.713249063992, -3.113705760799,            0, 1	!	#9   VertId=0
vert{2}	           0,            0,            0, 1	!	#10  VertId=0
pen 40
edge	   1,    2,    1,    0, 262144			!	#1   EdgeId=0
edge	   3,    1,    1,    0, 262144			!	#2   EdgeId=0
edge	   4,    3,    1,    0, 262144			!	#3   EdgeId=0
edge	   5,    4,    1,    0, 262144			!	#4   EdgeId=0
edge	   8,    5,    1,    0, 262144			!	#5   EdgeId=0
edge	   2,    6,    1,    0, 262144			!	#6   EdgeId=0
edge	   6,    7,    1,    0, 262144			!	#7   EdgeId=0
edge	   7,    9,    1,    0, 262144			!	#8   EdgeId=0
edge	   9,   10,    1,    0, 262144			!	#9   EdgeId=0
edge	  10,    8,    1,    0, 262144			!	#10  EdgeId=0
vect	           0,            0,            1	!	#1  
material "00_Metal Grey"
pgon	  10,    1,     18,					!	#1   PolyId=0
		   1,		   6,		   7,		   8,		   9,		  10,		   5,		   4,
		   3,		   2
material bms_53
coor{3}	   2,    0,
	-143269.3867815, -4384244.405668, -34.12500002384,
	-143268.3867815, -4384244.405668, -34.12500002384,
	-143269.3867815, -4384243.405668, -34.12500002384,
	-143269.3867815, -4384244.405668, -33.12500002384

body	262182

    material 0
    body    -1
endgroup
group 	"group_96535A5E_EB8B_4B7C_B072_CC961DDF7CA2"
    xform              1,            0,            0, 1432214.374078,
                       0,            1,            0, 4384249.928866,
                       0,            0,            1, 0.7250000238419
    placegroup ("group_C7977365_E51C_4B6E_BFD2_74489C2947A1")
    del          1
endgroup
placegroup ("group_96535A5E_EB8B_4B7C_B072_CC961DDF7CA2")
killgroup ("group_96535A5E_EB8B_4B7C_B072_CC961DDF7CA2")
killgroup ("group_C7977365_E51C_4B6E_BFD2_74489C2947A1")
end

"""

def getStringBetween(str1, str2, gdl):
    start = gdl.find(str1)
    end = gdl[start:].find(str2) + start
    content = gdl[start:end].rstrip()
    return content

def findCoords(gdl):
    originArea = getStringBetween("xform", "placegroup", gdl)

    originCoordsString1 = originArea.splitlines()[0].split(",")
    originCoordsString2 = originArea.splitlines()[1].split(",")

    originCoords = [originCoordsString1[3][:-1].strip(), originCoordsString2[3][:-1].strip()]
    print(originCoords)
    return originCoords

def findVerts(gdl, originCoords, x, y):
    vertArea = getStringBetween("vert", "pen", gdl)
    vertLines = vertArea.split("}")[1:]

    for line in vertLines:
        element = line.split(",")[0:2]
        x.append(float(element[0].strip()) + float(originCoords[0]) )
        y.append(float(element[1].strip()) + float(originCoords[1]) )

def findEdges(gdl):
    edgeArea = getStringBetween("edge", "material", gdl)
    edgeLines = edgeArea.splitlines()
    edgesConnections = []
    for edgeLine in edgeLines:
        edge1 = edgeLine[4:].strip().split(",")[0].strip()
        edge2 = edgeLine[4:].strip().split(",")[1].strip()
        edgesConnections.append([edge1,edge2])
    print(edgesConnections)

    graph = []
    # an search tote complementary -> append -> search = complementary
    search = edgesConnections[0][0]
    for i in range(len(edgesConnections)):
        for connection in edgesConnections:
            if (connection[0]==search):
                graph.append(int(connection[0])-1)
                search = connection[1]
                break;
    graph.reverse()
    return graph


def printTable(x,y,graph):
    print("----X----\t-----Y----")
    for i in range(len(x)):
        print("{:.3f}".format(x[graph[i]]),"\t","{:.3f}".format(y[graph[i]]) )

def printNumbers(x, add=0):
    for i in range(len(x)):
        print(i+1+add)

if __name__ == '__main__':
    x = []
    y = []
    groupOrigin = findCoords(gdl)
    findVerts(gdl,groupOrigin,x,y)

    graph = findEdges(gdl)
    print(graph)
    printTable(x,y,graph)