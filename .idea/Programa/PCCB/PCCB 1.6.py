# Importamos las librerias a ser utilizadas
import os
# Importamos wx.python
import wx
# Importamos numpy la renombramos sp
import numpy as np

__author__ = 'DP & EZ'

class variables:
    def __init__(self):
        # DEFINICION DE VARIABLES A UTILIZAR EN EL PROGRAMA
        # Variable que contiene la referencia del puente
        self.datos_rp = None
        # Variable que contiene los datos generales de la Estructura
        self.datos_dg = None
        # Variable que contiene los datos de los vanos
        self.datos_l = None
        # Variable que contiene los datos de las secciones
        self.datos_c = None

class MainWindow(wx.Frame):
    def __init__(self, parent, title):

        # Generamos el frame
        wx.Frame.__init__(self, parent, title=title, size=(-1, -1))
        print parent

        self.dirname = ''

        # Barra de menu
        self.menu_bar()

        # barra de herramientas
        self.toolbar()

        # Status Bar - Barra al fondo de la ventana
        self.CreateStatusBar()

        # Panel
        panel = wx.Panel(self, -1)
        panel.SetBackgroundColour('White')

        self.Center()
        self.Show()

    def toolbar(self):
        toolbar = self.CreateToolBar()
        dg_tool = toolbar.AddLabelTool(wx.ID_ANY, 'Datos Generales', wx.Bitmap('img/dgg.png'))
        dv_tool = toolbar.AddLabelTool(wx.ID_ANY, 'Datos Vanos', wx.Bitmap('img/dvg.png'))
        toolbar.AddSeparator()
        toolbar.Realize()
        # Eventos
        # Abre la ventana de datos generales
        self.Bind(wx.EVT_MENU, self.click_dg, dg_tool)
        # Abre la ventana de datos vano
        self.Bind(wx.EVT_MENU, self.click_dv, dv_tool)

    def menu_bar(self):

        # Declaramos los menu
        filemenu = wx.Menu()
        datosmenu = wx.Menu()
        ayudamenu = wx.Menu()
        sb_ds = wx.Menu()

        # Contenido del filemenu
        m_nvo = wx.MenuItem(filemenu, -1, '&Nuevo\tCtrl+N', 'Nuevo archivo')
        m_nvo.SetBitmap(wx.Bitmap('img/nvo.png'))
        m_e = wx.MenuItem(filemenu, -1, '&Quit\tCtrl+Q', 'Salir del programa')
        m_e.SetBitmap(wx.Bitmap('img/exit.png'))
        m_a = wx.MenuItem(filemenu, -1, '&Abrir\tCtrl+O', 'Abrir archivo')
        m_a.SetBitmap(wx.Bitmap('img/abrir.png'))
        m_g = wx.MenuItem(filemenu, -1, '&Guardar\tCtrl+S', 'Guardar archivo')
        m_g.SetBitmap(wx.Bitmap('img/g.png'))
        m_gc = wx.MenuItem(filemenu, -1, '&Guardar Como...\tCtrl+G', 'Guardar archivo como')
        m_g.SetBitmap(wx.Bitmap('img/g.png'))

        # Menu Archivo
        filemenu.AppendItem(m_nvo)
        filemenu.AppendItem(m_a)
        filemenu.AppendItem(m_g)
        filemenu.AppendItem(m_gc)
        filemenu.AppendSeparator()
        filemenu.AppendItem(m_e)

        # Contenido del datosmenu
        m_dg = wx.MenuItem(datosmenu, -1, 'Datos &Generales', 'Ingrese el valor de los datos generales')
        m_dg.SetBitmap(wx.Bitmap('img/dgc.png'))
        m_dv = wx.MenuItem(datosmenu, -1, 'Datos &Vanos', 'Ingrese datos referidos a los vanos')
        m_dv.SetBitmap(wx.Bitmap('img/dvc.png'))

        # Contenido de datos secciones
        sb_ds.Append(15, 'Datos solo &viga')
        sb_ds.Append(16, 'Datos viga + losa')

        # Menu Datos
        datosmenu.AppendItem(m_dg)
        datosmenu.AppendItem(m_dv)
        datosmenu.AppendMenu(-1, 'Datos &Secciones', sb_ds)

        # Contenido del ayudamenu
        m_ab = wx.MenuItem(ayudamenu, -1, 'About Us...', 'Acerca de nosotros')

        # Menu Ayuda
        ayudamenu.AppendItem(m_ab)

        # Suma al menu, las distintas etiquetas
        menubar = wx.MenuBar()
        menubar.Append(filemenu, "&Archivo")
        menubar.Append(datosmenu, "&Datos")
        menubar.Append(ayudamenu, "&Ayuda")
        self.SetMenuBar(menubar)

        # Eventos.
        # Abre Nuevo Archivo
        self.Bind(wx.EVT_MENU, self.click_nuevo, m_nvo)
        # Abre Nuevo Archivo
        self.Bind(wx.EVT_MENU, self.open, m_a)
        # Abre la ventana de datos generales
        self.Bind(wx.EVT_MENU, self.click_dg, m_dg)
        # Abre la ventana de datos vano
        self.Bind(wx.EVT_MENU, self.click_dv, m_dv)
        # Abre la ventana de datos de secciones
        self.Bind(wx.EVT_MENU, self.click_dssv, id=15)
        # Sale del programa
        self.Bind(wx.EVT_MENU, self.exit, m_e)
        # Abre el mensaje "Acerca de..."
        self.Bind(wx.EVT_MENU, self.about, m_ab)

        self.SetMenuBar(menubar)
        self.Centre()
        self.Show(True)

    # Abrir ventana datos generales
    def click_dg(self, event):
        DatosGenerales(self).Show()

    # Generar Variable Locales
    def click_nuevo(self, event):
        print 'a'

    # Abrir ventana datos vano
    def click_dv(self, event):
        DatosVanos(self).Show()

    # Abrir ventana datos de secciones
    def click_dssv(self, event):
        DatosSecciones(self).Show()

    # Ventana acerca de nosotros
    def about(self, event):
        # Create a message dialog box
        dlg = wx.MessageDialog(self,
                               "Desarrollado por JCT, ATA, DP & EZ para MyT Consultora SRL"
                               "\nBasado en Programa PCCB de Dr. Ing. Angel Carlos Aparicio"
                               "\n(Universidad Politecnica de Catalunia - Barcelona)",
                               "About PCCB Version 2015", wx.OK)
        dlg.ShowModal()  # Shows it
        dlg.Destroy()  # finally destroy it when finished.

    # Funcion para cerrar
    def exit(self, event):
        self.Close()  # Close the frame.

    # Funcion para open file
    def open(self, event):
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
        boton_ok = wx.Button(panel, wx.ID_OK, pos=(100, 300))
        boton_ok.Bind(wx.EVT_BUTTON, self.onclick_dg, boton_ok)
        boton_cancel = wx.Button(panel, wx.ID_CANCEL, pos=(210, 300))
        boton_cancel.Bind(wx.EVT_BUTTON, self.cancel, boton_cancel)

        # Voladizos Si o No
        self.vi_rbs = wx.RadioButton(panel, -1, "Si", style=wx.RB_GROUP)
        self.Bind(wx.EVT_RADIOBUTTON, self.onclick_dg, boton_ok)
        self.vi_rbn = wx.RadioButton(panel, -1, "No")
        self.vd_rbs = wx.RadioButton(panel, -1, "Si", style=wx.RB_GROUP)
        self.Bind(wx.EVT_RADIOBUTTON, self.onclick_dg, boton_ok)
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
        fgs6.Add(boton_ok, 0, wx.ALIGN_CENTER, 5)
        fgs6.Add(boton_cancel, 0, wx.ALIGN_CENTER, 5)

        fgs2.AddGrowableCol(1)
        fgs3.AddGrowableCol(0)

        # Asiganacion a la fila de la grilla
        tp_g.Add(wx.StaticLine(panel), 0, wx.EXPAND | wx.ALL, 5)
        tp_g.Add(fgs1, 0, wx.ALIGN_CENTER)
        tp_g.Add(wx.StaticLine(panel), 0, wx.EXPAND | wx.ALL, 5)
        tp_g.Add(fgs2, 0, wx.EXPAND | wx.ALL, 5)
        tp_g.Add(wx.StaticLine(panel), 0, wx.EXPAND | wx.ALL, 5)
        tp_g.Add(fgs3, 0, wx.EXPAND | wx.ALL, 5)
        tp_g.Add(wx.StaticLine(panel), 0, wx.EXPAND | wx.ALL, 5)
        tp_g.Add(fgs4, 0, wx.EXPAND | wx.ALL, 5)
        tp_g.Add(wx.StaticLine(panel), 0, wx.EXPAND | wx.ALL, 5)
        tp_g.Add(fgs5, 0, wx.EXPAND | wx.ALL, 5)
        tp_g.Add(wx.StaticLine(panel), 0, wx.EXPAND | wx.ALL, 5)
        tp_g.Add(fgs6, 0, wx.ALIGN_CENTER, 5)
        tp_g.Add(wx.StaticLine(panel), 0, wx.EXPAND | wx.ALL, 5)

        panel.SetSizer(tp_g)
        tp_g.Fit(panel)

        self.Center()
        self.Show()

    def onclick_dg(self, parent):

        # Definicion de datos.rp y datos.dg como vectores vacios
        parent.datos_rp = [0]
        parent.datos_dg = [0]*4

        parent.datos_rp[0] = str(self.rp_tc.GetValue())
        print parent.datos_rp
        parent.datos_dg[0] = int(self.nv_tc.GetValue())
        parent.datos_dg[1] = float(self.me_tc.GetValue())
        parent.datos_dg[2] = self.vi_rbs.GetValue()
        parent.datos_dg[3] = self.vd_rbs.GetValue()
        print parent.datos_dg
        self.Close(True)

    def cancel(self, event):
        self.Close(True)


