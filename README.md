# packaging
Alumet docker images and distro-specific packages

# Table of Contents
- [packaging](#packaging)
- [Table of Contents](#table-of-contents)
- [How to install ?](#how-to-install-)
- [How to uninstall](#how-to-uninstall)
- [What does the RPM do ?](#what-does-the-rpm-do-)


When you're downloading the rpm, use a compatible version particularly if you're not on fedora.

| Version of fedora 	| Version of libc 	|
|-------------------	|-----------------	|
| Fedora Linux 42   	| glibc 2.40      	|
| Fedora Linux 41   	| glibc 2.40      	|
| Fedora Linux 40   	| glibc 2.39      	|

# How to install ? 

```bash
sudo rpm -i <rpm file>
```

# How to uninstall

List all installed Alumet package: 

```bash
rpm -qa | grep -i alumet
```

Remove the correct Alumet package 
```bash
sudo rpm -e <package>
```

# What does the RPM do ? 

The RPM create a folder **alumet** inside the */etc/* folder. Here will be put the **alumet-config.toml** file which is the config file for Alumet by default. 
The RPM also put inside the */bin/* folder the Alumet binary. As usually */bin/* folder is in the path, you can just run Alumet like (it depends on which rpm you had installed):

```bash
alumet-local-agent
```