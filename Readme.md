Data_Block_Loader
=================

This is a simple function to load from a text file a particular block of data that is headed with some identification text.

Given a text file with blocks of data (each block headed with some title or comment), the function Data_Block_Loader() (see below) loads the data block from the file and return a list of data columns (tuples). It has been tested in Python 2.7.6 and in Python 3.4.1, and only makes use of the standard library (no use of Numpy or Scipy).
For very large data sets, a Numpy implementation would be desirable to avoid computing costs at loops. For normal data sets, this function should be more than enough.

Enjoy!
Jesús Martínez-Blanco