# Importamos las librerias a ser utilizadas
import os
# Importamos wx.python
import wx
# Importamos numpy la renombramos np
import numpy as np
# Importamos string para la validacion
import string

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
        m_as = wx.MenuItem(datosmenu, -1, 'Asignar Secciones', 'Asigne propiedades resistentes a cada seccion')
        m_ep = wx.MenuItem(datosmenu, -1, 'Estructuras Parciales', 'Ingrese datos de Estructuras Parciales')

        # Contenido de datos secciones
        sb_ds.Append(15, 'Datos solo &viga')
        sb_ds.Append(16, 'Datos viga + losa')

        # Menu Datos
        datosmenu.AppendItem(m_dg)
        datosmenu.AppendItem(m_dv)
        datosmenu.AppendMenu(-1, 'Datos &Secciones', sb_ds)
        datosmenu.AppendItem(m_as)
        datosmenu.AppendItem(m_ep)

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
        # Abre la ventana de Asignacion de Secciones
        self.Bind(wx.EVT_MENU, self.click_as, m_as)
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
    def click_as(self, event):
        AsignacionSecciones(self).Show()

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
        self.rp_tc = wx.TextCtrl(panel, value="", validator=CharValidator("no-digit"))
        self.nv_tc = wx.TextCtrl(panel, value="", size=(180, -1), validator=CharValidator("no-alpha"))
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

        datos_dg = [0]*4

        datos_rp = str(self.rp_tc.GetValue())
        datos_dg[0] = self.nv_tc.GetValue()
        datos_dg[1] = float(self.me_tc.GetValue())
        datos_dg[2] = self.vi_rbs.GetValue()
        datos_dg[3] = self.vd_rbs.GetValue()
        if len(datos_rp) == 0:
            self.rp_tc.SetBackgroundColour("pink")
            self.rp_tc.SetFocus()
            self.rp_tc.Refresh()

        elif len(datos_dg[0]) == 0:
            self.rp_tc.SetBackgroundColour(wx.SystemSettings_GetColour(wx.SYS_COLOUR_WINDOW))
            self.rp_tc.Refresh()
            self.nv_tc.SetBackgroundColour("pink")
            self.nv_tc.SetFocus()
            self.nv_tc.Refresh()

        else:
            self.Close(True)
            datos_dg[0] = int(datos_dg[0])
            np.save('datos/datos_dg', datos_dg)
            print datos_dg
            self.nv_tc.SetBackgroundColour(wx.SystemSettings_GetColour(wx.SYS_COLOUR_WINDOW))
            self.nv_tc.Refresh()

    def cancel(self, event):
        self.Close(True)


class CharValidator(wx.PyValidator):
    def __init__(self, flag):
         wx.PyValidator.__init__(self)
         self.flag = flag
         self.Bind(wx.EVT_CHAR, self.OnChar)

    def Clone(self):
         """
         Note that every validator must implement the Clone() method.
         """
         return CharValidator(self.flag)

    def Validate(self, win):
         return True

    def TransferToWindow(self):
         return True

    def TransferFromWindow(self):
         return True

    def OnChar(self, evt):
         key = chr(evt.GetKeyCode())
         if self.flag == "no-alpha" and key in string.letters:
              return
         if self.flag == "no-digit" and key in string.digits:
              return
         evt.Skip()


