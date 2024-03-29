# Ring Laser Experiment Simulator

## Overview
The Ring Laser Experiment Simulator is a Python script designed to simulate a ring laser experiment with gravitational effects such as frame dragging and time dilation. The script calculates adjusted pulse durations, generates points for visualization, conducts the experiment simulation, and visualizes the results using matplotlib.

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
The script consists of the following components:

- **RingLaserExperiment**: A class representing the ring laser experiment setup and simulation.
  - `__init__()`: Initializes experiment parameters.
  - `calculate_frame_dragging_effect()`: Calculates frame dragging effects caused by massive objects.
  - `calculate_time_dilation()`: Calculates time dilation effects caused by massive objects.
  - `generate_points()`: Generates random points for visualization.
  - `simulate_experiment()`: Simulates the ring laser experiment.
  - `visualize_spacetime_distortion()`: Visualizes spacetime distortion induced by the experiment.

- **MassiveObject**: A class representing massive objects in the scene.
  - `__init__()`: Initializes mass, position, and velocity of objects.

- **Scene**: A class representing the scene with multiple massive objects.
  - `__init__()`: Initializes the scene with a list of objects.

## Example
```python
import numpy as np
from TRL import RingLaserExperiment, MassiveObject, Scene

# Define massive objects
black_hole1 = MassiveObject(mass=10 ** 36, position=np.array([0, 0, 0]), velocity=0)
black_hole2 = MassiveObject(mass=5 * 10 ** 35, position=np.array([1e8, 0, 0]), velocity=1e7)
black_hole3 = MassiveObject(mass=2 * 10 ** 35, position=np.array([-1e8, 0, 0]), velocity=-1e7)

# Create scene with massive objects
scene = Scene(objects=[black_hole1, black_hole2, black_hole3])

# Initialize Ring Laser Experiment
ring_laser_experiment = RingLaserExperiment(
    laser_power=1e-3,
    laser_radius=1e9,
    num_detectors=360,
    num_points=5000,
    c=299792458,
    G=6.67430e-11
)

# Simulate experiment
frame_dragging_effects, time_dilation_factors = ring_laser_experiment.simulate_experiment(scene)

# Generate point cloud for visualization
point_cloud = ring_laser_experiment.generate_points(black_hole1)

# Visualize spacetime distortion
ring_laser_experiment.visualize_spacetime_distortion(point_cloud, frame_dragging_effects, time_dilation_factors)
```

## License
This project is licensed under the GNU General Public License v3.0 Affero - see the [LICENSE](LICENSE) file for details.
