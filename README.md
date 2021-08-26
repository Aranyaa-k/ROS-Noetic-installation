# ROS-Noetic-installation
Installation of ROS Noetic on VM ware

This README.md covers 
- Installation and setting up Ubuntu on the VMware Workstation 
- Installation of ROS Noetic on the VMware

## Installation and Set-up of VMware Workstation
Click this [link](https://customerconnect.vmware.com/en/downloads/details?downloadGroup=WKST-PLAYER-1612&productId=1039&rPId=66621)   
The above link will take you to a website from where you can install the VMware Workstation player. Choose and download the apropraite version of the VMware based on your system configuration.   

For further guidance on installation click [here.](https://xpertstec.com/how-to-install-vmware-workstation-player-16/)

### Set up Ubuntu on the VMware
You can either watch [this](https://www.youtube.com/watch?v=9rUhGWijf9U&ab_channel=ProgrammingKnowledge) video or scroll ahead to read through this guide    

- First download the Ubuntu ISO file from [here.](https://ubuntu.com/download/desktop/thank-you?version=20.04.3&architecture=amd64)
- Open your VMware and click on Create a New Virtual Machine
![](images/Screenshot1.png)    

- Choose I will install the operating system later option in the next window and click next
![](images/Screenshot2.png)   

- Choose Linux and change the Version according to your system and click next
![](images/Screenshot4.png)   

- Type in the name of your virtual machine and choose the desired location and click next   
- Give maximum disk space as 100GB and click next   
- Click on Customize hardware and the below window opens up. Under Memory move the slider to 8GB and Under processors change the Number of processor cores to 4    
 
- Click on New CD/DVD (SATA) on the left and choose Use ISO image and browse for the installed ISO file for ubuntu. Once that is done click on close and then finish.  
![](images/Screenshot7.png)   

- Now you should be able to see the newly created virtual machine in the VMware Workstation player. Click on Play virtual machine. 
- Next you see the below on your screen. Choose the language and click Install Ubuntu
![](images/Screenshot8.png)
- Choose your keyboard layout
- Select Normal installation and check Install third-party software and click continue
- Select the Installation type as below and click on Install now. This does not harm or remove the data on your host machine
![](images/Screenshot10.png)
- Follow the installation and your virtual machine is all set up and ready to use   

## Installation of ROS Noetic on the VMware
