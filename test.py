import tkinter

root = tkinter.Tk()
waitVar = tkinter.BooleanVar()
isDone = False


def trigger():
    global waitVar
    waitVar.set(True)


def script():
    global isDone, waitVar
    for count in range(10):
        print
        "script", count
        if not isDone:
            root.after(1000, trigger)
            root.wait_variable(waitVar)
        else:
            print
            "script cancelled"
            return
    print
    "script done"