import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class CirculatingLaserExperiment:
    def __init__(self, laser_power, laser_radius, num_detectors, num_points=1000, c=299792458, G=6.67430e-11):
        self.laser_power = laser_power
        self.laser_radius = laser_radius
        self.num_detectors = num_detectors
        self.num_points = num_points
        self.c = c
        self.G = G

    def calculate_adjusted_pulse_duration(self, obj):
        # Calculate adjusted pulse duration considering gravitational effects, Doppler shifts, and lensing
        r = np.linalg.norm(obj.position)
        schwarzschild_radius = 2 * self.G * obj.mass / (self.c ** 2)
        dilation_factor = np.sqrt(1 - (schwarzschild_radius / r))
        doppler_factor = np.sqrt((1 + (self.c / obj.velocity)) / (1 - (self.c / obj.velocity)))
        adjusted_pulse_duration = (self.laser_radius * dilation_factor * doppler_factor) / self.c
        return adjusted_pulse_duration

    def generate_points(self, obj):
        # Generate points for visualization
        points = np.random.uniform(low=obj.min_bound, high=obj.max_bound, size=(self.num_points, 3))
        return points

    def simulate_experiment(self, scene):
        # Simulate circulating laser experiment with gravitational effects
        adjusted_pulse_durations = np.zeros(len(scene.objects))
        for i, obj in enumerate(scene.objects):
            adjusted_pulse_durations[i] = self.calculate_adjusted_pulse_duration(obj)
        return adjusted_pulse_durations

    def visualize_point_cloud(self, point_cloud, adjusted_pulse_durations):
        # Visualize the generated point cloud with color mapping based on adjusted pulse durations
        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(point_cloud[:, 0], point_cloud[:, 1], point_cloud[:, 2], c=adjusted_pulse_durations, cmap='viridis', marker='.')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        plt.title("Circulating Laser Experiment Point Cloud")
        plt.colorbar(label='Adjusted Pulse Duration')
        plt.show()

if __name__ == "__main__":
    class MassObject:
        def __init__(self, mass, position, velocity):
            self.mass = mass
            self.position = position
            self.velocity = velocity
            # Define bounds for generating points
            self.min_bound = np.array([-1e9, -1e9, -1e9])  # Example: -1e9 for each axis
            self.max_bound = np.array([1e9, 1e9, 1e9])  # Example: 1e9 for each axis

    class Scene:
        def __init__(self, objects):
            self.objects = objects

    # Define multiple massive objects with different positions and velocities
    black_hole1 = MassObject(mass=10 ** 36, position=np.array([0, 0, 0]), velocity=0)
    black_hole2 = MassObject(mass=5 * 10 ** 35, position=np.array([1e8, 0, 0]), velocity=1e7)
    black_hole3 = MassObject(mass=2 * 10 ** 35, position=np.array([-1e8, 0, 0]), velocity=-1e7)
    scene = Scene(objects=[black_hole1, black_hole2, black_hole3])

    # Set up parameters for the circulating laser experiment
    laser_experiment = CirculatingLaserExperiment(
        laser_power=1e-3,  # Example laser power in watts
        laser_radius=1e9,  # Example laser radius
        num_detectors=360,  # Example number of detectors
        num_points=5000,  # Increase number of points for better visualization
        c=299792458,
        G=6.67430e-11
    )

    # Simulate the experiment and visualize the results
    adjusted_pulse_durations = laser_experiment.simulate_experiment(scene)
    print("Adjusted pulse durations:", adjusted_pulse_durations)

    # Generate and visualize the point cloud
    point_cloud = laser_experiment.generate_points(scene.objects[0])  # Generate points for the first object
    laser_experiment.visualize_point_cloud(point_cloud, adjusted_pulse_durations)