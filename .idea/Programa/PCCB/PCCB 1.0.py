__author__ = 'Diego'
import wx
import os


class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        self.dirname = ''
        wx.Frame.__init__(self, parent, title=title, size=(-1, -1))
        self.CreateStatusBar()  # A Statusbar in the bottom of the window

        # Etiquetas de menu
        filemenu = wx.Menu()
        menuOpen = filemenu.Append(wx.ID_OPEN, "A&brir", " Open a file to edit")
        menuSave = filemenu.Append(wx.ID_SAVE, "Guardar", " Save File")
        menuSaveAs = filemenu.Append(wx.ID_SAVEAS, "Guardar Como", " Save File As...")
        filemenu.AppendSeparator()  # linea divisoria
        menuExit = filemenu.Append(wx.ID_EXIT, "Exit", " Terminate the program")

        fileayudamenu = wx.Menu()
        menuAyuda = fileayudamenu.Append(wx.ID_OPEN, "&Ayuda", " Open a file to edit")
        menuAbout = fileayudamenu.Append(wx.ID_SAVE, "&About Us", " Save File")

        # Creating the menubar.
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, "&Archivos")  # Adding the "filemenu" to the MenuBar
        menuBar.Append(fileayudamenu, "&Ayuda")  # Adding the "filemenu" to the MenuBar
        self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.

        # Eventos.
        self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)

        # Botones
        panel = wx.Panel(self, -1)
        self.buttonDG = wx.Button(panel, id=wx.ID_OPEN, label="Datos Generales", pos=(0, 0))
        self.buttonDG.Bind(wx.EVT_BUTTON, self.OnClick, self.buttonDG)
        self.buttonDV = wx.Button(panel, id=wx.ID_OPEN, label="Datos Vanos", pos=(130, 0))
        self.buttonDV.Bind(wx.EVT_BUTTON, self.OnCli, self.buttonDV)
        self.Center()
        self.Show()

    def OnClick(self, event):
        DatosGenerales(self).Show()

    def OnCli(self, event):
        DatosVanos(self).Show()

    def OnAbout(self, e):
        # Create a message dialog box
        dlg = wx.MessageDialog(self, " Diego \n Piedrabuena", "About PCCB Version 2015", wx.OK)
        dlg.ShowModal()  # Shows it
        dlg.Destroy()  # finally destroy it when finished.

    def OnExit(self, e):
        self.Close()  # Close the frame.

    def OnOpen(self, e):
        """ Open a file"""
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            f = open(os.path.join(self.dirname, self.filename), 'r')
            self.control.SetValue(f.read())
            f.close()
        dlg.Destroy()

app = wx.App(False)
frame = MainWindow(None, "PCCB V.1.1-15")
app.MainLoop()
