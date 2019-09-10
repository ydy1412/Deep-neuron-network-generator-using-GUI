import wx
import wx.xrc
import os
from wx.lib.floatcanvas import FloatCanvas
from Dialog.Main_Dialog import New_Model_Dialog
from Dialog.Layer_dialog import *
from Frame_Canvas.Layer_status_panel import *
import time
import numpy as np

class StartFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Neuron Network Generator", pos=wx.DefaultPosition,
                          size=wx.Size(810, 632), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.Init_All()

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        self.SetMenuBar(self.Set_Menubar())

        """
                Essential_icon_dict = {'Data_manipulation' : ['Data_manipulate','Data Visualizing'],
                                       'Model_train_extract': [ 'Train Model', 'Extract Model'],
                                       'Undo_Redo': ['Undo','Redo'],
                                       'Layer_tree_icon': ['Dense','Dropout','Convolution','Pooling','Flatten','LSTM']}
                """

        ################### Toolbar layout

        self.Toolbar_Main_panel_sizer = wx.BoxSizer(wx.VERTICAL)

        self.Toolbar_Main_panel_sizer.Add(self.Set_Toolbar(),0 ,wx.EXPAND,0)


        ################### Main Layout

        self.Main_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.Main_sizer.SetMinSize((-1,self.Canvas_height))
        self.Canvas_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.Canvas = FloatCanvas.FloatCanvas(self,-1)
        self.Canvas.SetScrollbar(wx.VERTICAL, 0, 6, 50)

        self.Canvas.SetMinSize((self.Canvas_width, -1))
        self.Canvas.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        self.Canvas_sizer.Add(self.Canvas,1,wx.EXPAND,0)
        self.Main_sizer.Add(self.Canvas_sizer, 0, wx.EXPAND | wx.ALL, 0)

        self.Horizontal_sizer_panel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.Horizontal_sizer_panel.SetCursor(wx.Cursor(wx.CURSOR_SIZEWE))
        self.Horizontal_sizer_panel.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENU))
        self.Horizontal_sizer_panel.SetMaxSize(wx.Size(3, -1))

        self.Main_sizer.Add(self.Horizontal_sizer_panel, 1, wx.EXPAND | wx.ALL, 0)

        self.Layer_status_base_panel =wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.Layer_status_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.Connection_status_panel = Connection_layer_panel(self.Layer_status_base_panel)
        self.Connection_status_panel.SetMinSize((50, 50))
        self.Layer_status_sizer.Add(self.Connection_status_panel, 1, wx.ALL | wx.EXPAND, 0)
        self.Connection_status_panel.Hide()

        self.Dense_status_panel = Dense_layer_panel(self.Layer_status_base_panel)
        self.Dense_status_panel.SetMinSize((50,50))
        self.Layer_status_sizer.Add(self.Dense_status_panel, 1, wx.ALL | wx.EXPAND, 0)
        self.Dense_status_panel.Hide()

        self.Convolution_status_panel = Convolution_layer_panel(self.Layer_status_base_panel)
        self.Convolution_status_panel.SetMinSize((50,50))
        self.Layer_status_sizer.Add(self.Convolution_status_panel, 1, wx.ALL | wx.EXPAND, 0)
        self.Convolution_status_panel.Hide()

        self.Pooling_status_panel = Pooling_layer_panel(self.Layer_status_base_panel)
        self.Pooling_status_panel.SetMinSize((50,50))
        self.Layer_status_sizer.Add(self.Pooling_status_panel, 1, wx.ALL | wx.EXPAND, 0)
        self.Pooling_status_panel.Hide()

        self.LSTM_status_panel = LSTM_layer_panel(self.Layer_status_base_panel)
        self.LSTM_status_panel.SetMinSize((50,50))
        self.Layer_status_sizer.Add(self.LSTM_status_panel, 1, wx.ALL | wx.EXPAND, 0)
        self.LSTM_status_panel.Hide()

        self.Layer_status_base_panel.SetSizer(self.Layer_status_sizer)

        self.Main_sizer.Add(self.Layer_status_base_panel, 1, wx.ALL | wx.EXPAND, 0)

        self.Toolbar_Main_panel_sizer.Add(self.Main_sizer, 0, wx.EXPAND, 5)

        self.Vertical_sizer_panel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.Vertical_sizer_panel.SetCursor(wx.Cursor(wx.CURSOR_SIZENS))
        self.Vertical_sizer_panel.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENU))
        self.Vertical_sizer_panel.SetMaxSize(wx.Size(-1, 3))

        self.Toolbar_Main_panel_sizer.Add(self.Vertical_sizer_panel, 1, wx.EXPAND | wx.ALL, 0)

        self.Sub_panel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.Sub_panel.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))

        self.Toolbar_Main_panel_sizer.Add(self.Sub_panel, 1, wx.EXPAND | wx.ALL, 0)

        self.SetSizer(self.Toolbar_Main_panel_sizer)
        self.Layout()

        self.Centre(wx.BOTH)

        self.Bind_Tool_Event()
        self.Bind_Size_Event()

        self.Canvas.Bind(wx.EVT_SCROLLWIN,self.OnScrollchanged)
        self.Canvas.Bind(wx.EVT_SCROLLWIN_THUMBRELEASE,self.OnScrollreleased)


        ################ Mouse control

        self.Bind(wx.EVT_MOUSE_EVENTS, self.OnMouseEvent)

        self.Bind(wx.EVT_LEFT_UP, self.MouseLeft_Up)

        self.Init_All()
        print(self.Layer_status_base_panel.GetClientSize())
        print(self.Dense_status_panel.GetClientSize())

    def Init_All(self):
        self.New_model_dialog = New_model_dialog(None)

        self.Main_Client_size = self.GetClientSize()
        self.thick_of_size_panel = 4
        self.Layer_tree_width = 200
        self.Sub_panel_height = 200
        self.Canvas_width = self.Main_Client_size[0] - self.Layer_tree_width
        self.Canvas_height = self.Main_Client_size[1] - self.Sub_panel_height
        self.lastx = self.x = 30
        self.lasty = self.y = 30
        self.Dragging_start_point = None
        self.Dragging_last_point = None
        self.Dragging_previous_point = None
        self.Change_horizontal = False
        self.Change_vertical = False

        self.Layer_object_buffer = []
        self.Previus_selected_buffer = []
        self.Undo_list = []
        self.Redo_list = []
        self.Undo_redo_index = 0
        self.Input_node_buffer = []
        self.Output_node_buffer = []

        self.id_count = 0

        self.New_model_tool_id = 1
        self.Data_mani_tool_id = 2
        self.Data_visu_tool_id = 3
        self.Input_tool_id = 4
        self.Output_tool_id = 5
        self.Connection_tool_id = 6
        self.Dense_layer_tool_id = 7
        self.Pooling_layer_tool_id = 8
        self.Convolution_layer_tool_id = 9
        self.LSTM_layer_tool_id = 10
        self.Undo_tool_id = 11
        self.Redo_tool_id = 12
        self.Train_model_tool_id = 13



        self.Add_Layer = False
        #############  Toolbar item button
        # Add_btn_list = [input_btn,output_btn,connection_btn,dense_btn, pooling
        #                  , convolutiuon,lstm_btn]
        self.Input_btn_id = 0
        self.Output_btn_id = 1
        self.Connection_btn_id = 2
        self.Dense_layer_btn_id = 3
        self.Pooling_layer_btn_id = 4
        self.Convolution_layer_btn_id = 5
        self.LSTM_layer_btn_id = 6
        self.Add_btn_list = [False,False,False,False,False,False,False]

    def Set_Menubar(self):
        self.m_menubar1 = wx.MenuBar(0)
        self.File_menu_name = wx.Menu()
        self.Open_menu_item = wx.MenuItem(self.File_menu_name, wx.ID_ANY, u"Open...", wx.EmptyString, wx.ITEM_NORMAL)
        self.File_menu_name.Append(self.Open_menu_item)

        self.Save_as_menu_item = wx.MenuItem(self.File_menu_name, wx.ID_ANY, u"Save as...", wx.EmptyString,
                                             wx.ITEM_NORMAL)
        self.File_menu_name.Append(self.Save_as_menu_item)

        self.Save_menu_item = wx.MenuItem(self.File_menu_name, wx.ID_ANY, u"Save", wx.EmptyString, wx.ITEM_NORMAL)
        self.File_menu_name.Append(self.Save_menu_item)

        self.m_menubar1.Append(self.File_menu_name, u"File")

        self.edit_menu_name = wx.Menu()
        self.m_menubar1.Append(self.edit_menu_name, u"Edit")

        self.m_menu5 = wx.Menu()
        self.m_menubar1.Append(self.m_menu5, u"View")

        self.Tools_menu_name = wx.Menu()
        self.m_menubar1.Append(self.Tools_menu_name, u"Tools")

        self.help_menu_name = wx.Menu()
        self.m_menubar1.Append(self.help_menu_name, u"help")
        return self.m_menubar1

    def Set_Toolbar(self):

        #################### toolbar_icon_image #####################

        self.tool_bar_size = (15, 15)
        Directory = os.getcwd()

        str = Directory + '\\Icon_folder\\New.png'
        New_icon = wx.Image(str, wx.BITMAP_TYPE_PNG)
        New_icon.Rescale(self.tool_bar_size[0], self.tool_bar_size[1])
        New_icon = wx.Bitmap(New_icon)

        str = Directory + '\\Icon_folder\\Data_manipulation.png'
        Data_mani_icon = wx.Image(str, wx.BITMAP_TYPE_PNG)
        Data_mani_icon.Rescale(self.tool_bar_size[0], self.tool_bar_size[1])
        Data_mani_icon = wx.Bitmap(Data_mani_icon)

        str = Directory + '\\Icon_folder\\Data_visualization.png'
        Data_visu_icon = wx.Image(str, wx.BITMAP_TYPE_PNG)
        Data_visu_icon.Rescale(self.tool_bar_size[0], self.tool_bar_size[1])
        Data_visu_icon = wx.Bitmap(Data_visu_icon)

        str = Directory + '\\Icon_folder\\Train.png'
        Train_model_icon = wx.Image(str, wx.BITMAP_TYPE_PNG)
        Train_model_icon.Rescale(self.tool_bar_size[0], self.tool_bar_size[1])
        Train_model_icon = wx.Bitmap(Train_model_icon)

        str = Directory + '\\Icon_folder\\Extract.png'
        Extract_model_icon = wx.Image(str, wx.BITMAP_TYPE_PNG)
        Extract_model_icon.Rescale(self.tool_bar_size[0], self.tool_bar_size[1])
        Extract_model_icon = wx.Bitmap(Extract_model_icon)

        str = Directory + '\\Icon_folder\\Undo(2).png'
        Undo_icon = wx.Image(str, wx.BITMAP_TYPE_PNG)
        Undo_icon.Rescale(self.tool_bar_size[0], self.tool_bar_size[1])
        Undo_icon = wx.Bitmap(Undo_icon)

        str = Directory + '\\Icon_folder\\Redo(2).png'
        Redo_icon = wx.Image(str, wx.BITMAP_TYPE_PNG)
        Redo_icon.Rescale(self.tool_bar_size[0], self.tool_bar_size[1])
        Redo_icon = wx.Bitmap(Redo_icon)

        str = Directory + '\\Icon_folder\\I.png'
        Input_icon = wx.Image(str, wx.BITMAP_TYPE_PNG)
        Input_icon.Rescale(self.tool_bar_size[0], self.tool_bar_size[1])
        Input_icon = wx.Bitmap(Input_icon)

        str = Directory + '\\Icon_folder\\O.png'
        Output_icon = wx.Image(str, wx.BITMAP_TYPE_PNG)
        Output_icon.Rescale(self.tool_bar_size[0], self.tool_bar_size[1])
        Output_icon = wx.Bitmap(Output_icon)

        str = Directory + '\\Icon_folder\\Connection.png'
        Connection_icon = wx.Image(str, wx.BITMAP_TYPE_PNG)
        Connection_icon.Rescale(self.tool_bar_size[0], self.tool_bar_size[1])
        Connection_icon = wx.Bitmap(Connection_icon)

        str = Directory + '\\Icon_folder\\D.png'
        Dense_icon = wx.Image(str, wx.BITMAP_TYPE_PNG)
        Dense_icon.Rescale(self.tool_bar_size[0], self.tool_bar_size[1])
        Dense_icon = wx.Bitmap(Dense_icon)

        str = Directory + '\\Icon_folder\\C.png'
        Convolution_icon = wx.Image(str, wx.BITMAP_TYPE_PNG)
        Convolution_icon.Rescale(self.tool_bar_size[0], self.tool_bar_size[1])
        Convolution_icon = wx.Bitmap(Convolution_icon)

        str = Directory + '\\Icon_folder\\P.png'
        Pooling_icon = wx.Image(str, wx.BITMAP_TYPE_PNG)
        Pooling_icon.Rescale(self.tool_bar_size[0], self.tool_bar_size[1])
        Pooling_icon = wx.Bitmap(Pooling_icon)

        str = Directory + '\\Icon_folder\\L.png'
        LSTM_icon = wx.Image(str, wx.BITMAP_TYPE_PNG)
        LSTM_icon.Rescale(self.tool_bar_size[0], self.tool_bar_size[1])
        LSTM_icon = wx.Bitmap(LSTM_icon)

        ################################################################


        self.First_toolbar = wx.ToolBar(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                        wx.TB_HORIZONTAL | wx.NO_BORDER)

        # AddTool (self, toolId, label, bitmap, shortHelp=””, kind=ITEM_NORMAL)
        self.new_tool = self.First_toolbar.AddTool(self.New_model_tool_id, u'New Model', New_icon, shortHelp='New Model')

        self.First_toolbar.AddSeparator()
        self.First_toolbar.AddSeparator()
        self.First_toolbar.AddSeparator()


        self.data_mani_tool = self.First_toolbar.AddTool(self.Data_mani_tool_id, u"Data Manipulation", Data_mani_icon,
                                                         shortHelp='Data Manipulation')
        self.data_visu_tool = self.First_toolbar.AddTool(self.Data_visu_tool_id, u"Data Visualization", Data_visu_icon,
                                                         shortHelp='Data Visualization')

        self.First_toolbar.AddSeparator()
        self.First_toolbar.AddSeparator()
        self.First_toolbar.AddSeparator()

        self.Input_tool = self.First_toolbar.AddTool(self.Input_tool_id, u"Input node", Input_icon,
                                                          shortHelp='Selecting Input tool')
        self.Input_tool.SetToggle(True)

        self.Output_tool = self.First_toolbar.AddTool(self.Output_tool_id, u"Output node", Output_icon,
                                                           shortHelp='Selecting Output tool')
        self.Output_tool.SetToggle(True)



        self.Connection_tool = self.First_toolbar.AddTool(self.Connection_tool_id, u"Connection", Connection_icon,
                                                          shortHelp='Connection')
        self.Connection_tool.SetToggle(True)


        self.Dense_layer_tool = self.First_toolbar.AddTool(self.Dense_layer_tool_id, u"Dense Layer", Dense_icon,
                                                           shortHelp='Dense Layer')
        self.Dense_layer_tool.SetToggle(True)

        self.Pooling_layer_tool = self.First_toolbar.AddTool(self.Pooling_layer_tool_id, u"Pooling Layer", Pooling_icon,
                                                             shortHelp='Pooling Layer')
        self.Pooling_layer_tool.SetToggle(True)

        self.Convolution_layer_tool = self.First_toolbar.AddTool(self.Convolution_layer_tool_id, u"Convolution Layer", Convolution_icon,
                                                                 shortHelp='Convolution Layer')
        self.Convolution_layer_tool.SetToggle(True)


        self.LSTM_layer_tool = self.First_toolbar.AddTool(self.LSTM_layer_tool_id, u"LSTM Layer", LSTM_icon,
                                                          shortHelp='LSTM Layer')
        self.LSTM_layer_tool.SetToggle(True)

        self.First_toolbar.AddSeparator()
        self.First_toolbar.AddSeparator()
        self.First_toolbar.AddSeparator()
        self.First_toolbar.AddSeparator()

        self.Undo_tool = self.First_toolbar.AddTool(self.Undo_tool_id, u"Undo", Undo_icon,
                                                    shortHelp='Undo')

        self.Redo_tool = self.First_toolbar.AddTool(self.Redo_tool_id, u"Redo", Redo_icon,
                                                    shortHelp='Redo')
        self.First_toolbar.AddSeparator()
        self.First_toolbar.AddSeparator()
        self.First_toolbar.AddSeparator()
        self.First_toolbar.AddSeparator()


        self.Train_model_tool = self.First_toolbar.AddTool(self.Train_model_tool_id, u"Train Model", Train_model_icon,
                                                           shortHelp='Train Model')
        self.First_toolbar.Realize()
        return self.First_toolbar

    def Bind_Tool_Event(self):
        self.Bind(wx.EVT_TOOL, self.New_model, id=self.New_model_tool_id)
        self.Bind(wx.EVT_TOOL, self.OnData_mani, id=self.Data_mani_tool_id)
        self.Bind(wx.EVT_TOOL, self.OnData_visu, id=self.Data_visu_tool_id)
        self.Bind(wx.EVT_TOOL, self.Input_switch, id = self.Input_tool_id)
        self.Bind(wx.EVT_TOOL, self.Output_switch, id = self.Output_tool_id)
        self.Bind(wx.EVT_TOOL, self.Add_Connection, id=self.Connection_tool_id)
        self.Bind(wx.EVT_TOOL, self.Add_Dense, id=self.Dense_layer_tool_id)
        self.Bind(wx.EVT_TOOL, self.Add_Pooling, id=self.Pooling_layer_tool_id)
        self.Bind(wx.EVT_TOOL, self.Add_Convolution, id=self.Convolution_layer_tool_id)
        self.Bind(wx.EVT_TOOL, self.Add_LSTM, id=self.LSTM_layer_tool_id)
        self.Bind(wx.EVT_TOOL, self.OnUndo, id=self.Undo_tool_id)
        self.Bind(wx.EVT_TOOL, self.OnRedo, id=self.Redo_tool_id)
        self.Bind(wx.EVT_TOOL, self.Ontrain, id=self.Train_model_tool_id)

    def Bind_Size_Event(self):
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_MAXIMIZE, self.OnMaximize)
        self.Horizontal_sizer_panel.Bind(wx.EVT_LEFT_DOWN, self.Change_horizontal_size_on)
        self.Vertical_sizer_panel.Bind(wx.EVT_LEFT_DOWN, self.Change_vertical_size_on)

    def Unactivate_toggle_tool(self,id = None):
        btn_list = []
        number_of_tool = self.Train_model_tool_id
        if  id == None :
            for i in range(1, number_of_tool + 1):
                self.First_toolbar.ToggleTool(i, False)
        else :
            for i in range(1,number_of_tool+1):
                if (i != id ):
                    btn_list.append(False)
                else:
                    btn_list.append(True)
            for i in range(1,number_of_tool + 1):
                self.First_toolbar.ToggleTool(i, btn_list[i-1])

    def Unactivate_layer_btn(self,id = None):
        for i in range(len(self.Add_btn_list)):
            self.Add_btn_list[i] = False
        if id != None :
            self.Add_btn_list[id] = True
        else :
            pass

    def OnSize(self,evt):
        self.Main_sizer.SetMinSize((-1, self.GetClientSize()[1] - 30 - self.Sub_panel_height))
        self.Canvas.SetMinSize((self.GetClientSize()[0] - self.thick_of_size_panel - self.Layer_tree_width, -1))
        self.Layout()

    def OnMaximize(self,evt):
        self.Main_sizer.SetMinSize((-1, self.GetClientSize()[1] - 30 - self.Sub_panel_height))
        self.Canvas.SetMinSize((self.GetClientSize()[0] - self.thick_of_size_panel - self.Layer_tree_width, -1))
        self.Layout()

    def Change_horizontal_size_on(self,evt):
        self.Change_horizontal = True
        self.CaptureMouse()
        self.x, _ = wx.GetMousePosition()

    def Change_vertical_size_on(self,evt):
        self.Change_vertical = True
        self.CaptureMouse()
        _, self.y = wx.GetMousePosition()

    def OnScrollchanged(self,evt):
        pass

    def OnScrollreleased(self,evt):
        self.Canvas.SetScrollPos(0,evt.GetPosition(),refresh= True)

    def OnKey_Down(self,evt):
        print("yes")
        Keycode = evt.GetKeyCode()
        if (Keycode == wx.WXK_ESCAPE) :
             print("Yes!")

    def OnMouseEvent(self,evt):
        pass

    def MouseLeft_Up(self,evt):
        if (self.Change_vertical == True):
            _, self.lasty = wx.GetMousePosition()
            if (self.GetClientSize()[1] - evt.GetPosition()[1] < 100):
                self.Main_sizer.SetMinSize((-1, self.GetClientSize()[1] - 100))
                self.ReleaseMouse()
                self.Change_vertical = False
                self.Layout()
                self.Main_sizer.SetMinSize((-1, self.Main_sizer.GetSize()[1]))
                self.Sub_panel_height = self.Sub_panel.GetSize()[1]
            else:
                Canvas_height = self.Main_sizer.GetMinSize()[1] + self.lasty - self.y
                self.Main_sizer.SetMinSize((-1, Canvas_height))
                self.Change_vertical = False
                self.ReleaseMouse()
                self.Layout()
                self.Main_sizer.SetMinSize((-1, self.Main_sizer.GetSize()[1]))
                self.Sub_panel_height = self.Sub_panel.GetSize()[1]
        elif (self.Change_horizontal == True):
            self.lastx, _ = wx.GetMousePosition()
            if (self.GetClientSize()[0] - evt.GetPosition()[0] < 100):
                self.Canvas.SetMinSize((self.GetClientSize()[0] - 100, -1))
                self.ReleaseMouse()
                self.Layout()
                self.Change_horizontal = False
                self.Canvas.SetMinSize((self.Canvas.GetSize()[0], -1))
                self.Layer_tree_width = self.Layer_status_base_panel.GetSize()[0]
            else:
                Canvas_width = self.Canvas.GetMinWidth() + self.lastx - self.x
                self.Canvas.SetMinSize((Canvas_width, -1))
                self.Change_horizontal = False
                self.ReleaseMouse()
                self.Layout()
                self.Canvas.SetMinSize((self.Canvas.GetSize()[0], -1))
                self.Layer_tree_width = self.Layer_status_base_panel.GetSize()[0]

    def Dragging_rectangle(self, status_object):
        dc = wx.ClientDC(self)
        pen = wx.Pen(wx.Colour(192, 192, 192))
        dc.SetPen(pen)
        start_position, last_position = status_object.get_mouse_position()
        up_line = (start_position[0], start_position[1], last_position[0], start_position[1])
        right_line = (last_position[0], start_position[1], last_position[0], last_position[1])
        down_line = (last_position[0], last_position[1], start_position[0], last_position[1])
        left_line = (start_position[0], last_position[1], start_position[0], start_position[1])
        line_list = (up_line, right_line, down_line, left_line)
        dc.DrawLineList(line_list)

    def Erasing_dragging_rectangle(self, status_object):

        dc = wx.ClientDC(self)
        pen = wx.Pen(wx.Colour(255, 255, 255))
        dc.SetPen(pen)
        start_position, last_position = status_object.get_mouse_position()
        up_line = (start_position[0], start_position[1], last_position[0], start_position[1])
        right_line = (last_position[0], start_position[1], last_position[0], last_position[1])
        down_line = (last_position[0], last_position[1], start_position[0], last_position[1])
        left_line = (start_position[0], last_position[1], start_position[0], start_position[1])
        line_list = (up_line, right_line, down_line, left_line)
        dc.DrawLineList(line_list)

    #################### Tool event
    def Change_node_color(self,mode = 'All', next_object = None):
        def Change_all_node() :
            for i in self.Canvas._DrawList :
                if i.type == 'Input' :
                    i.SetColor('blue')
                elif i.type == 'Output' :
                    i.SetColor('green')
                else :
                    i.SetColor('black')
        def Change_one_node() :
            if len(self.Previus_selected_buffer) == 1 :
                if (self.Previus_selected_buffer[0].type == 'Input') :
                    self.Previus_selected_buffer.pop().SetColor('blue')
                    next_object.SetColor('red')
                    self.Previus_selected_buffer.append(next_object)
                elif (self.Previus_selected_buffer[0].type == 'Output') :
                    self.Previus_selected_buffer.pop().SetColor('green')
                    next_object.SetColor('red')
                    self.Previus_selected_buffer.append(next_object)
                else :
                    self.Previus_selected_buffer.pop().SetColor('black')
                    next_object.SetColor('red')
                    self.Previus_selected_buffer.append(next_object)
            else :
                self.Previus_selected_buffer.append(next_object)
                for i in self.Canvas._DrawList:
                    if i.id == next_object.id :
                        i.SetColor('red')
                    else :
                        if i.type =='Output':
                            i.SetColor('green')
                        elif i.type == 'Input' :
                            i.SetColor('blue')
                        else :
                            i.SetColor('Black')
        def Connection_mode() :
            next_object.SetColor('red')
            self.Canvas.Draw(Force=True)
            time.sleep(0.2)
            if next_object.type == 'Output' :
                next_object.SetColor('green')
                if self.Previus_selected_buffer[-1].type == 'Input':
                    self.Previus_selected_buffer.pop().SetColor('blue')
                else :
                    self.Previus_selected_buffer.pop().SetColor('black')
            else :
                next_object.SetColor('black')
                if self.Previus_selected_buffer[-1].type == 'Input':
                    self.Previus_selected_buffer.pop().SetColor('blue')
                else :
                    self.Previus_selected_buffer.pop().SetColor('black')
        if mode == 'All' :
            Change_all_node()
        elif mode == 'Link' :
            Connection_mode()
        else :
            Change_one_node()

        self.Canvas.Draw(Force = True)

    def New_model(self,evt):
        self.Unactivate_toggle_tool()
        self.SetCursor(wx.Cursor(wx.CURSOR_ARROW))
        self.Unactivate_layer_btn()
        self.New_model_dialog.Show(True)

    def OnData_mani(self,evt):
        self.Unactivate_toggle_tool()
        self.SetCursor(wx.Cursor(wx.CURSOR_ARROW))
        self.Unactivate_layer_btn()

    def OnData_visu(self,evt):
        self.Unactivate_toggle_tool()
        self.SetCursor(wx.Cursor(wx.CURSOR_ARROW))
        self.Unactivate_layer_btn()

    def Activate_all_layer_ojbect(self, mode=None):
            print("Activating all")
            for i in self.Canvas._DrawList:
                if i.type == 'Node':
                    if (mode == None) :
                        i.Bind(FloatCanvas.EVT_FC_LEFT_DOWN, self.Connection_ready)
                    elif (mode == 'Input'):
                        i.Bind(FloatCanvas.EVT_FC_LEFT_DOWN, self.Input_node_ready)
                    elif (mode == 'Output'):
                        i.Bind(FloatCanvas.EVT_FC_LEFT_DOWN, self.Output_node_ready)
                    else:
                        pass

    def Reactivating_all_layer_object(self):
        print("Reactivation all object")
        self.Canvas.SetCursor(wx.Cursor(wx.CURSOR_ARROW))
        for i in self.Canvas._DrawList:
            i.Bind(FloatCanvas.EVT_FC_LEFT_DOWN, self.Change_layer_status_panel)
            print(i.type)
        self.Change_node_color('All')
        print("connection color changer")

    ########### Connection object ###############
    # Add_connection => Activate_all_layer_object => connection_ready
    def Input_switch(self,evt):
        if self.Add_btn_list[self.Input_btn_id] == False:
            self.Unactivate_layer_btn(self.Input_btn_id)
            self.Unactivate_toggle_tool(self.Input_tool_id)
            self.Add_Layer = True
            self.Canvas.SetCursor(wx.Cursor(wx.CURSOR_HAND))
            self.Activate_all_layer_ojbect(mode = 'Input')
            self.Change_node_color(mode = 'All')

        elif self.Add_btn_list[self.Input_btn_id] == True:
            self.Add_btn_list[self.Input_btn_id] = False
            self.Canvas.SetCursor(wx.Cursor(wx.CURSOR_ARROW))
            self.Unactivate_toggle_tool()
            self.Unactivate_layer_btn()
            self.Reactivating_all_layer_object()
            self.Change_node_color(mode = 'All')
            self.Add_Layer = False

    def Input_node_ready(self,evt):
        evt.type = 'Input'
        print("Input node on")
        if len(self.Input_node_buffer) == 1 :
            obj = self.Input_node_buffer.pop()
            obj.type = None
            obj.SetColor('Black')
        self.Input_node_buffer.append(evt)
        self.Change_node_color(mode = 'One',next_object=evt)
        self.Reactivating_all_layer_object()
        self.Unactivate_layer_btn()
        self.Unactivate_toggle_tool()

    def Output_switch(self,evt):
        if self.Add_btn_list[self.Output_btn_id] == False:
            self.Unactivate_layer_btn(self.Output_btn_id)
            self.Unactivate_toggle_tool(self.Output_tool_id)
            self.Add_Layer = True
            self.Canvas.SetCursor(wx.Cursor(wx.CURSOR_HAND))
            self.Activate_all_layer_ojbect(mode = 'Output')
            self.Change_node_color('All')

        elif self.Add_btn_list[self.Output_btn_id] == True:
            self.Add_btn_list[self.Output_btn_id] = False
            self.Canvas.SetCursor(wx.Cursor(wx.CURSOR_ARROW))
            self.Unactivate_toggle_tool()
            self.Reactivating_all_layer_object()
            self.Change_node_color('All')
            self.Add_Layer = False

    def Output_node_ready(self,evt):
        evt.type = 'Output'
        if len(self.Output_node_buffer) == 1 :
            obj = self.Output_node_buffer.pop()
            obj.type = None
            obj.SetColor('Black')
        self.Output_node_buffer.append(evt)
        self.Change_node_color(mode='One', next_object=evt)
        self.Reactivating_all_layer_object()
        self.Unactivate_layer_btn()
        self.Unactivate_toggle_tool()

    def Add_Connection(self,evt) :
        if self.Add_btn_list[self.Connection_btn_id] == False:
            self.Unactivate_layer_btn(self.Connection_btn_id)
            self.Unactivate_toggle_tool(self.Connection_tool_id)
            self.Canvas.SetCursor(wx.Cursor(wx.CURSOR_HAND))
            self.Activate_all_layer_ojbect()
            self.Change_node_color('All')
            try :
                self.Previus_selected_buffer.pop()
            except :
                pass
            self.Add_Layer = True

        elif self.Add_btn_list[self.Connection_btn_id] == True :
            self.Unactivate_layer_btn()
            self.Canvas.SetCursor(wx.Cursor(wx.CURSOR_ARROW))
            self.Unactivate_toggle_tool()
            self.Reactivating_all_layer_object()
            self.Change_node_color('All')
            self.Add_Layer = False

    def Connection_ready(self,evt):
        def Initializing_all_setting() :
            try:
                self.Previus_selected_buffer.pop()
            except :
                print("Something happend")
                pass
            print("initial happend")
            self.Change_node_color('All')
            self.Reactivating_all_layer_object()
            self.Unactivate_toggle_tool()
            self.Unactivate_layer_btn()

        if len(self.Previus_selected_buffer) == 1:
            if evt.type == 'Input' :
                print("you should not connect to input layer")
                Initializing_all_setting()
            else :
                if (self.Find_object(evt.id).previus_id != None) :
                    Initializing_all_setting()
                else :
                    self.Creating_Link_object(self.Previus_selected_buffer[-1],evt)
                    self.Change_node_color(mode='Link', next_object=evt)
                    print("connection completed")
        else :
            if evt.type == 'Output' :
                print("you Can't connect From Output layer")
                Initializing_all_setting()
            else :
                if (evt.next_id != None) :
                    Initializing_all_setting()
                else :

                    self.Previus_selected_buffer.append(evt)
                    evt.SetColor("red")
                    self.Canvas.Draw(Force=True)

    def Inserting_data_to_object(self, obj , name ,id, type = 'Node', position = None, previus_id = None, next_id = None):
        obj.type = type
        obj.name = name
        obj.id = id
        obj.position = position
        obj.previus_id = previus_id
        obj.next_id = next_id

    def Disposition_after_inserting_data_to_object(self, obj, type = 'Node'):
        print("Disposition happened")
        if type == 'Node' :
            self.Canvas.Unbind(wx.EVT_LEFT_DOWN)
        else :
            pass
        self.Canvas.SetCursor(wx.Cursor(wx.CURSOR_ARROW))
        self.Canvas.AddObject(obj)
        obj.Bind(FloatCanvas.EVT_FC_LEFT_DOWN,self.Change_layer_status_panel)

        self.Reactivating_all_layer_object()
        self.Unactivate_layer_btn()
        self.Unactivate_toggle_tool()

    def Creating_Link_object(self,first_object,last_object):
        def Creating_object () :
            First_point = first_object.position
            Last_point = last_object.position
            x_vector = Last_point[0] - First_point[0]
            y_vector = Last_point[1] - First_point[1]
            diameter = 30
            Length = np.linalg.norm([x_vector, y_vector]) - diameter
            Direction = np.arctan2(y_vector, x_vector) * 180 / np.pi
            Direction2 = 90 - Direction
            Start_point = (int(First_point[0] + diameter / 2 * np.cos(np.deg2rad(Direction))),
                           int(First_point[1] + diameter / 2 * np.sin(np.deg2rad(Direction))))
            Connection_object = FloatCanvas.Arrow(Start_point, Length=int(Length), Direction=Direction2, LineWidth=3)
            Connection_object.HitLineWidth = 6
            return Connection_object
        Connection_object = Creating_object()
        self.id_count += 1
        self.Inserting_data_to_object(Connection_object,'Link',type = 'Link',id = self.id_count,
                                      previus_id=first_object.id, next_id = last_object.id)
        first_object.next_id = Connection_object.id
        last_object.previus_id = Connection_object.id
        self.Disposition_after_inserting_data_to_object(Connection_object,type = 'Link')
        self.Canvas.Draw(Force = True)
        print("link created")
        self.Undo_list.append('Create')

    ############ Add_Dense #######################
    def Add_Dense(self,evt) :
        if self.Add_btn_list[self.Dense_layer_btn_id] == False:
            self.Unactivate_layer_btn(self.Dense_layer_btn_id)
            self.Unactivate_toggle_tool(self.Dense_layer_tool_id)
            self.Add_Layer = True
            self.Canvas.SetCursor(wx.Cursor(wx.CURSOR_CROSS))
            self.Canvas.Bind(wx.EVT_LEFT_DOWN,self.Pointing_Dense_position)

        elif self.Add_btn_list[self.Dense_layer_btn_id] == True :
            self.Add_btn_list[self.Dense_layer_btn_id] = False
            self.Canvas.SetCursor(wx.Cursor(wx.CURSOR_ARROW))
            self.Canvas.Unbind(wx.EVT_LEFT_DOWN)
            self.Unactivate_toggle_tool()
            self.Add_Layer = False
        pass

    def Pointing_Dense_position(self,evt):
        X,Y = evt.GetPosition()
        width,height = self.Canvas.GetClientSize()
        x,y = (X-width/2,height/2-Y)
        Text = FloatCanvas.Text('D',(x,y), Weight = wx.BOLD,Position ='cc')
        Dense_object = FloatCanvas.Circle((x,y), 30, LineWidth=3)
        Dense_object = FloatCanvas.Group([Dense_object,Text])
        self.id_count += 1
        self.Inserting_data_to_object(Dense_object,name = 'Dense',position = (x,y),id = self.id_count)
        self.Disposition_after_inserting_data_to_object(Dense_object)
        self.Canvas.Draw(Force=True)
        self.Undo_list.append("Create")
    ############# Add Pooling ##############
    def Add_Pooling(self,evt):
        if self.Add_btn_list[self.Pooling_layer_btn_id] == False:
            self.Unactivate_layer_btn(self.Pooling_layer_btn_id)
            self.Unactivate_toggle_tool(self.Pooling_layer_tool_id)
            self.Add_Layer = True
            self.Canvas.SetCursor(wx.Cursor(wx.CURSOR_CROSS))
            self.Canvas.Bind(wx.EVT_LEFT_DOWN, self.Pointing_Pooling_position)

        elif self.Add_btn_list[self.Pooling_layer_btn_id] == True:
            self.Add_btn_list[self.Pooling_layer_btn_id] = False
            self.Canvas.SetCursor(wx.Cursor(wx.CURSOR_ARROW))
            self.Canvas.Unbind(wx.EVT_LEFT_DOWN)
            self.Unactivate_toggle_tool()
            self.Add_Layer = False

    def Pointing_Pooling_position(self,evt):
        X,Y = evt.GetPosition()
        width,height = self.Canvas.GetClientSize()
        x,y = (X-width/2,height/2-Y)
        Text = FloatCanvas.Text('P',(x,y), Weight = wx.BOLD,Position ='cc')
        Pooling_object = FloatCanvas.Circle((x,y), 30, LineWidth=3)
        Pooling_object = FloatCanvas.Group([Text,Pooling_object])
        self.id_count += 1
        self.Inserting_data_to_object(Pooling_object,name = 'Pooling',id = self.id_count,position = (x,y))
        #Dense_object.Bind(wx.EVT_ENTER_WINDOW, self.Show_layer_data)
        self.Disposition_after_inserting_data_to_object(Pooling_object)
        self.Canvas.Draw(Force=True)
        self.Undo_list.append('Create')
        self.Undo_redo_index += 1
    ############# Add Convolutioin

    def Add_Convolution(self,evt):
        if self.Add_btn_list[self.Convolution_layer_btn_id] == False:
            self.Unactivate_layer_btn(self.Convolution_layer_btn_id)
            self.Unactivate_toggle_tool(self.Convolution_layer_tool_id)
            self.Add_Layer = True
            self.Canvas.SetCursor(wx.Cursor(wx.CURSOR_CROSS))
            self.Canvas.Bind(wx.EVT_LEFT_DOWN, self.Pointing_Convolution_position)

        elif self.Add_btn_list[self.Convolution_layer_btn_id] == True:
            self.Add_btn_list[self.Convolution_layer_btn_id] = False
            self.Canvas.SetCursor(wx.Cursor(wx.CURSOR_ARROW))
            self.Canvas.Unbind(wx.EVT_LEFT_DOWN)
            self.Add_Layer = False
            self.Unactivate_toggle_tool()

    def Pointing_Convolution_position(self,evt):
        X,Y = evt.GetPosition()
        width,height = self.Canvas.GetClientSize()
        x,y = (X-width/2,height/2-Y)
        Text = FloatCanvas.Text('C',(x,y), Weight = wx.BOLD,Position ='cc')
        Convolution_object = FloatCanvas.Circle((x,y), 30, LineWidth=3)
        Convolution_object = FloatCanvas.Group([Text,Convolution_object])
        self.id_count += 1
        self.Inserting_data_to_object(Convolution_object,name = 'Convolution',id = self.id_count,position = (x,y))
        self.Disposition_after_inserting_data_to_object(Convolution_object)
        self.Canvas.Draw(Force=True)
        self.Undo_list.append("Create")
        self.Undo_redo_index += 1

    def Add_LSTM(self,evt):
        if self.Add_btn_list[self.LSTM_layer_btn_id] == False:
            self.Unactivate_layer_btn(self.LSTM_layer_btn_id)
            self.Unactivate_toggle_tool(self.LSTM_layer_tool_id)
            self.Add_Layer = True
            self.Canvas.SetCursor(wx.Cursor(wx.CURSOR_CROSS))
            self.Canvas.Bind(wx.EVT_LEFT_DOWN, self.Pointing_LSTM_position)

        elif self.Add_btn_list[self.LSTM_layer_btn_id] == True:
            self.Add_btn_list[self.LSTM_layer_btn_id] = False
            self.Canvas.SetCursor(wx.Cursor(wx.CURSOR_ARROW))
            self.Add_Layer = False
            self.Unactivate_toggle_tool()
            self.Canvas.Unbind(wx.EVT_LEFT_DOWN)

    def Pointing_LSTM_position(self,evt):
        X,Y = evt.GetPosition()
        width,height = self.Canvas.GetClientSize()
        x,y = (X-width/2,height/2-Y)
        Text = FloatCanvas.Text('L',(x,y), Weight = wx.BOLD,Position ='cc')
        LSTM_object = FloatCanvas.Circle((x,y), 30, LineWidth=3)
        LSTM_object = FloatCanvas.Group([Text,LSTM_object])
        self.id_count += 1
        self.Inserting_data_to_object(LSTM_object,name = 'LSTM',id = self.id_count,position = (x,y))
        self.Disposition_after_inserting_data_to_object(LSTM_object)
        self.Canvas.Draw(Force=True)
        self.Undo_list.append("Create")
        self.Undo_redo_index += 1
    ############ Utility #################

    def Change_layer_status_panel(self,evt):
        print("change layer_status panel on")
        self.Change_node_color(mode = 'one',next_object=evt)
        self.Bind(wx.WXK_DELETE,self.Delete_object)
        def Hide_all_panel(self) :
            self.Connection_status_panel.Hide()
            self.LSTM_status_panel.Hide()
            self.Pooling_status_panel.Hide()
            self.Dense_status_panel.Hide()
            self.Convolution_status_panel.Hide()

        if evt.name == "Dense":
            Hide_all_panel(self)
            self.Dense_status_panel.id = evt.id
            self.Dense_status_panel.Show()
            self.Layout()
        elif evt.name == "Convolution" :
            Hide_all_panel(self)
            self.Convolution_status_panel.id = evt.id
            self.Convolution_status_panel.Show()
            self.Layout()
        elif evt.name == "Pooling" :
            Hide_all_panel(self)
            self.Pooling_status_panel.id = evt.id
            self.Pooling_status_panel.Show()
            self.Layout()
        elif evt.name == 'LSTM' :
            Hide_all_panel(self)
            self.LSTM_status_panel.id = evt.id
            self.LSTM_status_panel.Show()
            self.Layout()
        else :
            Hide_all_panel(self)
            self.Connection_status_panel.id = evt.id
            self.Connection_status_panel.Show()
            self.Layout()
        print("change_layer_status_panel triggered")

    def Find_object(self, object_id,List = None,id_type = 'id'):
        if List == None :
            List = self.Canvas._DrawList
        if  id_type == 'id' :
            for i in List:
                if (i.id == object_id):
                    return i
                else:
                    pass
        elif id_type == 'previus_id' :
            for i in List :
                if (i.previus_id == object_id) :
                    return i
                else :
                    pass
        else :
            for i in List:
                if(i.next_id == object_id) :
                    return i
                else :
                    pass

    def Delete_object(self,evt):
        self.Unactivate_toggle_tool()
        self.SetCursor(wx.Cursor(wx.CURSOR_ARROW))
        self.Unactivate_layer_btn()
        self.Change_node_color('All')
        if (evt.type == 'Link') :
            obj_idx = self.Canvas._DrawList.index(evt)
            self.Layer_object_buffer.append(self.Canvas._DrawList.pop(obj_idx))
            self.Layer_object_buffer[-1].id
            self.Find_object(self.Layer_object_buffer[-1].id,List = self.Canvas._DrawList, id_type = 'next_id').next_id = None
            self.Find_object(self.Layer_object_buffer[-1].id, List=self.Canvas._DrawList,
                             id_type='previus_id').previus_id = None
        else :
            if (evt.previus_id != None) :
                if (evt.next_id != None) :
                    next_link_idx = self.Canvas._DrawList.index(self.Find_object(evt.next_id))
                    previus_link_idx = self.Canvas._DrawList.index(self.Find_object(evt.previus_id))
                    node_idx = self.Canvas._DrawList.index(self.Find_object(evt.id))
                    self.Find_object(self.Canvas._DrawList.pop(next_link_idx).id,List = self.Canvas._DrawList,id_type = 'previus_id').previus_id = None
                    self.Find_object(self.Canvas._DrawList.pop(previus_link_idx).id,List = self.Canvas._DrawList,id_type = 'next_id').next_id = None
                    self.Layer_object_buffer.append(self.Canvas._Drawlist.pop(node_idx))
                else :
                    previus_link_idx = self.Canvas._DrawList.index(self.Find_object(evt.previus_id))
                    node_idx = self.Canvas._DrawList.index(self.Find_object(evt.id))
                    self.Find_object(self.Canvas._DrawList.pop(previus_link_idx).id,List = self.Canvas._DrawList,id_type = 'next_id').next_id = None
                    self.Layer_object_buffer.append(self.Canvas._Drawlist.pop(node_idx))
            elif (evt.next_id != None) :
                next_link_idx = self.Canvas._DrawList.index(self.Find_object(evt.next_id))
                node_idx = self.Canvas._DrawList.index(self.Find_object(evt.id))
                self.Find_object(self.Canvas._DrawList.pop(next_link_idx).id, List=self.Canvas._DrawList,
                                 id_type='previus_id').previus_id = None
                self.Layer_object_buffer.append(self.Canvas._Drawlist.pop(node_idx))
            else :
                node_idx = self.Canvas._DrawList.index(self.Find_object(evt.id))
                self.Layer_object_buffer.append(self.Canvas._Drawlist.pop(node_idx))
        self.Undo_list.append("Delete")
        self.Canvas.Draw(Force = True)

    def OnUndo(self,evt):
        self.Unactivate_toggle_tool()
        self.SetCursor(wx.Cursor(wx.CURSOR_ARROW))
        self.Unactivate_layer_btn()
        self.Reactivating_all_layer_object()
        self.Change_node_color('All')
        if len(self.Undo_list) != 0:
            if (self.Undo_list[-1] == 'Create'):
                try :
                    if (self.Canvas._DrawList[-1].type == 'Link') :
                        self.Layer_object_buffer.append(self.Canvas._DrawList.pop())
                        self.Find_object(self.Layer_object_buffer[-1],List = self.Canvas._DrawList,id_type = 'previus_id').previus_id = None
                        self.Find_object(self.Layer_object_buffer[-1],List = self.Canvas._DrawList,id_type = 'next_id').next_id = None
                    else :
                        self.Layer_object_buffer.append(self.Canvas._DrawList.pop())

                except :
                    pass
                self.Redo_list.append(self.Undo_list.pop())
            else :
                if (self.Layer_object_buffer[-1].type =='Link') :
                    self.Canvas._DrawList.append(self.Layer_object_buffer.pop())
                    self.Find_object(self.Canvas._DrawList[-1].next_id,self.Canvas._DrawList).previus_id = self.Canvas._DrawList[-1].id
                    self.Find_object(self.Canvas._DrawList[-1].previus_id,self.Canvas._DrawList).next_id = self.Canvas._DrawList[-1].id
                else :
                    self.Canvas._DrawList.append(self.Layer_object_buffer.pop())
                    self.Canvas._DrawList[-1].next_id = None
                    self.Canvas._DrawList[-1].previus_id = None
                self.Redo_list.append(self.Undo_list.pop())
        print(self.Undo_list)
        print(self.Redo_list)
        print(self.Canvas._DrawList)
        print(self.Layer_object_buffer)
        self.Canvas.Draw(Force = True)

    def OnRedo(self,evt):
        self.Unactivate_toggle_tool()
        self.SetCursor(wx.Cursor(wx.CURSOR_ARROW))
        self.Unactivate_layer_btn()
        self.Reactivating_all_layer_object()
        self.Change_node_color('All')
        if (len(self.Redo_list) != 0):
            if (self.Redo_list[-1] == 'Create'):
                if (self.Layer_object_buffer[-1].type == 'Link'):
                    self.Canvas._DrawList.append(self.Layer_object_buffer.pop())
                    self.Find_object(self.Canvas._DrawList[-1].next_id, List=self.Canvas._DrawList).previus_id = self.Canvas._DrawList[-1].id
                    self.Find_object(self.Canvas._DrawList[-1].previus_id, List=self.Canvas._DrawList).next_id = self.Canvas._DrawList[-1].id
                else:
                    self.Canvas._DrawList.append(self.Layer_object_buffer.pop())
                self.Undo_list.append(self.Redo_list.pop())
            else:
                if (self.Canvas._DrawList[-1].type == 'Link'):
                    self.Layer_object_buffer.append(self.Canvas._DrawList.pop())
                    self.Find_object(self.Layer_object_buffer[-1], List=self.Canvas._DrawList,
                                     id_type='previus_id').previus_id = None
                    self.Find_object(self.Layer_object_buffer[-1], List=self.Canvas._DrawList,
                                     id_type='next_id').next_id = None
                else:
                    self.Layer_object_buffer.append(self.Canvas._DrawList.pop())
                self.Undo_list.append(self.Redo_list.pop())
        print(self.Undo_list)
        print(self.Redo_list)
        print(self.Canvas._DrawList)
        print(self.Layer_object_buffer)
        self.Canvas.Draw(Force=True)

    def Ontrain(self,evt):
        self.Unactivate_toggle_tool()
        self.SetCursor(wx.Cursor(wx.CURSOR_ARROW))
        self.Unactivate_layer_btn()

    def __del__(self):
        pass

