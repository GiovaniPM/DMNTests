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
