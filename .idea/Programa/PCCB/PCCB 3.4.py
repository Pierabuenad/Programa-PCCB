# Importamos las librerias a ser utilizadas
import os
# Importamos wx.python
import wx
# Importamos numpy la renombramos np
import numpy as np
# Importamos string para la validacion
import string
# Importamos matplolib
import matplotlib.pyplot as plt

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
        self.Bind(wx.EVT_MENU, self.click_imprimir, dg_tool)
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
        m_dp = wx.MenuItem(datosmenu, -1, 'Pretensado', 'Ingrese datos de Pretensado')

        # Contenido de datos secciones
        sb_ds.Append(15, 'Datos solo &viga')
        sb_ds.Append(16, 'Datos viga + losa')

        # Menu Datos
        datosmenu.AppendItem(m_dg)
        datosmenu.AppendItem(m_dv)
        datosmenu.AppendMenu(-1, 'Datos &Secciones', sb_ds)
        datosmenu.AppendItem(m_as)
        datosmenu.AppendItem(m_ep)
        datosmenu.AppendItem(m_dp)

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
        # Abre la ventana de Datos de Pretensado
        self.Bind(wx.EVT_MENU, self.click_dp, m_dp)
        # Sale del programa
        self.Bind(wx.EVT_MENU, self.exit, m_e)
        # Abre el mensaje "Acerca de..."
        self.Bind(wx.EVT_MENU, self.about, m_ab)

        self.SetMenuBar(menubar)
        self.Centre()
        self.Show(True)

    # Imprimir matrices
    def click_imprimir(self, event):
        Imprimir(self).Show()

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

    # Abrir ventana de Datos Pretensado
    def click_dp(self, event):
        DatosPretensado(self).Show()

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

        # Definicion de datos.dg como un vector vacio

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
        self.secsv = np.array([[0]*7]*int(self.nssv), float)
        for n in range(int(self.nssv)):

            self.secsv[n, 0] = float(self.a[n].GetValue())
            self.secsv[n, 1] = float(self.ine[n].GetValue())
            self.secsv[n, 2] = float(self.vsup[n].GetValue())
            self.secsv[n, 3] = float(self.vinf[n].GetValue())
            self.secsv[n, 4] = float(self.b[n].GetValue())
            self.secsv[n, 5] = float(self.bw[n].GetValue())
            self.secsv[n, 6] = float(0)

        np.save('datos/datos_secsv', self.secsv)

        self.Close()

    def cancel(self, event):
        self.Close()


class AsignacionSecciones(wx.Frame):

    def __init__(self, parent):
        super(AsignacionSecciones, self).__init__(parent, size=(1250, 700), style=wx.CLOSE_BOX | wx.CAPTION | wx.SYSTEM_MENU)
        self.panel = wx.ScrolledWindow(self, -1)

        # Lectura de DatosSecciones (Matriz secsv)
        self.secsv = np.load('datos/datos_secsv.npy')

        # Lectura de DatosGenerales (Vector datos_dg)
        self.datos_dg = np.load('datos/datos_dg.npy')

        # Lectura de Datosl
        self.datos_l = np.load('datos/datos_l.npy')

        # Asignacion de propiedades mecanicas
        wx.StaticLine(self.panel, -1, (5, 5), (1250, 2))
        as_st = wx.StaticText(self.panel, label="ASIGNAR SECCIONES", pos=(500, 10))
        as_st.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD))
        wx.StaticLine(self.panel, -1, (5, 30), (1250, 2))

        # Determinacion de filas para las Matrices
        self.filas = int(self.datos_dg[0])
        if int(self.datos_dg[2]) == 1:
            self.filas += 1
        if int(self.datos_dg[3]) == 1:
            self.filas += 1

        self.l = 40

        # self.csv = []
        self.entrada = []
        # self.sec1 = [0]*(self.filas*10+1)

        l = 40
        n = 11
        a = 1
        for o in range(self.filas):
            m = 115
            a -= 1
            for h in range(11):
                wx.StaticText(self.panel, label='SECCION \n      '+str(a+1), pos=(m, l))
                m += 100
                n += 10
                a += 1
            l += 85

        for q in range(self.filas):
            wx.StaticText(self.panel, label='VANO N:', pos=(15, self.l))

            j = 100

            self.ll = self.l + 35
            self.l += 35
            if self.datos_dg[2] == 1:
                if self.datos_dg[3] == 1:
                    if q == 0:
                        wx.StaticText(self.panel, label='V. Izquierdo', pos=(15, self.l+5))
                        self.l += 50
                    elif q+1 == self.filas:
                        wx.StaticText(self.panel, label='V. Derecho', pos=(15, self.l+5))
                        self.l += 50
                    else:
                        wx.StaticText(self.panel, label='      '+str(q), pos=(15, self.l+5))
                        self.l += 50
                else:
                    if q == 0:
                        wx.StaticText(self.panel, label='V. Izquierdo', pos=(15, self.l+5))
                        self.l += 50
                    else:
                        wx.StaticText(self.panel, label='      '+str(q), pos=(15, self.l+5))
                        self.l += 50
            elif self.datos_dg[2] == 0:
                if self.datos_dg[3] == 1:
                    if q+1 == self.filas:
                        wx.StaticText(self.panel, label='V. Derecho', pos=(15, self.l+5))
                        self.l += 50
                    else:
                        wx.StaticText(self.panel, label='      '+str(q+1), pos=(15, self.l+5))
                        self.l += 50
                else:
                    wx.StaticText(self.panel, label='      '+str(q+1), pos=(15, self.l+5))
                    self.l += 50

            for k in range(11):

                if q > 0 and k == 0:
                    wx.StaticText(self.panel, label= '', pos=(j, self.ll))
                else:
                    self.ent = wx.TextCtrl(self.panel, value='', pos=(j, self.ll), size=(80, -1))
                    self.entrada.append(self.ent)
                j += 100

        botonok = wx.Button(self.panel, wx.ID_OK, pos=(400, self.l))
        botonok.Bind(wx.EVT_BUTTON, self.onclick_as, botonok) #revisar
        botoncancel = wx.Button(self.panel, wx.ID_CANCEL, pos=(700, self.l))
        botoncancel.Bind(wx.EVT_BUTTON, self.cancel, botoncancel)
        self.l += 50

        self.panel.SetScrollbars(1, 1, -1, self.l)

    def cancel(self, parent):
        self.Close()

    def onclick_as(self, parent):

        self.csv = []
        self.sec1 = [0]*(self.filas*10+1)

        lv = []
        alfa = [0]*self.filas

        self.datos_l = np.transpose(self.datos_l)
        long = self.datos_l[1]

        for q in range(self.filas):
            for r in range(11):
                if not(r == 0 and q != 0):

                    ns = float(q*10 + r + 1)
                    for k in range(self.filas):
                        alfa[k] = round(max(0, min((ns - 1.0)/10-int(k), 1.0)),2)
                    l = round(np.dot(alfa, long), 4)
                    lv.append(l)

        for n in range(self.filas*10+1):
            self.sec1[n] = int(self.entrada[n].GetValue())

        np.save('datos/datos_sec1', self.sec1)

        for t in range(self.filas*10+1):
            h = int(self.sec1[t])
            self.csv.append(self.secsv[h-1])

        np.save('datos/datos_csv', self.csv)
        self.csv1 = np.load('datos/datos_csv.npy')

        for t in range(self.filas*10+1):
            self.csv1[t, 6] = lv[t]

        np.save('datos/datos_csv', self.csv1)

        self.Close()


