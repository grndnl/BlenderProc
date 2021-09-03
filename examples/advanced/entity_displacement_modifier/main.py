import blenderproc as bproc
from blenderproc.python.utility.SetupUtility import SetupUtility
SetupUtility.setup([])

from blenderproc.python.materials.MaterialLoaderUtility import MaterialLoaderUtility
from blenderproc.python.writer.WriterUtility import WriterUtility
from blenderproc.python.utility.Initializer import Initializer
from blenderproc.python.camera.CameraUtility import CameraUtility
from blenderproc.python.types.LightUtility import Light
from blenderproc.python.utility.MathUtility import MathUtility
from blenderproc.python.renderer.RendererUtility import RendererUtility

import random
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('scene', nargs='?', default="examples/resources/scene.obj", help="Path to the scene.obj file")
parser.add_argument('output_dir', nargs='?', default="examples/advanced/entity_displacement_modifier/output", help="Path to where the final files, will be saved")
args = parser.parse_args()

Initializer.init()

# load the objects into the scene
objs = bproc.loader.load_obj(args.scene)

# define a light and set its location and energy level
light = Light()
light.set_type("POINT")
light.set_location([5, -5, 5])
light.set_energy(1000)

# define the camera intrinsics
CameraUtility.set_intrinsics_from_blender_params(1, 512, 512, lens_unit="FOV")

# Add two camera poses
CameraUtility.add_camera_pose(MathUtility.build_transformation_mat([0, -13.741, 4.1242], [1.3, 0, 0]))
CameraUtility.add_camera_pose(MathUtility.build_transformation_mat([1.9488, -6.5202, 0.23291], [1.84, 0, 0.5]))

# Add displacement to all objects
for obj in objs:
    # Create a uv mapping based on a cylinder projection
    obj.add_uv_mapping("cylinder")

    # Create a random procedural texture
    texture = MaterialLoaderUtility.create_procedural_texture()
    # Displace the vertices of the object based on that random texture
    obj.add_displace_modifier(
        texture=texture,
        strength=random.gauss(0, 0.5),
        subdiv_level=random.randint(1, 3),
    )

# activate normal and distance rendering
RendererUtility.enable_normals_output()
RendererUtility.enable_distance_output()
# set the amount of samples, which should be used for the color rendering
RendererUtility.set_samples(350)

# render the whole pipeline
data = RendererUtility.render()

# write the data to a .hdf5 container
bproc.writer.write_hdf5(args.output_dir, data)