class New_model_dialog(New_Model_Dialog) :
    def __init__(self,parent):
        New_Model_Dialog.__init__(self,parent)
    def Yes_btn_On(self, evt):
        Start_Frame.Canvas._DrawList.clear()
        Start_Frame.Layer_object_list.clear()
        Start_Frame.Connection_list.clear()
        Start_Frame.Previus_selected_buffer.clear()
        Start_Frame.Layer_object_buffer.clear()
        Start_Frame.Input_node_buffer.clear()
        Start_Frame.Output_node_buffer.clear()
        Start_Frame.Canvas.Draw(Force = True)
        self.Close()
    def No_btn_On(self, evt):
        self.Close()

class Connection_layer_panel(Connection_panel) :
    def __init__(self,parent):
        Connection_panel.__init__(self,parent)

    def Insert_data_to_object(self,obj):
        obj.Flatten = self.Flatten
        obj.Dropout = self.Dropout

    def Adapt(self,evt):
        self.Flatten = bool(self.Flatten_cb.GetValue())
        if (self.Dropout_tctrl.GetValue() =='None'):
            self.Dropout = False
        else :
            self.Dropout = float(self.Dropout_tctrl.GetValue())
        self.Insert_data_to_object(Start_Frame.Find_object(self.id))
        print(Start_Frame.Find_object(self.id).Dropout)