class DatosVanos(wx.Frame):
    def __init__(self, parent):
        super(DatosVanos, self).__init__(parent, size=(340, 700), style=wx.CLOSE_BOX | wx.CAPTION | wx.SYSTEM_MENU)
        panel = wx.Panel(self, -1)


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

        # Bucle para definir la cantidad de filas de la matriz datos_l

        print parent.datos_dg
        self.filas = parent.datos_dg[0]
        if parent.datos_dg[2] is True:
            self.filas += 1
        if parent.datos_dg[3] is True:
            self.filas += 1
        parent.datos_l = np.array([[0] * 6] * self.filas)
        self.long = []
        l = 100
        i = 0

        # Si tengo voladizo izquierdo...
        if parent.datos_dg[2] is True:
            j = 30
            self.numvan = wx.StaticText(panel, label=str('Vol. Izq.'), pos=(12, l + 5))
            parent.datos_l[i, 0] = 0
            j += 30
            self.luz = wx.TextCtrl(panel, value="", pos=(j, l), size=(80, -1))
            self.long.append(self.luz)
            j += 125
            self.secin = wx.StaticText(panel, label=str(1 + 10 * i), pos=(j, l + 5), size=(80, -1))
            parent.datos_l[i, 2] = float(self.secin.GetLabel())
            j += 85
            self.secfin = wx.StaticText(panel, label=str(11 + 10 * i), pos=(j, l + 5), size=(80, -1))
            parent.datos_l[i, 3] = float(self.secfin.GetLabel())
            l += 50
            i += 1
            for i in range(1, parent.datos_dg[0] + 1):
                j = 30
                self.numvan = wx.StaticText(panel, label=str(i), pos=(j, l + 5))
                parent.datos_l[i, 0] = float(self.numvan.GetLabel())
                j += 30
                self.luz = wx.TextCtrl(panel, value="", pos=(j, l), size=(80, -1))
                self.long.append(self.luz)
                j += 125
                self.secin = wx.StaticText(panel, label=str(1 + 10 * i), pos=(j, l + 5), size=(80, -1))
                parent.datos_l[i, 2] = float(self.secin.GetLabel())
                j += 85
                self.secfin = wx.StaticText(panel, label=str(11 + 10 * i), pos=(j, l + 5), size=(80, -1))
                parent.datos_l[i, 3] = float(self.secfin.GetLabel())
                l += 50

            # Si tiene voladizo derecho...
            if parent.datos_dg[3] is True:
                j = 30
                self.numvan = wx.StaticText(panel, label=str('Vol. Der.'), pos=(12, l + 5))
                parent.datos_l[i + 1, 0] = parent.datos_dg[0] + 1
                j += 30
                self.luz = wx.TextCtrl(panel, value="", pos=(j, l), size=(80, -1))
                self.long.append(self.luz)
                j += 125
                self.secin = wx.StaticText(panel, label=str(1 + 10 * (i + 1)), pos=(j, l + 5), size=(80, -1))
                parent.datos_l[i + 1, 2] = float(self.secin.GetLabel())
                j += 85
                self.secfin = wx.StaticText(panel, label=str(11 + 10 * (i + 1)), pos=(j, l + 5), size=(80, -1))
                parent.datos_l[i + 1, 3] = float(self.secfin.GetLabel())
                l += 50
        else:
            for i in range(0, parent.datos_dg[0]):
                j = 30
                self.numvan = wx.StaticText(panel, label=str(i + 1), pos=(j, l + 5))
                parent.datos_l[i, 0] = float(self.numvan.GetLabel())
                j += 30
                self.luz = wx.TextCtrl(panel, value="", pos=(j, l), size=(80, -1))
                self.long.append(self.luz)
                j += 125
                self.secin = wx.StaticText(panel, label=str(1 + 10 * i), pos=(j, l + 5), size=(80, -1))
                parent.datos_l[i, 2] = float(self.secin.GetLabel())
                j += 85
                self.secfin = wx.StaticText(panel, label=str(11 + 10 * i), pos=(j, l + 5), size=(80, -1))
                parent.datos_l[i, 3] = float(self.secfin.GetLabel())
                l += 50
            if parent.datos_dg[3] is True:
                j = 30
                self.numvan = wx.StaticText(panel, label=str('Vol. Der.'), pos=(12, l + 5))
                parent.datos_l[i + 1, 0] = parent.datos_dg[0] + 1
                j += 30
                self.luz = wx.TextCtrl(panel, value="", pos=(j, l), size=(80, -1))
                self.long.append(self.luz)
                j += 125
                self.secin = wx.StaticText(panel, label=str(1 + 10 * (i + 1)), pos=(j, l + 5), size=(80, -1))
                parent.datos_l[i + 1, 2] = float(self.secin.GetLabel())
                j += 85
                self.secfin = wx.StaticText(panel, label=str(11 + 10 * (i + 1)), pos=(j, l + 5), size=(80, -1))
                parent.datos_l[i + 1, 3] = float(self.secfin.GetLabel())
                l += 50

        # Botones
        wx.StaticLine(panel, -1, (5, l), (325, 2))

        botonook = wx.Button(panel, wx.ID_OK, pos=(70, l + 15))
        botonook.Bind(wx.EVT_BUTTON, self.onclick_dv, botonook)
        botoncancel = wx.Button(panel, wx.ID_CANCEL, pos=(180, l + 15))
        botoncancel.Bind(wx.EVT_BUTTON, self.cancel, botoncancel)

        wx.StaticLine(panel, -1, (5, l + 50), (325, 2))
        self.Center()
        self.Show()

    # Funciones de los botones
    def cancel(self, parent):
        self.Close()

    def onclick_dv(self, parent):
        for n in range(0, self.filas):
            parent.datos_l[n, 1] = self.long[n].GetValue()
        parent.datos_l[0, 4] = 0
        parent.datos_l[0, 5] = parent.datos_l[0, 1]
        for t in range(1, self.filas):
            parent.datos_l[t, 4] = parent.datos_l[t - 1, 5]
            parent.datos_l[t, 5] = parent.datos_l[t, 4] + parent.datos_l[t, 1]
        print parent.datos_l

        # fichero = open('datos/matrizL.dat', 'w')
        #
        # for p in range(0, self.filas):
        #     for q in range(0, 6):
        #         # print self.L[p, q]
        #         fichero.write(str(self.L[p, q]) + '\n')
        #
        # fichero.close()

        self.Close()


