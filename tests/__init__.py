import os
# Get the directory of the current script (the __init__.py file)
package_directory = os.path.dirname(os.path.abspath(__file__))

# Navigate up one level to get the project directory
project_directory = os.path.dirname(package_directory)
