<div align="center">

![Title](http://satyr.io/1000x80/1?text=How+Install+JD+Edwards+Demo+Version)
![Title](http://satyr.io/1000x80/white?text=by)
![Title](http://satyr.io/1000x80/white?text=Giovani+Perotto+Mesquita)
![Title](http://satyr.io/1000x80/white?text=Thanks+to)
![Title](http://satyr.io/1000x80/white?text=RestfulClouds)
[![Email](https://img.shields.io/badge/mail-giovanipm%40gmaill.com-lightgray.svg)](mailto:giovanipm@gmail.com)

</div>

<br>
<br>
<br>

---

<div align="right">

[![JD Edwards 9.20](https://img.shields.io/badge/JD_Edwards-9.20-brightgreen.svg)](https://www.oracle.com/technical-resources/documentation/jd-edwards-enterpriseone.html)

</div>

<div align="center">

# JD Edwards 9.2 Standalone (DEMO) Installation Tutorial 

</div>

Standalone 9.2 Install JD Edwards Enterprise One 9.2 Standalone Demo (Oracle version) on your PC or server with this step by step guide.

![Welcome](https://raw.githubusercontent.com/GiovaniPM/DMNTests/main/Courses/JDE%20INSTALL/Images/w06p9oaa.bmp)

## Pay attention

1. This version (according to the Oracle Docs) is designed to run on Windows 7 x64, Windows 2012 R2, Windows 8.1 Even you 1. install successfully in another version of Windows 64, some business functions don’t work as expected, so, stay with Windows 1. 7 or 2012 R2 or 8.1 x64 and everything should work as expected.
1. Before you start with anything, turn OFF your Anti-virus, Firewall and Disable UAC (User Access Control). For security 1. purposes you could enable again the Firewall and Anti-virus AFTER the installation was completed.
1. From Release E920 OC4J is removed. So first we have to install Oracle Weblogic Server using 32 bit JDK

This procedure was a result from information that I gathered from tips from another users and “trial and error” tests. Suggestions and comments are always welcome.

Before we get started, if you find any issue, do read through the comments or visit the [troubleshooting guide for 9.2 installation](https://www.jdesource.com/enterpriseone/jd-edwards-standalone-e920-troubleshooting-guide/)

## Let's GO


1. Certification or MTR for JD Edwards Standalone can be verified from certification tab of support portal. **<span style="color:red;">⚠️Tips:</span>** JD Edwards Standalone Certification can be verified under product “JD Edwards Development client”
1. We verified the certifications, now we need to install the below components for complete the installation of JD Edwards 9.2 Standalone Successfully.
1. Software Download
1. Prerequisites
1. Installation of Oracle Web logic Server
1. Installation of Oracle 12c Client
1. Installation of Oracle E1local 12c DB
1. Installation of Standalone Development client

Standalone 9.2, Oracle WebLogic Server , Oracle 12c Client Setup files can be download from [Oracle Software Delivery Cloud](https://edelivery.oracle.com/)

## 1. Software Download

In the [Oracle Software Delivery Cloud](https://edelivery.oracle.com/) home page, login using your credentials. Accept the “Export Restrictions” and this will lead to the Product Selection screen.

### JDE 9.2

For Product select “**JD Edwards EnterpriseOne System Foundation**” and Platform as “**Microsoft Windows x64 (64-bit)**“

![JDE1](https://raw.githubusercontent.com/GiovaniPM/DMNTests/main/Courses/JDE%20INSTALL/Images/zrbk9sov.bmp)

JD Edwards 9.2 Standalone Setup files comes in 4 zip files .This setup files are divided in two parts JD Edwards Standalone components and Oracle Database 12c components.

![JDE2](https://raw.githubusercontent.com/GiovaniPM/DMNTests/main/Courses/JDE%20INSTALL/Images/nid962z4.bmp)

### Oracle 12C

As JD Edwards is 32 bit software, we need to install Oracle 12C 32 bit clientfor DB connection. For Product select “**Oracle Database Enterprise Edition**” and Platform as “**Microsoft Windows x64 (64-bit)**“

![ORACLE1](https://raw.githubusercontent.com/GiovaniPM/DMNTests/main/Courses/JDE%20INSTALL/Images/s0avbagr.bmp)

Download the Oracle 12C 32 bit software (V47124-01.zip) setup file.

![ORACLE2](https://raw.githubusercontent.com/GiovaniPM/DMNTests/main/Courses/JDE%20INSTALL/Images/48hnohds.bmp)

### WebLogic

For Product select “**Oracle Weblogic Server Enterprise Edition**” and Platform as “**Microsoft Windows x86 (32-bit)**“

![WL1](https://raw.githubusercontent.com/GiovaniPM/DMNTests/main/Courses/JDE%20INSTALL/Images/y5bcifoe.bmp)

Download the Oracle Web logic Server (V44413-01.zip) Setup file.

![WL2](https://raw.githubusercontent.com/GiovaniPM/DMNTests/main/Courses/JDE%20INSTALL/Images/qdj1sprk.bmp)

## 2. Prerequisites

JD Edwards E920 Standalone client requires some of the prerequisites software to works perfectly

1. Install 32 bit [JDK – Oracle JDK 1.7.0_91](http://www.oracle.com/technetwork/java/javase/downloads/java-archive-downloads-javase7-521261.html)
1. Install [Microsoft Visual C++ RTL 2013](https://www.microsoft.com/en-au/download/details.aspx?id=40784) (x86 & x64)
1. Install [Microsoft Visual Studio 2013](https://www.microsoft.com/en-au/download/details.aspx?id=44914).(Required for BSFN development)
1. Install [PDF Reader](https://www.foxitsoftware.com/products/pdf-reader/), Chrome or [Firefox](https://www.mozilla.org/en-US/firefox/new/)

## 3. Install

### 3.1. Installation of Oracle Weblogic Server

From Release 9.2, OC4J has been removed so we need to install Oracle Weblogic Server for installing Local Web client

The Standalone Web Client can be only Installed on Oracle WebLogic Server application server.

Extract the download weblogic setup (V44413-01 zip)file in desktop or any folder, we will get the jar file **fmw_12.1.3.0.0_wls.jar**.

Now Open the Command Prompt as **<span style="color:red;">Run administrator</span>** and use cd command to navigate to 32 bit Java Installed location( cd C:\Program Files (x86)\java\jdk1.7.0_91\bin) and run the weblogic Server Installer using the below command (Java -jar c:\users\JDE\Desktop\fmw_12.1.3.0.0_wls.jar)

Enter the Oracle_Home as per your requirement and once installation completed uncheck the automatically launch the configuration wizard as shown in the below screen shot and click on finish.

![WL1](https://raw.githubusercontent.com/GiovaniPM/DMNTests/main/Courses/JDE%20INSTALL/Images/jb6up0lz.bmp)

**<span style="color:red;">📓Note:</span>** No need to create a domain for web logic server

### 3.2. Install Oracle 12C 32 bit Client

From Release E920 with Oracle 12C 32 bit Client required non-administrator user for the Installation.

Unzip **V47124-01.zip** the file and run the Oracle Client Setup (“Setup.exe”) program.

**<span style="color:red;">🛑Very important:</span>** Select Option 2 Administrator Option while installing Oracle DB 12c Client. Oracle Documentation state that “Runtime” also will work. So you may use them if running low on space.

**<span style="color:red;">📓Note:</span>** Oracle 12c 32 bit Client required non-administrator user for Installation, during the installation Enter the non-administrator user for installing Oracle 12c Client. If you already created non admin user use option 1 or use option 2 allow OUI to create non admin user ID.

![Oracle1](https://raw.githubusercontent.com/GiovaniPM/DMNTests/main/Courses/JDE%20INSTALL/Images/s133rsut.bmp)

Now, it’s time to install Oracle E1local DB 12c and JDE standalone Client itself. The install process is divided in two parts: the first install the Oracle Database and the second the JDE Client. The four files that we downloaded earlier must be combined to make a working setup installation extract the four files and you will have a folder structure like this.

**<span style="color:red;">V100564-01-zip, V97804-01-zip, V97805-01-zip, V97806-01-zip</span>**


1. Move the contents from folder V97805-01-01 to folder V97806-01
1. Move the contents from folder V97804-01-01 to folder V100564-01
1. Now Move the contents from folder V97806-01-01 to folder V100564-01\ThirdParty\ORACLE

**<span style="color:red;">📓Note:</span>** Now rename the Folder V100564-01 as standalone. It has the correct structured installation setup files.

Follow the below screenshots

Extract all 4 Setup files

![Oracle2](https://raw.githubusercontent.com/GiovaniPM/DMNTests/main/Courses/JDE%20INSTALL/Images/sinv7am8.bmp)

1. Move the contents from folder V97805-01-01 to folder V97806-01

![Oracle3](https://raw.githubusercontent.com/GiovaniPM/DMNTests/main/Courses/JDE%20INSTALL/Images/9dnmqu39.bmp)

2. Move the contents from folder V97804-01-01 to folder V100564-01
2. Now Move the contents from folder V97806-01-01 to folder V100564-01\ThirdParty\ORACLE

**<span style="color:red;">📓Note:</span>** Now rename the Folder V100564-01 as standalone. It has the correct structured installation setup files.

### 3.3. Install E1Local 12c DB

From Release E920, Oracle E1local DB 12C required non-administrator user for Installation. Run the “InstallManager.exe”. Click Enterpriseone Oracle 12c Database Engine on JD Edwards Install Manager

![JDE1](https://raw.githubusercontent.com/GiovaniPM/DMNTests/main/Courses/JDE%20INSTALL/Images/00p8meim.bmp)

In the next screen as we already created Non admin user while installing Oracle 12c 32 bit client, Use the Option 1 and provide the non-administrator credentials and click on Next. Once E1local 12C Successfully Installed, we will receive a saying that message “E1local successfully installed”. Now click yes to reboot the machine.

![JDE2](https://raw.githubusercontent.com/GiovaniPM/DMNTests/main/Courses/JDE%20INSTALL/Images/8ab4r565.bmp)

**<span style="color:red;">Once this is completed, check the following</span>**

Oracle has noted that there is a problem with IMPDP.exe and EXPDP.exe in their 12c database client software.
The solution: Ensure that both the 32-bit client and the 64-bit client are both in your PATH. (ie: c:\app\oracle\product\12.1.0\client_1\bin;C:\Oracle\E1Local\bin). Rename the impdp.exe and expdp.exe in the c:\app\oracle\product\12.1.0\client_1\bin folder to impdp.exe.bak and expdp.exe.bak. The install will then use the impdp.exe from the database install and everything will work.  You can find the Path Envt variables in the System Settings (from control panel) – Advanced Tab – Environment Variables – System Variables

### 3.4. Install JD Edwards E920 Standalone Client

Once Machine rebooted we are ready to Install JD Edwards E920 Standalone client. Open InstallManager.exe as run as administrator. Click EnterpriseOne Standalone client on JD Edwards Install Manager. Enter the Installation path as per your requirement (i.e C:\JDEdwards\E920_1).

![JDE3](https://raw.githubusercontent.com/GiovaniPM/DMNTests/main/Courses/JDE%20INSTALL/Images/n5gmy46n.bmp)

In the Next screen the select the package and click on next

![JDE4](https://raw.githubusercontent.com/GiovaniPM/DMNTests/main/Courses/JDE%20INSTALL/Images/4ph95hml.bmp)

**<span style="color:red;">⚠️Tips:</span>** If you face error message “Unable to connect to Database” in this step.

Could be the configuration issue with listener.ora & tnsnames.ora. Best Practice Provide the Hostname(Instead of IP or Localhost) as machine name in both the files.

JDK will not be shipped with E920 Installer. Install JDK and provide the path of the JDK as below and click on Next

**<span style="color:red;">Summary:</span>** This screen will shows the information which we provided in the above Steps. Verify it once more before we click on Install button.

![JDE5](https://raw.githubusercontent.com/GiovaniPM/DMNTests/main/Courses/JDE%20INSTALL/Images/vfhl1rd2.bmp)

JD Edwards Standalone E920 Installation will goes for minimum 2 hours and more (**<span style="color:red;">📓Note:</span>** Time to complete the installation depends on Ram of your machine)

After the Installation of JD Edwards Standalone client completed, Installer automatically start to configure the Local web. During the local web configuration. We need to provide the web logic password(**welcome1**) for creating the domain and managed server for local web client as shown below

![JDE6](https://raw.githubusercontent.com/GiovaniPM/DMNTests/main/Courses/JDE%20INSTALL/Images/gvxer7en.bmp)

Installation of Local Web client will takes sometimes to configure the Local Web client on Oracle Weblogic Server 12C. Click on Exit Once you received below message.

![JDE7](https://raw.githubusercontent.com/GiovaniPM/DMNTests/main/Courses/JDE%20INSTALL/Images/w7df42et.bmp)

### 3.5. Post Installation Task

Copy the file tnsnames.ora from the location C:\Oracle\E1local\Network\ADMIN to the location C:\app\Oracle\product\12.1.0\network\admin

**<span style="color:red;">⚠️Tips:</span>** Oracle 12c 32 client required for JD Edwards to connect to E1loccal (64 bit) DB & Main DB (64 bit)

Click on JD Edwards Icon on the Desktop and Enter username: **DEMO**, Password: **DEMO**.

![JDE8](https://raw.githubusercontent.com/GiovaniPM/DMNTests/main/Courses/JDE%20INSTALL/Images/fddgy1wr.bmp)

![JDE9](https://raw.githubusercontent.com/GiovaniPM/DMNTests/main/Courses/JDE%20INSTALL/Images/899t44i6.bmp)

Now You will be successfully Logged into DEMO920 Environment

### 3.6. Verify the Login and Local web client

Open the JD Edwards icon on the desktop and Enter the username as DEMO and Password as DEMO. Now you will be able to login into JDE Fat client.

Go to Tools  EnterpriseOne Menu to start the local web client. It will start the web logic server , now Internet explorer will open the web client as shown below

![JDE10](https://raw.githubusercontent.com/GiovaniPM/DMNTests/main/Courses/JDE%20INSTALL/Images/vpmx1fdr.bmp)

We have installed JD Edwards 9.2 Demo Successfully. Cheers!!!

## Config files

For those who have issues with the Demo installation – Attached are the ini files from Jerome (jde.ini, jdbj.ini, jdeinterop.ini)

[E92 Standalone ini Files](https://www.jdesource.com/wp-content/uploads/E92-Standalone-ini-Files.zip)

### jdbj.ini
``` dos
#=======================================================================
#                    jdbj.ini - JDBj configuration
#
# This file contains configuration information for JDBj, which provides 
# general database access capabilities on behalf of J.D. Edwards Java 
# solutions.
#=======================================================================

#=======================================================================
#                    OneWorld specific information 
#
# These sections apply only when accessing OneWorld data.  These 
# sections are ignored for standalone database access.
#=======================================================================

#-----------------------------------------------------------------------
# Bootstrap session
#
# This information is used to sign on to provide access to system 
# tables.  JDBj signs this user on via the security server at bootstrap-
# time, so if it is not valid, then no OneWorld database access is 
# possible.
#
# NOTES: * This information in this section should match the 
#          corresponding information specified in the 
#          [DB SYSTEM SETTINGS] section of this installation's JDE.INI 
#          file.
#-----------------------------------------------------------------------

[JDBj-BOOTSTRAP SESSION]
user=DEMO
password=_
environment=DEMO920
role=*ALL

#-----------------------------------------------------------------------
# Bootstrap physical data source
#
# This defines the data source where the OCM and some other system 
# tables reside.  JDBj uses this at bootstrap time and later to look up 
# OCM entries on demand.  If it is not valid, then no OneWorld database 
# access is possible.
#
# Here is a description of each field in this section:
#
# ----------------  ---------------------------------------  -----------
# Field             Description                              Applies to
# ----------------  ---------------------------------------  -----------
# name              The data source name.  This is not that  All
#                   important for bootstrap connections, 
#                   but it does show up in error messages
#                   and the log.
# ----------------  ---------------------------------------  -----------
# databaseType      The database type.  One of the           All
#                   following:
#
#                   I = AS/400
#                   O = Oracle
#                   S = SQL Server
#                   W = UDB
# ----------------  ---------------------------------------  -----------
# server            The server (i.e. the host).              AS/400,
#                                                            SQL Server
# ----------------  ---------------------------------------  -----------
# database          The database.                            Oracle, UDB
# ----------------  ---------------------------------------  -----------
# serverPort        The server port.                         SQL Server
# ----------------  ---------------------------------------  -----------
# physicalDatabase  The physical database (used as library   AS/400,
#                   qualifier for AS/400).                   SQL Server
# ----------------  ---------------------------------------  -----------
# owner             The owner.                               Oracle, 
#                                                            SQL Server,
#                                                            UDB
# ----------------  ---------------------------------------  -----------
# lob               Supports lobs.                           Oracle, 
#                                                            
#                                                            AS/400
# ----------------  ---------------------------------------  -----------
# unicode           Performs unicode conversion.             SQL Server
# ----------------  ---------------------------------------  -----------
#
# NOTES: * This information in this section should match the 
#          corresponding information specified in the 
#          [DB SYSTEM SETTINGS] section of this installation's JDE.INI 
#          file.
#-----------------------------------------------------------------------

[JDBj-BOOTSTRAP DATA SOURCE]
name=System Local
databaseType=E
server=localhost
serverPort=1521
database=E1Local
physicalDatabase=JDESY920
owner=
lob=true
unicode=true
databaseInstance=

#-----------------------------------------------------------------------
# Bootstrap spec data source (Optional)
#
# This defines the data source where the serialized spec tables reside.  
# JDBj uses this at bootstrap time and after to look up serialized spec 
# objects on demand.  If this section is not specified, then JDBj will 
# use the OCM to find the serialized spec table.  If it is not valid, no 
# OneWorld database access is possible.
#
# See the description for "Bootstrap physical data source" above for 
# information about which fields must be filled in for a given database 
# platform.
#-----------------------------------------------------------------------

[JDBj-SPEC DATA SOURCE]
name=Local - DEMO
databaseType=E
server=localhost
serverPort=1521
database=E1Local
physicalDatabase=JDEVL920
owner=dbo
lob=true
unicode=true
databaseInstance=ERROR
user=sa
password=

#=======================================================================
#                END - OneWorld specific information 
#
# The rest of the sections apply when accessing OneWorld and standalone 
# data.
#=======================================================================

#-----------------------------------------------------------------------
# JDBC drivers
#
# This defines JDBC drivers and JDBC specific settings.
#-----------------------------------------------------------------------

[JDBj-JDBC DRIVERS]
ORACLE=oracle.jdbc.driver.OracleDriver
#AS400=com.ibm.as400.access.AS400JDBCDriver
#SQLSERVER=com.microsoft.jdbc.sqlserver.SQLServerDriver
#UDB=COM.ibm.db2.jdbc.app.DB2Driver

[JDBj-ORACLE]
tns=D:\JDEdwards\E920_1\DEMO\ini\sbf\Tnsnames.ora

[JDBj-LOGS]
jdbcTrace=false

[JDBj-SERVER]
dbcsConversionTolerant=true

#-----------------------------------------------------------------------
# Connection pool settings
#
# These are used only when J2EE connection pooling is not available.
#-----------------------------------------------------------------------

[JDBj-CONNECTION POOL]
jdbcPooling=false
minConnection=1
maxConnection=5
initialConnection=1
poolGrowth=1
connectionTimeout=1800000
cleanPoolInterval=600000
maxSize=50
purgeCacheSize=5

#-----------------------------------------------------------------------
# JDBj Runtime properties
#
# These are all optional.  They correspond to system runtime properties 
# applicable to JDBj logical connections.    
#
# NOTES: * In each case, the values listed are the defaults. The 
#          template default entries are commented out.  Make sure
#          and remove the pound sign (#) when changing these values.
#-----------------------------------------------------------------------

[JDBj-RUNTIME PROPERTIES]

	; Data cache entry size threshold property. Sets the maximum 
	; size (in rows) for a single entry in the data cache. If a 
	; potential entry exceeds this threshold, then it will not be 
	; cached. -1 indicates that all eligible entries should be 
	; cached. 
	;
	; Valid values: -1 or greater 

# dataCacheEntrySizeThreshold=500

	; Data cache entry threshold property. Sets the maximum size (in
	; entries) for the data cache. If the data cache exceeds this 
	; size, then the least recently used entries are removed to 
	; make room for the new entry. -1 indicates that there is no 
	; maximum. 
	;
	; Valid values: -1 or greater 

# dataCacheEntryThreshold=100

	; E1Menu cache purge property. Sets the number of
	; milliseconds after which inactive spec cache entries are
	; purged.  0 means to never purge spec cache entries.
	;
	; Valid values: 0 or greater
    
# E1MenuCachePurge=3600000

	; Force single data source property. Indicates whether JDBj 
	; should force operations involving multiple database objects to
	; run against a single data source. If this is true, JDBj will 
	; only resolve the physical data source for the first database 
	; object involved in a given operation. Otherwise, JDBj will 
	; resolve physical data sources for all database objects and 
	; throw an exception if a single operation spans multiple data 
	; sources. 
	;
	; Valid values: true, false 

# forceSingleDataSource=false

	; No where paren property.  Certain TableIO system function 
	; queries require a long list of selections in the where clause 
	; without any intermediate parentheses. Specifying a composite 
	; selections alone for this case creates intermediate 
	; parentheses. If this property is set to a true then the JDBj 
	; will create SQL without any intermediate parenetheses. 
	;
	; Valid values: true, false 

# noWhereParen=false

	; Result set timeout property. Sets the the number of 
	; milliseconds for the result set timeout. A result set will 
	; timeout if it has not had any operations for a period of time. 
	;
	; Valid values: -1 or greater 

# resultSetTimeout=60000

	; Retry interval property. Sets the interval (in milliseconds) 
	; to wait before retrying idempotent database operations. -1 
	; means not to retry, 0 means retry immediately. 
	;
	; Valid values: -1 or greater 

# retryInterval=0

	; Retry maximum property. Sets the number of times to retry 
	; idempotent database operations. -1 means to retry 
	; indefinitely. 
	;
	; Valid values: -1 or greater 

# retryMaximum=5

	; Spec consistency check property. Sets the level of spec 
	; consistency checking. Set this property to a higher level to 
	; improve exception messages relating to spec inconsistency 
	; problems. Set this to a lower level when it is not needed 
	; since it may degrade performance. 
	;
	; Valid values: full, minimal, none 

# specConsistencyCheck=minimal

	; Spec generate on demand property. Indicates whether JDBj 
	; should generate specs on demand if it can not find them
	; in the persistent cache.  
	;
	; Valid values: true, false 

specGenerateOnDemand=true

	; Transaction isolation property. Sets the isolation level to be 
	; used for transactions. 
	;
	; Valid values: default, none, read uncommitted, read committed, 
	;               repeatable read, serializable 

# transactionIsolation=default

	; Transaction timeout property. Sets the number of milliseconds 
	; for the transaction timeout. A transaction will timeout if it 
	; has not had any operations for a period of time. If this 
	; timeout is set to a -1 then the transaction timeout feature 
	; will be disabled.  (This currently only happens when JDBj is 
	; run as part of a JAS transaction.) 
	;
	; Valid values: -1 or greater 

# transactionTimeout=120000

	; Trigger auto fetch property. Indicates whether JDBj should 
	; automatically fetch rows to be changed in order to pass them 
	; to OneWorld triggers. This is needed for certain triggers to 
	; work properly. 
	;
	; Valid values: true, false 

# triggerAutoFetch=false

	; Updatable result set timeout property. Sets the the number of 
	; milliseconds for the updatable result set timeout. An 
	; updatable result set will timeout if it has not had any 
	; operations for a period of time. -1 indicates that updatable 
	; result sets should have the same value as RESULT_SET_TIMEOUT. 
	;
	; Valid values: -1 or greater 

# updatableResultSetTimeout=-1

	; Usage execution threshold property. Sets the expected maximum 
	; time (in milliseconds) for a single database operation to 
	; execute. If a single database operation takes longer than this 
	; threshold, then the statement and time will be logged as part 
	; of usage tracking. 
	;
	; Valid values: 0 or greater 

usageExecutionThreshold=20000

	; Usage fetch size threshold property. Sets the expected maximum 
	; fetch size (in rows) for a single fetch to return. If a single 
	; fetch returns more than than this threshold, then the actual 
	; fetch size will be logged as part of usage tracking. -1 
	; indicates that any fetch size is valid. 
	;
	; Valid values: -1 or greater 

usageFetchSizeThreshold=500

	; Usage result set open threshold property. Sets the expected 
	; maximum time (in milliseconds) for a result set to remain 
	; open. If a result set is left open longer than this threshold, 
	; then the result set and time will be logged as part of usage 
	; tracking. This does not automatically close the result set. A 
	; usage result set open threshold value of -1 indicates that no 
	; such usage tracking will occur. 
	;
	; Valid values: -1 or greater 

# usageResultSetOpenThreshold=60000

	; Usage tracking property. Enables or disables usage tracking. 
	; This provides additional tracking and logging to use during 
	; testing. Usage tracking does incur a performance penalty so it 
	; should be disabled for production code. 
	;
	; Valid values: true, false 

# usageTracking=false

	; Usage tracking output property. Specifies the destination of 
	; usage tracking output. 
	;
	; Valid values: log, exception 

# usageTrackingOutput=log

	; Usage transaction active threshold property. Sets the expected 
	; maximum time (in milliseconds) for a transaction to remain 
	; active. If a transaction is left active longer than this 
	; threshold, then the transaction and time will be logged as 
	; part of usage tracking. This does not automatically rollback 
	; the transaction. A usage transaction active threshold value of 
	; -1 indicates that no such usage tracking will occur. 
	;
	; Valid values: -1 or greater 

# usageTransactionActiveThreshold=120000

        ; Maximum number of parallel application generators.
        ; Controls how many serialized JAVA application
        ; objects can be generated at one time.
	; For a low-power server, use a lower value.
	; For a high-power server, use a higher value.
        ;
        ; valid values: 1 or greater

# ParallelAppGens=10

#=======================================================================
#                              END OF FILE
#=======================================================================
```

### jde.ini
``` dos
;OneWorld initialization file JDE.INI
;Client specific version - E920

[JDE_CG]
VisualStudioVersion=2013
STDLIBDIR=$(COMP)\VC98\lib
TPLNAME=EXEFORM2
ERRNAME=CGERR
TARGET=Optimize
INCLUDES=$(COMP)\VC98\include;$(SYSTEM)\include;$(SYSTEM)\cg;$(APP)\include;$(SYSTEM)\includev
LIBS=$(COMP)\VC98\lib;$(SYSTEM)\lib32;$(APP)\lib32;$(SYSTEM)\libv32
MAKEDIR=$(COMP)\VC98\bin;$(COMP)\Common\MSDev98\Bin
USER=JDE

[DEBUG]
TAMMultiUserOn=0
Output=NONE
ServerLog=0
LEVEL=BSFN,EVENTS
;BSFN,EVENTS,SF_CONTROL,SF_GRID,SF_PARENT_CHILD,SF_GENERAL,SF_MESSAGING,SF_WORKFLOW,SF_WORKFLOW_ADMIN,SF_MEDIA_OBJ
DebugFile=c:\jdedebug.log
JobFile=c:\jde.log
Frequency=10000
RepTrace=0

[Explorer]
ExplorerHomeURL=\E920\SolutionExplorer\data\index.html
ExplorerStart=INTERNET

[PORTALENVMAP]
PD9=JPD9
PY9=JPY9
DV9=JDV9
TS9=JTS9
PR9=JPR9

[EVEREST]
ColorScheme=1
ShowAlias=0
ServerHelpPath=\E920\helps

[SVR]
EnvType=1
EnvironmentName=DEMO
SpecPath=spec
SourcePath=source
ObjectPath=obj
HeaderPath=include
HeaderVPath=includev
BinPath=bin32
LibPath=lib32
LibVPath=libv32
MakePath=make
WorkPath=work
CodeGeneratorPath=cg
ResourcePath=res
IconPath=res\icons
HelpPath=helps
TreeBmpPath=res\treebmps
ModelPath=models
LocalePath=locale
IconvPath=locale\Iconv
LibraryListName=DEMO920

[INSTALL]
DefaultSystem=system
ClientPath=client
ClientInstallPath=EnterpriseOne Client Install
PackagePath=package
DataPath=data
HOSTS=hosts
HP9100=hp9100
SUN=sun
RS6000=rs6000
AS400=as400
Double_Byte=0
LocalCodeSet=WE_ISO88591
ActiveConsole=1
ExplorerShortCut=1
B9=D:\JDEdwards\E920_1
ClientType=standalone
MobileClientDeveloper=yes
SerialNumber=-1104552603

[LOCK MANAGER]
RequestedService=None

[DB SYSTEM SETTINGS]
Version=43
Default User=DEMO
Default Role=*ALL
Default Env=DEMO920
Default PathCode=DEMO
Base Datasource=System Local
Server=localhost
Database=E1Local
Load Library=
Decimal Shift =Y
Julian Dates=Y
Use Owner=N
Secured=Y
Type=E
Library List=
Library=
Default Pwd=_
DatabaseName2=JDESY920
ServerPort=1521
JDBNETUse=N
UnicodeFlag=Y
LOBFlag=Y
ConnectionPooling=0

[DB SYSTEM SETTINGS - SECONDARY]
Base Datasource=Versions Local
Object Owner=
Server=localhost
Database=E1Local
Load Library=
Decimal Shift=Y
Julian Dates=Y
Use Owner=N
Secured=Y
Type=E
Library List=
Library=
DatabaseName2=JDEVL920
ServerPort=1521
JDBNETUse=N
UnicodeFlag=Y
LOBFlag=Y

[REPLICATION]
DataSource=
DefaultEnvironment=DEMO920
RetryInterval=3600
RepTrace=0
ForcedSync=0

[SECURITY]
SecurityServer=localhost
User=DEMO
Password=DEMO
DefaultEnvironment=DEMO920
DataSource=System Local
Default Role=*ALL

[JDENET]
serviceNameListen=6012
serviceNameConnect=6012
netTrace=0
tempFileDir=c:\temp

[JDEMAIL]
mailProfile="Default Exchange Profile"
Rule1=90|OPT|MAILSERVER=mail.jdedwards.com
Rule2=100|DEFAULT|OWMON=OWMON@jdedwards.com
Rule3=110|DEFAULT|JDE_SYSTEM=JDE_System@jdedwards.com
Rule4=120|DEFAULT|WORKFLOW_SYSTEM=Workflow@jdedwards.com
Rule5=130|OPT|MERGELOCAL=1
Rule6=140|OPT|UPDATELOCAL=0

[NETWORK QUEUE SETTINGS]
UBEQueue=QE920
UBEPriority=5
PrintImmediate=FALSE
SaveOutput=TRUE
InstallSpecs=Y
JDENETTimeout=60

[INTERACTIVE RUNTIME]
DefaultMailServer=C:\Program Files\Microsoft Exchange\Exchng32.exe
DefaultBrowser=http://www.peoplesoft.com
PWndBackground=onemenu.bmp
BITMAP_StatusBar=stbr1.bmp
OBJECTQUEUE=
FONT_FaceName=Arial
FONT_Height=-12
FONT_Weight=400
COLOR_GridBackground=255,255,128
COLOR_GridForeground=0,0,0
COLOR_GridDesktop=64,128,128
COLOR_GridLines=0,0,0
CACHE_UseCache=1
CACHE_MaximumNodes=50
GRID_GridIntegralRows=1
GRID_FONT_FaceName=Arial
GRID_FONT_Height=-12
GRID_FONT_Weight=400
EXCEPTION_Enabled=True
Initial_Language_Code=
Text Limit=80
PWndLocation=0,0,768,537,327681
MirrorImage=0
MaxFileUploadSize=50

[UBE]
UBEDebugLevel=0
UBESaveLogFile=0
UBEFont_FaceName=Times New Roman
UBEFont_PointSize=8
BlindRDPrinterPrompt=FALSE
UBEFormatXML=1
UBEXMLVersion=2

[OBJECT LIBRARIAN]
OLTLogMode=YES
OLTLogContents=GENERAL

[SIGNON]
LASTENV=DEMO920
LASTUSER=DEMO
Default Role=*ALL
LastRole=*ALL
SHOWOPTIONS=1

[JDENET_KERNEL_DEF2]
krnlName=UBE KERNEL
dispatchDLLName=jdekrnl.dll
dispatchDLLFunction=_JDEK_DispatchUBEMessage@28
maxNumberOfProcesses=1
numberOfAutoStartProcesses=0

[JDENET_KERNEL_DEF4]
krnlName=SECURITY KERNEL
dispatchDLLName=jdekrnl.dll
dispatchDLLFunction=_JDEK_DispatchSecurity@28
maxNumberOfProcesses=1
numberOfAutoStartProcesses=0

[JDENET_KERNEL_DEF6]
krnlName=CALL OBJECT KERNEL
dispatchDLLName=XMLCallObj.dll
dispatchDLLFunction=_XMLCallObjectDispatch@28
maxNumberOfProcesses=1
numberOfAutoStartProcesses=0

[JDENET_KERNEL_DEF12]
krnlName=UBE SUBSYSTEM KERNEL
dispatchDLLName=jdekrnl.dll
dispatchDLLFunction=_JDEK_DispatchUBESBSMessage@28
maxNumberOfProcesses=1
numberOfAutoStartProcesses=0

[JDENET_KERNEL_DEF13]
#So html4apps will work with workflow
krnlName=WORK FLOW KERNEL
dispatchDLLName=workflow.dll
dispatchDLLFunction=_JDEK_DispatchWFServerProcess@28
maxNumberOfProcesses=1
numberOfAutoStartProcesses=0

[JDENET_KERNEL_DEF14]
krnlName=QUEUE KERNEL
dispatchDLLName=jdekrnl.dll
dispatchDLLFunction=_DispatchQueueMessage@28
maxNumberOfProcesses=1
numberOfAutoStartProcesses=0


[LOCALWEB]
# Installation flag, if it is 0, no HTML testing setup, disable all HTML testing
AppServerInstalled=1

# Datasource containing serialized specs for web runtime (F989998 F989999)
# Used for synchonization of specs through JDB
Spec Datasource=Versions Local

# Name of local web server, localhost is default but may not be valid always.
webhostname=localhost

# web server port , Websphere Express default is 7080
webport=9200

# executable for starting web server
webserverstart=D:\JDEdwards\E920_1\system\JAS\WLS_Scripts\E1StartManagedServer.cmd

# executable for stopping web server
webserverstop=D:\JDEdwards\E920_1\system\JAS\WLS_Scripts\E1StopManagedServer.cmd

# start web server on demand, or immediately
# valid values : ONDEMAND (web server will be started on the first HTTP request) ,
MANUAL (web server has to be started manually by user on port specified),
IMME (web server starts as soon as ActivConsole starts)
StartAppServer=IMME

# delay time between starting web server and launching browser window
# default value is 60 (60 secs)
WebDelay=



webserverstoparg=E1Server

webserverstartarg=E1Server

[MTR VALIDATION]
LiteRecords=12
MDACVersion=2.60.6526.2
NMakeVersion=6.00.8168.0
DeployDiskInMB=5000
CDiskInMB=200
BusobjInMB=350
EnterpriseDiskInMB=3000

[XML]
ICUPath=D:\JDEdwards\E920_1\system\locale\xml
```

### jdeinterop.ini
``` dos
[SERVER]
glossaryTextServer=LOCALHOST:6012
codePage=1252

[JDENET]
serviceNameListen=6667
serviceNameConnect=6012
enterpriseServerTimeout=90000
maxPoolSize=30
maxKernelRanges=1

[JDENET_KERNEL_DEF1]
krnlName=SBFServerJava Kernel
processClassName=oracle.e1.bssvfoundation.impl.jdenet.SBFServerJavaKernel
startMessageRange=16201
endMessageRange=16450
maxNumberOfThread=10

#==========================================================
# Define Cache feature for Connector
#==========================================================
[CACHE]
UserSession=18000000
SpecExpire=300000000

#==========================================================
# Define the features for inbound Business Function call
#==========================================================
[INTEROP]
enterpriseServer=LOCALHOST
port=6081
manual_timeout=30000000
Repository=c:\connector\repository

#==========================================================
# Define the features for outbound events
#==========================================================
[EVENTS]
port=6010
ListenerMaxConnection=100
ListenerMaxQueueEntry=100
outbound_timeout=6000000
#==========================================================
# JNDI information for communication with the J2EE server.
#==========================================================
initialContextFactory=com.ibm.websphere.naming.WsnInitialContextFactory
jndiProviderURL=corbaloc:iiop:localhost:2809
#==========================================================
#  URL for communicating with the event client service.
#==========================================================
eventServiceURL=http://localhost:9080/e1events/EventClientService

#==========================================================
# Security Server. Security server port is in [JDENET]
#==========================================================
[SECURITY]
NumServers=1
SecurityServer=localhost

#==========================================================
# OCMEnabled--It will enforce Connector to use OCM to find
# enterpriser server or use setting in [Interop]section.
#==========================================================
[OCM]
OCMEnabled=true

[TRANSACTIONS]
ReapInterval=5
MaxAge=10

[WEB DEVELOPMENT] 
WebDevelopment=TRUE

#==========================================================
# These settings are for Async HTTP callback from 
# third party system to BSSV server.
# HTTPCallbackEndpoint-This setting contains the server,
# port and context root information for the BSSV server.
#==========================================================
[HTTPCallbackSettings]
HTTPCallbackEndpoint=localhost:20002/LOCALDEV

#==========================================================
# These settings are for Async HTTP with SSL
# keystorefile - This setting will be the path to the
#                keystore file.
# keystorepasswd - This setting will be the keystore password.
# keyalias - This setting will be the keystore alias name.
# certificatepasswd -This setting will be the keystore
#                    certicate password.
# truststorefile - This setting will be the path to the
#                  truststore file.
# truststorepasswd - This setting will be the truststore
#                    password.
#==========================================================
[KEYSTORE]
keystorefile=
keystorepasswd=
keyalias=
certificatepasswd=

[TRUST_STORE]
truststorefile=
truststorepasswd=
```