class Dense_layer_panel(Dense_panel) :
    def __init__(self,parent):
        Dense_panel.__init__(self,parent)

    def Insert_data_to_object(self,obj):
        obj.Units = self.Units
        obj.Dropout = self.Dropout
        obj.Weight_initializer = self.Weight_initializer
        obj.Bias_initializer = self.Bias_initializer
        obj.Activation = self.Activation
        obj.Regularization = self.Regularization

    def Adapt(self,evt):
        self.Units = int(self.Unit_tctrl.GetValue())
        self.Dropout = float(self.Dropout_tcrl.GetValue())
        self.Weight_initializer = self.Weight_cb.GetValue()
        self.Bias_initializer = self.Bias_cb.GetValue()
        self.Activation = self.Activation_cb.GetValue()
        self.Regularization = self.Regularization_cb.GetValue()
        self.Insert_data_to_object(Start_Frame.Find_object(self.id))
        print(Start_Frame.Find_object(self.id).Regularization)

class Pooling_layer_panel(Pooling_panel) :
    def __init__(self,parent):
        Pooling_panel.__init__(self,parent)

    def Insert_data_to_object(self, obj):
        obj.Pooling_size  = self.Pooling_size
        obj.Strides = self.Strides
        obj.Padding = self.Padding


    def Adapt(self, evt):
        self.Pooling_size = int(self.size_tctrl.GetValue())
        self.Strides = int(self.Stride_tctrl.GetValue())
        self.Padding = self.Padding_cb.GetValue()
        self.Insert_data_to_object(Start_Frame.Find_object(self.id))
        print(Start_Frame.Find_object(self.id).Padding)