class EstructurasParciales(wx.Frame):

    def __init__(self, parent):
        super(EstructurasParciales, self).__init__(parent, size=(750, 700), style=wx.CLOSE_BOX | wx.CAPTION | wx.SYSTEM_MENU)
        self.panel = wx.ScrolledWindow(self, -1)

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

        self.panel.SetScrollbars(1, 1, -1, 700)

    def OnOk(self, event):
        self.nep = self.numestpar.GetValue()

        self.panel.SetScrollbars(1, 1, -1, 175 + int(self.nep)*50)

        self.l = 120
        j = 15
        self.name = []
        self.sec = []
        self.si = []
        self.sf = []
        self.n3 = []

        for i in range(int(self.nep)):

            n = wx.StaticText(self.panel, label=('Estr' + str(i + 1)), pos=(j, self.l + 5))
            self.name.append(n)
            # ingreso seccion resistente
            sr = wx.RadioButton(self.panel, -1, "Solo viga", style=wx.RB_GROUP, pos=(j+80, self.l))
            wx.RadioButton(self.panel, -1, "Viga + Losa", pos=(j+80, self.l+20))
            self.sec.append(sr)
            # ingreso seccion inicial
            secin = wx.TextCtrl(self.panel, value='', pos=(j + 180, self.l), size=(80, -1))
            self.si.append(secin)
            #ingreso seccion final
            secfin = wx.TextCtrl(self.panel, value='', pos=(j + 280, self.l), size=(80, -1))
            self.sf.append(secfin)
            #ingreso Numero de Apoyo
            nap = wx.TextCtrl(self.panel, value='', pos=(j + 380, self.l), size=(80, -1))
            self.n3.append(nap)

            self.l += 50

        # botones
        botonok = wx.Button(self.panel, wx.ID_OK, pos=(200, self.l))
        botonok.Bind(wx.EVT_BUTTON, self.aceptar, botonok)
        botoncancel = wx.Button(self.panel, wx.ID_CANCEL, pos=(500, self.l))
        botoncancel.Bind(wx.EVT_BUTTON, self.cancel, botoncancel)

    def aceptar(self, event):

        self.nep = self.numestpar.GetValue()
        self.datep = np.array([[0]*6]*int(self.nep), float)

        for n in range(int(self.nep)):
            self.datep[n, 0] = self.sec[n].GetValue()
            self.datep[n, 1] = self.si[n].GetValue()
            self.datep[n, 2] = self.sf[n].GetValue()
            self.datep[n, 3] = self.n3[n].GetValue()
            self.datep[n, 4] = 0.0                  # Aca voy a guardar W1 (voladizo izquierdo)
            self.datep[n, 5] = 0.0                  # Aca voy a guardar W2 (voladizo derecho)

        np.save('datos/datos_datep', self.datep)

        p = 0
        for k in range(int(self.nep)):
            p += self.datep[k, 3]

        self.panel.SetScrollbars(1, 1, -1, 175 + int(self.nep)*50 + int(p)*50)

        self.l += 30

        self.ss0 = []
        self.ss1 = []
        self.ss2 = []
        self.ss3 = []
        self.ss4 = []

        for q in range(int(self.nep)):

            wx.StaticText(self.panel, label='Num', pos=(15, self.l))
            wx.StaticText(self.panel, label='Altura Soporte\n    Superior', pos=(100, self.l))
            wx.StaticText(self.panel, label='Inercia Soporte\n    Superior', pos=(200, self.l))
            wx.StaticText(self.panel, label='Altura Soporte\n    Inferior', pos=(300, self.l))
            wx.StaticText(self.panel, label='Inercia Soporte\n    Inferior', pos=(400, self.l))
            wx.StaticText(self.panel, label='   Seccion\n    Apoyo', pos=(505, self.l))

            self.l += 50

            j = 15
            for r in range(int(self.datep[q, 3])):

                #Numero
                wx.StaticText(self.panel, label=str(r+1), pos=(25, self.l+5))
                # Alt. Soporte Superior
                s0 = wx.TextCtrl(self.panel, value='', pos=(j + 80, self.l), size=(80, -1))
                self.ss0.append(s0)
                # Inercia Soporte Superior
                s1 = wx.TextCtrl(self.panel, value='', pos=(j + 180, self.l), size=(80, -1))
                self.ss1.append(s1)
                # Alt. Soporte Inferior
                s2 = wx.TextCtrl(self.panel, value='', pos=(j + 280, self.l), size=(80, -1))
                self.ss2.append(s2)
                # Inercia Soporte Inferior
                s3 = wx.TextCtrl(self.panel, value='', pos=(j + 380, self.l), size=(80, -1))
                self.ss3.append(s3)
                # Seccion apoyo
                s4 = wx.TextCtrl(self.panel, value='', pos=(j + 480, self.l), size=(80, -1))
                self.ss4.append(s4)

                self.l += 50

        botonok = wx.Button(self.panel, wx.ID_OK, pos=(200, self.l))
        botonok.Bind(wx.EVT_BUTTON, self.guardar, botonok)
        botoncancel = wx.Button(self.panel, wx.ID_CANCEL, pos=(500, self.l))
        botoncancel.Bind(wx.EVT_BUTTON, self.cancel, botoncancel)
        self.l +=50
        self.panel.SetScrollbars(1, 1, -1, self.l)

    def guardar(self, event):

        self.SS = []
        self.KK = []
        self.RR = []

        for m in range(int(self.nep)):
            s = np.array([[0]*5]*int(self.datep[m, 3]), float)

            for k in range(int(self.datep[m, 3])):
                s[k,0] = self.ss0[k].GetValue()
                s[k,1] = self.ss1[k].GetValue()
                s[k,2] = self.ss2[k].GetValue()
                s[k,3] = self.ss3[k].GetValue()
                s[k,4] = self.ss4[k].GetValue()

            self.SS.append(s)

            self.ss0 = self.ss0[int(self.datep[m,3]):]
            self.ss1 = self.ss1[int(self.datep[m,3]):]
            self.ss2 = self.ss2[int(self.datep[m,3]):]
            self.ss3 = self.ss3[int(self.datep[m,3]):]
            self.ss4 = self.ss4[int(self.datep[m,3]):]

        np.save('datos/datos_SS', self.SS)

        E0 = float(self.datos_dg[1])

        # Entramos al bucle una vez por cada estructura parcial
        for q in range(int(self.nep)):

            # Definimos la cantidad de apoyos de cada EP
            N3 = int(self.datep[q, 3])

            # Definimos la Matriz de Flex para cada EP y su precision
            T = np.array([[0]*4]*(N3-1), np.float64)

            # Definimos la Matriz de Rig para cada EP y su precision
            K = np.array([[0]*4]*(N3-1), np.float64)

            # Leemos de la Mat 3D SS, la Mat S correspondiente
            S = self.SS[q]

            # Calcula las longitudes de los voladizos izquierdo y derecho de cada estructura parcial
            self.datep[q, 4] = float(self.csv1[int(S[0, 4])-1, 6]) - float(self.csv1[int(self.datep[q, 1])-1, 6])
            self.datep[q, 5] = float(self.csv1[int(self.datep[q, 2])-1, 6]) - float(self.csv1[int(S[N3-1, 4])-1, 6])

            print 'Esta matriz es datep:\n', self.datep

            # Entramos al bucle una vez por cada apoyo de la EP
            for i in range(N3-1):

                j3 = int(S[i, 4])           # es la seccion inicial de la EP
                j4 = int(S[i+1, 4])         # es la seccion final de la EP

                p = [0]*(N3-1)
                p[i] = self.csv1[j4-1, 6] - self.csv1[j3-1, 6]      # es la longitud entre j3 y j4

                epp = E0 * p[i] * p[i]                              # Esto es E0*pi*pi

                # Con este bucle recorremos el tramo entre j3 y j4 para obtener la flexibilidad total
                for j in range(j3-1, j4-1):
                    x1 = self.csv1[j, 6] - self.csv1[j3-1, 6]
                    x2 = self.csv1[j+1, 6] - self.csv1[j3-1, 6]
                    x0 = x2 - x1

                    v1 = p[i] - x1
                    v2 = p[i] - x2

                    T[i, 0] = T[i, 0] + 0.5 * (v1 * v1 / self.csv1[j, 1] + v2 * v2 / self.csv1[j+1, 1])*x0/epp
                    T[i, 1] = T[i, 1] + 0.5 * (x1 * v1 / self.csv1[j, 1] + x2 * v2 / self.csv1[j+1, 1])*x0/epp
                    T[i, 2] = T[i, 1]
                    T[i, 3] = T[i, 3] + 0.5 * (x1 * x1 / self.csv1[j, 1] + x2 * x2 / self.csv1[j+1, 1])*x0/epp

                k0 = T[i, 0] * T[i, 3] - T[i, 1] * T[i, 2]          # Determinante, se usa para la inversion

                K[i, 0] = T[i, 3] / k0
                K[i, 1] = T[i, 1] / k0
                K[i, 2] = T[i, 2] / k0
                K[i, 3] = T[i, 0] / k0

            self.KK.append(K)

            # Definimos la Matriz R para cada EP y su precision
            R = np.array([[0]*N3]*(N3), np.float64)

            for i in range(N3):
                for j in range(N3):
                    if j != i:
                        if abs(i - j) >= 2:             # Rama VI
                            R[i, j] = 0
                        elif j >= i:                    # Rama V
                            R[i, j] = K[i, 1]
                        else:                           # Rama IV
                            R[i, j] = K[i-1, 2]

                    elif i == 0:                        # Rama III
                        A = K[i, 0]
                        B = 0
                        R[i, j] = A + B + 4 * E0 * (S[i, 1] / S[i, 0] + S[i, 3] / S[i, 2])

                    elif i == N3-1:                     # Rama II
                        A = 0
                        B = K[i-1, 3]
                        R[i, j] = A + B + 4 * E0 * (S[i, 1] / S[i, 0] + S[i, 3] / S[i, 2])

                    else:                               # Rama I
                        A = K[i, 0]
                        B = K[i-1, 3]
                        R[i, j] = A + B + 4 * E0 * (S[i, 1] / S[i, 0] + S[i, 3] / S[i, 2])

            # inversion de matriz

            R = np.linalg.inv(R)
            self.RR.append(R)

        np.save('datos/datos_datep', self.datep)
        np.save('datos/datos_RR', self.RR)
        self.Close()

    def cancel(self, event):
        self.Close()


