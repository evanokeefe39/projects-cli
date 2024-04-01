from jinja2 import Environment, FileSystemLoader, Template
import os


template_path = os.path.join(os.path.dirname(__file__), 'templates')
env = Environment(loader=FileSystemLoader(template_path))