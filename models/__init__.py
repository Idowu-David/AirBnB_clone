#!/usr/bin/python3
""" creates a unique instance of filestorage """
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
