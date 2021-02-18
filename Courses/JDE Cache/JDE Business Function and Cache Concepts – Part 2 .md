# JDE Business Function and Cache Concepts – Part 2 

In our last article(part 1) we gave an overview of standard parameters of Business Function and usage of master business functions, also we spoke about cache APIs and its usage.

In this article we will demonstrate the process of cache creation using cache APIs and in our next article we will see how to use this BSFN to insert/update/fetch the data in/from cache.

Steps for Creating a Cache

## 1. Data structure Creation

Create a Datastructure for the Business Function.

Few parameters are compulsory in data structure to build a cache and other parameters are dependent on the requirement.

- Cachename – Mandatory
- ActionCode – Mandatory
- Cursor – Mandatory

![Cache Data Structure](https://raw.githubusercontent.com/GiovaniPM/DMNTests/main/Courses/JDE%20Cache/ej0lzbf7.bmp)

## 2. Attach the Data structure to C BSFN

![Attach DS to BSFN](https://raw.githubusercontent.com/GiovaniPM/DMNTests/main/Courses/JDE%20Cache/nr7xbz9b.bmp)

## 3. Generate the Skeleton for the Business function

![Function Creation](https://raw.githubusercontent.com/GiovaniPM/DMNTests/main/Courses/JDE%20Cache/a9wzpec0.bmp)
![Function Prototype](https://raw.githubusercontent.com/GiovaniPM/DMNTests/main/Courses/JDE%20Cache/jby2fxmt.bmp)

## 4. Create Data structure definition in the .h file

![DS Design](https://raw.githubusercontent.com/GiovaniPM/DMNTests/main/Courses/JDE%20Cache/o1kxvqol.bmp)
![DS .h](https://raw.githubusercontent.com/GiovaniPM/DMNTests/main/Courses/JDE%20Cache/jgj3nt0m.bmp)

## 5. Define the Cache Structure in .h

![Cache DS](https://raw.githubusercontent.com/GiovaniPM/DMNTests/main/Courses/JDE%20Cache/avk28gbz.bmp)

## 6. Define the Cache Key Structure in .h file

![Cache Key](https://raw.githubusercontent.com/GiovaniPM/DMNTests/main/Courses/JDE%20Cache/zvpwa2hl.bmp)

## 7. Create Instances For Cache and Cache Key in .c file

![Instances](https://raw.githubusercontent.com/GiovaniPM/DMNTests/main/Courses/JDE%20Cache/idgw25eb.bmp)

## 8. Declare pointers and Variables in .c file

![Pointers](https://raw.githubusercontent.com/GiovaniPM/DMNTests/main/Courses/JDE%20Cache/6plq3scq.bmp)

## 9. Initialize User

![Initialize User](https://raw.githubusercontent.com/GiovaniPM/DMNTests/main/Courses/JDE%20Cache/dcjf2pe9.bmp)

## Initialize Cache

The Cache is initialized using ‘jdeCacheInit’ API. This is the most important step for creating a cache.

‘jdeCacheInit’ initializes a named cache, associates the initialized cache with a user and returns a handle to the initialized cache. This API contains four things:

1. Creates a cache in memory.
1. Creates an index that will be used to access records in the cache.
1. Names the cache with the name passed in this API.
1. Associates the cache with a cache handle (HCACHE) that the user will use to reference the cache in call to JDE Cache 1. APIs.
