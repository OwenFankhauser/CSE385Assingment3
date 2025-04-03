# CSE385Assingment3
In this assignment your goal is to create a GUI application that creates a network connection between your application frontend and your database backend using the JDBC connector.

Page
1
of 3
Summary
In this assignment your goal is to create a GUI application that creates a network connection between
your application frontend and your database backend using the JDBC connector.
Your application will establish a connection to the world database and retrieve data from a specific
table and specific columns. Then this data is to be displayed in your application in a table using a native
table GUI element (Such as a JTable in Java).
Details
This application must be a GUI application. No command line or terminal applications are allowed. For
this assignment, you may use either JAVA or PYTHON only; no other languages are allowed (though
other langues will be allowed in the final project).
Your application will connect to your database using the JDBC connector for Java or the MySQL
connector for Python. Links to the official documentation for both of these libraries are provided
below:
Java and JDBC
• https://dev.mysql.com/doc/connector-j/en/connector-j-usagenotes-basic.html
Python and MySQL Connector
• https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html
Once you have established a connection to your database, you are to retrieve the entire world.city
table. You may use the following code to retrieve the entire table.
SELECT * FROM world.city;
The end result should look similar to (but not exactly the same) as the picture below.
The point of this picture is to show the bare minimum needed for this assignment. From this picture we
see that you only need something that displays the data; you don’t need any buttons or user interactivity
or anything of that sort. You DO need the ability to see all the data via something like a scroll bar
(because there will be many hundreds of records and that will not fit into a single screen).
You will need to make sure that all the rows and all the columns are properly displayed with the correct
column headers. Again, the picture is for references. You will need to find the correct headers for the
table that you will be reading from.
You are to use one of three possible connection methods. Two of them we discussed in class and the
third option is left for you to explore on your own and earn a few extra credit points if you choose to do
so. The three connection options are:
• Driver Manager style connection
◦ This is where connection information (such as ip address or user name) is embedded
directly in the code
• Data Source style connection
◦ Connection information is stored in an external file. This file is then accessed via a relative
file path (NOT an absolute file path
• Connection Pooling style connection
◦ A finite number of connections are permanently established and each connection thread
request an available connection that is not closed when finished
◦ Your connection pool must have a pool size of at least 3 if you choose this option
Grading
This assignment is graded on completion and function not on form. So long
as your application is usable and viewable and functional, I do not care about
if it ‘looks good’. This is a database class not a UI/UX class. Your application
must still be usable and functional, but I do not care about background color or similar such notions.
Grading scheme
Grading is out of 100 points. Partial credit is awarded for partially completed
work. Extra credit is also available based on the work completed.
• Application runs and displays a GUI (10)
• Application displays data from the file correctly (10)
• Application connects to the database and retrieves data (70-90)
◦ Uses Driver Manager style connection (70)
◦ Uses a Data Source style connection (80)
◦ Uses a Connection Pooling style connection (90)
