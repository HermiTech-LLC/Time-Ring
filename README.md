
# Ring Laser Experiment Simulator

## Overview
This enhanced version of the Ring Laser Experiment Simulator incorporates a graphical user interface (GUI) using wxPython, providing interactive controls to adjust the parameters of the experiment. It simulates the gravitational effects on a ring laser, such as frame dragging and time dilation, and visualizes these effects in three dimensions.

![Art Image](https://github.com/LoQiseaking69/TimeRing-/blob/main/IMG_8634.jpeg) 

## Requirements
- Python 3.x
- numpy
- matplotlib
- wxPython

## Usage
1. Clone or download the repository.
2. Install required dependencies:
   ```
   pip install numpy matplotlib wxPython
   ```
3. Run the script:
   ```
   python TRL.py
   ```

## Components
### RingLaserExperiment Class
- `__init__(laser_power, laser_radius)`: Initializes experiment with specified laser power and radius.
- `simulate_experiment()`: Calculates and returns coordinates and time dilation based on current experiment settings.

### MainFrame Class (GUI Component)
- Initializes the application window and sliders for dynamic interaction.
- `update_experiment()`: Updates the experiment parameters based on slider input and re-runs the simulation.
- `update_plot()`: Visualizes the results in a 3D scatter plot using matplotlib.

## Example Code
```python
# Main execution block to initialize the GUI
if __name__ == "__main__":
    app = wx.App(False)
    frame = MainFrame()
    frame.Show()
    app.MainLoop()
```

## License
This project is licensed under the GNU General Public License v3.0 - see the LICENSE file for details.