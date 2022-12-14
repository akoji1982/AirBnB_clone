#!/usr/bin/env python3
"""This the AirBnB console line interpreter"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage

class HBNBCommand(cmd.Cmd):
    """Class containing the entry point of the command interperter"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Command to exit the program."""
        exit()

    def do_EOF(self, arg):
        """Command to exit the program."""
        return True

    def help_quit(self):
        print('Quit command to exit the program\n')

    def help_create(self):
        """`create` command help"""
        print('Creates a new instance of BaseModel\n')

    def help_show(self):
        """`show` command help"""
        print('Shows a BaseModel instance if exists\n')

    def emptyline(self):
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if arg:
            try:
                kclass = globals().get(arg, None)
                obj = kclass()
                print(obj.id)
            except:
                print ("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, arg):
        """Shows an instance given its id"""
        if not arg:
            print("** class name missing **")
            return
        strs = arg.split(" ")

        if not strs:
            print("** class name missing **")
            return

        kclass = globals().get(strs[0], None)
        if kclass is None:
            print("** class doesn't exist **") 
            return

        if len(strs) != 2:
           print("** instance id missing **")
           return
       
        if strs[1] in storage.all():
           print(storage.all()[strs[1]])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Destroys an instance based on he class name and id"""
        if not arg:
            print("** class name missing**")
            return
        strs = arg.split(" ")
        count = len(strs)

        if count == 0:
            print ("** class name missing**")
            return
        class_name = strs[0]

        kclass = globals().get(class_name, None)
        if kclass is None:
            print("** class doesn't exist **")
            return

        if count < 2:
            print("** instance id missing **")
            return
        obj_id = strs[1]
    
        if obj_id not in storage.all():
            print("** no instance found **")
            return

        obj = storage.all()[obj_id]
        if obj.__class__.__name__ != class_name:
            print("** no instance found **")
            return

        storage.all().pop(obj_id, None)
        storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        kclass = globals().get(arg, None)
        if kclass is None:
            print("** class doesn't exist **")
            return
        for k, v in storage.all().items():
            if v.__class__.__name__ != arg:
                continue
            print(v)

    def do_update(self, arg):
        """Update an instance base of class name and id"""
        if not arg:
            print("** class name missing **")
            return
        strs = arg.split(" ")
        count = len(strs)
        if not strs:
            print("** class name missing **")
            return
        
        kclass = globals().get(strs[0], None)
        if kclass is None:
            print ("** class doesn't exist **")
            return
        class_name = strs[0]

        if count < 2:
            print("** instance id missing **")
            return
        obj_id = strs[1]

        if  obj_id not in storage.all():
            print("** no instance found **")
            return

        obj = storage.all()[obj_id]
        if obj.__class__.__name__ != class_name:
            print("** no instance found **")
            return

        if count < 3:
            print("** attribute name missing **")
            return
        attr_name = strs[2]

        if count < 4:
            print("** value missing **")
            return
        attr_value = strs[3]

        if hasattr(obj, attr_name):
            setattr(obj, attr_name, type(getattr(obj, attr_name))(attr_value))
        else:
            setattr(obj, attr_name, attr_value)

        obj.save()

        





if __name__ == '__main__':
    HBNBCommand().cmdloop()
