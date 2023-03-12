import tkinter as tk 
from tkinter import filedialog
import os

root = tk.Tk()

resizeArray = [800,600]
themeArray = ["#FFFFFF"]
fileArray = [""]

root.title("CompStock: Welcome")
root.geometry(str(resizeArray[0])+"x"+str(resizeArray[1]))
root.config(bg=themeArray[0])

def changeTitle(newTitle= str):
    global root
    root.title("CompStock: " + newTitle)

def deleteChildren():
    global root
    for children in root.winfo_children():
        children.destroy()

def makeMenu(menuType: str):
    global root, resizeArray

    route = tk.Frame(root,bg="#FF0000")
    route.pack(side="top")

    if(menuType == "Compare"):
        selection = tk.Button(route,text="Selection",command=createSelection)
        selection.pack(side="left")
        forecast = tk.Button(route,text="Forecast",command=createForecast)
        forecast.pack(side="left")
    if(menuType == "Forecast"):
        selection = tk.Button(route,text="Selection",command=createSelection)
        selection.pack(side="left")
        compare = tk.Button(route,text="Comparison",command=createCompare)
        compare.pack(side="left")
    
def openFile():
    global fileArray
    fileArray[0] = filedialog.askopenfilename()

def createCompare():
    global root, resizeArray, themeArray, fileArray

    deleteChildren()
    changeTitle("Compare")
    makeMenu("Compare")

    main = tk.Frame(root)
    main.pack(side="top")

    comparisonMenu = tk.Frame(main)
    comparisonMenu.pack(side="left")
    menuTitle = tk.Label(comparisonMenu,text="Comparison Options")
    menuTitle.pack(side="top")

    fileSelect = tk.Frame(main)
    fileSelect.pack(side="right")

    title = "File Selection"

    if(len(os.listdir("StockData")) == 0):
        title = "No current stock data"

    selectTitle = tk.Label(fileSelect,text=title)
    selectTitle.pack(side="top")
    getFile = tk.Button(fileSelect,text="Add Files To Stock Data",command=openFile)
    getFile.pack(side="top")

def createForecast():
    global root, resizeArray, themeArray
    
    deleteChildren()
    changeTitle("Forecast")
    makeMenu("Forecast")

def createSelection():
    global root, resizeArray, themeArray, routingArray
    
    deleteChildren()
    changeTitle("Selection")
    
    compare = tk.Frame(root,width=resizeArray[0]/3,height=resizeArray[1]-100,bg="#FF0000")
    compare.pack(side="left",padx=50,expand=True)
    compareButton = tk.Button(compare,text="Compare",command=createCompare)
    compareButton.pack()

    forecast = tk.Frame(root,width=resizeArray[0]/3,height=resizeArray[1]-100,bg="#FF0000")
    forecast.pack(side="left",padx=50,expand=True)
    forecastButton = tk.Button(forecast,text="Forecast",command=createForecast)
    forecastButton.pack()

def createWelcome():
    global root, resizeArray, themeArray

    deleteChildren()
    changeTitle("Welcome")

    logoLabel = tk.Label(root,text="CompStock")
    logoLabel.pack(side="top",pady=10,expand=True)
    button = tk.Button(root,text="Continue",command=createSelection)
    button.pack(side="top",pady=10,expand=True)

createWelcome()

root.mainloop()