class DatosVanos(wx.Frame):

    def __init__(self, parent):
        super(DatosVanos, self).__init__(parent, size=(340, 700), style=wx.CLOSE_BOX | wx.CAPTION | wx.SYSTEM_MENU)

        panel = wx.ScrolledWindow(self, -1)

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
        self.datos_l = np.array([[0] * 6] * self.filas, float)
        self.long = []
        l = 100
        i = 0

        # Si tengo voladizo izquierdo...
        if datos_dg[2] == 1:
            j = 30
            self.numvan = wx.StaticText(panel, label=str('Vol. Izq.'), pos=(12, l + 5))
            self.datos_l[i, 0] = 0
            j += 30
            self.luz = wx.TextCtrl(panel, value="", pos=(j, l), size=(80, -1), validator=CharValidator("no-alpha"))
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
                self.luz = wx.TextCtrl(panel, value="", pos=(j, l), size=(80, -1), validator=CharValidator("no-alpha"))
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
                self.luz = wx.TextCtrl(panel, value="", pos=(j, l), size=(80, -1), validator=CharValidator("no-alpha"))
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
                self.luz = wx.TextCtrl(panel, value="", pos=(j, l), size=(80, -1), validator=CharValidator("no-alpha"))
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
                self.luz = wx.TextCtrl(panel, value="", pos=(j, l), size=(80, -1), validator=CharValidator("no-alpha"))
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
        l += 60
        panel.SetScrollbars(1, 1, -1, l)

        self.Center()
        self.Show()

    # Funciones de los botones
    def cancel(self, parent):
        self.Close()

    def onclick_dv(self, parent):
        for n in range(0, self.filas):
            self.datos_l[n, 1] = self.long[n].GetValue()
            self.datos_l[0, 4] = 0
            self.datos_l[0, 5] = float(self.datos_l[0, 1])
        for t in range(1, self.filas):
            self.datos_l[t, 4] = float(self.datos_l[t - 1, 5])
            self.datos_l[t, 5] = float(self.datos_l[t, 4] + self.datos_l[t, 1])

        np.save('datos/datos_l', self.datos_l)
        print self.datos_l
        self.Close()


class DatosSecciones(wx.Frame):
    def __init__(self, parent):
        super(DatosSecciones, self).__init__(parent, size=(700, 500), style=wx.CLOSE_BOX | wx.CAPTION | wx.SYSTEM_MENU)
        self.panel = wx.ScrolledWindow(self, -1)

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
        self.numsecsv = wx.TextCtrl(self.panel, value="", pos=(200, 40), size=(80, -1),
                                    validator=CharValidator("no-alpha"))

        botonok = wx.Button(self.panel, wx.ID_OK, pos=(300, 37))
        botonok.Bind(wx.EVT_BUTTON, self.OnOk, botonok)

    def OnOk(self, event):
        self.nssv = self.numsecsv.GetValue()

        # botonok = None
        # botoncancel = None

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
            self.area = wx.TextCtrl(self.panel, value='', pos=(j + 75, l), size=(80, -1),
                                    validator=CharValidator("no-alpha"))
            self.a.append(self.area)

            self.inercia = wx.TextCtrl(self.panel, value='', pos=(j + 175, l), size=(80, -1),
                                       validator=CharValidator("no-alpha"))
            self.ine.append(self.inercia)

            self.v1 = wx.TextCtrl(self.panel, value='', pos=(j + 275, l), size=(80, -1),
                                  validator=CharValidator("no-alpha"))
            self.vsup.append(self.v1)

            self.v2 = wx.TextCtrl(self.panel, value='', pos=(j + 375, l), size=(80, -1),
                                  validator=CharValidator("no-alpha"))
            self.vinf.append(self.v2)

            self.ancho = wx.TextCtrl(self.panel, value='', pos=(j + 475, l), size=(80, -1),
                                     validator=CharValidator("no-alpha"))
            self.b.append(self.ancho)

            self.almas = wx.TextCtrl(self.panel, value='', pos=(j + 575, l), size=(80, -1),
                                     validator=CharValidator("no-alpha"))
            self.bw.append(self.almas)

            l += 50

        botonok = wx.Button(self.panel, wx.ID_OK, pos=(200, l))
        botonok.Bind(wx.EVT_BUTTON, self.aceptar, botonok)
        botoncancel = wx.Button(self.panel, wx.ID_CANCEL, pos=(500, l))
        botoncancel.Bind(wx.EVT_BUTTON, self.cancel, botoncancel)
        l += 60
        self.panel.SetScrollbars(1, 1, -1, l)

    def aceptar(self, event):
        self.secsv = np.array([[0]*6]*int(self.nssv), float)
        for n in range(int(self.nssv)):

            self.secsv[n, 0] = float(self.a[n].GetValue())
            self.secsv[n, 1] = float(self.ine[n].GetValue())
            self.secsv[n, 2] = float(self.vsup[n].GetValue())
            self.secsv[n, 3] = float(self.vinf[n].GetValue())
            self.secsv[n, 4] = float(self.b[n].GetValue())
            self.secsv[n, 5] = float(self.bw[n].GetValue())

        np.save('datos/secsv', self.secsv)
        print self.secsv
        for i in range(int(self.nssv)):
            for j in range(6):
                print self.secsv[i, j]
        self.Close()

    def cancel(self, event):
        self.Close()


