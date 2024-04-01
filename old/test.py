from model import DirectoryTree, NodeType, Node

from llama_index.program.openai import OpenAIPydanticProgram
from llama_index.agent.openai import OpenAIAssistantAgent
from llama_index.core.types import ChatMessage
from llama_index.llms.openai import OpenAI
from pydantic import BaseModel
from dotenv import load_dotenv
import os
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))



class StringTree(BaseModel):
    """
    a class representing filesystem
    """
    string_tree: str

class ProjectDescription(BaseModel):
    """
    A class representing a project description
    """
    project_description: str

expand_project_description_template = """
Given the project description:
{project_description}
Determine the type of person/professional that would do these types of projects 
and act as a an experienced professional of that type. Generate a more detailed explanation of what files and folders would be required for the project as if 
it were for an advanced professional version of the project in the relevant industry. 

As an example for python projects, many professionals will opt to create a virtual environment for the project.
The user may not explicitly say they want a virtual environment but it is a common practice in the industry.
You must act as if you are the professional and know what is best for the project while also considering the project description.

return the new project description.
"""

generate_fs_template = """
You are a highly experienced developer across multiple software, analytics and multimedia domains.
You are given a project description: '{project_description}'. You must return the correct and extremely detailed filesystem structure that will match the project description.
Below is an example of what a filesystem structure can look like as a string:

root
├── folder1
│   ├── file1.txt
│   └── file2.txt
└── folder2
    ├── file3.txt
    └── subfolder1
        └── file4.txt

return the string representation of the filesystem.
"""


parse_fs_template = """
You are a perfect file system parsing algorithm. You are given a string representing a directory tree. You must return the correct filesystem structure.
Consider the data below:
{string_fs}
and return the correctly labeled filesystem structure. the top level is always a folder e.g. 'root' is a node type of folder in this example, the top level of the hierarchy might not always be called root.
"""

expand_project_description_program = OpenAIPydanticProgram.from_defaults(
    output_cls=ProjectDescription,
    prompt_template_str=expand_project_description_template,
    verbose=True,
)


generate_fs_program = OpenAIPydanticProgram.from_defaults(
    output_cls=StringTree,
    prompt_template_str=generate_fs_template,
    verbose=True,
)


parse_fs_program = OpenAIPydanticProgram.from_defaults(
    output_cls=DirectoryTree,
    prompt_template_str=parse_fs_template,
    verbose=True,
)

project_description = """
Generate the folder structure for a professional cli tool in python.

"""

string_tree: StringTree = generate_fs_program(project_description=project_description)
print(f"string_fs: {string_tree}")
directoryTree: DirectoryTree = parse_fs_program(string_fs=string_tree.string_tree)
print(f"directoryTree: {directoryTree}")

assert directoryTree.root.node_type == NodeType.FOLDER, "The root node should be a folder"
directoryTree.print_paths()

