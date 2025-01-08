"""
Setup configuration for MQTT Docker Controller package.
Handles package installation and dependencies.
"""

from setuptools import setup, find_packages
import pathlib

# Get current directory
here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="mqtt-docker-controller",
    version="0.1.0",
    description="A comprehensive and handy MQTT and Docker broker management tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    
    # Project URLs
    url="https://github.com/DylanWall96/mqtt-docker-controller",
    project_urls={
        "Bug Reports": "https://github.com/DylanWall96/mqtt-docker-controller/issues",
        "Source": "https://github.com/DylanWall96/mqtt-docker-controller/",
    },
    
    # Author details
    author="Dylan Wall",
    author_email="",  # Left empty for privacy
    
    # Classifiers help users find your project
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Communications",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3 :: Only",
    ],
    
    # Keywords for package discovery
    keywords="mqtt, docker, broker, iot, messaging, controller, automation",
    
    # Package configuration
    packages=find_packages(include=['mqtt_docker_controller', 'mqtt_docker_controller.*']),
    python_requires=">=3.8",
    
    # Dependencies
    install_requires=[
        'paho-mqtt>=1.6.1',
        'docker>=6.1.0',
    ],
    
    # Optional dependencies
    extras_require={
        'dev': [
            'check-manifest',
            'pytest',
            'pytest-cov',
            'flake8',
            'black',
            'mypy'
        ],
        'test': [
            'pytest',
            'pytest-cov'
        ],
    },
    
    # Entry points
    entry_points={
        'console_scripts': [
            'mqtt-docker-controller=mqtt_docker_controller.cli:main',
        ],
    },
    
    # Package data
    package_data={
        "mqtt_docker_controller": ["py.typed"],
    },
    
    # Platform compatibility
    platforms=['any'],
    
    # Build settings
    zip_safe=False,
    
    # Testing
    test_suite='tests',
)