class Convolution_layer_panel(Convolution_panel) :
    def __init__(self,parent):
        Convolution_panel.__init__(self,parent)

    def Insert_data_to_object(self, obj):
        obj.Map_number = self.Map_number
        obj.Window_size = self.Window_size
        obj.Strides = self.Strides
        obj.Activation = self.Activation

    def Adapt(self, evt):
        self.Map_number = int(self.Map_tctrl.GetValue())
        self.Window_size = int(self.Window_tctrl.GetValue())
        self.Strides = int(self.Stride_tctrl.GetValue())
        self.Activation = self.Activation_cb.GetValue()
        self.Insert_data_to_object(Start_Frame.Find_object(self.id))
        print(Start_Frame.Find_object(self.id).Activation)

class LSTM_layer_panel(LSTM_panel) :
    def __init__(self,parent):
        LSTM_panel.__init__(self,parent)
    def Get_value(self):
        return (self.Units,self.Recurrent_intializer,self.Recurrent_activation,self.Weight_initializer,
                self.Bias_initializer,self.Activation,self.Regularization)

    def Insert_data_to_object(self, obj):
        obj.Units = self.Units
        obj.Recurrent_initializer = self.Recurrent_intializer
        obj.Recurrent_activation = self.Recurrent_activation
        obj.Weight_initializer = self.Weight_initializer
        obj.Bias_initializer = self.Bias_initializer
        obj.Activation = self.Activation
        obj.Regularization = self.Regularization

    def Adapt(self, evt):
        self.Units = int(self.Unit_tctrl.GetValue())
        self.Recurrent_intializer = self.Recurrent_init_cb.GetValue()
        self.Recurrent_activation = self.Recurrent_acti_cb.GetValue()
        self.Weight_initializer = self.Weight_cb.GetValue()
        self.Bias_initializer = self.Bias_cb.GetValue()
        self.Activation = self.Activation_cb.GetValue()
        self.Regularization = self.Regularization_cb.GetValue()
        self.Insert_data_to_object(Start_Frame.Find_object(self.id))
        print(Start_Frame.Find_object(self.id).Regularization)
"""
app = wx.App()

Start_Frame = StartFrame(None)
Start_Frame.Show(True)
app.MainLoop()
"""
