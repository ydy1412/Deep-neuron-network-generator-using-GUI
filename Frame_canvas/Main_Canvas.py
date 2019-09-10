import wx
import wx.xrc
import numpy as np
import os
import Layer_dialog
import wx.lib.agw.shapedbutton as SB
from Layer_object import layer_context
from wx.lib.floatcanvas import  FloatCanvas, Resources,GUIMode
Directory = os.getcwd()

class myCanvas(FloatCanvas.FloatCanvas):
    def __init__(self, parent,id = wx.ID_ANY,size = wx.DefaultSize,**kwargs):
        FloatCanvas.FloatCanvas.__init__(self,parent,**kwargs)
        # self.dc_list = ['dense','pooling','convolution','flatten','dropout','Input','Connection',output
        self.InitAll()
        self.Test_object()
        self.Modes = [("Pointer", GUIMode.GUIMouse(), Resources.getPointerBitmap()),
                      ("Zoom In", GUIMode.GUIZoomIn(), Resources.getMagPlusBitmap()),
                      ("Zoom Out", GUIMode.GUIZoomOut(), Resources.getMagMinusBitmap()),
                      ("Pan", GUIMode.GUIMove(), Resources.getHandBitmap()),
                      ]
        self.SetMode(self.Modes[0][1])

    def Test_object(self):
        print("test object")
        self.RotArrow = self.AddArrow((16, 4), 80, Direction=0, LineWidth=3, LineColor="Green", ArrowHeadAngle=30)
        self.RotArrow.HitLineWidth = 6
        self.RotArrow.Bind(FloatCanvas.EVT_FC_LEFT_DOWN, self.Trigger_Pooling_layer_dialog)

        self.Dense_object = FloatCanvas.Circle((10,10), 20, LineWidth=3, FillColor='red')
        self.AddObject(self.Dense_object)
        self.Dense_object.Bind(FloatCanvas.EVT_FC_LEFT_DOWN, self.Trigger_Pooling_layer_dialog)
        #Dense_object.Bind(FloatCanvas.EVT_ENTER_WINDOW, self.Show_layer_data)
        self.Draw(Force=True)

    def Trigger_Pooling_layer_dialog(self, evt):
        print("yes")


    def Dragging_rectangle(self,status_object) :
        dc = wx.ClientDC(self)
        pen = wx.Pen(wx.Colour(192, 192, 192))
        dc.SetPen(pen)
        start_position,last_position = status_object.get_mouse_position()
        up_line = (start_position[0],start_position[1],last_position[0],start_position[1])
        right_line = (last_position[0],start_position[1],last_position[0],last_position[1])
        down_line = (last_position[0],last_position[1],start_position[0],last_position[1])
        left_line = (start_position[0],last_position[1],start_position[0],start_position[1])
        line_list = (up_line,right_line,down_line,left_line)
        dc.DrawLineList(line_list)

    def Erasing_dragging_rectangle(self,status_object) :

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

    def Draw_Input_pipe_layer(self,start_position,last_position,id) :
        pass
    def Draw_Output_pipe_layer(self,start_position,last_position,id) :
        pass
    def Draw_Connection(self,start_position,last_position,id) :
        pass

    def Draw_Denselayer(self,status_object):
        # 'Dense' : [[int'units',str'init',str'activation', str 'regularization'
        start_position, last_position = status_object.get_mouse_position()
        object_id = status_object.get_layer_id()
        Dense_object = FloatCanvas.Circle(start_position,20,LineWidth=3,FillColor = 'red')
        Dense_object.id = object_id
        self.AddObject(Dense_object)
        Dense_object.Bind(FloatCanvas.EVT_FC_LEFT_DOWN,self.Trigger_Dense_layer_dialog)
        Dense_object.Bind(wx.EVT_ENTER_WINDOW,self.Show_layer_data)
        self.Draw(Force = True)

    def Trigger_Dense_layer_dialog(self,evt):
        pass

    def Draw_Poolinglayer(self,status_object) :
        start_position, last_position = status_object.get_mouse_position()
        object_id = status_object.get_layer_id()
        Dense_object = FloatCanvas.Circle(start_position, 20, LineWidth=3, FillColor='green')
        Dense_object.id = object_id
        self.AddObject(Dense_object)
        Dense_object.Bind(FloatCanvas.EVT_FC_LEFT_DOWN, self.Trigger_Pooling_layer_dialog)
        Dense_object.Bind(wx.EVT_ENTER_WINDOW, self.Show_layer_data)
        self.Draw(Force=True)

    #def Trigger_Pooling_layer_dialog(self,evt):
    #    print("yes")



    def Draw_Convolutionlayer(self,status_object) :
        start_position, last_position = status_object.get_mouse_position()
        object_id = status_object.get_layer_id()
        Dense_object = FloatCanvas.Circle(start_position, 20, LineWidth=3, FillColor='blue')
        Dense_object.id = object_id
        self.AddObject(Dense_object)
        Dense_object.Bind(FloatCanvas.EVT_FC_LEFT_DOWN, self.Trigger_Convolution_layer_dialog)
        Dense_object.Bind(wx.EVT_ENTER_WINDOW, self.Show_layer_data)
        self.Draw(Force=True)

    def Trigger_Convolution_layer_dialog(self,evt):
        pass

    def Draw_LSTMlayer(self,status_object) :
        start_position, last_position = status_object.get_mouse_position()
        object_id = status_object.get_layer_id()
        Dense_object = FloatCanvas.Circle(start_position, 20, LineWidth=3, FillColor='yellow')
        Dense_object.id = object_id
        self.AddObject(Dense_object)
        Dense_object.Bind(FloatCanvas.EVT_FC_LEFT_DOWN, self.Trigger_LSTM_layer_dialog)
        Dense_object.Bind(wx.EVT_ENTER_WINDOW, self.Show_layer_data)
        self.Draw(Force=True)

    def Trigger_LSTM_layer_dialog(self,evt):
        pass

    def Show_layer_data(self,evt):
        pass

