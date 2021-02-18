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

## 10. Initialize Cache

The Cache is initialized using ‘jdeCacheInit’ API. This is the most important step for creating a cache.

‘jdeCacheInit’ initializes a named cache, associates the initialized cache with a user and returns a handle to the initialized cache. This API contains four things:

1. Creates a cache in memory.
1. Creates an index that will be used to access records in the cache.
1. Names the cache with the name passed in this API.
1. Associates the cache with a cache handle (HCACHE) that the user will use to reference the cache in call to JDE Cache 1. APIs.

![Initialize Cache](https://raw.githubusercontent.com/GiovaniPM/DMNTests/main/Courses/JDE%20Cache/2gjwkt4u.bmp)

## 11. Cache Processing

Most of the time cache processing is consist of adding, updating, fetching and deleting the cache.

Some of them are listed below:

### Cache Add/Update

‘jdeCacheAdd’ adds a record to the cache identified by the cache handle hCache that was obtained from the call to ‘jdeCacheInit’.

‘jdeCacheUpdate’ updates the record that is currently being pointed to by the passed HJDECURSOR with the passed data.

![Cache Add/Update](https://raw.githubusercontent.com/GiovaniPM/DMNTests/main/Courses/JDE%20Cache/sbsb5k40.bmp)

### Cache Single Fetch

‘jdeCacheFetchPosition’ retrieves the record that corresponds to the given key. This API can be used to position the HJDECURSOR to a specific location within the data set. When a call to jdeCacheFetch is made, it will start fetching from the next position. This is useful for making sequential fetches beginning at a specific location in the cache.

![Cache Fetch Single](https://raw.githubusercontent.com/GiovaniPM/DMNTests/main/Courses/JDE%20Cache/t4tpy2gf.bmp)

### Cache Multiple Fetch

Multiple fetch is possible through the  ‘JdeCacheFetch’ API. ‘JdeCacheFetch’ advances the cursor to the next record in the data set relative to the current cursor position and retrieves the record. This will now be the new position associated with HJDECURSOR. This API does not search for a record in the cache but fetches whatever record is after the record that is currently being pointed to the passed HJDECURSOR. The API is ideal for performing sequential fetches

![Cache Multiple Fetch](https://raw.githubusercontent.com/GiovaniPM/DMNTests/main/Courses/JDE%20Cache/3ci2vjt2.bmp)

### Cache Delete

‘jdeCacheDelete’ is the API that deletes the record that is pointed by the cursor. Only one record can be deleted at a time.

![Cache Delete](https://raw.githubusercontent.com/GiovaniPM/DMNTests/main/Courses/JDE%20Cache/afu9mc5s.bmp)

### Cache Terminate

Once all the processing is complete, the memory allocated for cache should be destroyed. ‘jdeCacheTerminateAll’ destroys all caches with the same name as the one with the given hCache. The caches are physically removed from memory.

![Cache Terminate](https://raw.githubusercontent.com/GiovaniPM/DMNTests/main/Courses/JDE%20Cache/s1qxvfe8.bmp)

Sample code (below) for creating cache is given for reference.