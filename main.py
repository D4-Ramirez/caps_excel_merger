from statistics import mode
import eel
import wx
import files as file

array = []
i = 0

eel.init("web")

@eel.expose
def readFile(wildcard="*"):
    global i
    global array
    app = wx.App(None)
    style = wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
    dialog = wx.FileDialog(None, 'Open', wildcard=wildcard, style=style)
    if dialog.ShowModal() == wx.ID_OK:
        path = dialog.GetPath()
    else:
        path = None
    dialog.Destroy()
    array.append(path)
    i += 1
    print(f"🔵 {path}")
    return path

@eel.expose
def mergeRegistrationList():
    global i
    global array
    file.prepareRegistrationList(array[1], array[2], array[0])
    array = []
    i = 0

@eel.expose
def transformTeamsList():
    global i
    global array
    file.prepareTeamsAttendanceList(array[0])
    array = []
    i = 0
    
@eel.expose
def transformAttendanceList():
    global i
    global array
    file.prepareFile(array[0], "lista_asistencia")
    array = []
    i = 0
    
@eel.expose
def transformSatisfactionList():
    global i
    global array
    file.prepareFile(array[0], "lista_satisfaccion")
    array = []
    i = 0

@eel.expose
def finalTransform():
    global i
    global array
    file.finalMerge(array[0], array[1], array[2], array[3])
    array = []
    i = 0

try:
    eel.start("index.html", mode='app', size=(800, 600), port=0)
except EnvironmentError:
    eel.start("index.html", mode='edge', size=(800, 600))
