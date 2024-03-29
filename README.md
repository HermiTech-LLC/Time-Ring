# Ring Laser Time Viewer

## Overview
The Ring Laser Time Viewer is a Python script inspired by the work of Dr. Ron Mallat. It simulates a ring laser scanning experiment with gravitational time dilation effects. The script calculates adjusted pulse durations, generates points for visualization, simulates the experiment, and visualizes the results using matplotlib.

![art](https://github.com/LoQiseaking69/TimeRing-/blob/main/IMG_8634.jpeg) 

## Requirements
- Python 3.x
- numpy
- matplotlib

## Usage
1. Clone or download the repository.
2. Install the required dependencies: `pip install numpy matplotlib`
3. Run the script: `python TRL.py`

## Description
The script comprises the following components:

- **RingLaserTimeViewer**: A class that simulates the ring laser experiment and visualizes the results.
  - `__init__()`: Initializes the parameters of the experiment.
  - `calculate_adjusted_pulse_duration()`: Calculates adjusted pulse durations considering gravitational effects.
  - `generate_points()`: Generates points for visualization.
  - `simulate_experiment()`: Simulates the ring laser scanning experiment.
  - `visualize_point_cloud()`: Visualizes the generated point cloud.

- **MassObject**: A class representing massive objects in the scene.
  - `__init__()`: Initializes the mass and position of the object.

- **Scene**: A class representing the scene containing multiple objects.
  - `__init__()`: Initializes the scene with a list of objects.

- **Main Script**: Sets up parameters for the experiment, creates objects, simulates the experiment, and visualizes the results.

## Example
```python
# Set up the parameters for the ring laser time viewer
time_viewer = RingLaserTimeViewer(
    wavelength=1550e-9,
    beam_power=1e-3,
    ring_radius=1e9,
    num_detectors=360,
    c=299792458,
    G=6.67430e-11
)

# Simulate the experiment and visualize the results
adjusted_pulse_durations = time_viewer.simulate_experiment(scene)
print("Adjusted pulse durations:", adjusted_pulse_durations)

# Generate and visualize the point cloud
point_cloud = time_viewer.generate_points(scene.objects[0])
time_viewer.visualize_point_cloud(point_cloud)
```

## License
This project is licensed under the GNU General Public License v3.0 Affero - see the [LICENSE](LICENSE) file for details.
