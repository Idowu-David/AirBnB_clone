#!/usr/bin/python3
"""
The BaseModel class defines all common attributes/methods
for other classes

Attr:
    id: string
    created_at: datetime - current datetime when an instance is created
    updated_at: datetime - current datetime when a created instance is
         updated everytime there's a change.
    save - updates the public instance attribute updated_at
         with the current datetime
    to_dict - returns a dictionary containing all keys/values of __dict__
        of the instance.
"""
import uuid
from datetime import datetime

format = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """defines all common attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        """Constructor"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        value = datetime.strptime(value, format)
                    setattr(self, key, value)
        else:
            from models import storage
            storage.new(self)

    def __str__(self):
        """the string representation of the object"""
        name = self.__class__.__name__
        return f"[{name}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the public instance attribute `updated_at` with the current
        datetime"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__
        of the instance"""
        d = self.__dict__.copy()
        d["__class__"] = self.__class__.__name__
        d["created_at"] = self.created_at.isoformat()
        d["updated_at"] = self.updated_at.isoformat()

        return d
