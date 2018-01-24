# CODEX-Minor-Project  &nbsp;&nbsp;:octocat:

## Group Name : ALUCARD

### Group Members
* [Gayatri Chakraborty](https://github.com/gayatric)
* [Debashish Mishra](https://github.com/Zanark)
* [Syed Salif Moin](https://github.com/salif-04)

## About the program
This is the Web Scraper for the website https://alpha.wallhaven.cc .  
It asks the user for a search tag on the basis of which it searchs for wallpapers on the above mentioned website.  
After the user enters his choice of genre of wallapers, the program searches for wallpapers related to that genre and then downloads it into the directory `/home/$USERNAME/images` and then the downloaded image will be used as bootloader wallpaper. 

### How to edit grub file
The user needs to edit the grub file to make this program fully functional.

1. Edit the file `/etc/default/grub` and add the following line to it, replacing $USERNAME with your username.

         export GRUB_MENU_PICTURE = "/home/$USERNAME/images/grub.jpg"

2. On execution, the program will then copy the downloaded image into the folder in `/home/$USERNAME/images` and rename it to `grub.jpg` , so that it will be shown as the grub menu background.

### Requirements
Other than Python3.x, you'll require the following libraries:<br>
* click<br>
* bs4<br>
* requests<br>
* random<br>

### Instructions
1. Clone the repository to your machine.

2. Open your terminal and change directory to your cloned folder.

3. Enter the command `$ pip3 install --editable . ` to install all dependcies.

4. Now run the program using `$ grubwallpaper`
