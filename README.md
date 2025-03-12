# DEB Packaging

Alumet debian based system image package

# Create your own package

To create a .deb package file to ensure its compatibility with an operating system, you need to build the **Alumet** project on it. 
Run the *config.sh* script that downloading **Alumet** project sources on github ("https://github.com/alumet-dev/alumet"), 
extract and compile its content in a final binary according the targeted operating system version and distribution.

# How to install ? 

With **apt** package manager :
```bash
sudo apt install ./<package_file.deb>
```

# How to uninstall

Remove the correct **Alumet** package with **apt** package manager :
```bash
sudo apt remove alumet-agent
```

# What does the DEB package do ? 

On Debian based operating system, the DEB create a folder **alumet** inside the */etc/alumet/* folder,
to put the *alumet-config.toml* file, which is the configuration file used for Alumet by default.
It also creating a daemon disable by default, but runnable and usable by the *systemd* services manager.
Finally, the package put the **Alumet** binary program in the */usr/lib/alumet* folder, and its runnable script in */usr/bin/*.

    alumet/
    ├── etc
    |   └── alumet
    │       └── alumet-config.toml
    └── usr
        ├── bin
        │   └── alumet-agent
        └── lib
            ├── alumet
            |   └── alumet-agent
            └── systemd
                └── system
                    └── alumet.service

Finally, you can just run **Alumet** program like this :

```bash
alumet-agent
```
