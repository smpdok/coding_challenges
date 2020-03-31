Tames of Thrones(Python 3.8)
================================
Requirement
-----------------
* Python 3 versions preferably 3.6 and above

Project Structure
-----------------
This project has two packages:
* geektrust.py --> Main function
* scripts --> contains all the classes and other scripts
* test --> unittest cases for each classes and functions
* data --> contains parameter.py file which has all the dynamic variables
* sample_io --> contains sample input and output txt files

Running Code
-----------------
To run the code from root dir run the following command:
* python -m geektrust "<absolute_path_to_input_file>"
* python -m geektrust "sample_io/input1.txt"

Output will be printed to console.


Running Tests
-------------

To run tests go to 'test' dir (cd test) and run one of the following commands:

* To discover all unit tests in a project : python -m unittest discover 
* To run the test module by name : python -m unittest test_decrypt_message

Additional Info
----------------

* context.py inside test folder is used for importing the scripts files for unit testing. This is done by ading root path of project to sys.path.

