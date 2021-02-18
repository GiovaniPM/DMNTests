# JDE Business Function and Cache Concepts – Part 3 

In our last article (part 2) we demonstrated the process of cache creation business function (step by step) using cache APIs and explained the purpose of cache APIs.

In this article we will see how to use the cache business function in JDE object and how the values will get stored in cache and how can we manipulate the same.  

Steps for using the business function

## 1. Create the application to pass or retrieve the values as given below

![Form](https://raw.githubusercontent.com/GiovaniPM/DMNTests/main/Courses/JDE%20Cache/0mplafhi.bmp)

Action Code Values:

1. Add/Update
2. Fetch based on key
3. Delete from cache

## 2. In Add Record Button Call the C BSFN to add the records in cache

![Add](https://raw.githubusercontent.com/GiovaniPM/DMNTests/main/Courses/JDE%20Cache/8drx92cw.bmp)

## 3. In Update Record Button Call the C BSFN to update the records in cache

![Update](https://raw.githubusercontent.com/GiovaniPM/DMNTests/main/Courses/JDE%20Cache/2pn6zl49.bmp)

## 4. In Fetch Record Button Call the C BSFN to fetch the records from cache

![Fetch](https://raw.githubusercontent.com/GiovaniPM/DMNTests/main/Courses/JDE%20Cache/j3smdgc5.bmp)

## 5. In Delete Record Button Call the C BSFN to add the records from cache

![Delete](https://raw.githubusercontent.com/GiovaniPM/DMNTests/main/Courses/JDE%20Cache/3d7isns2.bmp)

## 6. Run the application in web client and key in the values for inserting the record in cache and press the Add Record button

![Cache 1](https://raw.githubusercontent.com/GiovaniPM/DMNTests/main/Courses/JDE%20Cache/jvj2l6rd.bmp)

We can see the values have been added in cache after jdeCacheAdd API is called in the C BSFN

![Cache 2](https://raw.githubusercontent.com/GiovaniPM/DMNTests/main/Courses/JDE%20Cache/zko0oi6b.bmp)