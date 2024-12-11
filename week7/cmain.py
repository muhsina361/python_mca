from cpackage.graphics.rectangle import rectangle_area,rectangle_parameter
from cpackage.graphics.circle import circle_area, cicle_parameter

from cpackage.graphics.three_d.cuboid import cuboid_tsa,cuboid_volume
from cpackage.graphics.three_d.sphere import sphere_tsa, sphere_volume


print("Rectangle Area:", rectangle_area(5, 3))
print("Rectangle Perimeter:", rectangle_parameter(5, 3))

print("Circle Area:", circle_area(7))
print("Circle Perimeter:",  cicle_parameter(7))

print("Cuboid Surface Area:", cuboid_tsa(5, 3, 4))
print("Cuboid Volume:", cuboid_volume(5, 3, 4))

print("Sphere Surface Area:", sphere_tsa(7))
print("Sphere Volume:", sphere_volume(7))


