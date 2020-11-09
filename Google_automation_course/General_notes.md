# General Informations managing system

---

## Creating a python virtual Environment (windows - on bash terminal)

  ---

```python
python -m venv <name_VE>
# To activate, run the script on windows terminal
<name_VE>\Scripts\activate.bat
# On git-bash or linux
# cd to <name_VE>\Scripts, then run
. activate
# To deactivate, just type deactivate with environment active
deactivate
```

### To update pip

`pip install --upgrade pip --user`

### To view currently installed packages

`pip freeze`

## Add To path in windows.

---

1. Search for 'env' on windows, choose **edit system environment variables**, option.
2. Go to **Environment variables**,
3. Edit the system variables to add a new program to the path, test it in terminal.

## To create a shared folder from VirtualBox to Ubuntu

---

1. VirtualBox Version: 6.1.8, Ubuntu version(`lsb_release -a`): 20.04.1
2. Create a folder shared in the virtualbox path (like, /users/user_name/virtualbox Vms/Ubuntu/shared)
3. In the virual box, virtual machine settings > shared folder > + add folder.
4. Choose the make it permanent option, un-check read only and auto mount options.
5. Start the Virtual machine, go to devices -> insert guest addition CD image,
6. When prompted run it to install VBox_GA_6.XX
7. When it finishes restart VM, when Ubuntu gets back in a terminal, make a shared folder in the root '`mkdir ~/shared`'.
8. Mount the shared folder: `sudo mount -t vboxsf shared ~/shared`.
