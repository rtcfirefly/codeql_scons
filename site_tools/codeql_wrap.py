def wrap_with_codeql(env, command_var):
    original_command = env[command_var]
    codeql_command = 'codeql database trace-command --'
    
    # Wrap the original command with the CodeQL trace command
    wrapped_command = f'{codeql_command} {original_command}'
    env[command_var] = wrapped_command

def generate(env):
    # List of command types to wrap with CodeQL
    command_types_to_wrap = ['CCCOM', 'CXXCOM', 'LINKCOM', 'SHCCCOM', 'SHCXXCOM', 'SHLINKCOM']

    # Wrap each command type with CodeQL
    for command_type in command_types_to_wrap:
        if command_type in env:
            wrap_with_codeql(env, command_type)

def exists(env):
    return True
