import os

# Specify that the custom tools are located in the site_tools directory
env = Environment(tools=['default'], toolpath=['site_tools'])

# Explicitly load the custom codeql_wrap tool
env.Tool('codeql_wrap')

# Define the build targets
env.Program(target='my_program', source=['main.cpp', 'utils.cpp'])
