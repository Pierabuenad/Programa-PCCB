import os
import wx
import numpy as np
# import scipy as sp

__author__ = 'DP & EZ'


class MainWindow(wx.Frame):


    def __init__(self, parent, title):

        self.atr1 = 0
        self.atr2 = 11.1

        self.DG = None

        wx.Frame.__init__(self, parent, title=title, size=(-1, -1))
        self.dirname = ''
        # Status Bar - Barra al fondo de la ventana
        self.CreateStatusBar()

        # Barra de Menu

        # Menu Archivo
        filemenu = wx.Menu()
        menuOpen = filemenu.Append(wx.ID_OPEN, "&Abrir", " Abrir archivo")
        menuSave = filemenu.Append(wx.ID_SAVE, "&Guardar", "Guardar archivo")
        menuSaveAs = filemenu.Append(wx.ID_SAVEAS, "&Guardar Como...", " Guardar Archivo Como...")
        filemenu.AppendSeparator()  # linea divisoria
        menuExit = filemenu.Append(wx.ID_EXIT, "Exit", " Cerrar programa")

        # Menu Datos
        datosmenu = wx.Menu()
        menu_dg = datosmenu.Append(-1, "&Datos Generales", " Ingrese el valor de los datos generales")
        menu_dv = datosmenu.Append(-1, "&Datos Vanos", " Ingrese datos referidos a los vanos")
        menu_ds = datosmenu.Append(-1, "&Datos Secciones", " Ingrese los datos de las secciones")
        menu_trapre = datosmenu.Append(-1,"&Trazado de Pretensado", "Cargar datos de cable de pre/postesado")

        # Menu Ayuda
        ayudamenu = wx.Menu()
        menuAyuda = ayudamenu.Append(wx.ID_ABOUT, "&Ayuda", "Ayuda")
        menuAbout = ayudamenu.Append(wx.ID_ABOUT, "&About Us", " Acerca de nosotros ")

        # Suma al menu, las distintas etiquetas
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, "&Archivo")
        menuBar.Append(datosmenu, "&Datos")
        menuBar.Append(ayudamenu, "&Ayuda")
        self.SetMenuBar(menuBar)

        # Barra de herramientas
        toolbar = self.CreateToolBar()
        dg_tool = toolbar.AddLabelTool(wx.ID_ANY, 'Datos Generales', wx.Bitmap('img/dgg.png'))
        dv_tool = toolbar.AddLabelTool(wx.ID_ANY, 'Datos Vanos', wx.Bitmap('img/dvg.png'))
        toolbar.AddSeparator()
        abou = toolbar.AddLabelTool(wx.ID_ANY, 'Acerca', wx.Bitmap('img/dgc.png'))
        abou = toolbar.AddLabelTool(wx.ID_ANY, 'Acerca', wx.Bitmap('img/dvc.png'))
        toolbar.Realize()

        # Eventos.
        self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)           # Abre Nuevo Archivo
        self.Bind(wx.EVT_MENU, self.OnClick1, menu_dg)          # Abre, desde la MenuBar, la ventana de datos generales
        self.Bind(wx.EVT_MENU, self.OnClick1, dg_tool)          # Abre, desde la ToolBar, la ventana de datos generales
        self.Bind(wx.EVT_MENU, self.OnClick2, menu_dv)          # Abre, desde la MenuBar, la ventana de datos vano
        self.Bind(wx.EVT_MENU, self.OnClick2, dv_tool)          # Abre, desde la ToolBar, la ventana de datos vano
        self.Bind(wx.EVT_MENU, self.OnClick3, menu_ds)          # Abre, desde la MenuBar, la ventana de datos de secciones

        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)       # Sale del programa, desde el MenuBar
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)     # Abre el Mensaje "Acerca de..."

        # PANEL
        panel = wx.Panel(self, -1)
        panel.SetBackgroundColour('White')

        self.Center()
        self.Show()

    # Abrir ventana datos generales
    def OnClick1(self, event):
        DatosGenerales(self).Show()

    # Abrir ventana datos vano
    def OnClick2(self, event):
        DatosVanos(self).Show()

    # Abrir ventana datos de secciones
    def OnClick3(self,event):
        DatosSecciones(self).Show()

    # Ventana acerca de nosotros
    def OnAbout(self, e):
        # Create a message dialog box
        dlg = wx.MessageDialog(self, "Desarrollado por JCT, ATA, DP & EZ para MyT Consultora SRL\nBasado en Programa PCCB de Dr. Ing. Angel Carlos Aparicio\n(Universidad Politecnica de Catalunia - Barcelona)", "About PCCB Version 2015", wx.OK)
        dlg.ShowModal()  # Shows it
        dlg.Destroy()  # finally destroy it when finished.

    # Funcion para cerrar
    def OnExit(self, e):
        self.Close()  # Close the frame.

    # Funcion para open file
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
        dg_st = wx.StaticText(panel, -1, "DATOS GENERALES")
        dg_st.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD))
        rp_st = wx.StaticText(panel, -1, "Referencia del puente:")
        de_st = wx.StaticText(panel, -1, "DATOS ESTRUCTURA DEFINITIVA")
        de_st.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD))
        nv_st = wx.StaticText(panel, -1, "Numero de vanos:")
        me_st = wx.StaticText(panel, -1, "Modulo elasticidad:")
        vi_st = wx.StaticText(panel, -1, "Voladizo izquierdo:")
        vd_st = wx.StaticText(panel, -1, "Voladizo derecho:")

        # Textos Estaticos Unidades
        nv_su = wx.StaticText(panel, -1, "[1]")
        me_su = wx.StaticText(panel, -1, "[T/m2]")

        # Cuadros de relleno
        self.rp_tc = wx.TextCtrl(panel, value="")
        self.nv_tc = wx.TextCtrl(panel, value="", size=(180, -1))
        self.me_tc = wx.TextCtrl(panel, value="3400000", size=(180, -1))

        # Botones
        BotonOK = wx.Button(panel, wx.ID_OK, pos=(100, 300))
        BotonOK.Bind(wx.EVT_BUTTON, self.OnClick, BotonOK)
        BotonCancel = wx.Button(panel, wx.ID_CANCEL, pos=(210, 300))
        BotonCancel.Bind(wx.EVT_BUTTON, self.OnCancel, BotonCancel)

        # Voladizos Si o No
        self.vi_rbs = wx.RadioButton(panel, -1, "Si", style=wx.RB_GROUP)
        self.Bind(wx.EVT_RADIOBUTTON, self.OnClick, BotonOK)
        self.vi_rbn = wx.RadioButton(panel, -1, "No")
        self.vd_rbs = wx.RadioButton(panel, -1, "Si", style=wx.RB_GROUP)
        self.Bind(wx.EVT_RADIOBUTTON, self.OnClick, BotonOK)
        self.vd_rbn = wx.RadioButton(panel, -1, "No")

        # Grilla de posicionamiento
        tp_g = wx.BoxSizer(wx.VERTICAL)

        # Asignacion a la columna de la grilla
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

        # Asiganacion a la fila de la grilla
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

        archi = open('datos/datgen.dat','w')
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
        print parent.atr1
        # Abre el archivo datgen.dat para crear el vector RP y DG
        archi = open('datos/datgen.dat','r')
        self.RP = []
        parent.DG = []
        n = 0
        for linea in archi:
            if linea[-1] == '\n':
                linea = linea [:-1]
            if n == 0:
                self.RP.append(linea)
            else: parent.DG.append(int(linea))
            n = n + 1
        print 'El nombre del puente es ', self.RP[0]        # IMPRESIONES AUXILIARES -> ELIMINAR
        print ''                                            # IMPRESIONES AUXILIARES -> ELIMINAR
        print parent.DG                                       # IMPRESIONES AUXILIARES -> ELIMINAR
        archi.close()

        # Datos Generales

        wx.StaticLine(panel, -1, (5, 5), (325, 2))
        dv_st = wx.StaticText(panel, label="DATOS GENERALES", pos=(100, 10))
        wx.StaticLine(panel, -1, (5, 30), (325, 2))
        dv_st.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD))
        wx.StaticLine(panel)
        wx.StaticText(panel, label="VANO N:", pos=(10, 45))
        wx.StaticText(panel, label="LUZ \n [m]", pos=(90, 45))
        wx.StaticText(panel, label="SECCION \n INICIAL", pos=(165, 45))
        wx.StaticText(panel, label="SECCION \n FINAL", pos=(255, 45))
        wx.StaticLine(panel, -1, (5, 85), (325, 2))

        # Bucle

        self.filas = parent.DG[0]
        if parent.DG[2]:
            self.filas = self.filas + 1
        if parent.DG[3]:
            self.filas = self.filas + 1
        self.L = np.array([[0]*6]*self.filas)
        self.long = []
        l = 100
        i = 0

        # Si tengo voladizo izquierdo...
        if parent.DG[2]:
            j = 30
            self.numvan = wx.StaticText(panel, label=str('Vol. Izq.'), pos=(12, l+5))
            self.L[i, 0] = 0
            j += 30
            self.luz = wx.TextCtrl(panel, value="", pos=(j, l), size=(80, -1))
            self.long.append(self.luz)
            j = j + 125
            self.secin = wx.StaticText(panel, label=str(1+10*i), pos=(j, l+5), size=(80, -1))
            self.L[i, 2] = float(self.secin.GetLabel())
            j = j + 85
            self.secfin = wx.StaticText(panel, label=str(11+10*i), pos=(j, l+5), size=(80, -1))
            self.L[i, 3] = float(self.secfin.GetLabel())
            l = l + 50
            i = i + 1
            for i in range(1, parent.DG[0]+1):
                j = 30
                self.numvan = wx.StaticText(panel, label=str(i), pos=(j, l+5))
                self.L[i, 0] = float(self.numvan.GetLabel())
                j = j + 30
                self.luz = wx.TextCtrl(panel, value="", pos=(j, l), size=(80, -1))
                self.long.append(self.luz)
                j = j + 125
                self.secin = wx.StaticText(panel, label=str(1+10*i), pos=(j, l+5), size=(80, -1))
                self.L[i, 2] = float(self.secin.GetLabel())
                j = j + 85
                self.secfin = wx.StaticText(panel, label=str(11+10*i), pos=(j, l+5), size=(80, -1))
                self.L[i, 3] = float(self.secfin.GetLabel())
                l = l + 50


            # Si tiene voladizo derecho...
            if parent.DG[3]:
                j = 30
                self.numvan = wx.StaticText(panel, label=str('Vol. Der.'), pos=(12, l+5))
                self.L[i+1, 0] = parent.DG[0]+1
                j = j + 30
                self.luz = wx.TextCtrl(panel, value="", pos=(j, l), size=(80, -1))
                self.long.append(self.luz)
                j = j + 125
                self.secin = wx.StaticText(panel, label=str(1+10*(i+1)), pos=(j, l+5), size=(80, -1))
                self.L[i+1, 2] = float(self.secin.GetLabel())
                j = j + 85
                self.secfin = wx.StaticText(panel, label=str(11+10*(i+1)), pos=(j, l+5), size=(80, -1))
                self.L[i+1, 3] = float(self.secfin.GetLabel())
                l = l + 50
        else:
            for i in range(0, parent.DG[0]):
                j = 30
                self.numvan = wx.StaticText(panel, label=str(i+1), pos=(j, l+5))
                self.L[i, 0] = float(self.numvan.GetLabel())
                j = j + 30
                self.luz = wx.TextCtrl(panel, value="", pos=(j, l), size=(80, -1))
                self.long.append(self.luz)
                j = j + 125
                self.secin = wx.StaticText(panel, label=str(1+10*i), pos=(j, l+5), size=(80, -1))
                self.L[i, 2] = float(self.secin.GetLabel())
                j = j + 85
                self.secfin = wx.StaticText(panel, label=str(11+10*i), pos=(j, l+5), size=(80, -1))
                self.L[i, 3] = float(self.secfin.GetLabel())
                l = l + 50
            if parent.DG[3]:
                j = 30
                self.numvan = wx.StaticText(panel, label=str('Vol. Der.'), pos=(12, l+5))
                self.L[i+1, 0] = parent.DG[0]+1
                j = j + 30
                self.luz = wx.TextCtrl(panel, value="", pos=(j, l), size=(80, -1))
                self.long.append(self.luz)
                j = j + 125
                self.secin = wx.StaticText(panel, label=str(1+10*(i+1)), pos=(j, l+5), size=(80, -1))
                self.L[i+1, 2] = float(self.secin.GetLabel())
                j = j + 85
                self.secfin = wx.StaticText(panel, label=str(11+10*(i+1)), pos=(j, l+5), size=(80, -1))
                self.L[i+1, 3] = float(self.secfin.GetLabel())
                l = l + 50

        # Botones
        wx.StaticLine(panel, -1, (5, l), (325, 2))

        BotonOK = wx.Button(panel, wx.ID_OK, pos=(70, l+15))
        BotonOK.Bind(wx.EVT_BUTTON, self.OnClick, BotonOK)
        BotonCancel = wx.Button(panel, wx.ID_CANCEL, pos=(180, l+15))
        BotonCancel.Bind(wx.EVT_BUTTON, self.OnClick, BotonCancel)

        wx.StaticLine(panel, -1, (5, l+50), (325, 2))
        self.Center()
        self.Show()

    # Funciones de los botones
    def OnCancel(self, event):
        self.Close()

    def OnClick(self, event):
        for n in range(0, self.filas):
            self.L[n, 1] = self.long[n].GetValue()
        self.L[0, 4] = 0
        self.L[0, 5] = self.L[0, 1]
        for t in range(1, self.filas):
            self.L[t, 4] = self.L[t-1, 5]
            self.L[t, 5] = self.L[t, 4] + self.L[t, 1]
        print self.L

        fichero = open('datos/matrizL.dat','w')

        for p in range(0, self.filas):
            for q in range(0, 6):
                # print self.L[p, q]
                fichero.write(str(self.L[p, q])+'\n')

        fichero.close()

        self.Close()


