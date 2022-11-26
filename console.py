#!/usr/bin/python3
""" AirBnB console"""

from datetime import datetime
import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import shlex
import cmd


class HBNBCommand(cmd.Cmd):
    """HBNB command lines"""
    prompt = "(hbnb) "

    def do_EOF(self, arg):
        """Exits console"""
        return True

    def do_quit(self, arg):
        """Quit the program and save"""
        return True

    def do_nothing(self, arg):
        """ nothing """
        pass

    def emptyline(self):
        """ override emptyline method """
        return False

    def _key_value_parser(self, args):
        """creates a dictionary from a list of strings"""
        new_dict = {}
        for arg in args:
            if "=" in arg:
                kvp = arg.split('=', 1)
                key = kvp[0]
                value = kvp[1]
                if value[0] == value[-1] == '"':
                    value = shlex.split(value)[0].replace('_', ' ')
                else:
                    try:
                        value = int(value)
                        try:
                            value = float(value)
                            continue
                        new_dict[key] = value
            return new_dict

    def do_create(self, arg):
        """Create a new instance"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            new_dict = self._key_value_parser(args[1:])
            instance = classes[args[0]](**new_dict)
        else:
            print("** class doesn't exist **")
            return False
        print(instance.id)
        instance.save()

    def do_show(self, arg):
        """ Prints the string representation of an instance based"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")
                else:
                    print("** instance id missing **")
                else:
                    print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    models.storage.all().pop(key)
                    models.storage.save()
                else:
                    print("** no instance found **")
                else:
                    print("** instance id missing **")
                else:
                    print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all string representation of all instances based"""
        args = shlex.split(arg)
        obj_list = []
        if len(args) == 0:
            obj_dict = models.storage.all()
        elif args[0] in classes:
            obj_dict = models.storage.all(classes[args[0]])
        else:
            print("** class doesn't exist **")
            return False
        for key in obj_dict:
            obj_list.append(str(obj_dict[key]))
            print("[", end="")
            print(", ".join(obj_list), end="")
            print("]")

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = shlex.split(arg)
        integers = ["number_rooms", "number_bathrooms", "max_guest",
                    "price_by_night"]
        floats = ["latitude", "longitude"]
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in classes:
            if len(args) > 1:
                k = args[0] + "." + args[1]
                if k in models.storage.all():
                    if len(args) > 2:
                        if len(args) > 3:
                            if args[0] == "Place":
                                if args[2] in integers:
                                    try:
                                        args[3] = int(args[3])
                                        args[3] = 0
                                    elif args[2] in floats:
                                        try:
                                            args[3] = float(args[3])
                                            args[3] = 0.0
            setattr(models.storage.all()[k], args[2], args[3])
            models.storage.all()[k].save()
        else:
            print("** value missing **")
        else:
            print("** attribute name missing **")
        else:
            print("** no instance found **")
        else:
            print("** instance id missing **")
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
