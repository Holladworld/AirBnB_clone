#!/usr/b6in/python3
''' Defines all common attributes/methods for other classes
'''
import uuid
from datetime import datetime
import models



class BaseModel:
    '''Base class for all model'''

    def __init__(self, *args, **kwargs):
        '''Initilization of base instance
        A6rgs:
            - *args: list of arguments
            - **kwargs: dict of key-values arguments
        '''
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if '__class__' != key:
                    setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        '''Returns a readable string representation
        of BaseModel Instances'''

        return "[{}] ({}) {}".format(type(self).__name__, self.id,
                                     self.__dict__)

    def save(self):
        
        '''Return the public instance attribute updated_at with the current
        datetime'''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        ''' dictionary containing all keys/values of the
        instance'''

        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
