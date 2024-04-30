import wx
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from mpl_toolkits.mplot3d import Axes3D

class RingLaserExperiment:
    def __init__(self, laser_power, laser_radius):
        self.laser_power = laser_power
        self.laser_radius = laser_radius
        self.c = 299792458
        self.G = 6.67430e-11

    def simulate_experiment(self):
        theta = np.linspace(0, 2 * np.pi, 360)
        x = self.laser_radius * np.cos(theta)
        y = self.laser_radius * np.sin(theta)
        z = np.zeros(360)
        gravitational_effect = self.G * self.laser_power / (self.laser_radius * self.c ** 2)
        time_dilation = np.sqrt(1 - 2 * gravitational_effect / (self.c ** 2))
        return x, y, z, time_dilation

class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="Ring Laser Experiment", size=(800, 600))
        self.experiment = RingLaserExperiment(laser_power=1e-3, laser_radius=1e9)
        
        self.panel = wx.Panel(self)
        self.fig, self.ax = plt.subplots(subplot_kw={'projection': '3d'})
        self.canvas = FigureCanvas(self.panel, -1, self.fig)
        
        self.power_slider = wx.Slider(self.panel, value=1, minValue=1, maxValue=10, pos=(20, 20), size=(250, -1))
        self.radius_slider = wx.Slider(self.panel, value=1000, minValue=100, maxValue=5000, pos=(20, 70), size=(250, -1))
        
        self.power_slider.Bind(wx.EVT_SCROLL, self.update_experiment)
        self.radius_slider.Bind(wx.EVT_SCROLL, self.update_experiment)
        
        self.update_plot()

    def update_experiment(self, event):
        power = self.power_slider.GetValue() * 1e-4
        radius = self.radius_slider.GetValue() * 1e7
        self.experiment.laser_power = power
        self.experiment.laser_radius = radius
        self.update_plot()

    def update_plot(self):
        x, y, z, time_dilation = self.experiment.simulate_experiment()
        self.ax.clear()
        sc = self.ax.scatter(x, y, z, c=time_dilation, cmap='viridis')
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.set_zlabel('Z')
        self.fig.colorbar(sc, ax=self.ax, label='Time Dilation Factor')
        self.canvas.draw()

if __name__ == "__main__":
    app = wx.App(False)
    frame = MainFrame()
    frame.Show()
    app.MainLoop()
