# E1 Cache Concepts – JDB Cache – Part 1 

In previous articles, have shared the JDE Cache concepts and its creation. JDE has two types of cache, the one we have explained in recent posts is known as **User Cache** or **JDECACHE**.

This article will speak about the second type of cache which JDE offers to its users which is called **JDB F98613/ DB Cache**.

As we know storing database data in program memory rather than fetching it from database is known as **Caching**. This helps in eliminating the overhead of database.

JDB Cache is not a shared memory accessed by all processes rather it is local heap memory to each process. Every process has its **own copy** of DB cache.

JDB cache is an **automated table caching** mechanism feature in EnterpriseOne.

When the process completes, JDB cache will also **goes away** with the process into the bit bucket.

JDB Cache can be implemented through **C Code in Business Function or Event Rules** of JDE.

There is no **replication or synchronization** across each of the JDB cache instances.

Implementing JDB cache can help in **improving the performance** of the process provided it is done after complete analysis.

JDB cache is local process heap memory and it is limited to a **total of 2GB** in 32-bit operating systems.

In next article we will see the how we can **implement** and what are the **conditions** to use the JDB Cache in EnterpriseOne.

Reference:
- JDB cache in EnterpriseOne
- JDEdwards EnterpriseOne Applications Task Force