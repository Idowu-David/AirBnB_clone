"""This module contains the FileStorage class"""


import json
from models.base_model import BaseModel

classes = {
    "BaseModel": BaseModel
}


class FileStorage:
    """serializes instances to a JSON file and deserializes JSON files
    to instances"""
    __file_path = "file.json"
    __objects = dict()

    def __init__(self):
        """initializer"""
        pass

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets the __objects"""
        class_name = obj.__class__.__name__
        key = f"{class_name}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(FileStorage.__file_path, "w") as fp:
            json.dump(obj_dict, fp)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r") as fp:
                content = json.load(fp)
                for key, obj_dict in content.items():
                    cls_name = obj_dict["__class__"]
                    clss = classes[cls_name]
                    if clss:
                        obj = clss(**obj_dict)
                        self.__objects[key] = obj
        except FileNotFoundError:
            pass
