from setuptools import setup
from glob import glob
import os

package_name = 'maze_bot'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name,'launch'), glob('launch/*')),
        (os.path.join('share', package_name,'urdf'), glob('urdf/*')),
        (os.path.join('share', package_name,'meshes'), glob('meshes/*')),
        (os.path.join('share', package_name,'worlds'), glob('worlds/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='zahid',
    maintainer_email='zahid@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'driving_mazebot = maze_bot.driving_node:main' ,
            'go_to_goal = maze_bot.go_to_goal:main',
            'go_to_goal_2 = maze_bot.go_to_goal_2:main',
            'video_recorder = maze_bot.video_saver:main',
            'maze_solver = maze_bot.maze_solver:main',  

        ],
    },
)
