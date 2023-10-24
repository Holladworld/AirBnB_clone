#!/usr/bin/python3
''' An interactive shell?
This is the main Airbnb console'''

import re
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import cmd
import models


def cmd_loop(line, obj_upt):
    '''
    Loop format: <class name>.update(<id>, <dictionary representation>)
    '''
    dic = 4
    while dic <= len(line):
        try:
            atrribute = line[dic]
        except IndexError:
            print("** attribute name missing **")
        else:
            try:
                value = line[dic+1]
            except IndexError:
                print("** value missing **")
            else:
                setattr(obj_upt, atrribute, value)
                obj_upt.save()
                if dic+1 == len(line) - 1:
                    break
        dic += 1


def cmd_pattern(arg):
    ''' Retrieve cmd and respective arguments according
    to pattern:  <class>. <cmd> ([args, ...])'''
    cmd_pattern = '\.([^.]+)\(|([^(),]+)[,\s()]*[,\s()]*'
    argum = re.findall(cmd_pattern, arg)
    cmd = argum[0][0]
    argum = argum[1:]
    line = ' '.join(map(lambda x: x[1].strip('"'), argum))
    return cmd, line


class HBNBCommand(cmd.Cmd):
    ''' AirBnB console '''
    prompt = "(hbnb) "

    def do_EOF(self, arg):
        '''Exits console '''
        return True

    def do_quit(self, arg):
        '''Quit command to exit the program'''
        return True

    def help_quit(self):
        '''when two arguments areinvolve'''
        print('\n'.join(["Quit command to exit the program"]))

    def emptyline(self):
        '''Do nothin if line is empty'''
        pass
        # OR
        # False

    def do_create(self, arg):
        '''
        Creates a new instance of BaseModel class
        '''
        if len(arg) == 0:
            print("** class name missing **")
        else:
            try:
                cls = models.classes[arg]
            except KeyError:
                print("** class doesn't exist **")
            else:
                obj = cls()
                obj.save()
                print(obj.id)

    def do_show(self, arg):
        '''Print <clss name> <id>'''
        if len(arg) == 0:
            print("** class name missing **")
        else:
            line = arg.split(' ')
            if line[0] in models.classes:
                try:
                    key = "{}.{}".format(line[0], line[1])
                except IndexError:
                    print("** instance id missing **")
                else:
                    try:
                        print(models.storage.all()[key])
                    except KeyError:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_destroy(self, arg):
        ''' Destroy command deletes an instances base
        on the class name and id '''
        if len(arg) == 0:
            print("** class name missing **")
        else:
            line = arg.split(' ')
            if line[0] in models.classes:
                try:
                    key = "{}.{}".format(line[0], line[1])
                except IndexError:
                    print("** instance id missing **")
                else:
                    try:
                        objects = storage.all()
                        models.storage.delete(objects[key])
                    except KeyError:
                        print("** no instance found **")
                    else:
                        models.storage.save()
            else:
                print("** class doesn't exist **")

    def do_all(self, arg):
        ''' Prints all instances instring representation'''
        if len(arg) == 0:
            print([str(value) for value in models.storage.all().values()])
        elif arg not in models.classes:
            print("** class doesn't exist **")
        else:
            print([str(value) for key, value in models.storage.all().items()
                   if arg in key])

    def do_update(self, arg):
        '''
        Updates an instance based on the class name and id
        usage: Update <class><id> <attribute_name> <attribute_value>
        Ex: $ update BaseModel 1234-1234-1234 email
        '''
        if len(arg) == 0:
            print("** class name missing **")
        else:
            line = arg.split(' ')
            for iter in range(len(line)):
                line[iter] = line[iter].strip("\"'\"{\"}:\"'")
            if line[0] in models.classes:
                try:
                    key = "{}.{}".format(line[0], line[1])
                except IndexError:
                    print("** instance id missing **")
                else:
                    try:
                        obj_upt = models.storage.all()[key]
                    except KeyError:
                        print("** no instance found **")
                    else:
                        try:
                            atrribute = line[2]
                        except IndexError:
                            print("** attribute name missing **")
                        else:
                            try:
                                value = line[3]
                            except IndexError:
                                print("** value missing **")
                            else:
                                setattr(obj_upt, atrribute, value)
                                obj_upt.save()
                                if len(line) >= 5:
                                    cmd_loop(line, obj_upt)
            else:
                print("** class doesn't exist **")

    def do_BaseModel(self, arg):
        '''for BaseModel class '''
        cmd, line = cmd_pattern(arg)
        self.onecmd(' '.join([cmd, 'BaseModel', line]))

    def do_Amenity(self, arg):
        '''Invoke Amenities'''
        cmd, line = cmd_pattern(arg)
        self.onecmd(' '.join([cmd, 'Amenity', line]))

    def do_City(self, arg):
        '''cmd all, create, update, show destroy'''
        cmd, line = cmd_pattern(arg)
        self.onecmd(' '.join([cmd, 'City', line]))

    def do_Place(self, arg):
        '''
        Lets you invoke each of the console methods'''
        cmd, line = cmd_pattern(arg)
        self.onecmd(' '.join([cmd, 'Place', line]))

    def do_Review(self, arg):
        '''
        for the Review class with the following syntax:
        Review.<cmd>([args, ...])'''
        cmd, line = cmd_pattern(arg)
        self.onecmd(' '.join([cmd, 'Review', line]))

    def do_State(self, arg):
        '''invoke state'''

        cmd, line = cmd_pattern(arg)
        self.onecmd(' '.join([cmd, 'State', line]))

    def do_User(self, arg):
        cmd, line = cmd_pattern(arg)
        self.onecmd(' '.join([cmd, 'User', line]))

    def do_count(self, arg):
        '''Retrieve instances'''
        if len(arg) == 0:
            print(len([str(value) for value in models.storage.all().values()]))
        elif arg in models.classes:
            print(len([str(value) for key, value in
                       models.storage.all().items()
                      if arg in key]))
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