class AsignacionSecciones(wx.Frame):
    def __init__(self, parent):
        super(AsignacionSecciones, self).__init__(parent, size=(400, 500))
        self.panel = wx.ScrolledWindow(self, -1)

        # Lectura de DatosSecciones (Matriz secsv)
        self.secsv = np.load('datos/secsv.npy')
        print self.secsv

        # Lectura de DatosGenerales (Vector datos_dg)
        self.datos_dg = np.load('datos/datos_dg.npy')

        # Lectura de Datosl
        self.datos_l = np.load('datos/datos_l.npy')

        # Asignacion de propiedades mecanicas

        wx.StaticLine(self.panel, -1, (5, 5), (400, 2))
        dv_st = wx.StaticText(self.panel, label="ASIGNAR SECCIONES", pos=(100, 10))
        wx.StaticLine(self.panel, -1, (5, 30), (400, 2))

        dv_st.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD))
        wx.StaticLine(self.panel)
        wx.StaticText(self.panel, label="VANO N:", pos=(10, 45))
        wx.StaticText(self.panel, label="N SECCION", pos=(80, 45))
        wx.StaticText(self.panel, label="SECCION \n RESISTENTE", pos=(165, 45))
        wx.StaticText(self.panel, label="AREA \n [m2]", pos=(270, 45))
        wx.StaticText(self.panel, label="INERCIA \n [m4]", pos=(325, 45))
        wx.StaticLine(self.panel, -1, (5, 85), (400, 2))

        # Bucle para definir la cantidad de filas de la matriz csv (C1)

        self.filas = int(self.datos_dg[0])
        if int(self.datos_dg[2]) == 1:
            self.filas += 1
        if int(self.datos_dg[3]) == 1:
            self.filas += 1
        self.filas *= 10
        self.filas += 1

        self.csv = []
        self.entrada = []
        self.sec1 = [0]*self.filas
        print self.sec1

        l = 100
        # i = 0

        # Si tengo voladizo izquierdo...
        if self.datos_dg[2] == 1:
            finvanos = self.datos_dg[0]*10 + 11
            for t in range(self.filas):
                if t < 10:
                    wx.StaticText(self.panel, label=str('Vol. Izq.'), pos=(12, l))
                    j = 110
                    nsec = wx.StaticText(self.panel, label=str(t+1), pos=(j, l))
                    j += 50
                    self.ent = wx.TextCtrl(self.panel, value='', pos=(j, l - 5), size=(80, -1),
                                           validator=CharValidator("no-alpha"))
                    l += 50
                else:
                    if t >= 10 and t < finvanos:
                        if t % 10 == 0:
                            wx.StaticText(self.panel, label=str('Apoyo'), pos=(12, l))
                        else:
                            wx.StaticText(self.panel, label=str('Vano ' + str(int((t-10)/10 + 2))), pos=(12, l))
                        j = 110
                        nsec = wx.StaticText(self.panel, label=str(t+1), pos=(j, l))
                        j += 50
                        self.ent = wx.TextCtrl(self.panel, value='', pos=(j, l - 5), size=(80, -1),
                                               validator=CharValidator("no-alpha"))
                        l += 50
                    # Si tiene voladizo derecho...
                    else:
                        if self.datos_dg[3] == 1:
                            wx.StaticText(self.panel, label=str('Vol. Der.'), pos=(12, l))
                            j = 110
                            nsec = wx.StaticText(self.panel, label=str(t+1), pos=(j, l))
                            j += 50
                            self.ent = wx.TextCtrl(self.panel, value='', pos=(j, l - 5), size=(80, -1), validator=CharValidator("no-alpha"))
                            l += 50
                self.entrada.append(self.ent)

        else:
            finvanos = self.datos_dg[0]*10 + 1
            for t in range(self.filas):
                if t < finvanos:
                        if t % 10 == 0:
                            wx.StaticText(self.panel, label=str('Apoyo'), pos=(12, l))
                        else:
                            wx.StaticText(self.panel, label=str('Vano ' + str(int((t-10)/10 + 2))), pos=(12, l))
                        j = 110
                        nsec = wx.StaticText(self.panel, label=str(t+1), pos=(j, l))
                        j += 50
                        self.ent = wx.TextCtrl(self.panel, value='', pos=(j, l - 5), size=(80, -1), validator=CharValidator("no-alpha"))
                        l += 50
                # Si tiene voladizo derecho...
                else:
                    if self.datos_dg[3] == 1:
                        wx.StaticText(self.panel, label=str('Vol. Der.'), pos=(12, l))
                        j = 110
                        nsec = wx.StaticText(self.panel, label=str(t+1), pos=(j, l))
                        j += 50
                        self.ent = wx.TextCtrl(self.panel, value='', pos=(j, l - 5), size=(80, -1),
                                               validator=CharValidator("no-alpha"))
                        l += 50
                self.entrada.append(self.ent)

        # Botones
        wx.StaticLine(self.panel, -1, (5, l), (400, 2))

        botonook = wx.Button(self.panel, label='Cargar', pos=(70, l + 15))
        botonook.Bind(wx.EVT_BUTTON, self.onclick_as, botonook)
        botoncancel = wx.Button(self.panel, wx.ID_CANCEL, pos=(180, l + 15))
        botoncancel.Bind(wx.EVT_BUTTON, self.cancel, botoncancel)
        wx.StaticLine(self.panel, -1, (5, l + 50), (325, 2))
        l += 60
        self.panel.SetScrollbars(1, 1, -1, l)
        self.Center()
        self.Show()

    # Funciones de los botones
    def cancel(self, parent):
        self.Close()

    def onclick_as(self, parent):
        self.csv = []
        for n in range(self.filas):
            self.sec1[n] = int(self.entrada[n].GetValue())
        print self.sec1
        np.save('datos/datos_sec1', self.sec1)

        for t in range(self.filas):
            h = int(self.sec1[t])
            self.csv.append(self.secsv[h-1])

        np.save('datos/datos_csv', self.csv)
        self.csv1 = np.load('datos/datos_csv.npy')

        l = 100
        for i in range(self.filas):
            wx.StaticText(self.panel, label=str(self.csv1[i, 0]), pos=(280, l))
            wx.StaticText(self.panel, label=str(self.csv1[i, 1]), pos=(335, l))
            l += 50

        print self.csv1
        print ''


