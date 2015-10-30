# Importamos las librerias a ser utilizadas
import os
# Importamos wx.python
import wx
# Importamos numpy la renombramos np
import numpy as np

__author__ = 'DP & EZ'


class MainWindow(wx.Frame):
    def __init__(self, parent, title):

        # Generamos el frame
        wx.Frame.__init__(self, parent, title=title, size=(-1, -1))

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
        m_ep = wx.MenuItem(datosmenu, -1, 'Estructuras Parciales', 'Ingrese datos de Estructuras Parciales')

        # Contenido de datos secciones
        sb_ds.Append(15, 'Datos solo &viga')
        sb_ds.Append(16, 'Datos viga + losa')

        # Menu Datos
        datosmenu.AppendItem(m_dg)
        datosmenu.AppendItem(m_dv)
        datosmenu.AppendMenu(-1, 'Datos &Secciones', sb_ds)
        datosmenu.AppendItem( m_ep)

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
        # Abre la ventana de Estructuras Parciales
        self.Bind(wx.EVT_MENU, self.click_ep, m_ep)
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

    # Abrir ventana de Estructuras Parciales
    def click_ep(self, event):
        EstructurasParciales(self).Show()

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

    def onclick_dg(self, event):

        # Definicion de datos.rp y datos.dg como vectores vacios
        event.datos_rp = [0]
        event.datos_dg = [0]*4

        event.datos_rp[0] = str(self.rp_tc.GetValue())
        print event.datos_rp
        event.datos_dg[0] = int(self.nv_tc.GetValue())
        event.datos_dg[1] = float(self.me_tc.GetValue())
        event.datos_dg[2] = self.vi_rbs.GetValue()
        event.datos_dg[3] = self.vd_rbs.GetValue()
        print event.datos_dg
        np.save('datos/datos_dg', event.datos_dg)

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

        datos_dg = np.load('datos/datos_dg.npy')

        self.filas = int(datos_dg[0])
        if int(datos_dg[2]) == 1:
            self.filas += 1
        if int(datos_dg[3]) == 1:
            self.filas += 1
        self.datos_l = np.array([[0] * 6] * self.filas)
        self.long = []
        l = 100
        i = 0

        # Si tengo voladizo izquierdo...
        if datos_dg[2] == 1:
            j = 30
            self.numvan = wx.StaticText(panel, label=str('Vol. Izq.'), pos=(12, l + 5))
            self.datos_l[i, 0] = 0
            j += 30
            self.luz = wx.TextCtrl(panel, value="", pos=(j, l), size=(80, -1))
            self.long.append(self.luz)
            j += 125
            self.secin = wx.StaticText(panel, label=str(1 + 10 * i), pos=(j, l + 5), size=(80, -1))
            self.datos_l[i, 2] = float(self.secin.GetLabel())
            j += 85
            self.secfin = wx.StaticText(panel, label=str(11 + 10 * i), pos=(j, l + 5), size=(80, -1))
            self.datos_l[i, 3] = float(self.secfin.GetLabel())
            l += 50
            i += 1
            for i in range(1, int(datos_dg[0]) + 1):
                j = 30
                self.numvan = wx.StaticText(panel, label=str(i), pos=(j, l + 5))
                self.datos_l[i, 0] = float(self.numvan.GetLabel())
                j += 30
                self.luz = wx.TextCtrl(panel, value="", pos=(j, l), size=(80, -1))
                self.long.append(self.luz)
                j += 125
                self.secin = wx.StaticText(panel, label=str(1 + 10 * i), pos=(j, l + 5), size=(80, -1))
                self.datos_l[i, 2] = float(self.secin.GetLabel())
                j += 85
                self.secfin = wx.StaticText(panel, label=str(11 + 10 * i), pos=(j, l + 5), size=(80, -1))
                self.datos_l[i, 3] = float(self.secfin.GetLabel())
                l += 50

            # Si tiene voladizo derecho...
            if datos_dg[3] == 1:
                j = 30
                self.numvan = wx.StaticText(panel, label=str('Vol. Der.'), pos=(12, l + 5))
                self.datos_l[i + 1, 0] = datos_dg[0] + 1
                j += 30
                self.luz = wx.TextCtrl(panel, value="", pos=(j, l), size=(80, -1))
                self.long.append(self.luz)
                j += 125
                self.secin = wx.StaticText(panel, label=str(1 + 10 * (i + 1)), pos=(j, l + 5), size=(80, -1))
                self.datos_l[i + 1, 2] = float(self.secin.GetLabel())
                j += 85
                self.secfin = wx.StaticText(panel, label=str(11 + 10 * (i + 1)), pos=(j, l + 5), size=(80, -1))
                self.datos_l[i + 1, 3] = float(self.secfin.GetLabel())
                l += 50
        else:
            for i in range(0, int(datos_dg[0])):
                j = 30
                self.numvan = wx.StaticText(panel, label=str(i + 1), pos=(j, l + 5))
                self.datos_l[i, 0] = float(self.numvan.GetLabel())
                j += 30
                self.luz = wx.TextCtrl(panel, value="", pos=(j, l), size=(80, -1))
                self.long.append(self.luz)
                j += 125
                self.secin = wx.StaticText(panel, label=str(1 + 10 * i), pos=(j, l + 5), size=(80, -1))
                self.datos_l[i, 2] = float(self.secin.GetLabel())
                j += 85
                self.secfin = wx.StaticText(panel, label=str(11 + 10 * i), pos=(j, l + 5), size=(80, -1))
                self.datos_l[i, 3] = float(self.secfin.GetLabel())
                l += 50
            if datos_dg[3] == 1:
                j = 30
                self.numvan = wx.StaticText(panel, label=str('Vol. Der.'), pos=(12, l + 5))
                self.datos_l[i + 1, 0] = datos_dg[0] + 1
                j += 30
                self.luz = wx.TextCtrl(panel, value="", pos=(j, l), size=(80, -1))
                self.long.append(self.luz)
                j += 125
                self.secin = wx.StaticText(panel, label=str(1 + 10 * (i + 1)), pos=(j, l + 5), size=(80, -1))
                self.datos_l[i + 1, 2] = float(self.secin.GetLabel())
                j += 85
                self.secfin = wx.StaticText(panel, label=str(11 + 10 * (i + 1)), pos=(j, l + 5), size=(80, -1))
                self.datos_l[i + 1, 3] = float(self.secfin.GetLabel())
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
            self.datos_l[n, 1] = self.long[n].GetValue()
            self.datos_l[0, 4] = 0
            self.datos_l[0, 5] = self.datos_l[0, 1]
        for t in range(1, self.filas):
            self.datos_l[t, 4] = self.datos_l[t - 1, 5]
            self.datos_l[t, 5] = self.datos_l[t, 4] + self.datos_l[t, 1]

        np.save('datos/datos_l', self.datos_l)
        print self.datos_l

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
        wx.StaticText(self.panel, label='NOMBRE', pos=(15, 80))
        wx.StaticText(self.panel, label='A [m2]', pos=(115, 80))
        wx.StaticText(self.panel, label='I [m4]', pos=(215, 80))
        wx.StaticText(self.panel, label='v sup [m]', pos=(300, 80))
        wx.StaticText(self.panel, label='v inf [m]', pos=(400, 80))
        wx.StaticText(self.panel, label='B [m]', pos=(515, 80))
        wx.StaticText(self.panel, label='bw [m]', pos=(615, 80))

        # Pide los datos de las secciones tipo

        wx.StaticText(self.panel, label='Numero de Secciones a Ingresar: ', pos=(10, 45))
        self.numsecsv = wx.TextCtrl(self.panel, value="", pos=(200, 40), size=(80, -1))

        botonok = wx.Button(self.panel, wx.ID_OK, pos=(300, 37))
        botonok.Bind(wx.EVT_BUTTON, self.OnOk, botonok)

    def OnOk(self, event):
        self.nssv = self.numsecsv.GetValue()

        l = 120
        j = 15
        self.a = []
        self.ine = []
        self.vsup = []
        self.vinf = []
        self.b = []
        self.bw = []

        for i in range(int(self.nssv)):

            wx.StaticText(self.panel, label=('SV' + str(i + 1)), pos=(j, l + 5))
            self.area = wx.TextCtrl(self.panel, value='', pos=(j + 75, l), size=(80, -1))
            self.a.append(self.area)

            self.inercia = wx.TextCtrl(self.panel, value='', pos=(j + 175, l), size=(80, -1))
            self.ine.append(self.inercia)

            self.v1 = wx.TextCtrl(self.panel, value='', pos=(j + 275, l), size=(80, -1))
            self.vsup.append(self.v1)

            self.v2 = wx.TextCtrl(self.panel, value='', pos=(j + 375, l), size=(80, -1))
            self.vinf.append(self.v2)

            self.ancho = wx.TextCtrl(self.panel, value='', pos=(j + 475, l), size=(80, -1))
            self.b.append(self.ancho)

            self.almas = wx.TextCtrl(self.panel, value='', pos=(j + 575, l), size=(80, -1))
            self.bw.append(self.almas)

            l += 50

        botonok = wx.Button(self.panel, wx.ID_OK, pos=(200, l))
        botonok.Bind(wx.EVT_BUTTON, self.aceptar, botonok)
        botoncancel = wx.Button(self.panel, wx.ID_CANCEL, pos=(500, l))
        botoncancel.Bind(wx.EVT_BUTTON, self.cancel, botoncancel)

    def aceptar(self, event):
        self.c1 = np.array([[0]*6]*int(self.nssv))
        for n in range(int(self.nssv)):

            self.c1[n, 0] = self.a[n].GetValue()
            self.c1[n, 1] = self.ine[n].GetValue()
            self.c1[n, 2] = self.vsup[n].GetValue()
            self.c1[n, 3] = self.vinf[n].GetValue()
            self.c1[n, 4] = self.b[n].GetValue()
            self.c1[n, 5] = self.bw[n].GetValue()

        np.save('datos/c1', self.c1)
        print self.c1
        self.Close()

    def cancel(self, event):
        self.Close()


