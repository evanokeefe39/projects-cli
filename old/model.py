import enum

from typing import List
from pydantic import BaseModel, Field
import os



class NodeType(str, enum.Enum):
    """Enumeration representing the types of nodes in a filesystem."""

    FOLDER = "folder"
    FILE = "file"
    

class Node(BaseModel):
    """
    Class representing a single node in a filesystem. Can be either a file or a folder.
    Note that a file cannot have children, but a folder can.

    Args:
        name (str): The name of the node.
        children (List[Node]): The list of child nodes (if any).
        node_type (NodeType): The type of the node, either a file or a folder.

    Methods:
        print_paths: Prints the path of the node and its children.
    """

    name: str = Field(..., description="Name of the folder")
    children: List["Node"] = Field(
        default_factory=list,
        description="List of children nodes, only applicable for folders, files cannot have children",
    )
    node_type: NodeType = Field(
        default=NodeType.FOLDER,
        description="Either a file or folder, use the name to determine which it could be",
    )

    def print_paths(self, parent_path=""):
        """Prints the path of the node and its children."""
        root = os.getcwd()
        if self.node_type == NodeType.FOLDER:
            path = f"{parent_path}/{self.name}" if parent_path != "" else self.name
            path = os.path.join(root, path)
            os.makedirs(path, exist_ok=True)
            print(path, self.node_type)

            if self.children is not None:
                for child in self.children:
                    child.print_paths(path)
        else:
            # create the file in the parent path
            with open(f"{parent_path}/{self.name}", "w") as f:
                f.write("This is a sample file.")
            print(f"{parent_path}/{self.name}", self.node_type)


class DirectoryTree(BaseModel):
    """
    Container class representing a directory tree.

    Args:
        root (Node): The root node of the tree which is a folder.

    Methods:
        print_paths: Prints the paths of the root node and its children.
    """

    root: Node = Field(..., description="Root folder of the directory tree")

    def print_paths(self):
        """Prints the paths of the root node and its children."""

        self.root.print_paths()


