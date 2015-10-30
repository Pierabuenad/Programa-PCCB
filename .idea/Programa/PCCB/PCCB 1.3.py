import os
import wx
import numpy as np
# import scipy as sp

__author__ = 'DP EZ'



class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(-1, -1))
        self.dirname = ''
        #Status Bar - Barra al fondo de la ventana
        self.CreateStatusBar()

        #Barra de menu

        #Menu Archivo
        filemenu = wx.Menu()
        menuOpen = filemenu.Append(wx.ID_OPEN, "&Abrir", " Abrir archivo")
        menuSave = filemenu.Append(wx.ID_SAVE, "&Guardar", "Guardar archivo")
        menuSaveAs = filemenu.Append(wx.ID_SAVEAS, "&Guardar Como...", " Guardar Archivo Como...")
        filemenu.AppendSeparator()  # linea divisoria
        menuExit = filemenu.Append(wx.ID_EXIT, "Exit", " Cerrar programa")

        #Menu Datos
        datosmenu = wx.Menu()
        menu_dg = datosmenu.Append(-1, "&Datos Generales", " Ingrese el valor de los datos generales")
        menu_dv = datosmenu.Append(-1, "&Datos Vanos", " Ingrese datos referidos a los vanos")
        menu_ds = datosmenu.Append(-1, "&Datos Secciones", " Ingrese los datos de las secciones")
        menu_trapre = datosmenu.Append(-1,"&Trazado de Pretensado", "Cargar datos de cable de pre/postesado")

        #Menu Ayuda
        ayudamenu = wx.Menu()
        menuAyuda = ayudamenu.Append(wx.ID_ABOUT, "&Ayuda", "Ayuda")
        menuAbout = ayudamenu.Append(wx.ID_ABOUT, "&About Us", " Acerca de nosotros ")

        #Suma al menu, las distintas etiquetas
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, "&Archivo")
        menuBar.Append(datosmenu, "&Datos")
        menuBar.Append(ayudamenu, "&Ayuda")
        self.SetMenuBar(menuBar)

        #Barra de herramientas
        toolbar = self.CreateToolBar()
        dg_tool = toolbar.AddLabelTool(wx.ID_ANY, 'Datos Generales', wx.Bitmap('img/dgg.png'))
        dv_tool = toolbar.AddLabelTool(wx.ID_ANY, 'Datos Vanos', wx.Bitmap('img/dvg.png'))
        toolbar.AddSeparator()
        abou = toolbar.AddLabelTool(wx.ID_ANY, 'Acerca', wx.Bitmap('img/dgc.png'))
        abou = toolbar.AddLabelTool(wx.ID_ANY, 'Acerca', wx.Bitmap('img/dvc.png'))
        toolbar.Realize()

        # Eventos.
        self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)   #Abre Nuevo Archivo
        self.Bind(wx.EVT_MENU, self.OnClick, menu_dg)   #Abre, desde la MenuBar, la ventana de datos generales
        self.Bind(wx.EVT_MENU, self.OnClick, dg_tool)   #Abre, desde la ToolBar, la ventana de datos generales
        self.Bind(wx.EVT_MENU, self.OnCli, menu_dv)     #Abre, desde la MenuBar, la ventana de datos vano
        self.Bind(wx.EVT_MENU, self.OnCli, dv_tool)     #Abre, desde la ToolBar, la ventana de datos vano
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)   #Sale del programa, desde el MenuBar
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout) #Abre el Mensaje "Acerca de..."

        # PANEL
        panel = wx.Panel(self, -1)
        panel.SetBackgroundColour('White')

        self.Center()
        self.Show()


    #Abrir ventana datos generales
    def OnClick(self, event):
        DatosGenerales(self).Show()

    #Abrir ventana datos vano
    def OnCli(self, event):
        DatosVanos(self).Show()

    #Ventanaa acerca de nosotros
    def OnAbout(self, e):
        # Create a message dialog box
        dlg = wx.MessageDialog(self, "Desarrolladores: JCT, ATA, DP, EZ\n basado", "About PCCB Version 2015", wx.OK)
        dlg.ShowModal()  # Shows it
        dlg.Destroy()  # finally destroy it when finished.

    #Funcion para cerrar
    def OnExit(self, e):
        self.Close()  # Close the frame.

    #Funcion para open file
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