class EstructurasParciales(wx.Frame):
    def __init__(self, parent):
        super(EstructurasParciales, self).__init__(parent, size=(750, 1000), style=wx.CLOSE_BOX | wx.CAPTION | wx.SYSTEM_MENU)
        self.panel = wx.Panel(self, -1)

        # Datos Secciones

        wx.StaticLine(self.panel, -1, (5, 5), (750, 2))
        dv_st = wx.StaticText(self.panel, label="DATOS ESTRUCTURAS PARCIALES", pos=(250, 10))
        wx.StaticLine(self.panel, -1, (5, 30), (750, 2))
        dv_st.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD))
        wx.StaticLine(self.panel)
        wx.StaticText(self.panel, label='NOMBRE', pos=(15, 80))
        wx.StaticText(self.panel, label='SECCION RESISTENTE', pos=(115, 80))
        wx.StaticText(self.panel, label='Seccion\nInicial', pos=(215, 80))
        wx.StaticText(self.panel, label='Seccion\nFinal', pos=(315, 80))
        wx.StaticText(self.panel, label='Numero de apoyos', pos=(415, 80))
        wx.StaticText(self.panel, label='', pos=(515, 80))
        # wx.StaticText(self.panel, label='bw [m]', pos=(615, 80))

        # Pide los datos de las secciones tipo

        wx.StaticText(self.panel, label='Numero de Estructuras a Ingresar: ', pos=(10, 45))
        self.numestpar = wx.TextCtrl(self.panel, value="", pos=(200, 40), size=(80, -1))

        botonok = wx.Button(self.panel, wx.ID_OK, pos=(300, 37))
        botonok.Bind(wx.EVT_BUTTON, self.OnOk, botonok)

    def OnOk(self, event):
        self.nep = self.numestpar.GetValue()

        l = 120
        j = 15
        self.name = []
        self.sec = []
        self.si = []
        self.sf = []

        for i in range(int(self.nep)):

            wx.StaticText(self.panel, label=('Estr' + str(i + 1)), pos=(j, l + 5))
            n = wx.TextCtrl(self.panel, value='', pos=(j + 75, l), size=(80, -1))
            self.name.append(n)

            sr = wx.TextCtrl(self.panel, value='', pos=(j + 175, l), size=(80, -1))
            self.sec.append(sr)

            secin = wx.TextCtrl(self.panel, value='', pos=(j + 275, l), size=(80, -1))
            self.si.append(secin)

            secfin = wx.TextCtrl(self.panel, value='', pos=(j + 375, l), size=(80, -1))
            self.sf.append(secfin)

            nap = wx.TextCtrl(self.panel, value='', pos=(j + 475, l), size=(80, -1))
            self.n3.append(nap)

            l += 50

        botonok = wx.Button(self.panel, wx.ID_OK, pos=(200, l))
        botonok.Bind(wx.EVT_BUTTON, self.aceptar, botonok)
        botoncancel = wx.Button(self.panel, wx.ID_CANCEL, pos=(500, l))
        botoncancel.Bind(wx.EVT_BUTTON, self.cancel, botoncancel)

    def aceptar(self, event):
        for n in range(int(self.nep)):
            self.c1 = np.array([[0]*6]*int(self.nep))
            self.c1[n, 0] = self.a[n].GetValue()
            self.c1[n, 1] = self.ine[n].GetValue()
            self.c1[n, 2] = self.vsup[n].GetValue()
            self.c1[n, 3] = self.vinf[n].GetValue()
            self.c1[n, 4] = self.b[n].GetValue()
            self.c1[n, 5] = self.bw[n].GetValue()
        print self.c1

    def cancel(self, event):
        self.Close()

app = wx.App()
frame = MainWindow(None, "PCCB Version 2.0 2015")
app.MainLoop()
