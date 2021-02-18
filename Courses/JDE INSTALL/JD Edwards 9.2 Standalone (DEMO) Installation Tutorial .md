# JD Edwards 9.2 Standalone (DEMO) Installation Tutorial 

Standalone 9.2 Install JD Edwards Enterprise One 9.2 Standalone Demo (Oracle version) on your PC or server with this step by step guide.

![Welcome](https://raw.githubusercontent.com/GiovaniPM/DMNTests/main/Courses/JDE%20INSTALL/Images/w06p9oaa.bmp)

## Pay attention

1. This version (according to the Oracle Docs) is designed to run on Windows 7 x64, Windows 2012 R2, Windows 8.1 Even you 1. install successfully in another version of Windows 64, some business functions don’t work as expected, so, stay with Windows 1. 7 or 2012 R2 or 8.1 x64 and everything should work as expected.
1. Before you start with anything, turn OFF your Anti-virus, Firewall and Disable UAC (User Access Control). For security 1. purposes you could enable again the Firewall and Anti-virus AFTER the installation was completed.
1. From Release E920 OC4J is removed. So first we have to install Oracle Weblogic Server using 32 bit JDK

This procedure was a result from information that I gathered from tips from another users and “trial and error” tests. Suggestions and comments are always welcome.

Before we get started, if you find any issue, do read through the comments or visit the [troubleshooting guide for 9.2 installation](https://www.jdesource.com/enterpriseone/jd-edwards-standalone-e920-troubleshooting-guide/)

## Let's GO


1. Certification or MTR for JD Edwards Standalone can be verified from certification tab of support portal. Tips: JD Edwards Standalone Certification can be verified under product “JD Edwards Development client”
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

## 3. Installation of Oracle Weblogic Server

From Release 9.2, OC4J has been removed so we need to install Oracle Weblogic Server for installing Local Web client

The Standalone Web Client can be only Installed on Oracle WebLogic Server application server.

Extract the download weblogic setup (V44413-01 zip)file in desktop or any folder, we will get the jar file **fmw_12.1.3.0.0_wls.jar**.

Now Open the Command Prompt as **<span style="color:red;">Run administrator</span>** and use cd command to navigate to 32 bit Java Installed location( cd C:\Program Files (x86)\java\jdk1.7.0_91\bin) and run the weblogic Server Installer using the below command (Java -jar c:\users\JDE\Desktop\fmw_12.1.3.0.0_wls.jar)

Enter the Oracle_Home as per your requirement and once installation completed uncheck the automatically launch the configuration wizard as shown in the below screen shot and click on finish.

![WL1](https://raw.githubusercontent.com/GiovaniPM/DMNTests/main/Courses/JDE%20INSTALL/Images/jb6up0lz.bmp)

**<span style="color:red;">Note:</span>** No need to create a domain for web logic server

## 4. Install Oracle 12C 32 bit Client

From Release E920 with Oracle 12C 32 bit Client required non-administrator user for the Installation.

Unzip **V47124-01.zip** the file and run the Oracle Client Setup (“Setup.exe”) program.

**<span style="color:red;">Very important:</span>** Select Option 2 Administrator Option while installing Oracle DB 12c Client. Oracle Documentation state that “Runtime” also will work. So you may use them if running low on space.

**<span style="color:red;">Note:</span>** Oracle 12c 32 bit Client required non-administrator user for Installation, during the installation Enter the non-administrator user for installing Oracle 12c Client. If you already created non admin user use option 1 or use option 2 allow OUI to create non admin user ID.

![Oracle1](https://raw.githubusercontent.com/GiovaniPM/DMNTests/main/Courses/JDE%20INSTALL/Images/s133rsut.bmp)

Now, it’s time to install Oracle E1local DB 12c and JDE standalone Client itself. The install process is divided in two parts: the first install the Oracle Database and the second the JDE Client. The four files that we downloaded earlier must be combined to make a working setup installation extract the four files and you will have a folder structure like this.

**<span style="color:red;">V100564-01-zip, V97804-01-zip, V97805-01-zip, V97806-01-zip</span>**


1. Move the contents from folder V97805-01-01 to folder V97806-01
1. Move the contents from folder V97804-01-01 to folder V100564-01
1. Now Move the contents from folder V97806-01-01 to folder V100564-01\ThirdParty\ORACLE

**<span style="color:red;">Note:</span>** Now rename the Folder V100564-01 as standalone. It has the correct structured installation setup files.

Follow the below screenshots

Extract all 4 Setup files

![Oracle2](https://raw.githubusercontent.com/GiovaniPM/DMNTests/main/Courses/JDE%20INSTALL/Images/sinv7am8.bmp)

1. Move the contents from folder V97805-01-01 to folder V97806-01

![Oracle3](https://raw.githubusercontent.com/GiovaniPM/DMNTests/main/Courses/JDE%20INSTALL/Images/9dnmqu39.bmp)

2. Move the contents from folder V97804-01-01 to folder V100564-01
3. Now Move the contents from folder V97806-01-01 to folder V100564-01\ThirdParty\ORACLE

**<span style="color:red;">Note:</span>** Now rename the Folder V100564-01 as standalone. It has the correct structured installation setup files.

## 5. Install E1Local 12c DB

From Release E920, Oracle E1local DB 12C required non-administrator user for Installation. Run the “InstallManager.exe”.Click Enterpriseone Oracle 12c Database Engine on JD Edwards Install Manager

![JDE1](https://raw.githubusercontent.com/GiovaniPM/DMNTests/main/Courses/JDE%20INSTALL/Images/00p8meim.bmp)

In the next screen as we already created Non admin user while installing Oracle 12c 32 bit client, Use the Option 1 and provide the non-administrator credentials and click on Next. Once E1local 12C Successfully Installed, we will receive a saying that message “E1local successfully installed”. Now click yes to reboot the machine.

![JDE2](https://raw.githubusercontent.com/GiovaniPM/DMNTests/main/Courses/JDE%20INSTALL/Images/8ab4r565.bmp)

**<span style="color:red;">Once this is completed, check the following</span>**

Oracle has noted that there is a problem with IMPDP.exe and EXPDP.exe in their 12c database client software.
The solution: Ensure that both the 32-bit client and the 64-bit client are both in your PATH. (ie: c:\app\oracle\product\12.1.0\client_1\bin;C:\Oracle\E1Local\bin). Rename the impdp.exe and expdp.exe in the c:\app\oracle\product\12.1.0\client_1\bin folder to impdp.exe.bak and expdp.exe.bak. The install will then use the impdp.exe from the database install and everything will work.  You can find the Path Envt variables in the System Settings (from control panel) – Advanced Tab – Environment Variables – System Variables