# JDE Business Function and Cache Concepts – Part 1 

Using the Cache or caching is one of the fundamental concepts for web applications or say any application. Be it Database tier, Application tier, or Web tier. In JD Edwards, Caching is done on the Application tier through code, and web tier through the Server manager (HTML Server). 

We can go through the code based caching, which is typically done through Business Function (BSFN). 

We always use or see the few business function parameters which JDE uses for communicating or passing information

## LPBHVRCOM

- Pointer to a data structure used for communications with business functions
- It has capability to identify the current software version
- It will identify the current user’s access privilege
- It has parameters which will handle the current window and controls in the window
- It can identify the current control which has focus
- It identifies the current timing of the event being processed
- It has ID component for global run time Identifier for job running from menu driver
- It has information about system preferences
- It has information about user preferences
- It can display error message ID or 0L
- It will set the flag to TRUE when changing database behavior
- It contains error message event key for event rules
- It has information about environment handle for ODBC
- It contains pointers for section of RDA
- It has error linked list for batch programs
- It stores form runtime information for FDA
- It has flag which will indicate runtime call or business function call
- It stores flag to indicate remote or 3rd party call object
- It has subscription/publish Address Info of application
- It holds the logic process ID of the caller of API jdeLaunchUBEEx
- It contains future use area for new items as well

## LPVOID


- Pointer to a void data structure currently used for error processing
- It will be used for security in the future.

We have **Master Business Function** for most of the processes which inserts data in transaction tables. Each master business function uses Begin Doc, Edit Line, Edit Doc and End Doc to insert the records in the tables.

In simple layman term, below are the usage of each function which gets called in sequence to create the records.

|Function Name|Usage|
|:-----|:-----|
|Begin Doc|Initialize both Header and Detail Cache<br>Add or Update the Header|
|Edit Line|Add Detail Cache Record|
|Edit Doc|Read Header Cache<br>Update Header Cache|
|End Doc|Read the Records from Header and Detail Cache and write to tables|
|Clear Doc|Delete Header Cache<br>Read Detail Cache<br>Delete Detail Cache<br>Terminate Cache|

## What is Cache:

Cache is a memory which has recently used information and can be accessed extremely fast for performing data manipulation while creating or updating a transaction in an application.

## Pros of Using Cache:


- Cache improves the performance of application where it has been used.
- Cache reduces the load on servers.
- Using cache we can store data from multiple tables and access them as and when require.
- Cache is useful in place of temporary tables by reducing load on the servers.

## Cons Of Using Cache:


- Cache has a limitation of storage capacity.
- Implementing cache require knowledge of JDECACHE APIs.
- Troubleshooting of cache memory is difficult.

Few **Cache APIs** which we use commonly to create the cache and use it to store and update records:

|Proposal|Command|
|:-----|:-----|
|Connect to OneWorld|JDB_InitBhvr|
|Create Index Data Structure Definition|Index.CacheKey[n].nOffset<br>Index.CacheKey[n].nSize<br>Index.CacheKey[n].idDataType|
|Initialize the Cache|jdeCacheInit|
|Add a record to Cache|jdeAddCache|
|Open a cursor in Cache|jdeCacheOpenCursor|
|Any Cache manipulation|Cursor Advancing:<br>   Þ jdeCacheFetch<br>   · jdeCacheFetchPosition<br>   · jdeCacheResetCursor<br>Non Cursor Advancing:<br>   · jdeCacheUpdate<br>   · jdeCacheDelete|
|Close the Cursor|jdeCacheCloseCursor|
|Terminate the Cache|jdeCacheTerminate|
|Free Behavior|JDB_FreeBhvr|