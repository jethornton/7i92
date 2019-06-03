==========
Installing
==========

7i76e Configuration Tool

1. Install required dependencies. In a terminal do:
::

    sudo apt install python3-pip python3-pyqt5 libpci-dev git

2. Install the 7i92 Configuration Tool. in a terminal do:
::

    pip3 install git+https://github.com/jethornton/7i92.git

3. Create a file in your home directory called ``.xsessionrc`` and add the
following if your using Debian 9 then log out and back in or reboot the PC.

::

  if [ -d $HOME/.local/bin ]; then
    export PATH="$HOME/.local/bin:$PATH"
  fi

4. Run the 7i92 Configuration Tool. In a terminal do:
::

    7i92

To upgrade the 7i92 Configuration Tool In a terminal do
::

    pip3 install git+https://github.com/jethornton/7i92.git --upgrade


To uninstall the 7i92 Configuration Tool
::

    pip3 uninstall 7i92

