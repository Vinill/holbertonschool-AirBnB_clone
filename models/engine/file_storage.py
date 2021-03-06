#!/usr/bin/python3
"""Serializes instances to a JSON file and
deserializes JSON file to instances"""


import json


class FileStorage:
    """initialization of FileStorage"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """writes an object to a textfile"""
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            return f.write(json.dumps(self.__objects, default=str))

    def reload(self):
        """creates an object from a “JSON file”"""
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as f:
                self.__objects = json.loads(f.read())
        except Exception:
            pass
