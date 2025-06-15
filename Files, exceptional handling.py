"""
1.What is the difference between interpreted and compiled languages?
A. 
Interpreted: Code is executed line by line (e.g., Python, JavaScript).
Compiled: Code is translated to machine code before execution (e.g., C, C++).

2. What is exception handling in Python?
A. A mechanism to catch and manage runtime errors using try, except, finally, and else blocks.
3. What is the purpose of the finally block in exception handling?
A. It always executes, whether an exception occurred or not—commonly used for cleanup actions like closing files or releasing resources
4. What is logging in Python?
A. Executes only if no exceptions occur in the try block. It's useful for code that should run after the try succeeds.
5.  What is the significance of the __del__ method in Python?
A. 
try: Wraps the code that might raise exceptions.
except: Defines how to handle specific exceptions.
6. What is the difference between import and from ... import in Python?
A. 1. import module
    Imports the entire module.
    You must use the module name to access its functions, classes, or variables
    Example:
    import math
    print(math.sqrt(16))  
   2. from module import name
    Imports specific parts of a module (function, class, variable).
    Example:
    from math import sqrt
    print(sqrt(16))  
You can use the imported name directly, without the module prefix.
7. How can you handle multiple exceptions in Python?
A. 1. Use multiple except blocks:
    try:
        x = int("abc")
        y = 10 / 0
    except ValueError:
        print("ValueError occurred")
    except ZeroDivisionError:
        print("Cannot divide by zero")
    2. Single except Block for Multiple Exceptions:
    try:
        x = int("abc")
        y = 10 / 0
    except (ValueError, ZeroDivisionError) as e:
        print(f"An error occurred: {e}")
    3. Generic except Block:
    try:
        x = int("abc")
    except Exception as e:
        print(f"Unexpected error: {e}")
8. What is the purpose of the with statement when handling files in Python?
A. The with statement in Python is used for efficient and safe file handling by automatically managing resources. 
When working with files, it ensures that the file is properly closed after its suite finishes execution, even if 
an error occurs during the operation. This eliminates the need to manually call close() and helps prevent resource 
leaks or file corruption. By simplifying syntax and reducing the chance of errors, the with statement promotes cleaner, 
more readable, and more reliable code when opening, reading, or writing files.

9. What is the difference between multithreading and multiprocessing?
A. The main difference between multithreading and multiprocessing in Python lies in how they handle concurrency and 
system resources. Multithreading allows multiple threads to run in the same process and memory space, making it ideal 
for I/O-bound tasks (like reading files or network operations) but limited by the Global Interpreter Lock (GIL), which 
prevents multiple threads from executing Python bytecode simultaneously. In contrast, multiprocessing uses separate processes 
with their own memory space, allowing true parallel execution, which is better suited for CPU-bound tasks (like heavy computations), 
as it bypasses the GIL. While multithreading is lighter and faster to start, multiprocessing provides better performance for tasks 
that need intensive CPU usage.
10. What are the advantages of using logging in a program?
A. 
1. Error Tracking: Helps identify and debug issues by recording errors and exceptions during program execution.
2.Monitoring & Auditing: Provides a historical record of application activity, useful for audits and system monitoring.
3. Configurable Output: Supports different log levels (DEBUG, INFO, WARNING, ERROR, CRITICAL) and can log to files, consoles, or remote servers.
4. Better than Print Statements: Unlike print(), logging can be enabled or disabled globally and configured without modifying the code logic.
5. Safe for Production: Allows capturing issues in live systems without crashing the program or exposing sensitive data to users.
11. What is memory management in Python?
A. 
1. Automatic Memory Handling: Python manages memory automatically, reducing the need for manual allocation and deallocation.
2. Garbage Collection: It uses a garbage collector to clean up memory by removing objects that are no longer referenced.
3. Reference Counting: Every object has a reference count; when the count drops to zero, the object is eligible for garbage collection.
4. Private Heap Space: All Python objects and data structures are stored in a private heap, managed internally by the Python memory manager.
5. Minimizes Memory Leaks: Proper memory management helps prevent memory leaks and improves application stability and performance.
12. What are the basic steps involved in exception handling in Python?
A.
1. Identify Risky Code: Wrap the code that might cause an error inside a try block.
2. Catch the Exception: Use one or more except blocks to catch and handle specific exceptions that may occur.
3. Optional else Block: Use an else block to run code only if no exception occurred in the try block.
4. Use finally Block: Add a finally block to define code that should run no matter what, like closing files or releasing resources.
5. Raise Exceptions (if needed): Optionally, use raise to throw custom exceptions when certain conditions are not met.
13. Why is memory management important in Python?
A.Memory management is important in Python because it ensures efficient use of system resources, maintains program performance, 
and prevents crashes or memory leaks. Proper memory handling allows Python to automatically allocate and free memory for objects 
as needed, which is especially critical in large or long-running applications. Without good memory management, programs can consume 
excessive memory, slow down, or even terminate unexpectedly. It also helps developers focus on writing logic rather than worrying 
about low-level memory operations, thanks to features like garbage collection and reference counting.
14. What is the role of try and except in exception handling?
A. 
1. try Block: Wraps code that may cause an error during execution.
2. except Block: Catches and handles specific exceptions that occur in the try block.
3. Prevents Crashes: Helps the program continue running smoothly instead of crashing when errors occur.
4. Custom Error Handling: Allows you to define specific actions or messages for different types of exceptions.
5. mproves Code Robustness: Makes your code more reliable and user-friendly by handling unexpected issues gracefully.
15.  How does Python's garbage collection system work?
A. 
1. Automatic Memory Management: Python automatically manages memory using a built-in garbage collector to clean up unused objects.
2. Reference Counting: Each object has a reference count; when it drops to zero (no more references), the object is deleted.
3. Detecting Cycles: Python’s garbage collector can also detect reference cycles (where two or more objects reference each other but are no longer accessible).
4. gc Module: The gc module provides tools to interact with and control garbage collection manually, if needed.
5. Improves Performance: Garbage collection helps free memory space, preventing memory leaks and ensuring efficient resource use in long-running programs.
16. What is the purpose of the else block in exception handling?
A. The else block in Python exception handling is used to define a section of code that should execute only if no exceptions occur in the try block. 
Its purpose is to clearly separate the error-prone code from the code that should run when everything goes smoothly, improving the readability and 
structure of the program. While the try block contains potentially risky operations and the except block handles errors, the else block is ideal 
for post-processing logic that should only happen if the try block succeeds. Though it's optional, using an else block makes your exception handling 
more precise and organized, and it can be combined with a finally block for comprehensive control.
17. What are the common logging levels in Python?
A. The common logging levels in Python, from lowest to highest severity, are:

1. DEBUG – Used for detailed diagnostic information, mostly helpful during development.
2. INFO – Used to confirm that things are working as expected.
3. WARNING – Indicates a potential problem or something unexpected, but the program continues to run.
4. ERROR – Signifies a more serious problem that prevented some part of the program from functioning.
5. CRITICAL – Reports very serious errors that may prevent the program from continuing to run.
18. What is the difference between os.fork() and multiprocessing in Python?
A. The main difference between os.fork() and the multiprocessing module in Python lies in portability, usability, and abstraction level:
1. os.fork() is a low-level system call that creates a new child process by duplicating the current process. It's available only on 
Unix/Linux systems, not on Windows. It gives the programmer more control but requires manual handling of inter-process communication 
and resources.
2. The multiprocessing module is a high-level, cross-platform API in Python that allows the creation of independent processes. 
It abstracts away the system-level details and provides easy-to-use tools like Process, Queue, and Pool for parallel execution, 
communication, and synchronization between
19. What is the importance of closing a file in Python?
A.Closing a file in Python is important because it frees up system resources, ensures that all data is written properly, and prevents 
data corruption. When a file is open, it occupies system memory and file handles; if not closed, it can lead to resource leaks, especially 
when working with many files. Additionally, when writing to a file, Python may buffer the data—so closing the file ensures all buffered content 
is actually written to disk. Properly closing files also helps maintain data integrity and avoids unexpected behavior during future file operations. 
Using the with statement is the recommended way to handle files, as it closes them automatically.
20. What is the difference between file.read() and file.readline() in Python?
A. The difference between file.read() and file.readline() in Python lies in how much content they read from a file:
1. file.read() reads the entire contents of the file as a single string. It’s useful when you want to process the whole file at once.
2. file.readline() reads only one line at a time from the file, up to the next newline character. It's more memory-efficient for large files and ideal when you want to process the file line by line.
Example: 
with open("sample.txt", "r") as f:
    content = f.read()        
    f.seek(0)
    first_line = f.readline() 
21. What is the logging module in Python used for?
A. The logging module in Python is used to record messages about a program’s execution, which helps in debugging, monitoring, and tracking errors. It provides a flexible 
framework for emitting log messages from Python programs, supporting multiple levels of severity (DEBUG, INFO, WARNING, ERROR, and CRITICAL). Unlike using print() statements, 
logging allows messages to be directed to different outputs such as files, the console, or remote servers, and can be formatted with timestamps, error details, and more. This 
makes it a powerful tool for maintaining and troubleshooting both small scripts and large applications.
22. What is the os module in Python used for in file handling?
A. The os module in Python is used for interacting with the operating system, and it plays an important role in file handling operations. It allows you to perform tasks such as:
1. Creating, deleting, and renaming files and directories (os.remove(), os.rename(), os.mkdir(), os.rmdir()).
2. Navigating the file system using functions like os.chdir() (change directory) and os.getcwd() (get current directory).
3. Checking file or directory existence and properties with os.path.exists(), os.path.isfile(), and os.path.isdir().
4. Listing directory contents using os.listdir().
23. What are the challenges associated with memory management in Python?
A. The challenges associated with memory management in Python include:
1. Reference Cycles: Python uses reference counting for memory management, but when objects reference each other (circular references), they may not be immediately cleaned up without the help of the garbage collector.
2. Memory Leaks: If objects are unintentionally kept alive (e.g., through global references or caches), they may consume memory unnecessarily, leading to memory leaks over time.
3. High Memory Usage: Python abstracts memory management but may use more memory compared to lower-level languages, especially in large applications or data-heavy tasks.
4. Inefficient Use of Containers: Overusing large data structures like lists or dictionaries without releasing or clearing them can bloat memory usage.
5. Delayed Garbage Collection: Python’s garbage collector may not immediately reclaim memory, which can be a problem for memory-critical applications unless explicitly managed.
24. How do you raise an exception manually in Python?
A. age = -5
if age < 0:
    raise ValueError("Age cannot be negative")
25. Why is it important to use multithreading in certain applications?
A. Using multithreading is important in certain applications because it allows a program to perform multiple tasks concurrently, improving efficiency and responsiveness. Here are key reasons:
1. Improved Performance: Multithreading can significantly speed up applications by allowing them to perform multiple operations simultaneously, especially in I/O-bound tasks like file reading or network requests.
2. Responsiveness: In GUI applications, multithreading keeps the user interface responsive by offloading long-running tasks to background threads, preventing the UI from freezing.
3. Resource Sharing: Threads within the same process share memory and resources, making communication between them faster and more efficient than inter-process communication.
4. Scalability: Multithreading can help applications scale better on multi-core processors, allowing them to utilize available CPU cores effectively.
5. Simplified Design: For certain problems, using threads can lead to simpler code structures compared to managing multiple processes or asynchronous programming.
"""
#Practice Questions
# 1. How can you open a file for writing in Python and write a string to i?
with open("C:/Users/Asus/OneDrive/Desktop/assessment.txt", "w") as file:
    file.write("Hello, this is a sample string.")