class DatosPretensado(wx.Frame):

    def __init__(self, parent):
        super(DatosPretensado, self).__init__(parent, size=(500, 520))

        self.panel = wx.ScrolledWindow(self, -1)

        # Importacion de Matrices Necesarias en esta class

        # Importacion de Datos Generales datos_dg
        self.datos_dg = np.load('datos/datos_dg.npy')

        # Importacion de Datos Vanos datos_l
        self.datos_l = np.load('datos/datos_l.npy')

        # Importacion de Datos de Secciones csv
        self.csv1 = np.load('datos/datos_csv.npy')
        print 'Esto es csv1: ', self.csv1

        # Importacion de Datos Estructuras Parciales datos_datep
        self.datep = np.load('datos/datos_datep.npy')

        # Importacion de Matriz SS
        self.SS = np.load('datos/datos_SS.npy')
        # print 'Esto es SS: ', self.SS

        # Datos Generales del Pretensado

        # Creo un vector vacio para guardar los datos generales del pretensado
        self.datos_dgp = np.array([0]*6, np.float)
        self.auxiliar = []

        # Escritura de etiquetas y TextControl para tomar datos generales de pretensado

        wx.StaticLine(self.panel, -1, (5, 5), (500, 2))
        dv_st = wx.StaticText(self.panel, label="PRETENSADO", pos=(200, 10))
        dv_st.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD))
        wx.StaticLine(self.panel, -1, (5, 30), (500, 2))

        dv_st = wx.StaticText(self.panel, label="Datos Generales", pos=(10, 45))
        dv_st.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD))
        wx.StaticLine(self.panel, -1, (5, 70), (500, 2))

        wx.StaticText(self.panel, label="Coeficiente de Creep", pos=(10, 85))
        wx.StaticText(self.panel, label="- [1]", pos=(230, 85))
        fyp = wx.TextCtrl(self.panel, value="2.4", pos=(300, 80), size=(80, -1), validator=CharValidator("no-alpha"))
        self.auxiliar.append(fyp)

        wx.StaticText(self.panel, label="Epsilon de Retraccion", pos=(10, 120))
        wx.StaticText(self.panel, label="- [1]", pos=(230, 120))
        er = wx.TextCtrl(self.panel, value="0.00024", pos=(300, 115), size=(80, -1), validator=CharValidator("no-alpha"))
        self.auxiliar.append(er)

        wx.StaticText(self.panel, label="Tension de Rotura Armadura Activa", pos=(10, 155))
        wx.StaticText(self.panel, label="- [kg/mm2]", pos=(230, 155))
        fua = wx.TextCtrl(self.panel, value="190.0", pos=(300, 150), size=(80, -1), validator=CharValidator("no-alpha"))
        self.auxiliar.append(fua)

        wx.StaticText(self.panel, label="Tension de Fluencia Armadura Activa", pos=(10, 190))
        wx.StaticText(self.panel, label="- [kg/mm2]", pos=(230, 190))
        fya = wx.TextCtrl(self.panel, value="170.0", pos=(300, 185), size=(80, -1), validator=CharValidator("no-alpha"))
        self.auxiliar.append(fya)

        wx.StaticText(self.panel, label="Modulo de Elasticidad Armadura Activa", pos=(10, 225))
        wx.StaticText(self.panel, label="- [kg/mm2]", pos=(230, 225))
        ea = wx.TextCtrl(self.panel, value="19000", pos=(300, 220), size=(80, -1), validator=CharValidator("no-alpha"))
        self.auxiliar.append(ea)

        wx.StaticText(self.panel, label="Relajacion", pos=(10, 260))
        wx.StaticText(self.panel, label="- [1]", pos=(230, 260))
        rel = wx.TextCtrl(self.panel, value="0.02", pos=(300, 255), size=(80, -1), validator=CharValidator("no-alpha"))
        self.auxiliar.append(rel)

        wx.StaticLine(self.panel, -1, (5, 285), (500, 2))

        self.l = 285

        # self.fam es un vector que guarda la cantidad de familias a trazar por cada EP
        self.fam = np.array([0]*int(len(self.datep)))

        # self.aux2 es una lista para guardar los datos del TextControl hasta que lee los datos ingresados
        self.aux2 = []

        for i in range(len(self.datep)):
            wx.StaticText(self.panel, label='Numero de Familias en Estructura Parcial ' + str(i+1), pos=(15, self.l+20))
            aux = wx.TextCtrl(self.panel, value='2', pos=(300, self.l+15), size=(80, -1))
            self.aux2.append(aux)
            self.l += 30

        # Botones

        botonook = wx.Button(self.panel, wx.ID_OK, pos=(100, self.l+15))
        botonook.Bind(wx.EVT_BUTTON, self.onclick_dp, botonook)
        botoncancel = wx.Button(self.panel, wx.ID_CANCEL, pos=(250, self.l+15))
        botoncancel.Bind(wx.EVT_BUTTON, self.cancel, botoncancel)
        wx.StaticLine(self.panel, -1, (5, self.l+45), (500, 2))

        self.panel.SetScrollbars(1, 1, -1, 100 + int(len(self.datep))*30)

        self.Center()
        self.Show()

    def cancel(self, event):
        self.Close()

    def onclick_dp(self, event):

        # En este bucle leemos los datos ingresados y los guardamos en datos_dgp
        for n in range(6):
            self.datos_dgp[n] = self.auxiliar[n].GetValue()
        # print 'Estos son los datos generales de pretensado\n', self.datos_dgp
        # print 'Coeficiente de Creep: ', self.datos_dgp[0]
        # print 'Epsilon de Retraccion: ', self.datos_dgp[1]
        # print 'Tension de Rotura: ', self.datos_dgp[2]
        # print 'Tension de Fluencia: ', self.datos_dgp[3]
        # print 'Modulo de Elasticidad: ', self.datos_dgp[4]
        # print 'Relajacion: ', self.datos_dgp[5]
        np.save('datos/datos_dgp', self.datos_dgp)

        # En este bucle leemos la cantidad de familias en cada EP y lo guardamos en self.fam
        for m in range(int(len(self.datep))):
            self.fam[m] = self.aux2[m].GetValue()

        self.l += 50
        print 'Esto vale self.l antes de cargar los datos de las familias', self.l

        self.ord = self.l
        print 'Coordenada ord= ', self.ord
        wx.StaticText(self.panel, label='ACA SE SUPONE QUE TIENEN QUE QUEDAR LAS GRILLAS', pos=(350, self.ord))

        # Listas auxiliares para lectura de datos de pretensado de cada familia
        self.auxt1 = []
        self.auxt2 = []
        self.auxt3 = []
        self.auxt4 = []
        self.auxt5 = []
        self.auxt6 = []
        self.auxt7 = []
        self.auxt8 = []
        self.auxt9 = []
        self.auxt10 = []
        self.auxt11 = []
        self.auxt12 = []
        # self.auxt13 = []

        # Variables Auxiliares para el trazado de cada familia
        self.trapre_ip = []
        self.trapre_x0 = []
        self.trapre_x1 = []
        self.trapre_x2 = []
        self.trapre_x3 = []
        self.trapre_x4 = []
        self.trapre_x5 = []
        self.trapre_x6 = []
        self.trapre_v1 = []
        self.trapre_v2 = []
        self.trapre_v3 = []
        self.trapre_v4 = []

        # Entra a este bucle una vez por cada Estructura Parcial
        for q in range(int(len(self.datep))):

            st = wx.StaticText(self.panel, label='Trazado de pretensado Estructura Parcial ' + str(q+1), pos=(15, self.l))
            st.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD))

            N3 = self.datep[q, 3]
            print 'N3= ', N3

            S = self.SS[q]
            print 'S= ', S

            nfam = self.fam[q]
            print '----------\nEstructura Parcial ', q+1, '\n Numero de familias: ', nfam, '\n----------'

            # Entra una vez por cada familia
            for i in range(nfam):

                wx.StaticText(self.panel, label='Familia ' + str(i+1), pos=(15, self.l+30))
                # st.SetFont(wx.Font(9, wx.SWISS, wx.NORMAL))

                wx.StaticText(self.panel, label='Seccion Inicial', pos=(15, self.l+60))
                aux1 = wx.TextCtrl(self.panel, value='1', pos=(185, self.l+55), size=(80, -1))
                self.auxt1.append(aux1)

                wx.StaticText(self.panel, label='Anclaje Inicial', pos=(15, self.l+90))
                aux2 = wx.RadioButton(self.panel, -1, "Activo", style=wx.RB_GROUP, pos=(175, self.l+90))
                wx.RadioButton(self.panel, -1, "Pasivo", pos=(250, self.l+90))
                self.auxt2.append(aux2)

                wx.StaticText(self.panel, label='Seccion Final', pos=(15, self.l+120))
                aux3 = wx.TextCtrl(self.panel, value='11', pos=(185, self.l+115), size=(80, -1))
                self.auxt3.append(aux3)

                wx.StaticText(self.panel, label='Anclaje Final', pos=(15, self.l+150))
                aux4 = wx.RadioButton(self.panel, -1, "Activo", style=wx.RB_GROUP, pos=(175, self.l+150))
                wx.RadioButton(self.panel, -1, "Pasivo", pos=(250, self.l+150))
                self.auxt4.append(aux4)

                wx.StaticText(self.panel, label='Tension de Tesado [kg/mm2]', pos=(15, self.l+180))
                aux5 = wx.TextCtrl(self.panel, value='100.0', pos=(185, self.l+175), size=(80, -1))
                self.auxt5.append(aux5)

                wx.StaticText(self.panel, label='Tension de Clavado [kg/mm2]', pos=(15, self.l+210))
                aux6 = wx.TextCtrl(self.panel, value='100.0', pos=(185, self.l+205), size=(80, -1))
                self.auxt6.append(aux6)

                wx.StaticText(self.panel, label='Coeficiente de Friccion', pos=(15, self.l+240))
                aux7 = wx.TextCtrl(self.panel, value='0.23', pos=(185, self.l+235), size=(80, -1))
                self.auxt7.append(aux7)

                wx.StaticText(self.panel, label='Beta', pos=(15, self.l+270))
                aux8 = wx.TextCtrl(self.panel, value='0.0008', pos=(185, self.l+265), size=(80, -1))
                self.auxt8.append(aux8)

                wx.StaticText(self.panel, label='Penetracion Cunas [mm]', pos=(15, self.l+300))
                aux9 = wx.TextCtrl(self.panel, value='7.0', pos=(185, self.l+295), size=(80, -1))
                self.auxt9.append(aux9)

                wx.StaticText(self.panel, label='Area Acero Pretensado [mm2]', pos=(15, self.l+330))
                aux10 = wx.TextCtrl(self.panel, value='3570.2', pos=(185, self.l+325), size=(80, -1))
                self.auxt10.append(aux10)

                wx.StaticText(self.panel, label='Numero de Vainas por alma', pos=(15, self.l+360))
                aux11 = wx.TextCtrl(self.panel, value='1', pos=(185, self.l+355), size=(80, -1))
                self.auxt11.append(aux11)

                wx.StaticText(self.panel, label='Diametro Vainas [cm]', pos=(15, self.l+390))
                aux12 = wx.TextCtrl(self.panel, value='10.0', pos=(185, self.l+385), size=(80, -1))
                self.auxt12.append(aux12)

                wx.StaticLine(self.panel, -1, (5, self.l+420), (500, 2))
                self.l += 420

                print 'Esto vale self.l al final de la estructura %d familia %d: ' %(q+1, i+1), self.l

        print '----------\nEsto vale self.l al terminar los ciclos de estructuras y familias: ', self.l, '\n----------'
        # Botones
        botonook = wx.Button(self.panel, label = 'Cargar Trazados', pos=(100, self.l+15))
        botonook.Bind(wx.EVT_BUTTON, self.aceptar_familias, botonook)
        botoncancel = wx.Button(self.panel, wx.ID_CANCEL, pos=(250, self.l+15))
        botoncancel.Bind(wx.EVT_BUTTON, self.cancel, botoncancel)
        wx.StaticLine(self.panel, -1, (5, self.l+45), (500, 2))

        self.l += 45
        print 'XXXXXXXXXX\nEsto vale self.l luego de insertar los botones Ok y Cancel: ', self.l, '\n XXXXXXXXXX'

        self.panel.SetScrollbars(1, 1, -1, int(self.l))

    def aceptar_familias(self, event):

        self.TT = []
        # c es un contador para recoger los datos de pretensado de cada familia
        c = 0

        # Este ciclo va a leer todos los datos de las familias de pretensado
        # Entra una vez por cada EP
        for i in range(int(len(self.datep))):
            T = np.array([[0]*20]*int(self.fam[i]), np.float16)
            # Entra una vez por cada familia
            for j in range(int(self.fam[i])):
                T[j, 0] = self.auxt1[c].GetValue()
                T[j, 1] = self.auxt3[c].GetValue()
                T[j, 13] = self.auxt2[c].GetValue()
                T[j, 14] = self.auxt4[c].GetValue()
                T[j, 11] = self.auxt5[c].GetValue()
                T[j, 12] = self.auxt6[c].GetValue()
                T[j, 15] = self.auxt7[c].GetValue()
                T[j, 16] = self.auxt8[c].GetValue()
                T[j, 17] = self.auxt9[c].GetValue()
                T[j, 6] = self.auxt10[c].GetValue()
                T[j, 7] = self.auxt11[c].GetValue()
                T[j, 8] = self.auxt12[c].GetValue()
                # T[j, 18] = self.auxt13[c].GetValue()
                T[j, 19] = int(i)
                c += 1
            self.TT.append(T)

        np.save('datos/datos_TT', self.TT)
        # print 'Esto es TT:\n', self.TT

        wide_win = 0

        # Este vector guarda la cantidad de vanos por cada familia (filas de trepre)
        flias = int(max(self.fam))
        est = int(len(self.datep))
        self.fi = np.zeros((est, flias))

        # Entramos una vez por cada estructura parcial
        for i in range(int(len(self.datep))):

            S = self.SS[i]
            print 'S:\n', S
            T = self.TT[i]
            print 'T:\n', T

            N3 = int(self.datep[i, 3])
            print 'N3: ', N3
            W1 = self.datep[i, 4]
            print 'W1: ', W1
            W2 = self.datep[i, 5]
            print 'W2: ', W2

            # Entramos una vez por cada familia de cables
            print 'Cantidad total de familias: ', int(len(T))
            for j in range(int(len(T))):

                self.xcoor = 325

                qest = 0

                IG = 1                  # Es una variable auxiliar
                J3 = T[j, 0]
                J4 = T[j, 1]

                print 'xxxxxxxxxxxxxxxxxxxxx\n Esto vale self.ord en la EP%d Familia %d: ' %(i+1, j+1), self.ord

                # Esto verifica si tiene o no voladizo izquierdo. Entra al bucle cuando TIENE VOLADIZO
                if J3 < S[0,4]:
                    NN = str('Voladizo Izquierdo')
                    qest +=1
                    print NN
                    IG = 2
                    print 'Pedir datos de trazado para el Voladizo Izquierdo de la EP ', i+1
                    print 'Luego calcular el trazado correspondiente\n'

                    wx.StaticText(self.panel, label=NN, pos=(self.xcoor + 50, self.ord+30))

                    wx.StaticText(self.panel, label='Codigo de Tesado (1, 2 o 3)', pos=(self.xcoor, self.ord+60))
                    ip = wx.TextCtrl(self.panel, value='1', pos=(self.xcoor + 150, self.ord+55), size=(60, -1))
                    self.trapre_ip.append(ip)

                    wx.StaticText(self.panel, label='Coordenada X0', pos=(self.xcoor, self.ord+90))
                    x0 = wx.TextCtrl(self.panel, value='1', pos=(self.xcoor + 150, self.ord+85), size=(60, -1))
                    self.trapre_x0.append(x0)

                    wx.StaticText(self.panel, label='Coordenada X1', pos=(self.xcoor, self.ord+120))
                    x1 = wx.TextCtrl(self.panel, value='1', pos=(self.xcoor + 150, self.ord+115), size=(60, -1))
                    self.trapre_x1.append(x1)

                    wx.StaticText(self.panel, label='Coordenada X2', pos=(self.xcoor, self.ord+150))
                    x2 = wx.TextCtrl(self.panel, value='1', pos=(self.xcoor + 150, self.ord+145), size=(60, -1))
                    self.trapre_x2.append(x2)

                    wx.StaticText(self.panel, label='Coordenada X3', pos=(self.xcoor, self.ord+180))
                    x3 = wx.TextCtrl(self.panel, value='1', pos=(self.xcoor + 150, self.ord+175), size=(60, -1))
                    self.trapre_x3.append(x3)

                    wx.StaticText(self.panel, label='Coordenada X4', pos=(self.xcoor, self.ord+210))
                    x4 = wx.TextCtrl(self.panel, value='1', pos=(self.xcoor + 150, self.ord+205), size=(60, -1))
                    self.trapre_x4.append(x4)

                    wx.StaticText(self.panel, label='Coordenada X5', pos=(self.xcoor, self.ord+240))
                    x5 = wx.TextCtrl(self.panel, value='1', pos=(self.xcoor + 150, self.ord+235), size=(60, -1))
                    self.trapre_x5.append(x5)

                    wx.StaticText(self.panel, label='Coordenada X6', pos=(self.xcoor, self.ord+270))
                    x6 = wx.TextCtrl(self.panel, value='1', pos=(self.xcoor + 150, self.ord+265), size=(60, -1))
                    self.trapre_x6.append(x6)

                    wx.StaticText(self.panel, label='Coordenada v1', pos=(self.xcoor, self.ord+300))
                    v1 = wx.TextCtrl(self.panel, value='1', pos=(self.xcoor + 150, self.ord+295), size=(60, -1))
                    self.trapre_v1.append(v1)

                    wx.StaticText(self.panel, label='Coordenada v2', pos=(self.xcoor, self.ord+330))
                    v2 = wx.TextCtrl(self.panel, value='1', pos=(self.xcoor + 150, self.ord+325), size=(60, -1))
                    self.trapre_v2.append(v2)

                    wx.StaticText(self.panel, label='Coordenada v3', pos=(self.xcoor, self.ord+360))
                    v3 = wx.TextCtrl(self.panel, value='1', pos=(self.xcoor + 150, self.ord+355), size=(60, -1))
                    self.trapre_v3.append(v3)

                    wx.StaticText(self.panel, label='Coordenada v4', pos=(self.xcoor, self.ord+390))
                    v4 = wx.TextCtrl(self.panel, value='1', pos=(self.xcoor + 150, self.ord+385), size=(60, -1))
                    self.trapre_v4.append(v4)

                    self.xcoor += 300

                    if self.xcoor > wide_win:
                        wide_win = self.xcoor
                    print 'Esto vale xcoor luego del voladizo izquierdo = ', self.xcoor

                # Entra a cada vano de la Estructura Parcial para definir los trazados
                for k in range(N3-1):
                    if J3 >= S[k+1,4]:
                        pass
                    elif J4 <= S[k, 4]:
                        pass
                    else:
                        NN = str('Vano ' + str(k+1))
                        qest +=1
                        IG = 2
                        print 'Pedir datos de trazado para el Vano ', k+1, ' de la EP ', i+1
                        print 'Luego calcular el trazado correspondiente\n'

                        wx.StaticText(self.panel, label=NN, pos=(self.xcoor + 150*(k)+50, self.ord+30))

                        wx.StaticText(self.panel, label='Codigo de Tesado (1, 2 o 3)', pos=(self.xcoor + 150*(k), self.ord+60))
                        ip = wx.TextCtrl(self.panel, value='1', pos=(self.xcoor + 150*(k+1), self.ord+55), size=(60, -1))
                        self.trapre_ip.append(ip)

                        wx.StaticText(self.panel, label='Coordenada X0', pos=(self.xcoor + 150*(k), self.ord+90))
                        x0 = wx.TextCtrl(self.panel, value='1', pos=(self.xcoor + 150*(k+1), self.ord+85), size=(60, -1))
                        self.trapre_x0.append(x0)

                        wx.StaticText(self.panel, label='Coordenada X1', pos=(self.xcoor + 150*(k), self.ord+120))
                        x1 = wx.TextCtrl(self.panel, value='1', pos=(self.xcoor + 150*(k+1), self.ord+115), size=(60, -1))
                        self.trapre_x1.append(x1)

                        wx.StaticText(self.panel, label='Coordenada X2', pos=(self.xcoor + 150*(k), self.ord+150))
                        x2 = wx.TextCtrl(self.panel, value='1', pos=(self.xcoor + 150*(k+1), self.ord+145), size=(60, -1))
                        self.trapre_x2.append(x2)

                        wx.StaticText(self.panel, label='Coordenada X3', pos=(self.xcoor + 150*(k), self.ord+180))
                        x3 = wx.TextCtrl(self.panel, value='1', pos=(self.xcoor + 150*(k+1), self.ord+175), size=(60, -1))
                        self.trapre_x3.append(x3)

                        wx.StaticText(self.panel, label='Coordenada X4', pos=(self.xcoor + 150*(k), self.ord+210))
                        x4 = wx.TextCtrl(self.panel, value='1', pos=(self.xcoor + 150*(k+1), self.ord+205), size=(60, -1))
                        self.trapre_x4.append(x4)

                        wx.StaticText(self.panel, label='Coordenada X5', pos=(self.xcoor + 150*(k), self.ord+240))
                        x5 = wx.TextCtrl(self.panel, value='1', pos=(self.xcoor + 150*(k+1), self.ord+235), size=(60, -1))
                        self.trapre_x5.append(x5)

                        wx.StaticText(self.panel, label='Coordenada X6', pos=(self.xcoor + 150*(k), self.ord+270))
                        x6 = wx.TextCtrl(self.panel, value='1', pos=(self.xcoor + 150*(k+1), self.ord+265), size=(60, -1))
                        self.trapre_x6.append(x6)

                        wx.StaticText(self.panel, label='Coordenada v1', pos=(self.xcoor + 150*(k), self.ord+300))
                        v1 = wx.TextCtrl(self.panel, value='1', pos=(self.xcoor + 150*(k+1), self.ord+295), size=(60, -1))
                        self.trapre_v1.append(v1)

                        wx.StaticText(self.panel, label='Coordenada v2', pos=(self.xcoor + 150*(k), self.ord+330))
                        v2 = wx.TextCtrl(self.panel, value='1', pos=(self.xcoor + 150*(k+1), self.ord+325), size=(60, -1))
                        self.trapre_v2.append(v2)

                        wx.StaticText(self.panel, label='Coordenada v3', pos=(self.xcoor + 150*(k), self.ord+360))
                        v3 = wx.TextCtrl(self.panel, value='1', pos=(self.xcoor + 150*(k+1), self.ord+355), size=(60, -1))
                        self.trapre_v3.append(v3)

                        wx.StaticText(self.panel, label='Coordenada v4', pos=(self.xcoor + 150*(k), self.ord+390))
                        v4 = wx.TextCtrl(self.panel, value='1', pos=(self.xcoor + 150*(k+1), self.ord+385), size=(60, -1))
                        self.trapre_v4.append(v4)

                self.xcoor += (N3-1)*150
                print 'Esto vale xcoor luego de recorrer todos los vanos= ', self.xcoor

                if self.xcoor > wide_win:
                    wide_win = self.xcoor

                # Verifica si tiene voladizo derecho; si tiene, entra al ciclo
                if W2 != 0:
                    if J4 > S[N3-1, 4]:
                        NN = str('Voladizo Derecho')
                        qest +=1
                        IG = 2
                        print 'Pedir datos de trazado para el Voladizo Derecho de la EP', i+1
                        print 'Luego calcular el trazado correspondiente\n'

                        wx.StaticText(self.panel, label=NN, pos=(self.xcoor + 200, self.ord+30))

                        wx.StaticText(self.panel, label='Codigo de Tesado (1, 2 o 3)', pos=(self.xcoor + 150, self.ord+60))
                        ip = wx.TextCtrl(self.panel, value='1', pos=(self.xcoor + 300, self.ord+55), size=(60, -1))
                        self.trapre_ip.append(ip)

                        wx.StaticText(self.panel, label='Coordenada X0', pos=(self.xcoor + 150, self.ord+90))
                        x0 = wx.TextCtrl(self.panel, value='1', pos=(self.xcoor + 300, self.ord+85), size=(60, -1))
                        self.trapre_x0.append(x0)

                        wx.StaticText(self.panel, label='Coordenada X1', pos=(self.xcoor + 150, self.ord+120))
                        x1 = wx.TextCtrl(self.panel, value='1', pos=(self.xcoor + 300, self.ord+115), size=(60, -1))
                        self.trapre_x1.append(x1)

                        wx.StaticText(self.panel, label='Coordenada X2', pos=(self.xcoor + 150, self.ord+150))
                        x2 = wx.TextCtrl(self.panel, value='1', pos=(self.xcoor + 300, self.ord+145), size=(60, -1))
                        self.trapre_x2.append(x2)

                        wx.StaticText(self.panel, label='Coordenada X3', pos=(self.xcoor + 150, self.ord+180))
                        x3 = wx.TextCtrl(self.panel, value='1', pos=(self.xcoor + 300, self.ord+175), size=(60, -1))
                        self.trapre_x3.append(x3)

                        wx.StaticText(self.panel, label='Coordenada X4', pos=(self.xcoor + 150, self.ord+210))
                        x4 = wx.TextCtrl(self.panel, value='1', pos=(self.xcoor + 300, self.ord+205), size=(60, -1))
                        self.trapre_x4.append(x4)

                        wx.StaticText(self.panel, label='Coordenada X5', pos=(self.xcoor + 150, self.ord+240))
                        x5 = wx.TextCtrl(self.panel, value='1', pos=(self.xcoor + 300, self.ord+235), size=(60, -1))
                        self.trapre_x5.append(x5)

                        wx.StaticText(self.panel, label='Coordenada X6', pos=(self.xcoor + 150, self.ord+270))
                        x6 = wx.TextCtrl(self.panel, value='1', pos=(self.xcoor + 300, self.ord+265), size=(60, -1))
                        self.trapre_x6.append(x6)

                        wx.StaticText(self.panel, label='Coordenada v1', pos=(self.xcoor + 150, self.ord+300))
                        v1 = wx.TextCtrl(self.panel, value='1', pos=(self.xcoor + 300, self.ord+295), size=(60, -1))
                        self.trapre_v1.append(v1)

                        wx.StaticText(self.panel, label='Coordenada v2', pos=(self.xcoor + 150, self.ord+330))
                        v2 = wx.TextCtrl(self.panel, value='1', pos=(self.xcoor + 300, self.ord+325), size=(60, -1))
                        self.trapre_v2.append(v2)

                        wx.StaticText(self.panel, label='Coordenada v3', pos=(self.xcoor + 150, self.ord+360))
                        v3 = wx.TextCtrl(self.panel, value='1', pos=(self.xcoor + 300, self.ord+355), size=(60, -1))
                        self.trapre_v3.append(v3)

                        wx.StaticText(self.panel, label='Coordenada v4', pos=(self.xcoor + 150, self.ord+390))
                        v4 = wx.TextCtrl(self.panel, value='1', pos=(self.xcoor + 300, self.ord+385), size=(60, -1))
                        self.trapre_v4.append(v4)

                        if self.xcoor > wide_win:
                            wide_win = self.xcoor

                self.ord += 420
                self.fi[i, j] = qest
                print 'SELF.FI ', self.fi

        print self.fi

        self.panel.SetScrollbars(10, 10, int(wide_win), int(self.ord))

        # Botones
        botonook = wx.Button(self.panel, label = 'Aceptar', pos=(100, self.l+15))
        botonook.Bind(wx.EVT_BUTTON, self.tomar_valores, botonook)
        botoncancel = wx.Button(self.panel, label = 'Cancelar', pos=(250, self.l+15))
        botoncancel.Bind(wx.EVT_BUTTON, self.cancel, botoncancel)
        wx.StaticLine(self.panel, -1, (5, self.l+45), (500, 2))

    def tomar_valores(self, event):

        esp = int(len(self.datep))
        print 'Espacios: ', esp
        plan = max(self.fam)
        print '\nPlanos: ', plan
        row = 0
        print '\nFilas: '
        col = 12
        self.trapre_all = np.zeros((esp, plan, row, col))

#        for i in range()



class Imprimir(wx.Frame):

    def __init__(self, parent):
        super(Imprimir, self).__init__(parent, size=(340, 700), style=wx.CLOSE_BOX | wx.CAPTION | wx.SYSTEM_MENU)

        datos_dg = np.load('datos/datos_dg.npy')
        datos_l = np.load('datos/datos_l.npy')
        datos_secsv = np.load('datos/datos_csv.npy')
        datos_SS = np.load('datos/datos_SS.npy')
        datos_datep = np.load('datos/datos_datep.npy')

        print 'DG =\n', datos_dg
        print 'L =\n', datos_l
        print 'Secciones Solo Viga =\n', datos_secsv
        print 'Matriz SS =\n', datos_SS
        print 'Matriz Datos Estructuras Parciales=\n', datos_datep
        self.Show()
        self.Center()


app = wx.App()
frame = MainWindow(None, "PCCB Version 3.1 2015")
app.MainLoop()