class DatosSecciones(wx.Frame):
    def __init__(self, parent):
        super(DatosSecciones, self).__init__(parent, size=(750, 1000), style=wx.CLOSE_BOX | wx.CAPTION | wx.SYSTEM_MENU)
        self.panel = wx.Panel(self, -1)

        # Datos Secciones

        wx.StaticLine(self.panel, -1, (5, 5), (750, 2))
        dv_st = wx.StaticText(self.panel, label="DATOS SECCIONES TIPICAS", pos=(250, 10))
        wx.StaticLine(self.panel, -1, (5, 30), (750, 2))
        dv_st.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD))
        wx.StaticLine(self.panel)
        wx.StaticText(self.panel, label=('NOMBRE'), pos=(15, 80))
        wx.StaticText(self.panel, label=('A [m2]'), pos=(115, 80))
        wx.StaticText(self.panel, label=('I [m4]'), pos=(215, 80))
        wx.StaticText(self.panel, label=('v sup [m]'), pos=(315, 80))
        wx.StaticText(self.panel, label=('v inf [m]'), pos=(415, 80))
        wx.StaticText(self.panel, label=('B [m]'), pos=(515, 80))
        wx.StaticText(self.panel, label=('bw [m]'), pos=(615, 80))

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

        fichero2 = open('datos/matrizL.dat', 'r')

        self.filas = parent.datos_dg[0]
        if parent.datos_dg[2]:
            self.filas += 1
        if parent.datos_dg[3]:
            self.filas += 1

        self.L = np.array([[0] * 6] * self.filas)

        p = 0
        q = 0
        for linea in fichero2:
            if linea[-1] == '\n':
                linea = linea[:-1]
                self.L[p, q] = float(linea)
            q += 1
            if q > 5:
                q = 0
                p += 1

        print 'Matriz L ', self.L  # IMPRESIONES AUXILIARES -> ELIMINAR
        print ''  # IMPRESIONES AUXILIARES -> ELIMINAR
        print 'Vector Datos Generales ', parent.datos_dg  # IMPRESIONES AUXILIARES -> ELIMINAR

        fichero2.close()

        # Pide los datos de las secciones tipo

        wx.StaticText(self.panel, label='Numero de Secciones a Ingresar: ', pos=(10, 45))
        self.numsecsv = wx.TextCtrl(self.panel, value="", pos=(200, 40), size=(80, -1))

        botonok = wx.Button(self.panel, wx.ID_OK, pos=(300, 37))
        botonok.Bind(wx.EVT_BUTTON, self.OnOk, botonok)

    def OnOk(self, event):
        self.nssv = self.numsecsv.GetValue()
        # print self.nssv

        self.C1 = np.array([[0] * 7] * (self.filas * 10 - 1))

        self.A = None
        self.I = None
        self.vsup = None
        self.vinf = None
        self.B = None
        self.bw = None

        l = 120
        j = 15

        for i in range(int(self.nssv)):
            print i
            # panel = wx.Panel (self, -1)

            # self.namesec =
            wx.StaticText(self.panel, label=('SV' + str(i + 1)), pos=(j, l + 5))
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

        botonok = wx.Button(self.panel, wx.ID_OK, pos=(200, l))
        botonok.Bind(wx.EVT_BUTTON, self.aceptar, botonok)
        botoncancel = wx.Button(self.panel, wx.ID_CANCEL, pos=(500, l))
        botoncancel.Bind(wx.EVT_BUTTON, self.cancel, botoncancel)

    def aceptar(self, event):
        for n in range(int(self.nssv)):
            self.C1[n, 0] = self.A[n].GetValue()
            self.C1[n, 1] = self.I[n].GetValue()
            # print self.vsup
            # print self.vinf
            # print self.B
            # print self.bw
        print self.C1

    def cancel(self, event):
        self.Close()


app = wx.App()
frame = MainWindow(None, "PCCB Version 1.1 15")
app.MainLoop()
