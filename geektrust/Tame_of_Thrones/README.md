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
* data/parameter.py --> contains parameter.py file which has all the dynamic variables
* sample_io --> contains sample input and output txt files

Running Code
-----------------
To run the code from root dir run the following command:

* python -m geektrust "<absolute_path_to_input_file>"
* python -m geektrust "sample_io/input1.txt"
* python geektrust --file "<absolute_path_to_input_file>"
* python geektrust --file "<absolute_path_to_input_file>" --king ""<king's_name>"
  eg: python geektrust.py --file "sample_io\input4.txt" --king "Captain Jack Sparrow"
* python geektrust "<absolute_path_to_input_file>" --king ""<king's_name>"
* For argument help : python geektrust.py --help

Note: Available Kings and Kingdoms available : {
	'King Shan': ['SPACE'],
    'Al Falcone': ['AIR'],
    'Shenron': ['FIRE'],
    'Mao Zedong': ['LAND'],
    'Captain Jack Sparrow': ['WATER'],
    'Night King': ['ICE']
}
  
Output will be printed to console.

Changes from Previous version
---------------------------------
* Added two optional arguments while running the main file:
	- filename parameter : '--file' "<absolute_path_to_input_file>"
	- king parameter : '--king' "<king's_name>"
	Note: Please call the both parameters in double quotes ("")
* Earlier we could send messages only for 'SPACE' kingdom. This has been extended to other kingdoms using the argument '--king'.
* Remove magic_numbers and literals from code. Parameters are added to data/parameters.py file.
* Removed Kingdom and Ally classes. Changes DecryptMessage class to Message class. 
* There are 3 classes in the code now: Southeros, Message , ReadFile
* Revamped decrypt message function. Earlier there were 4 functions to decrypt the message. Now it is reduced to 1.
	- The newfunction has capability to decrypt both ascii_lowercase and ascii_uppercase messages.
	- Encrypted direction can be set in parameters file. By default(as per the problem) messages were encrypted in 'clockwise' direction and hence decryption  was in 'anticlockwise' direction. Now, vice-versa is possible by changing "encrypted_direction" in parameter file to 'anticlockwise'.
* 'Message.verify_message' was earlier 'Ally.ally_check'. The code is imporved and is faster.
* 'parse_message' function in main file has been changed to 'send_the_ravens' to match the lore. The code is imporved and is shorter.
* Changed unitest test function naming convention to convey it's intent properly.
* Additional after successful sending of the message, ruler will be set and his/her name can be retrieved from Southeros class.
* 'read_from_file' function in ReadFile class is changed to 'read_from_file_as_rows'. This class can be replaced to a single function, intent of keeping the function is incorporate any changes to reading from files in future.
* Allies required to be a ruler can be set in parameter file. By Default the King sending the messages will be 'King Shan', this can be changed in parameter file 


Running Tests
-------------

To run tests go to 'test' dir (cd test) and run one of the following commands:

* To discover all unit tests in a project : python -m unittest discover 
* To run the test module by name : python -m unittest test_message

Additional Info
----------------

* context.py inside test folder is used for importing the scripts files for unit testing. This is done by ading root path of project to sys.path.
* To test '--king' argument . I recommend testing with input4.txt file as this file contains higher number of valid messages. Others may return None, depending on the king.
* Please note that Output4 has allies of WATER while all others have output of SPACE

