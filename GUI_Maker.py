'''
Author: Reese Wells
Copyright 2016
'''
'''
A program that makes 
'''

from tkinter import *

class GuiBuilder:
    
    def __init__(self):
        self.master = Tk()
        self.frames = {}
        self.canvases = {}
        self.buttons = {}
        self.entries = {}

    def getMaster(self):
        return self.master
    
    def getFrame(self, name):
        return self.frames[name]

    def getCanvas(self, name):
        return self.canvases[name]

    def getButton(self, name):
        return self.buttons[name]

    def getEntry(self, name):
        return self.entries[name]

    '''
    FRAMES
    ====================================================================================================
    '''

    '''
    Adds a simple sunken frame to the main window, stacking frames as they are added
    @param name: string: the name of the frame for future reference
    @param position: string: left, right, bottom, center
    @return boolean: whether or not the frame was made
    '''
    def addStockFrame(self, name, position):
        if name in self.frames:
            return False
        
        newFrame = Frame(self.master, bd = 1, relief = SUNKEN )
        self.frames[name] = newFrame
        
        if position == "left":
            newFrame.pack(fill=X, padx = 5, pady = 5, side = LEFT)
        elif position == "right":
            newFrame.pack(fill=X, padx = 5, pady = 5, side = RIGHT)
        elif position == "bottom":
            newFrame.pack(fill=X, padx = 5, pady = 5, side = BOTTOM)
        else:
            newFrame.pack(fill=X, padx = 5, pady = 5)
        return True

    '''
    Adds a custom frame to the main window
    @param frame: Frame: a frame object
    @param position: string: left, right, bottom, center
    @param name: string: the name of the frame
    @return boolean: whether or not the frame was added
    '''
    def addCustFrame(self, frame, name, position):
        if name in self.frames:
            return False
        
        if position == "left":
            frame.pack(fill=X, padx = 5, pady = 5, side = LEFT)
        elif position == "right":
            frame.pack(fill=X, padx = 5, pady = 5, side = RIGHT)
        elif position == "bottom":
            frame.pack(fill=X, padx = 5, pady = 5, side = BOTTOM)
        else:
            frame.pack(fill=X, padx = 5, pady = 5)
        return True
    
    '''
    Removes a frame from the window
    @param name: string: the name of the frame
    @return boolean: whether or not the frame was deleted
    '''
    def delFrame(self, name):
        if name in self.frames:
            self.frames[name].pack_forget()
            del self.frames[name]
            return True
        else:
            return False

    '''
    Lists the frames currently in the window
    @return list: the list of frames
    '''
    def listFrames(self):
        return list(self.frames)

    '''
    CANVASES
    ====================================================================================================
    '''

    '''
    Adds a simple canvas to the specified frame, stacking canvases as they are added
    @param width: int: the width of the canvas in pixels
    @param height: int: the height of the canvas in pixels
    @param name: string: the name of the canvas for future reference
    @return boolean: whether or not the canvas was made
    '''
    def addStockCanvas(self, frame, position, width, height, name):
        if name in self.canvases:
            return False
        else:
            newCanvas = Canvas(frame, width = width, height = height)
            self.canvases[name] = newCanvas

            #==========FOR TESTING PURPOSES ONLY -->
            newCanvas.create_line(0, 0, width, height, width = 2, fill = "red")
            newCanvas.create_line(0, height, width, 0, width = 2, fill = "red")
            #==========FOR TESTING PURPOSES ONLY <--

            if position == "left":
                newCanvas.pack(side = LEFT)
            elif position == "right":
                newCanvas.pack(side = RIGHT)
            elif position == "bottom":
                newCanvas.pack(side = BOTTOM)
            else:
                newCanvas.pack()
            return True

    def addTextCanvas(self, frame, position, width, height, name):
        if name in self.canvases:
            return False
        else:
            newFrame = Frame(frame)
            newFrame.pack(fill=X, padx = 5, pady = 5)
            newCanvas = Canvas(newFrame, width = width, height = height, scrollregion = (0,0,0,height*2))

            vbar=Scrollbar(newFrame,orient=VERTICAL)
            vbar.pack(side=RIGHT,fill=Y)
            vbar.config(command=newCanvas.yview)

            newCanvas.config(yscrollcommand=vbar.set)
            
            #==========FOR TESTING PURPOSES ONLY -->
            newCanvas.create_line(0, 0, width, height, width = 2, fill = "red")
            newCanvas.create_line(0, height, width, 0, width = 2, fill = "red")
            #==========FOR TESTING PURPOSES ONLY <--

            if position == "left":
                newCanvas.pack(side = LEFT)
            elif position == "right":
                newCanvas.pack(side = RIGHT)
            elif position == "bottom":
                newCanvas.pack(side = BOTTOM)
            else:
                newCanvas.pack()
            return True
            

    '''
    Adds a custom canvas to the specified frame
    @param frame: Frame: a frame object
    @param name: string: the name of the canvas
    @return boolean: whether or not the canvas was added
    '''
    def addCustCanvas(self, position, canvas, name):
        if name in self.canvases:
            return False
        else:
            self.canvases[name] = canvas
            if position == "left":
                canvas.pack(side = LEFT)
            elif position == "right":
                canvas.pack(side = RIGHT)
            elif position == "bottom":
                canvas.pack(side = BOTTOM)
            else:
                canvas.pack()
            return True

    '''
    Deletes a canvas
    @param name: string: the name of the canvas
    @return boolean: whether or not it was deleted
    '''
    def delCanvas(self, name):
        if name in self.canvases:
            self.canvases[name].pack_forget()
            del self.canvases[name]
            return True
        else:
            return False

    '''
    Lists the canvases currently displayed
    @return list: the list of frames
    '''
    def listCanvases(self):
        return list(self.canvases)

    '''
    TESTS
    ====================================================================================================
    '''
    def test():
        gui = GuiBuilder()

        #stock frame test
        print(gui.addStockFrame("main", "center"))
        print("attempted to add stock frame")
        print(gui.addStockFrame("secondary", "left"))
        print("attempted to add a second frame to the left")
        print("attempted to add stock frame")
        print(gui.addStockFrame("main", "center"))
        print("attempted to add stock frame with same name")

        #custom frame test
        testFrame = Frame(gui.getMaster(), height = 200, width = 200, bd = 1, relief = FLAT )
        print(gui.addCustFrame(testFrame, "main", "center"))
        print("attempted to add custom frame with same name as stock frame to master")

        testFrame = Frame(gui.getMaster(), height = 200, width = 200, bd = 1, relief = FLAT )
        print(gui.addCustFrame(testFrame, "extra", "center"))
        print("attempted to add custom frame to master")

        testFrame = Frame(gui.getMaster(), height = 200, width = 200, bd = 1, relief = FLAT )
        print(gui.addCustFrame(testFrame, "extra", "center"))
        print("attempted to add custom frame to master with same name")

        #delete a frame
        print(gui.delFrame("extra"))
        print("attempted to delete custom frame")

        #list frames
        print(gui.listFrames())
        print("attempted to list frames")
        
        #add a second canvas
        print(gui.addStockCanvas(gui.getFrame("main"), "right", 200, 200, "right_x"))
        print("attempted to add a right canvas")
        print(gui.addStockCanvas(gui.getFrame("main"), "left", 200, 200, "left_x"))
        print("attempted to add a left canvas")
        print(gui.addStockCanvas(gui.getFrame("main"), "center", 200, 200, "top_x"))
        print("attempted to add a center canvas")
        print(gui.addStockCanvas(gui.getFrame("main"), "bottom", 200, 200, "bottom_x"))

        #add a custom canvas
        testCanvas = Canvas(gui.getFrame("main"), width = 500, height = 500, bg = "red")
        print(gui.addCustCanvas("center", testCanvas, "red"))
        print("attempted to add a right custom canvas")
        testCanvas = Canvas(gui.getFrame("main"), width = 500, height = 500, bg = "green")
        print(gui.addCustCanvas("center", testCanvas, "green"))
        print("attempted to add a left custom canvas")
        testCanvas = Canvas(gui.getFrame("main"), width = 500, height = 500, bg = "blue")
        print(gui.addCustCanvas("center", testCanvas, "blue"))
        print("attempted to add a center custom canvas")


        #delete canvases
        print(gui.delCanvas("red"))
        print("attempted to delete the red canvas")

        #list canvases
        print(gui.listCanvases())
        print("attempted to list canvases")

        #make a new text canvas
        gui2 = GuiBuilder()
        print(gui2.addStockFrame("main", "center"))
        print("attempted a second gui")
        print(gui2.addTextCanvas(gui2.getFrame("main"), "center", 200, 500, "text_box"))
        print("attempted to add a scrollable text canvas")
















                               
