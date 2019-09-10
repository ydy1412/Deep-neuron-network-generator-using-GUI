import wx
import wx.xrc


###########################################################################
## Class MyPanel1
###########################################################################


class Connection_panel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize,
                          style=wx.TAB_TRAVERSAL)

        sbSizer1 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, wx.EmptyString), wx.VERTICAL)

        bSizer1 = wx.BoxSizer(wx.HORIZONTAL)

        ### 1
        self.Flatten_txt = wx.StaticText(sbSizer1.GetStaticBox(), wx.ID_ANY, u"Flatten :", wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        self.Flatten_txt.Wrap(-1)
        bSizer1.Add(self.Flatten_txt, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        Flatten_cbChoices = ['True','False']
        self.Flatten_cb = wx.ComboBox(sbSizer1.GetStaticBox(), wx.ID_ANY, u"False", wx.DefaultPosition, wx.DefaultSize,
                                      Flatten_cbChoices, 0)
        bSizer1.Add(self.Flatten_cb, 1, wx.ALIGN_CENTER | wx.ALL, 5)

        sbSizer1.Add(bSizer1, 1, wx.EXPAND, 5)

        sbSizer1.Add(bSizer1, 1, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 5)

        self.m_staticline2 = wx.StaticLine(sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                           wx.LI_HORIZONTAL)
        sbSizer1.Add(self.m_staticline2, 0, wx.EXPAND | wx.ALL, 5)

        bSizer141 = wx.BoxSizer(wx.HORIZONTAL)

        ### 3
        self.Dropout_txt = wx.StaticText(sbSizer1.GetStaticBox(), wx.ID_ANY, u"Drop out :", wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        self.Dropout_txt.Wrap(-1)
        bSizer141.Add(self.Dropout_txt, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        # self.Unit_tctrl = wx.TextCtrl(sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
        #                                        wx.DefaultSize, 0)
        self.Dropout_tctrl = wx.TextCtrl(sbSizer1.GetStaticBox(), wx.ID_ANY, u'None', wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer141.Add(self.Dropout_tctrl, 1, wx.ALIGN_CENTER | wx.ALL, 5)

        sbSizer1.Add(bSizer141, 1, wx.EXPAND, 5)
        ###
        self.m_staticline5 = wx.StaticLine(sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                           wx.LI_HORIZONTAL)
        sbSizer1.Add(self.m_staticline5, 0, wx.EXPAND | wx.ALL, 5)

        bSizer28 = wx.BoxSizer(wx.HORIZONTAL)

        Adator_btn = wx.StdDialogButtonSizer()
        self.Adaptor_btnOK = wx.Button(sbSizer1.GetStaticBox(), wx.ID_OK)
        Adator_btn.AddButton(self.Adaptor_btnOK)
        Adator_btn.Realize()
        self.Adaptor_btnOK.Bind(wx.EVT_BUTTON,self.Adapt)

        bSizer28.Add(Adator_btn, 1, wx.EXPAND, 5)

        sbSizer1.Add(bSizer28, 1, wx.EXPAND, 5)

        self.SetSizer(sbSizer1)
        self.Layout()
        self.initall()

    def initall(self):
        self.id = None
        self.name = None
        self.start_id = None
        self.last_id = None
        self.Flatten = False
        self.Dropout = False


    def Adapt(self,evt):
        pass

    def __del__(self):
        pass

class Dense_panel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize,
                          style=wx.TAB_TRAVERSAL)

        sbSizer1 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, wx.EmptyString), wx.VERTICAL)

        bSizer1 = wx.BoxSizer(wx.HORIZONTAL)

        self.Unit_label = wx.StaticText(sbSizer1.GetStaticBox(), wx.ID_ANY, u"Units  : ", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.Unit_label.Wrap(-1)
        bSizer1.Add(self.Unit_label, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.Unit_tctrl = wx.TextCtrl(sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                       wx.DefaultSize, 0)
        bSizer1.Add(self.Unit_tctrl, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        sbSizer1.Add(bSizer1, 1, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 5)

        self.m_staticline2 = wx.StaticLine(sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                           wx.LI_HORIZONTAL)
        sbSizer1.Add(self.m_staticline2, 0, wx.EXPAND | wx.ALL, 5)

        bSizer141 = wx.BoxSizer(wx.HORIZONTAL)

        self.Weight_initializer_label = wx.StaticText(sbSizer1.GetStaticBox(), wx.ID_ANY, u"Weight initializer  :",
                                                      wx.DefaultPosition, wx.DefaultSize, 0)
        self.Weight_initializer_label.Wrap(-1)
        bSizer141.Add(self.Weight_initializer_label, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        Weight_cbChoices = []
        self.Weight_cb = wx.ComboBox(sbSizer1.GetStaticBox(), wx.ID_ANY, u"glorot_uniform", wx.DefaultPosition,
                                     wx.DefaultSize, Weight_cbChoices, 0)
        bSizer141.Add(self.Weight_cb, 1, wx.ALIGN_CENTER_VERTICAL| wx.ALL, 5)

        sbSizer1.Add(bSizer141, 1, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5)

        self.m_staticline5 = wx.StaticLine(sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                           wx.LI_HORIZONTAL)
        sbSizer1.Add(self.m_staticline5, 0, wx.EXPAND | wx.ALL, 5)

        bSizer142 = wx.BoxSizer(wx.HORIZONTAL)

        self.Bias_initializer = wx.StaticText(sbSizer1.GetStaticBox(), wx.ID_ANY, u"Bias initializer  :",
                                              wx.DefaultPosition, wx.DefaultSize, 0)
        self.Bias_initializer.Wrap(-1)
        bSizer142.Add(self.Bias_initializer, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        Bias_cbChoices = []
        self.Bias_cb = wx.ComboBox(sbSizer1.GetStaticBox(), wx.ID_ANY, u"zeros", wx.DefaultPosition, wx.DefaultSize,
                                   Bias_cbChoices, 0)
        bSizer142.Add(self.Bias_cb, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)

        sbSizer1.Add(bSizer142, 1, wx.EXPAND, 5)

        self.m_staticline6 = wx.StaticLine(sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                           wx.LI_HORIZONTAL)
        sbSizer1.Add(self.m_staticline6, 0, wx.EXPAND | wx.ALL, 5)

        bSizer143 = wx.BoxSizer(wx.HORIZONTAL)

        self.Activation_txt = wx.StaticText(sbSizer1.GetStaticBox(), wx.ID_ANY, u"Activation  : ", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.Activation_txt.Wrap(-1)
        bSizer143.Add(self.Activation_txt, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        Activation_cbChoices = []
        self.Activation_cb = wx.ComboBox(sbSizer1.GetStaticBox(), wx.ID_ANY, u"sigmoid", wx.DefaultPosition,
                                         wx.DefaultSize, Activation_cbChoices, 0)
        bSizer143.Add(self.Activation_cb, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)

        sbSizer1.Add(bSizer143, 1, wx.EXPAND, 5)

        self.m_staticline7 = wx.StaticLine(sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                           wx.LI_HORIZONTAL)
        sbSizer1.Add(self.m_staticline7, 0, wx.EXPAND | wx.ALL, 5)

        bSizer144 = wx.BoxSizer(wx.HORIZONTAL)

        self.Regularization_txt = wx.StaticText(sbSizer1.GetStaticBox(), wx.ID_ANY, u"Regularization : ",
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.Regularization_txt.Wrap(-1)
        bSizer144.Add(self.Regularization_txt, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        Regularization_cbChoices = []
        self.Regularization_cb = wx.ComboBox(sbSizer1.GetStaticBox(), wx.ID_ANY, u"L1", wx.DefaultPosition,
                                             wx.DefaultSize, Regularization_cbChoices, 0)
        bSizer144.Add(self.Regularization_cb, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)

        sbSizer1.Add(bSizer144, 1, wx.EXPAND, 5)

        self.m_staticline8 = wx.StaticLine(sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                           wx.LI_HORIZONTAL)
        sbSizer1.Add(self.m_staticline8, 0, wx.EXPAND | wx.ALL, 5)

        bSizer28 = wx.BoxSizer(wx.HORIZONTAL)

        Adator_btn = wx.StdDialogButtonSizer()
        self.Adaptor_btnOK = wx.Button(sbSizer1.GetStaticBox(), wx.ID_OK)
        Adator_btn.AddButton(self.Adaptor_btnOK)

        Adator_btn.Realize()

        self.Adaptor_btnOK.Bind(wx.EVT_BUTTON,self.Adapt)

        bSizer28.Add(Adator_btn, 1, wx.EXPAND, 5)

        sbSizer1.Add(bSizer28, 1, wx.EXPAND, 5)

        self.SetSizer(sbSizer1)
        self.Layout()
        self.initall()
    def initall(self):
        self.id = None
        self.name = None
        self.Units = None
        self.Weight_initializer = None
        self.Bias_initializer = None
        self.Activation = None
        self.Regularization = None


    def Adapt(self,evt):
        pass

    def __del__(self):
        pass

class Convolution_panel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize,
                          style=wx.TAB_TRAVERSAL)

        sbSizer1 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, wx.EmptyString), wx.VERTICAL)

        bSizer1 = wx.BoxSizer(wx.HORIZONTAL)

        self.Map_txt = wx.StaticText(sbSizer1.GetStaticBox(), wx.ID_ANY, u"Map number  : ", wx.DefaultPosition,
                                     wx.DefaultSize, 0)
        self.Map_txt.Wrap(-1)
        bSizer1.Add(self.Map_txt, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.Map_tctrl = wx.TextCtrl(sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                       wx.DefaultSize, 0)
        bSizer1.Add(self.Map_tctrl, 1, wx.ALIGN_CENTER | wx.ALL, 5)

        sbSizer1.Add(bSizer1, 1, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 5)

        self.m_staticline2 = wx.StaticLine(sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                           wx.LI_HORIZONTAL)
        sbSizer1.Add(self.m_staticline2, 0, wx.EXPAND | wx.ALL, 5)

        bSizer14 = wx.BoxSizer(wx.HORIZONTAL)

        self.Window_txt = wx.StaticText(sbSizer1.GetStaticBox(), wx.ID_ANY, u"Window size  : ", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.Window_txt.Wrap(-1)
        bSizer14.Add(self.Window_txt, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.Window_tctrl = wx.TextCtrl(sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        bSizer14.Add(self.Window_tctrl, 1, wx.ALIGN_CENTER | wx.ALL, 5)

        sbSizer1.Add(bSizer14, 1, wx.EXPAND, 5)

        self.m_staticline4 = wx.StaticLine(sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                           wx.LI_HORIZONTAL)
        sbSizer1.Add(self.m_staticline4, 0, wx.EXPAND | wx.ALL, 5)

        bSizer141 = wx.BoxSizer(wx.HORIZONTAL)

        self.Stride_txt = wx.StaticText(sbSizer1.GetStaticBox(), wx.ID_ANY, u"Strides  :", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.Stride_txt.Wrap(-1)
        bSizer141.Add(self.Stride_txt, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.Stride_tctrl = wx.TextCtrl(sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        bSizer141.Add(self.Stride_tctrl, 1, wx.ALIGN_CENTER | wx.ALL, 5)

        sbSizer1.Add(bSizer141, 1, wx.EXPAND, 5)

        self.m_staticline5 = wx.StaticLine(sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                           wx.LI_HORIZONTAL)
        sbSizer1.Add(self.m_staticline5, 0, wx.EXPAND | wx.ALL, 5)

        bSizer144 = wx.BoxSizer(wx.HORIZONTAL)

        self.Activation_txt = wx.StaticText(sbSizer1.GetStaticBox(), wx.ID_ANY, u"Activation :", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.Activation_txt.Wrap(-1)
        bSizer144.Add(self.Activation_txt, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        Activation_cbChoices = []
        self.Activation_cb = wx.ComboBox(sbSizer1.GetStaticBox(), wx.ID_ANY, u"None", wx.DefaultPosition,
                                         wx.DefaultSize, Activation_cbChoices, 0)
        bSizer144.Add(self.Activation_cb, 1, wx.ALIGN_CENTER | wx.ALL, 5)

        sbSizer1.Add(bSizer144, 1, wx.EXPAND, 5)

        self.m_staticline8 = wx.StaticLine(sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                           wx.LI_HORIZONTAL)
        sbSizer1.Add(self.m_staticline8, 0, wx.EXPAND | wx.ALL, 5)

        bSizer28 = wx.BoxSizer(wx.HORIZONTAL)

        Adator_btn = wx.StdDialogButtonSizer()
        self.Adaptor_btnOK = wx.Button(sbSizer1.GetStaticBox(), wx.ID_OK)
        Adator_btn.AddButton(self.Adaptor_btnOK)

        self.Adaptor_btnOK.Bind(wx.EVT_BUTTON,self.Adapt)

        Adator_btn.Realize()

        bSizer28.Add(Adator_btn, 1, wx.EXPAND, 5)

        sbSizer1.Add(bSizer28, 1, wx.EXPAND, 5)

        self.SetSizer(sbSizer1)
        self.Layout()
        self.initall()

    def initall(self):
        self.id = None
        self.name = None
        self.Map_number = None
        self.Window_size = None
        self.Strides = None
        self.Activation = None

    def Adapt(self,evt):
        pass

    def __del__(self):
        pass

class Pooling_panel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize,
                          style=wx.TAB_TRAVERSAL)

        sbSizer1 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, wx.EmptyString), wx.VERTICAL)

        bSizer1 = wx.BoxSizer(wx.HORIZONTAL)

        self.size_txt = wx.StaticText(sbSizer1.GetStaticBox(), wx.ID_ANY, u"Pooling size : ", wx.DefaultPosition,
                                      wx.DefaultSize, 0)
        self.size_txt.Wrap(-1)
        bSizer1.Add(self.size_txt, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.size_tctrl = wx.TextCtrl(sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        bSizer1.Add(self.size_tctrl, 1, wx.ALIGN_CENTER | wx.ALL, 5)

        sbSizer1.Add(bSizer1, 1, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 5)

        self.m_staticline2 = wx.StaticLine(sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                           wx.LI_HORIZONTAL)
        sbSizer1.Add(self.m_staticline2, 0, wx.EXPAND | wx.ALL, 5)

        bSizer141 = wx.BoxSizer(wx.HORIZONTAL)

        self.Stride_txt = wx.StaticText(sbSizer1.GetStaticBox(), wx.ID_ANY, u"Strides  :", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.Stride_txt.Wrap(-1)
        bSizer141.Add(self.Stride_txt, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.Stride_tctrl = wx.TextCtrl(sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                       wx.DefaultSize, 0)
        bSizer141.Add(self.Stride_tctrl, 1, wx.ALIGN_CENTER | wx.ALL, 5)

        sbSizer1.Add(bSizer141, 1, wx.EXPAND, 5)

        self.m_staticline4 = wx.StaticLine(sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                           wx.LI_HORIZONTAL)
        sbSizer1.Add(self.m_staticline4, 0, wx.EXPAND | wx.ALL, 5)

        bSizer14 = wx.BoxSizer(wx.HORIZONTAL)

        self.Padding_txt = wx.StaticText(sbSizer1.GetStaticBox(), wx.ID_ANY, u"Padding :", wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        self.Padding_txt.Wrap(-1)
        bSizer14.Add(self.Padding_txt, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        Padding_cbChoices = []
        self.Padding_cb = wx.ComboBox(sbSizer1.GetStaticBox(), wx.ID_ANY, u"valid", wx.DefaultPosition, wx.DefaultSize,
                                      Padding_cbChoices, 0)
        bSizer14.Add(self.Padding_cb, 1, wx.ALIGN_CENTER | wx.ALL, 5)

        sbSizer1.Add(bSizer14, 1, wx.EXPAND, 5)

        self.m_staticline5 = wx.StaticLine(sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                           wx.LI_HORIZONTAL)
        sbSizer1.Add(self.m_staticline5, 0, wx.EXPAND | wx.ALL, 5)

        bSizer28 = wx.BoxSizer(wx.HORIZONTAL)

        Adator_btn = wx.StdDialogButtonSizer()
        self.Adaptor_btnOK = wx.Button(sbSizer1.GetStaticBox(), wx.ID_OK)
        Adator_btn.AddButton(self.Adaptor_btnOK)
        Adator_btn.Realize()
        self.Adaptor_btnOK.Bind(wx.EVT_BUTTON,self.Adapt)

        bSizer28.Add(Adator_btn, 1, wx.EXPAND, 5)

        sbSizer1.Add(bSizer28, 1, wx.EXPAND, 5)

        self.SetSizer(sbSizer1)
        self.Layout()
        self.initall()

    def initall(self):
        self.id = None
        self.name = None
        self.Pooling_size = None
        self.Strides = None
        self.Padding = None


    def Adapt(self,evt):
        pass

    def __del__(self):
        pass

class LSTM_panel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size = wx.DefaultSize,
                          style=wx.TAB_TRAVERSAL)

        sbSizer1 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, wx.EmptyString), wx.VERTICAL)

        bSizer1 = wx.BoxSizer(wx.HORIZONTAL)

        self.Unit_label = wx.StaticText(sbSizer1.GetStaticBox(), wx.ID_ANY, u"Units  : ", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.Unit_label.Wrap(-1)
        bSizer1.Add(self.Unit_label, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.Unit_tctrl = wx.TextCtrl(sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                      wx.DefaultSize, 0)
        bSizer1.Add(self.Unit_tctrl, 1,wx.ALIGN_CENTER_VERTICAL| wx.ALL, 5)

        sbSizer1.Add(bSizer1, 1, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 5)

        self.m_staticline2 = wx.StaticLine(sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                           wx.LI_HORIZONTAL)
        sbSizer1.Add(self.m_staticline2, 0, wx.EXPAND | wx.ALL, 5)

        bSizer145 = wx.BoxSizer(wx.HORIZONTAL)

        self.Recurrent_init_txt = wx.StaticText(sbSizer1.GetStaticBox(), wx.ID_ANY, u"Recurrent initializer  :",
                                                wx.DefaultPosition, wx.DefaultSize, 0)
        self.Recurrent_init_txt.Wrap(-1)
        bSizer145.Add(self.Recurrent_init_txt, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        Weight_cb11Choices = []
        self.Recurrent_init_cb = wx.ComboBox(sbSizer1.GetStaticBox(), wx.ID_ANY, u"orthogonal", wx.DefaultPosition,
                                       wx.DefaultSize, Weight_cb11Choices, 0)
        bSizer145.Add(self.Recurrent_init_cb, 1, wx.ALIGN_CENTER | wx.ALL, 5)

        sbSizer1.Add(bSizer145, 1, wx.EXPAND, 5)

        self.m_staticline21 = wx.StaticLine(sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                            wx.LI_HORIZONTAL)
        sbSizer1.Add(self.m_staticline21, 0, wx.EXPAND | wx.ALL, 5)

        bSizer14 = wx.BoxSizer(wx.HORIZONTAL)

        self.Recurrent_acti_txt = wx.StaticText(sbSizer1.GetStaticBox(), wx.ID_ANY, u"Recurrent activation  :",
                                                wx.DefaultPosition, wx.DefaultSize, 0)
        self.Recurrent_acti_txt.Wrap(-1)
        bSizer14.Add(self.Recurrent_acti_txt, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        Recurrent_acti_cbChoices = []
        self.Recurrent_acti_cb = wx.ComboBox(sbSizer1.GetStaticBox(), wx.ID_ANY, u"hard_sigmoid", wx.DefaultPosition,
                                             wx.DefaultSize, Recurrent_acti_cbChoices, 0)
        bSizer14.Add(self.Recurrent_acti_cb, 1, wx.ALIGN_CENTER | wx.ALL, 5)

        sbSizer1.Add(bSizer14, 1, wx.EXPAND, 5)

        self.m_staticline4 = wx.StaticLine(sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                           wx.LI_HORIZONTAL)
        sbSizer1.Add(self.m_staticline4, 0, wx.EXPAND | wx.ALL, 5)

        bSizer141 = wx.BoxSizer(wx.HORIZONTAL)

        self.Weight_initializer_label = wx.StaticText(sbSizer1.GetStaticBox(), wx.ID_ANY, u"Weight initializer  :",
                                                      wx.DefaultPosition, wx.DefaultSize, 0)
        self.Weight_initializer_label.Wrap(-1)
        bSizer141.Add(self.Weight_initializer_label, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        Weight_cbChoices = []
        self.Weight_cb = wx.ComboBox(sbSizer1.GetStaticBox(), wx.ID_ANY, u"glorot_uniform", wx.DefaultPosition,
                                     wx.DefaultSize, Weight_cbChoices, 0)
        bSizer141.Add(self.Weight_cb, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)

        sbSizer1.Add(bSizer141, 1, wx.EXPAND, 5)

        self.m_staticline5 = wx.StaticLine(sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                           wx.LI_HORIZONTAL)
        sbSizer1.Add(self.m_staticline5, 0, wx.EXPAND | wx.ALL, 5)

        bSizer142 = wx.BoxSizer(wx.HORIZONTAL)

        self.Bias_initializer = wx.StaticText(sbSizer1.GetStaticBox(), wx.ID_ANY, u"Bias initializer  :",
                                              wx.DefaultPosition, wx.DefaultSize, 0)
        self.Bias_initializer.Wrap(-1)
        bSizer142.Add(self.Bias_initializer, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        Bias_cbChoices = []
        self.Bias_cb = wx.ComboBox(sbSizer1.GetStaticBox(), wx.ID_ANY, u"zeros", wx.DefaultPosition, wx.DefaultSize,
                                   Bias_cbChoices, 0)
        bSizer142.Add(self.Bias_cb, 1,wx.ALIGN_CENTER_VERTICAL| wx.ALL, 5)

        sbSizer1.Add(bSizer142, 1, wx.EXPAND, 5)

        self.m_staticline6 = wx.StaticLine(sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                           wx.LI_HORIZONTAL)
        sbSizer1.Add(self.m_staticline6, 0, wx.EXPAND | wx.ALL, 5)

        bSizer143 = wx.BoxSizer(wx.HORIZONTAL)

        self.Activation_txt = wx.StaticText(sbSizer1.GetStaticBox(), wx.ID_ANY, u"Activation  : ", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.Activation_txt.Wrap(-1)
        bSizer143.Add(self.Activation_txt, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        Activation_cbChoices = []
        self.Activation_cb = wx.ComboBox(sbSizer1.GetStaticBox(), wx.ID_ANY, u"tanh", wx.DefaultPosition,
                                         wx.DefaultSize, Activation_cbChoices, 0)
        bSizer143.Add(self.Activation_cb, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)

        sbSizer1.Add(bSizer143, 1, wx.EXPAND, 5)

        self.m_staticline7 = wx.StaticLine(sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                           wx.LI_HORIZONTAL)
        sbSizer1.Add(self.m_staticline7, 0, wx.EXPAND | wx.ALL, 5)

        bSizer144 = wx.BoxSizer(wx.HORIZONTAL)

        self.Regularization_txt = wx.StaticText(sbSizer1.GetStaticBox(), wx.ID_ANY, u"Regularization : ",
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.Regularization_txt.Wrap(-1)
        bSizer144.Add(self.Regularization_txt, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        Regularization_cbChoices = []
        self.Regularization_cb = wx.ComboBox(sbSizer1.GetStaticBox(), wx.ID_ANY, u"L1", wx.DefaultPosition,
                                             wx.DefaultSize, Regularization_cbChoices, 0)
        bSizer144.Add(self.Regularization_cb, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)

        sbSizer1.Add(bSizer144, 1, wx.EXPAND, 5)

        self.m_staticline8 = wx.StaticLine(sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                           wx.LI_HORIZONTAL)
        sbSizer1.Add(self.m_staticline8, 0, wx.EXPAND | wx.ALL, 5)

        bSizer28 = wx.BoxSizer(wx.HORIZONTAL)

        Adator_btn = wx.StdDialogButtonSizer()
        self.Adaptor_btnOK = wx.Button(sbSizer1.GetStaticBox(), wx.ID_OK)
        Adator_btn.AddButton(self.Adaptor_btnOK)
        Adator_btn.Realize()

        bSizer28.Add(Adator_btn, 1, wx.EXPAND, 5)
        self.Adaptor_btnOK.Bind(wx.EVT_BUTTON,self.Adapt)

        sbSizer1.Add(bSizer28, 1, wx.EXPAND, 5)

        self.SetSizer(sbSizer1)
        self.Layout()
        self.initall()

    def initall(self):
        self.id = None
        self.name = None
        self.Units = None
        self.Recurrent_intializer = None
        self.Recurrent_activation = None
        self.Weight_initializer = None
        self.Bias_initializer = None
        self.Activation = None
        self.Regularization = None

    def Adapt(self,evt):
        pass

    def __del__(self):
        pass