class DatosGenerales(wx.Frame):

    def __init__(self, parent):
        super(DatosGenerales, self).__init__(parent, size=(350, 325), style=wx.CLOSE_BOX | wx.CAPTION | wx.SYSTEM_MENU)
        panel = wx.Panel(self)

        # Textos Estaticos
        dg_st=wx.StaticText(panel, -1, "DATOS GENERALES")
        dg_st.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD))
        rp_st=wx.StaticText(panel, -1, "Referencia del puente:")
        de_st=wx.StaticText(panel, -1, "DATOS ESTRUCTURA DEFINITIVA")
        de_st.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD))
        nv_st=wx.StaticText(panel, -1, "Numero de vanos:")
        me_st=wx.StaticText(panel, -1, "Modulo elasticidad:")
        vi_st=wx.StaticText(panel, -1, "Voladizo izquierdo:")
        vd_st=wx.StaticText(panel, -1, "Voladizo derecho:")

        #Textos Estaticos Unidades
        nv_su=wx.StaticText(panel, -1, "[1]")
        me_su=wx.StaticText(panel, -1, "[T/m2]")

        #Cuadros de relleno
        self.rp_tc=wx.TextCtrl(panel, value="")
        self.nv_tc=wx.TextCtrl(panel, value="", size=(180, -1))
        self.me_tc=wx.TextCtrl(panel, value="3400000", size=(180, -1))


        #Botones
        BotonOK = wx.Button(panel, wx.ID_OK, pos=(100, 300))
        BotonOK.Bind(wx.EVT_BUTTON, self.OnClick, BotonOK)
        BotonCancel = wx.Button(panel, wx.ID_CANCEL, pos=(210, 300))
        BotonCancel.Bind(wx.EVT_BUTTON, self.OnCancel, BotonCancel)


        #voladizos Si o No
        self.vi_rbs=wx.RadioButton(panel, -1, "Si", style=wx.RB_GROUP)
        self.Bind(wx.EVT_RADIOBUTTON, self.OnClick, BotonOK)
        self.vi_rbn=wx.RadioButton(panel, -1, "No")
        self.vd_rbs=wx.RadioButton(panel, -1, "Si", style=wx.RB_GROUP)
        self.Bind(wx.EVT_RADIOBUTTON, self.OnClick, BotonOK)
        self.vd_rbn=wx.RadioButton(panel, -1, "No")

        #Grilla de posicionamiento
        tp_g= wx.BoxSizer(wx.VERTICAL)

        #Asignacion a la columna de la grilla
        fgs1 = wx.FlexGridSizer(1, 1, 5, 5)
        fgs1.Add(dg_st, 0, wx.ALIGN_CENTER, 5)

        fgs2 = wx.FlexGridSizer(1, 3, 5, 5)
        fgs2.Add(rp_st, 0, wx.ALIGN_RIGHT, 5)
        fgs2.Add(self.rp_tc, 0, wx.EXPAND, 5)

        fgs3 = wx.FlexGridSizer(1, 1, 5, 5)
        fgs3.Add(de_st, 0, wx.ALIGN_CENTER, 5)

        fgs4 = wx.FlexGridSizer(2, 3, 5, 5)
        fgs4.Add(nv_st, 0, wx.ALIGN_LEFT, 5)
        fgs4.Add(self.nv_tc, 0, wx.ALIGN_LEFT, 5)
        fgs4.Add(nv_su, 0, wx.ALIGN_CENTER, 5)
        fgs4.Add(me_st, 0, wx.ALIGN_LEFT, 5)
        fgs4.Add(self.me_tc, 0, wx.ALIGN_LEFT, 5)
        fgs4.Add(me_su, 0, wx.ALIGN_CENTER, 5)

        fgs5 = wx.FlexGridSizer(2, 3, 5, 5)
        fgs5.Add(vi_st, 0, wx.ALIGN_LEFT, 5)
        fgs5.Add(self.vi_rbs, 0, wx.ALIGN_LEFT, 5)
        fgs5.Add(self.vi_rbn, 0, wx.EXPAND, 5)
        fgs5.Add(vd_st, 0, wx.ALIGN_LEFT, 5)
        fgs5.Add(self.vd_rbs, 0, wx.ALIGN_LEFT, 5)
        fgs5.Add(self.vd_rbn, 0, wx.EXPAND, 5)

        fgs6 = wx.FlexGridSizer(1, 2, 5, 5)
        fgs6.Add(BotonOK, 0, wx.ALIGN_CENTER, 5)
        fgs6.Add(BotonCancel, 0, wx.ALIGN_CENTER, 5)

        fgs2.AddGrowableCol(1)
        fgs3.AddGrowableCol(0)

        #Asiganacion a la fila de la grilla
        tp_g.Add(wx.StaticLine(panel), 0, wx.EXPAND|wx.ALL, 5)
        tp_g.Add(fgs1, 0, wx.ALIGN_CENTER)
        tp_g.Add(wx.StaticLine(panel), 0, wx.EXPAND|wx.ALL, 5)
        tp_g.Add(fgs2, 0, wx.EXPAND|wx.ALL, 5)
        tp_g.Add(wx.StaticLine(panel), 0, wx.EXPAND|wx.ALL, 5)
        tp_g.Add(fgs3, 0, wx.EXPAND|wx.ALL, 5)
        tp_g.Add(wx.StaticLine(panel), 0, wx.EXPAND|wx.ALL, 5)
        tp_g.Add(fgs4, 0, wx.EXPAND|wx.ALL, 5)
        tp_g.Add(wx.StaticLine(panel), 0, wx.EXPAND|wx.ALL, 5)
        tp_g.Add(fgs5, 0, wx.EXPAND|wx.ALL, 5)
        tp_g.Add(wx.StaticLine(panel), 0, wx.EXPAND|wx.ALL, 5)
        tp_g.Add(fgs6, 0, wx.ALIGN_CENTER, 5)
        tp_g.Add(wx.StaticLine(panel), 0, wx.EXPAND|wx.ALL, 5)

        panel.SetSizer(tp_g)
        tp_g.Fit(panel)

        self.Center()
        self.Show()

    def OnClick(self, event):

        rp = self.rp_tc.GetValue()
        nv = self.nv_tc.GetValue()
        me = self.me_tc.GetValue()
        vi = self.vi_rbs.GetValue()
        vd = self.vd_rbs.GetValue()
        print vi
        print vd

        archi=open('datos/datgen.dat','w')
        archi.write(rp +'\n')
        archi.write(nv +'\n')
        archi.write(me +'\n')

        if vi == True:
            archi.write('1' +'\n')
        else:
            archi.write('0' +'\n')

        if vd == True:
            archi.write('1' +'\n')
        else:
            archi.write('0' +'\n')

        archi.close
        self.Close(True)

    def OnCancel(self, event):
        self.Close(True)