class DatosSecciones(wx.Frame):

    def __init__(self, parent):
        super(DatosSecciones, self).__init__(parent, size=(750, 1000), style=wx.CLOSE_BOX | wx.CAPTION | wx.SYSTEM_MENU)
        self.panel = wx.Panel (self, -1)

        # Datos Secciones

        wx.StaticLine(self.panel, -1, (5, 5), (750, 2))
        dv_st = wx.StaticText(self.panel, label="DATOS SECCIONES TIPICAS", pos=(250, 10))
        wx.StaticLine(self.panel, -1, (5, 30), (750, 2))
        dv_st.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD))
        wx.StaticLine(self.panel)
        wx.StaticText (self.panel, label=('NOMBRE'), pos=(15, 80))
        wx.StaticText (self.panel, label=('A [m2]'), pos=(115, 80))
        wx.StaticText (self.panel, label=('I [m4]'), pos=(215, 80))
        wx.StaticText (self.panel, label=('v sup [m]'), pos=(315, 80))
        wx.StaticText (self.panel, label=('v inf [m]'), pos=(415, 80))
        wx.StaticText (self.panel, label=('B [m]'), pos=(515, 80))
        wx.StaticText (self.panel, label=('bw [m]'), pos=(615, 80))

        # Abre el archivo datgen.dat para crear el vector RP y DG

        # fichero1 = open('datos/datgen.dat','r')
        # self.RP = []
        # self.DG = []
        # n = 0
        # for linea in fichero1:
        #     if linea[-1] == '\n':
        #         linea = linea [:-1]
        #     if n == 0:
        #         self.RP.append(linea)
        #     else: self.DG.append(int(linea))
        #     n = n + 1

        # fichero1.close()

        # Abre el archivo matrizL.dat para re armar la matriz L

        fichero2 = open('datos/matrizL.dat','r')

        self.filas = parent.DG[0]
        if parent.DG[2]:
            self.filas = self.filas + 1
        if parent.DG[3]:
            self.filas = self.filas + 1

        self.L = np.array([[0]*6]*self.filas)

        p = 0
        q = 0
        for linea in fichero2:
            if linea[-1] == '\n':
                linea = linea [:-1]
                self.L[p, q] = float(linea)
            q += 1
            if q > 5:
                q = 0
                p += 1

        print 'Matriz L ', self.L                           # IMPRESIONES AUXILIARES -> ELIMINAR
        print ''                                            # IMPRESIONES AUXILIARES -> ELIMINAR
        print 'Vector Datos Generales ', parent.DG            # IMPRESIONES AUXILIARES -> ELIMINAR

        fichero2.close()

        # Pide los datos de las secciones tipo

        wx.StaticText(self.panel, label='Numero de Secciones a Ingresar: ', pos=(10, 45))
        self.numsecsv = wx.TextCtrl(self.panel, value="", pos=(200, 40), size=(80, -1))

        BotonOK = wx.Button(self.panel, wx.ID_OK, pos=(300, 37))
        BotonOK.Bind(wx.EVT_BUTTON, self.OnOk, BotonOK)

    def OnOk(self, event):
        self.nssv = self.numsecsv.GetValue()
        # print self.nssv

        self.C1 = np.array([[0]*7]*(self.filas*10 - 1))

        self.A = []
        self.I = []
        self.vsup = []
        self.vinf = []
        self.B = []
        self.bw = []

        l = 120
        j = 15

        for i in range(int(self.nssv)):
            print i
            # panel = wx.Panel (self, -1)

            # self.namesec =
            wx.StaticText(self.panel, label=('SV' + str(i+1)), pos=(j, l+5))
            self.Area = wx.TextCtrl(self.panel, value='', pos=(j + 75, l), size=(80, -1))
            self.A.append(self.Area)

            self.Inercia = wx.TextCtrl(self.panel, value='', pos=(j + 175, l), size=(80, -1))
            self.I.append(self.Inercia)

            self.v1 = wx.TextCtrl(self.panel, value='', pos=(j + 275, l), size=(80, -1))
            self.vsup.append(self.v1)

            self.v2 = wx.TextCtrl(self.panel, value='', pos=(j + 375, l), size=(80, -1))
            self.vinf.append(self.v2)

            self.Ancho = wx.TextCtrl(self.panel, value='', pos=(j + 475, l), size=(80, -1))
            self.B.append(self.Ancho)

            self.Almas = wx.TextCtrl(self.panel, value='', pos=(j + 575, l), size=(80, -1))
            self.bw.append(self.Almas)
            l += 50

        BotonOK = wx.Button(self.panel, wx.ID_OK, pos=(200, l))
        BotonOK.Bind(wx.EVT_BUTTON, self.OnAceptar, BotonOK)
        BotonCancel = wx.Button(self.panel, wx.ID_CANCEL, pos=(500, l))
        BotonCancel.Bind(wx.EVT_BUTTON, self.OnCancelar, BotonCancel)

    def OnAceptar(self, event):
        for n in range(int(self.nssv)):
            self.C1[n,0] = self.A[n].GetValue()
            self.C1[n,1] = self.I[n].GetValue()
            # print self.vsup
            # print self.vinf
            # print self.B
            # print self.bw
        print self.C1


        #     self.L[n, 1] = self.long[n].GetValue()
        # self.L[0, 4] = 0
        # self.L[0, 5] = self.L[0, 1]
        # for t in range(1, self.filas):
        #     self.L[t, 4] = self.L[t-1, 5]
        #     self.L[t, 5] = self.L[t, 4] + self.L[t, 1]
        # print self.L
        #
        # fichero = open('datos/matrizL.dat','w')
        #
        # for p in range(0, self.filas):
        #     for q in range(0, 6):
        #         # print self.L[p, q]
        #         fichero.write(str(self.L[p, q])+'\n')
        #
        # fichero.close()

    def OnCancelar(self, event):
        self.Close()












        # for i in range(1, self.DG[0]+1):
        #         j = 30
        #         self.numvan = wx.StaticText(panel, label=str(i), pos=(j, l+5))
        #         self.L[i, 0] = float(self.numvan.GetLabel())
        #         j = j + 30
        #         self.luz = wx.TextCtrl(panel, value="", pos=(j, l), size=(80, -1))
        #         self.long.append(self.luz)
        #         j = j + 125
        #         self.secin = wx.StaticText(panel, label=str(1+10*i), pos=(j, l+5), size=(80, -1))
        #         self.L[i, 2] = float(self.secin.GetLabel())
        #         j = j + 85
        #         self.secfin = wx.StaticText(panel, label=str(11+10*i), pos=(j, l+5), size=(80, -1))
        #         self.L[i, 3] = float(self.secfin.GetLabel())
        #         l = l + 50



app = wx.App(False)
frame = MainWindow(None, "PCCB Version 1.1 15")
app.MainLoop()
