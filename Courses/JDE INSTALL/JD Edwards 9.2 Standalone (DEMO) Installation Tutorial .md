# JD Edwards 9.2 Standalone (DEMO) Installation Tutorial 

Standalone 9.2 Install JD Edwards Enterprise One 9.2 Standalone Demo (Oracle version) on your PC or server with this step by step guide.

![Welcome](https://raw.githubusercontent.com/GiovaniPM/DMNTests/main/Courses/JDE%20INSTALL/Images/w06p9oaa.bmp)

## Pay attention

1. This version (according to the Oracle Docs) is designed to run on Windows 7 x64, Windows 2012 R2, Windows 8.1 Even you 1. install successfully in another version of Windows 64, some business functions don’t work as expected, so, stay with Windows 1. 7 or 2012 R2 or 8.1 x64 and everything should work as expected.
1. Before you start with anything, turn OFF your Anti-virus, Firewall and Disable UAC (User Access Control). For security 1. purposes you could enable again the Firewall and Anti-virus AFTER the installation was completed.
1. From Release E920 OC4J is removed. So first we have to install Oracle Weblogic Server using 32 bit JDK

This procedure was a result from information that I gathered from tips from another users and “trial and error” tests. Suggestions and comments are always welcome.

Before we get started, if you find any issue, do read through the comments or visit the [troubleshooting guide for 9.2 installation](https://www.jdesource.com/enterpriseone/jd-edwards-standalone-e920-troubleshooting-guide/)