class DatosVanos(wx.Frame):

    def __init__(self, parent):
        super(DatosVanos, self).__init__(parent, size=(340, 700), style=wx.CLOSE_BOX | wx.CAPTION | wx.SYSTEM_MENU)
        panel = wx.Panel (self, -1)

        # Abre el archivo datgen.dat para crear el vector RP y DG
        archi=open('datos/datgen.dat','r')
        self.RP = []
        self.DG = []
        n = 0
        for linea in archi:
            if linea[-1]=='\n':
                linea = linea [:-1]
            if n == 0:
                self.RP.append(linea)
            else: self.DG.append(int(linea))
            n = n + 1
        print 'El nombre del puente es ', self.RP[0]
        print ''
        print self.DG
        archi.close()

        #Datos Generales
        wx.StaticLine(panel, -1, (5, 5), (325,2))
        dv_st = wx.StaticText(panel, label="DATOS GENERALES", pos=(100,10))
        wx.StaticLine(panel, -1, (5, 30), (325,2))
        dv_st.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD))
        wx.StaticLine(panel)
        vanon_st = wx.StaticText(panel, label="VANO N:", pos=(10,45))
        luz_st = wx.StaticText(panel, label="LUZ \n [m]", pos=(90,45))
        secin_st = wx.StaticText(panel, label="SECCION \n INICIAL", pos=(165,45))
        secfin_st = wx.StaticText(panel, label="SECCION \n FINAL", pos=(255,45))
        wx.StaticLine(panel, -1, (5, 85), (325,2))

        #bucle

        self.editname = []

        self.filas = self.DG[0]
        if self.DG[2]: self.filas = self.filas + 1
        if self.DG[3]: self.filas = self.filas + 1
        self.L = np.array([[0]*6]*(self.filas))
        self.long =[]
        l=100
        i = 0
        if self.DG[2]:
            j=30
            self.numvan = wx.StaticText(panel, label=str('Vol. Izq.'), pos=(12, l+5))
            self.L [i,0] = 0
            j=j+30
            self.luz = wx.TextCtrl(panel, value="", pos=(j, l), size=(80,-1))
            self.long.append(self.luz)
            j=j+125
            self.secin = wx.StaticText(panel, label=str(1+10*i), pos=(j, l+5), size=(80,-1))
            self.L [i,2] = float(self.secin.GetLabel())
            j=j+85
            self.secfin = wx.StaticText(panel, label=str(11+10*i), pos=(j, l+5), size=(80,-1))
            self.L [i,3] = float(self.secfin.GetLabel())
            l=l+50
            i = i + 1
            for i in range(1, self.DG[0]+1):
                j=30
                self.numvan = wx.StaticText(panel, label=str(i), pos=(j, l+5))
                self.L [i,0] = float(self.numvan.GetLabel())
                j=j+30
                self.luz = wx.TextCtrl(panel, value="", pos=(j, l), size=(80,-1))
                self.long.append(self.luz)
                j=j+125
                self.secin = wx.StaticText(panel, label=str(1+10*i), pos=(j, l+5), size=(80,-1))
                self.L [i,2] = float(self.secin.GetLabel())
                j=j+85
                self.secfin = wx.StaticText(panel, label=str(11+10*i), pos=(j, l+5), size=(80,-1))
                self.L [i,3] = float(self.secfin.GetLabel())
                l=l+50
            if self.DG[3]:
                j=30
                self.numvan = wx.StaticText(panel, label=str('Vol. Der.'), pos=(12, l+5))
                self.L [i+1,0] = self.DG[0]+1
                j=j+30
                self.luz = wx.TextCtrl(panel, value="", pos=(j, l), size=(80,-1))
                self.long.append(self.luz)
                j=j+125
                self.secin = wx.StaticText(panel, label=str(1+10*(i+1)), pos=(j, l+5), size=(80,-1))
                self.L [i+1,2] = float(self.secin.GetLabel())
                j=j+85
                self.secfin = wx.StaticText(panel, label=str(11+10*(i+1)), pos=(j, l+5), size=(80,-1))
                self.L [i+1,3] = float(self.secfin.GetLabel())
                l=l+50
        else:
            for i in range(0, self.DG[0]):
                j=30
                self.numvan = wx.StaticText(panel, label=str(i+1), pos=(j, l+5))
                self.L [i,0] = float(self.numvan.GetLabel())
                j=j+30
                self.luz = wx.TextCtrl(panel, value="", pos=(j, l), size=(80,-1))
                self.long.append(self.luz)
                j=j+125
                self.secin = wx.StaticText(panel, label=str(1+10*i), pos=(j, l+5), size=(80,-1))
                self.L [i,2] = float(self.secin.GetLabel())
                j=j+85
                self.secfin = wx.StaticText(panel, label=str(11+10*i), pos=(j, l+5), size=(80,-1))
                self.L [i,3] = float(self.secfin.GetLabel())
                l=l+50
        if self.DG[3]:
            j=30
            self.numvan = wx.StaticText(panel, label=str('Vol. Der.'), pos=(12, l+5))
            self.L [i+1,0] = self.DG[0]+1
            j=j+30
            self.luz = wx.TextCtrl(panel, value="", pos=(j, l), size=(80,-1))
            self.long.append(self.luz)
            j=j+125
            self.secin = wx.StaticText(panel, label=str(1+10*(i+1)), pos=(j, l+5), size=(80,-1))
            self.L [i+1,2] = float(self.secin.GetLabel())
            j=j+85
            self.secfin = wx.StaticText(panel, label=str(11+10*(i+1)), pos=(j, l+5), size=(80,-1))
            self.L [i+1,3] = float(self.secfin.GetLabel())
            l=l+50


            #Botones
        wx.StaticLine(panel, -1, (5, l), (325,2))

        BotonOK = wx.Button(panel, wx.ID_OK, pos=(70, l+15))
        BotonOK.Bind(wx.EVT_BUTTON, self.OnClick, BotonOK)
        BotonCancel = wx.Button(panel, wx.ID_CANCEL, pos=(180, l+15))
        BotonCancel.Bind(wx.EVT_BUTTON, self.OnClick, BotonCancel)

        wx.StaticLine(panel, -1, (5, l+50), (325,2))
        self.Center()
        self.Show()

    #Funciones de los botones
    def OnCancel(self, event):

        self.Close()

    def OnClick(self, event):
        for n in range(0, self.filas):
            self.L[n, 1] = self.long[n].GetValue()
        self.L[0,4] = 0
        self.L[0,5]=self.L[0,1]
        for t in range (1, self.filas):
            self.L [t,4] = self.L[t-1,5]
            self.L [t,5] = self.L[t,4] + self.L[t,1]
        print self.L

        self.Close()


app = wx.App(False)
frame = MainWindow(None, "PCCB Version1.1 15")
app.MainLoop()





