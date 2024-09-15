from setuptools import find_packages, setup

package_name = 'mediapipe_face_tracker'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools', 'mediapipe', 'cv2'],
    zip_safe=True,
    maintainer='selexin',
    maintainer_email='selexin@selexin.com',
    description='A node that publishes the location of a tracked face using mediapipe',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'mediapipe_face_tracker = mediapipe_face_tracker.mediapipe_face_tracker:main',
            'example_subscriber = mediapipe_face_tracker.example_subscriber:main',
        ],
    },
)
