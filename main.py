import tkinter as tk 

root = tk.Tk()

resizeArray = [800,600]
themeArray = ["#FFFFFF"]

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

def makeMenu():
    global root, resizeArray

    route = tk.Frame(root,bg="#FF0000")
    route.pack(side="top")
    welcome = tk.Button(route,text="Welcome",command=createWelcome)
    welcome.pack(side="left")
    selection = tk.Button(route,text="Selection",command=createSelection)
    selection.pack(side="left")
    compare = tk.Button(route,text="Comparison",command=createCompare)
    compare.pack(side="left")
    forecast = tk.Button(route,text="Forecast",command=createForecast)
    forecast.pack(side="left")

def createCompare():
    global root, resizeArray, themeArray

    deleteChildren()
    changeTitle("Compare")
    makeMenu()

def createForecast():
    global root, resizeArray, themeArray
    
    deleteChildren()
    changeTitle("Forecast")
    makeMenu()

def createSelection():
    global root, resizeArray, themeArray, routingArray
    
    deleteChildren()
    changeTitle("Selection")
    makeMenu()
    
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