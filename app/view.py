#import
import tkinter as tk
import COVID19Py as covidAPI

#{'confirmed': 27492023, 'deaths': 480887, 'recovered': 0}

covid = covidAPI.COVID19()

#function
def OutResult(event):
    try:
        resultOfFound = covid.getLocationByCountryCode(entryCC.get())[0]
        inj["text"] = "Заражено: " + str(resultOfFound['latest']['confirmed'])
        died["text"] = "Умерло: " + str(resultOfFound['latest']['deaths'])
    except:
        pass

#elements
root = tk.Tk()
root.title("covid")
root.geometry("220x320")
root.resizable(0, 0)
Tframe = tk.Frame(root)
Bframe = tk.Frame(root)
entryCC = tk.Entry(Tframe)
entryCC.insert(0, 'Country code')
button = tk.Button(Bframe, text="Получить")
inj = tk.Label(Tframe, text="", anchor=tk.W, padx=10)
died = tk.Label(Tframe, text="", anchor=tk.W, padx=10)

#portray
Tframe.pack(side=tk.TOP)
Bframe.pack(side=tk.BOTTOM)
entryCC.pack(pady=5)
button.pack(pady=5)
inj.pack()
died.pack()
#bind
button.bind("<Button-1>", OutResult)

#mainloop
root.mainloop()