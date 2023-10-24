![HBNB Image](https://camo.githubusercontent.com/2756611b7152e3a082a906de8e91f9260de0c7054948cda6060f1e35debd233b/68747470733a2f2f692e696d6775722e636f6d2f4e6c38764e32472e6a7067)

# AirBnB_clone project
This project focuses on creating an Airbnb clone.
## Description
Airbnb is an online marketplace and hospitality service platform that allows people to list, discover, and book accommodations, primarily in the form of home stays, vacation rentals, apartments, and hotel rooms. It was founded in 2008 and has since become a well-known and popular platform for both travelers and hosts. Here are some key aspects of Airbnb:

1. **Accommodation Listings:** Hosts can list their properties or spare rooms on Airbnb, providing details such as pricing, availability, location, and descriptions. These accommodations can range from private homes and apartments to unique and unconventional spaces like treehouses and boats.

2. **Booking System:** Travelers can search for accommodations based on their preferences, location, dates, and budget. They can then book their chosen lodging directly through the Airbnb platform.

3. **Host-Guest Interaction:** Airbnb provides a platform for communication between hosts and guests. Hosts can answer questions and provide information about their properties, while guests can inquire about specific details.

4. **Reviews and Ratings:** Both hosts and guests can leave reviews and ratings after a stay. This feedback system helps maintain trust and transparency within the Airbnb community.

5. **Payment Processing:** Airbnb handles the financial transactions, collecting payments from guests and disbursing the funds to hosts. They also charge service fees.

6. **Global Reach:** Airbnb has a global presence, with listings available in numerous countries and cities around the world.

7. **Diverse Options:** Airbnb offers a wide range of accommodation options, catering to various budgets and preferences. Users can find affordable shared spaces, luxury villas, and everything in between.

8. **Experiences and Activities:** In addition to accommodations, Airbnb offers experiences and activities hosted by locals in various destinations. These can include guided tours, cooking classes, and more.

Airbnb has disrupted the traditional hospitality industry by enabling property owners to monetize their extra space and offering travelers more choices and personalized experiences. It has also led to discussions and regulations in various places regarding home-sharing, property rental, and issues like housing affordability.
## Usage
- First, clone the repository into your directory.
    ```
    $ git clone https://github.com/lisale0/AirBnB_clone
    ```

- Run the executable `./console.py`

- Type help for a list of the commands available with console.py.
    help is an action provided by default by cmd.
    Enter help + command for information about respective command and usage.

### Documented commands (type help <topic>):
========================================

```
Amenity    City  Place   State  all     destroy  quit  update
BaseModel  EOF   Review  User   create  help   show

(hbnb) create City
4af7890c-007f-42ff-97d8-074214f1094f
(hbnb) show City 4af7890c-007f-42ff-97d8-074214f1094f
[City] (4af7890c-007f-42ff-97d8-074214f1094f) {'id': '4af7890c-007f-42ff-97d8-074214f1094f',
 'updated_at': datetime.datetime(2017, 6, 11, 1, 6, 39, 679386), '__class__': 'City',
 'created_at': datetime.datetime(2017, 6, 11, 1, 6, 39, 679362)}
(hbnb)$
```

- quit -- exits the program

- EOF -- exits the program

### Execution
#### interactive mode
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
### non-interactive mode
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

### Files
 | File | Description |
 | ------------- | ------------- |
 | console.py | entry point of the command interpreter |
 | models/init.py | creates an instance of FileStorage |
 | models/base_model.py | class BaseModel that defines all common attributes/methods for other classes |
 | models/amenity.py | class Amenity, inherits from BaseModel |
 | models/city.py | class City, inherits from BaseModel |
 | models/place.py | class Place, inherits from BaseModel |
 | models/review.py | class Review, inherits from BaseModel |
 | models/state.py | class State, inherits from BaseModel |
 | models/user.py | class User, inherits from BaseModel |
 | models/engine/file_storage.py | class FileStorage, serializes instances to a JSON file and deserializes JSON file to instances |
 | models/engine/file_storage.py | class FileStorage, serializes instances to a JSON file and deserializes JSON file to instances |
 | tests/ | folder where are all the tests of the program |

## Resources:books:
Read or watch:
* [cmd module](https://docs.python.org/3.4/library/cmd.html)
* [packages](https://intranet.hbtn.io/concepts/66)
* [uuid module](https://docs.python.org/3.4/library/uuid.html)
* [datetime](https://docs.python.org/3.4/library/datetime.html)
* [unittest module](https://docs.python.org/3.4/library/unittest.html#module-unittest)
* [args/kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)
* [Python test cheatsheet](https://www.pythonsheets.com/notes/python-tests.html)

## Learning Objectives:bulb:
* How to create a Python package
* How to create a command interpreter in Python using the cmd module
* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* How to manage datetime
* What is an UUID
* What is *args and how to use it
* What is **kwargs and how to use it
* How to handle named arguments in a function

## Project Requirements
### Python Scripts
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the PEP 8 style (version 1.7 or more)
- All your files must be executable
- The length of your files will be tested using wc
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')

### Python Unit Tests
- Allowed editors: vi, vim, emacs
- All your files should end with a new line
- All your test files should be inside a folder tests
- You have to use the unittest module
- All your test files should be python files (extension: .py)
- All your test files and folders should start by test_
- Your file organization in the tests folder should be the same as your project
e.g., For models/base_model.py, unit tests must be in: tests/test_models/test_base_model.py
e.g., For models/user.py, unit tests must be in: tests/test_models/test_user.py
- All your tests should be executed by using this command: python3 -m unittest discover tests
- You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
- We strongly encourage you to work together on test cases, so that you don’t miss any edge case

## Tasks
## 0. README, AUTHORS
- Write a README.md
- You should have an AUTHORS file at the root of your repository, listing all individuals having contributed content to the repository.

## 1. Be PEP8 compliant!
- Write beautiful code that passes the PEP8 checks.

## 2. Unittests
- All your files, classes, functions must be tested with unit tests

## 3. BaseModel
- Write a class BaseModel that defines all common attributes/methods for other classes

## 4. Create BaseModel from dictionary
- Create an instance with the previous dictionary representation

## 5. Store first object
- recreate a BaseModel from another one by using a dictionary representation

## 6. Console 0.0.1
- Write a program called console.py that contains the entry point of the command interpreter

## 7. Console 0.1
- Update your command interpreter (console.py) to have these commands:
  - create
  - show
  - destroy
  - all
  - update

## 8. First User
- Write a class User that inherits from BaseModel

## 9. More classes!
- Write all those classes that inherit from BaseModel:
  - State
  - City
  - Amenity
  - Place
  - Review

## 10. Console 1.0
- Update FileStorage to manage correctly serialization and deserialization of all our new classes: Place, State, City, Amenity and Review

## 11. All instances by class name
- Update your command interpreter (console.py) to retrieve all instances of a class by using: <class name>.all()

## 12. Count instances
- Update your command interpreter (console.py) to retrieve the number of instances of a class: <class name>.count()

## 13. Show
- Update your command interpreter (console.py) to retrieve an instance based on its ID: <class name>.show(<id>)

## 14. Destroy
- Update your command interpreter (console.py) to destroy an instance based on his ID: <class name>.destroy(<id>)

## 15. Update
- Update your command interpreter (console.py) to update an instance based on his ID: <class name>.update(<id>, <attribute name>, <attribute value>)

## 16. Update from dictionary
- pdate your command interpreter (console.py) to update an instance based on his ID with a dictionary: <class name>.update(<id>, <dictionary representation>)

## 17. Unittests for the Console!
- Write all unittests for console.py, all features!

## Author
- **Oldimeji Olayinka Esther** - [Holladworld github](https://github.com/holladworld)
- 
