import click
import os

from projx.util import env as util_env
from projx.pipe import env as pipe_env

@click.group()
def pipe():
    pass

def _fill_template(env, template_name, path, **kwargs):
    template = env.get_template(template_name) 
    with open(path, 'w') as f:
        f.write(template.render(**kwargs))

@pipe.command()
@click.option('--name', required=True, help='The name of the pipe project')
@click.option('--description',default="", help='The description of the pipe project')
@click.option('--output', default=os.getcwd(), help='The output directory of the pipe project')
@click.option('--verbose', default=False, help='The verbosity of the pipe project')
def new(name, description, output, verbose, **kwargs):
    """
    Create a new pipe project.

    Args:
        name (str): The name of the project.
        description (str): The description of the project.
        output (str): The output directory for the project.
        verbose (bool): Whether to enable verbose output.
        **kwargs: Additional keyword arguments.

    Returns:
        None
    """

    print(f"Creating new pipe project: {name} with options: {kwargs}")

    root = os.path.join(output, name)
    src = os.path.join(root, name)
    os.makedirs(root, exist_ok=True)
    os.makedirs(src, exist_ok=True)

    with open(os.path.join(src, '__init__.py'), 'w') as f:
        f.write("")

    ctxt = {name: name, **kwargs}
    
    for e in pipe_env.list_templates():
        print(e)
        
        with open(os.path.join(src, e.rstrip('.j2')), 'w') as f:
            f.write(pipe_env.get_template(e).render(**ctxt))

    # pipe_template = pipe_env.get_template('pipe.py.j2').render(name=name)
    # requirements_template = util_env.get_template('requirements.txt.j2').render()

    # # Write the pipe.py file
    # with open(os.path.join(root,'pipe.py'), 'w') as f:
    #     f.write(pipe_template)

    # # Write the requirements.txt file
    # with open(os.path.join(root,'requirements.txt'), 'w') as f:
    #     f.write(requirements_template)

    # with open(os.path.join(root,'.gitignore'), 'w') as f:
    #     f.write('')

if __name__ == '__main__':
    pass