# 2. Write a Python program to read the contents of a file and print each line?
with open("C:/Users/Asus/OneDrive/Desktop/assessment.txt", "r") as file:
    for line in file:
        print(line.strip())
# 3. How would you handle a case where the file doesn't exist while trying to open it for reading?
try:
    with open("C:/Users/Asus/OneDrive/Desktop/assessment.txt", "r") as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("The file does not exist.")
# 4. Write a Python script that reads from one file and writes its content to another file?
file_1_path = "C:/Users/Asus/OneDrive/Desktop/file_1.txt"
file_2_path = "C:/Users/Asus/OneDrive/Desktop/file_2.txt"
try:
    with open("C:/Users/Asus/OneDrive/Desktop/file_1.txt", "r") as f_1, open("C:/Users/Asus/OneDrive/Desktop/file_2.txt", "w") as f_2 :
        for line in f_1:
            f_2.write(line)
    print("File copied successfully.")
except FileNotFoundError:
    print("Source file does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
# 5. How would you catch and handle division by zero error in Python?
try:
    num = 10
    den = 0
    res = num / den
    print("Result", res)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
# 6. Write a Python program that logs an error message to a log file when a division by zero exception occurs?
import logging

logging.basicConfig(
    filename='error_log.txt',
    level = logging.ERROR,
    format =  '%(asctime)s - %(levelname)s - %(message)s'
)
try:
    num = 10
    den = 0
    res = num / den
    print("Result", res)
except ZeroDivisionError as e:
    logging.error("Attempted to divide by zero", exc_info=True)
    print("An error occurred. Check the log file for details.")
# 7. How do you log information at different levels (INFO, ERROR, WARNING) in Python using the logging module?
logging.basicConfig(
    filename='app_log.txt',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logging.debug("This is a debug message.")
logging.info("This is an info message.")
logging.warning("This is a warning message.")
logging.error("This is an error message.")
logging.critical("This is a critical message.")
# 8. rite a program to handle a file opening error using exception handling?
filename2 = "file_3.txt"
try:
    with open(filename2, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"Error: The file '{filename2}' does not exist.")
except PermissionError :
    print(f"Error: Permission denied to read the file '{filename2}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
# 9. How can you read a file line by line and store its content in a list in Python?
try:
    with open("C:/Users/Asus/OneDrive/Desktop/assessment.txt", "r") as file:
        lines = file.readlines()
    print(lines)
except FileNotFoundError:
    print("The file does not exist.")
# 10. How can you append data to an existing file in Python?
try:
    with open("C:/Users/Asus/OneDrive/Desktop/assessment.txt", "a") as file:
        file.write("\nAppending this line to the existing file.")
    print("Data appended successfully.")
except Exception as e:
    print(f"An error occurred while appending data: {e}")
# 11. Write a Python program that uses a try-except block to handle an error when attempting to access a dictionary key that doesn't exist
x = {
    'name' : 'Johnny',
    'Age' : 25
}
try:
    print("City of person:", x['city'])
except KeyError:
    print("Error: The key 'city' does not exist in the dictionary.")
# 12. Write a program that demonstrates using multiple except blocks to handle different types of exceptions
try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print("Result:", result)

    my_list = [1, 2, 3]
    print("Fourth item:", my_list[3]) 

except ValueError:
    print("Error: Invalid input. Please enter numeric values only.")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except IndexError:
    print("Error: List index out of range.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
# 13. How would you check if a file exists before attempting to read it in Python?
import os
file_path = "C:/Users/Asus/OneDrive/Desktop/assessment.txt"
if os.path.exists(file_path):
    with open(file_path, "r") as file:
        content1 = file.read()
        print(content1)
else:
    print("File doesnt exists.")
# 14. Write a program that uses the logging module to log both informational and error messages?
logging.basicConfig(
    filename='app_log.txt',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logging.info("Program Started successfully.")
try:
    num3 = 10
    den3 = 0
    res3 = num3 / den3
except ZeroDivisionError as e:
    logging.error("Attempted division by zero", exc_info=True)
    print("An error occurred. Check the log file for details.")
logging.info("Program finished running.")
# 15. Write a Python program that prints the content of a file and handles the case when the file is empty?
def read_file(file_path_1):
    try:
        with open(file_path_1, "r") as file:
            content2 = file.read()
            if content2.strip() == "":
                print("The file is empty.")
            else:
                print("File content:\n", content2)
    except FileNotFoundError:
        print(f"Error: The file '{file_path_1}' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

file_path_1 = "C:/Users/Asus/OneDrive/Desktop/assessment.txt"
read_file(file_path_1)
# 16. Demonstrate how to use memory profiling to check the memory usage of a small program?
from memory_profiler import profile
@profile
def create_list():
    my_list1 = [i for i in range(10000)]
    return my_list1
if __name__ == "__main__":
    create_list()
# 17. Write a Python program to create and write a list of numbers to a file, one number per line?
num4 = [1,2,3,4,6]
file_path_2 = "C:/Users/Asus/OneDrive/Desktop/numbers.txt"
try: 
    with open(file_path_2, "w") as file:
        for num in num4:
            file.write(f"{num}\n")
    print("Numbers written to file successfully.")
except Exception as e:
    print(f"An error occurred while writing to the file: {e}")
# 18. How would you implement a basic logging setup that logs to a file with rotation after 1MB?
from logging.handlers import RotatingFileHandler
log_file = "C:/Users/Asus/OneDrive/Desktop/numbers.txt"
handler = RotatingFileHandler(
    log_file, maxBytes=1 * 1024 * 1024, backupCount=5
)
formatter = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(message)s'
)
handler.setFormatter(formatter)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)
for i in range(10000):
    logger.info(f"This is log entry number {i}")
# 19. Write a program that handles both IndexError and KeyError using a try-except block?
my_list_2 = [3,5,7,9,10]
my_dic = {
    'name' : 'Vijay',
    'age' : 30
}
try:
    print("List item:", my_list_2[5])
    print("Dictionary value:", my_dic['city'])
except IndexError:
    print("IndexError: Tried to access a list index that is out of range.")

except KeyError:
    print("KeyError: Tried to access a dictionary key that doesn't exist.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
# 20. How would you open a file and read its contents using a context manager in Python?
file_path_3 = "C:/Users/Asus/OneDrive/Desktop/assessment.txt"
try:
    with open(file_path_3, "r") as file:    
        content3 = file.read()
        print(content3)
except FileNotFoundError:
    print(f"Error: The file '{file_path_3}' does not exist.")
# 21. Write a Python program that reads a file and prints the number of occurrences of a specific word
def count_word_occurrences(file_path, target_word):
    try:
        with open(file_path, "r") as file:
            content = file.read()
            words = content.lower().split()
            count = words.count(target_word.lower())
            print(f"The word '{target_word}' occurred {count} times.")
    except FileNotFoundError:
        print(f"The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
file_path = "C:/Users/Asus/OneDrive/Desktop/assessment.txt"
target_word = "sample"
count_word_occurrences(file_path, target_word)
# 22. How can you check if a file is empty before attempting to read its contents?
file_path_4 = "C:/Users/Asus/OneDrive/Desktop/assessment.txt"
if os.path.exists(file_path):
    if os.path.getsize(file_path) == 0:
        print("The file is empty.")
    else:
        with open(file_path, "r") as file:
            print(file.read())
else:
    print("The file does not exist.")
# 23. Write a Python program that writes to a log file when an error occurs during file handling?
logging.basicConfig(
    filename='file_handling_errors.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
def read_file(file_path):
    try:
        with open(file_path, "r") as file:
            content = file.read()
            print("File content:\n", content)
    except FileNotFoundError:
        logging.error("File not found: %s", file_path)
        print("Error: The file was not found.")
    except PermissionError:
        logging.error("Permission denied: %s", file_path)
        print("Error: Permission denied to access the file.")
    except Exception as e:
        logging.error("An unexpected error occurred: %s", str(e), exc_info=True)
        print("An unexpected error occurred.")
file_path = "C:/Users/Asus/OneDrive/Desktop/nonexistent.txt"
read_file(file_path)