class EstructurasParciales(wx.Frame):
    def __init__(self, parent):
        super(EstructurasParciales, self).__init__(parent, size=(750, 1000), style=wx.CLOSE_BOX | wx.CAPTION | wx.SYSTEM_MENU)
        self.panel = wx.Panel(self, -1)

        # Lectura de Datos de Matrices

        # Matriz de Datos Generales
        self.datos_dg = np.load('datos/datos_dg.npy')

        # Matriz de Datos Vanos
        self.datos_l = np.load('datos/datos_l.npy')

        # Matriz de Datos Seccionales Solo Viga
        self.csv1 = np.load('datos/datos_csv.npy')

        # Matriz de Datos Seccionales Viga + Losa
        # self.csv2 = np.load('datos/datos_cvl.npy')

        # Datos Estructuras Parciales

        wx.StaticLine(self.panel, -1, (5, 5), (750, 2))
        dv_st = wx.StaticText(self.panel, label="DATOS ESTRUCTURAS PARCIALES", pos=(250, 10))
        wx.StaticLine(self.panel, -1, (5, 30), (750, 2))
        dv_st.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD))
        wx.StaticLine(self.panel)
        wx.StaticText(self.panel, label='NOMBRE', pos=(15, 80))
        wx.StaticText(self.panel, label='  SECCION\nRESISTENTE', pos=(105, 80))
        wx.StaticText(self.panel, label='Seccion\n Inicial', pos=(215, 80))
        wx.StaticText(self.panel, label='Seccion\n  Final', pos=(315, 80))
        wx.StaticText(self.panel, label='Numero de\n   apoyos', pos=(405, 80))
        # wx.StaticText(self.panel, label='', pos=(515, 80))

        # Pide los datos de las secciones tipo

        wx.StaticText(self.panel, label='Numero de Estructuras a Ingresar: ', pos=(10, 45))
        self.numestpar = wx.TextCtrl(self.panel, value="", pos=(200, 40), size=(80, -1))

        botonok = wx.Button(self.panel, wx.ID_OK, pos=(300, 37))
        botonok.Bind(wx.EVT_BUTTON, self.OnOk, botonok)

    def OnOk(self, event):
        self.nep = self.numestpar.GetValue()

        self.l = 120
        j = 15
        self.name = []
        self.sec = []
        self.si = []
        self.sf = []
        self.n3 = []

        for i in range(int(self.nep)):

            n = wx.StaticText(self.panel, label=('Estr' + str(i + 1)), pos=(j, self.l + 5))

            # n = wx.TextCtrl(self.panel, value='', pos=(j + 75, self.l), size=(80, -1))
            self.name.append(n)

            sr = wx.TextCtrl(self.panel, value='', pos=(j + 80, self.l), size=(80, -1))
            self.sec.append(sr)

            secin = wx.TextCtrl(self.panel, value='', pos=(j + 180, self.l), size=(80, -1))
            self.si.append(secin)

            secfin = wx.TextCtrl(self.panel, value='', pos=(j + 280, self.l), size=(80, -1))
            self.sf.append(secfin)

            nap = wx.TextCtrl(self.panel, value='', pos=(j + 380, self.l), size=(80, -1))
            self.n3.append(nap)

            self.l += 50

        botonok = wx.Button(self.panel, wx.ID_OK, pos=(200, self.l))
        botonok.Bind(wx.EVT_BUTTON, self.aceptar, botonok)
        botoncancel = wx.Button(self.panel, wx.ID_CANCEL, pos=(500, self.l))
        botoncancel.Bind(wx.EVT_BUTTON, self.cancel, botoncancel)

    def aceptar(self, event):

        self.datep = np.array([[0]*4]*int(self.nep))

        for n in range(int(self.nep)):
            self.datep[n, 0] = self.sec[n].GetValue()
            self.datep[n, 1] = self.si[n].GetValue()
            self.datep[n, 2] = self.sf[n].GetValue()
            self.datep[n, 3] = self.n3[n].GetValue()
        print self.datep

        np.save('datos/datos_datep', self.datep)

        self.l += 50

        self.s = np.array()

        for q in range(int(self.nep)):

            wx.StaticText(self.panel, label='Num', pos=(15, self.l))
            wx.StaticText(self.panel, label='Altura Soporte\n    Superior', pos=(105, self.l))
            wx.StaticText(self.panel, label='Inercia Soporte\n    Superior', pos=(215, self.l))
            wx.StaticText(self.panel, label='Altura Soporte\n    Inferior', pos=(315, self.l))
            wx.StaticText(self.panel, label='Inercia Soporte\n    Inferior', pos=(405, self.l))

            self.l += 50

            for r in range(int(self.datep[q, 3])):

                s0 = wx.TextCtrl(self.panel, value='', pos=(j + 80, self.l), size=(80, -1))
                self.sec.append(sr)

                s1 = wx.TextCtrl(self.panel, value='', pos=(j + 180, self.l), size=(80, -1))
                self.si.append(secin)

                s2 = wx.TextCtrl(self.panel, value='', pos=(j + 280, self.l), size=(80, -1))
                self.sf.append(secfin)

                s3 = wx.TextCtrl(self.panel, value='', pos=(j + 380, self.l), size=(80, -1))
                self.n3.append(nap)

                s4 = wx.TextCtrl(self.panel, value='', pos=(j + 380, self.l), size=(80, -1))
                self.n3.append(nap)

                s5 = wx.TextCtrl(self.panel, value='', pos=(j + 380, self.l), size=(80, -1))
                self.n3.append(nap)

                self.l += 50



        N3 = 2
        print 'N3= ', N3

        S = np.array([[1, 2, 3, 4, 5, 6],[7, 8, 9, 10, 11, 12]])
        print 'S= ', S

        T = np.array([[0]*4]*N3)
        print 'T= ', T

        c1 = [[1.5, 1.25, 0.6, 0.6, 2.4, 0.6]]
        print 'C1= ', c1

        E0 = 10

        for i in range(N3):
            j3 = S[i, 5]
            j4 = S[i+1, 5]
            x1 = 0
            T[i, 1] = 0
            T[i, 2] = 0
            T[i, 3] = 0
            T[i, 4] = 0

            for j in range(j3, j4):
                x1 = c1[7, j] - c1[7, j3]
                x2 = c1[7, j+1] - c1[7, j3]
                x0 = x2 - x1
                v1 = p[i] - x1
                v2 = p[i] - x2
                epp = E0 * p[i] * p[i]

                T[i, 1] = T[i, 1] + 0.5 * (v1 * v1 / c1[2,j] + v2 * v2 / c1[2, j+1])*x0/epp
                T[i, 2] = T[i, 2] + 0.5 * (x1 * v1 / c1[2,j] + x2 * v2 / c1[2, j+1])*x0/epp
                T[i, 3] = T[i, 2]
                T[i, 4] = T[i, 4] + 0.5 * (x1 * x1 / c1[2,j] + x2 * x2 / c1[2, j+1])*x0/epp

            ko = T[i, 1] * T[i, 4] - T[i, 2] * T[i, 3]
            k[i, 1] = T[i, 4] / k0
            k[i, 2] = T[i, 2] / k0
            k[i, 3] = T[i, 3] / k0
            k[i, 4] = T[i, 1] / k0
        print k

        # for i in range(0, N3):
        #
        #     for j in range(0, N3):
        #
        #         if j != i:
        #
        #             if abs(i - j) >= 2:
        #                 R[i, j] = 0
        #
        #             else:
        # 		if j >= i:
        #                 	R[i, j] = k[i, 2]
        # 		else:
        # 			R[i, j] = k[i-1, 3]
        #
        # 	elif i == 1:
        #
        # 		A = k[i, 1]
        #                 B = 0
        #                 R[i, j] = A + B + 4 * E0 * (S[i, 3] / S[i, 2] + S[i, 5] / S[i, 4])
        #
        # 	elif i == N3:
        #
        #                 A = 0
        #                 B = k[i-1, 4]
        #                 R[i, j] = A + B + 4 * E0 * (S[i, 3] / S[i, 2] + S[i, 5] / S[i, 4])









        self.Close()

    def cancel(self, event):
        self.Close()

app = wx.App()
frame = MainWindow(None, "PCCB Version 2.0 2015")
app.MainLoop()
