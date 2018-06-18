# 33270 - Design-Build 4: Autonomous devices for controlling and studying living systems 

This is the github repository for group 5 in the 2018 version of the course 33270. The project aims to conduct an experiment with mussels and algae, while controlling the environment they're in. More specifically, the code in this repository handles uploading to the adafruit webserver (webupload.py), reading the temperature (read_temp.py), a PID algorithm implementation to control the temperature (PID.py) and more. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Installing

The software was specifically designed for the Feather HUZZAH ESP32 board, running with micropython on it. 
To access the board we used the following guide from [ESP-IDF](http://esp-idf.readthedocs.io/en/latest/get-started/establish-serial-connection.html). On mac you most likely have to install a driver from [Silabs](https://www.silabs.com/products/development-tools/software/usb-to-uart-bridge-vcp-drivers) and run the following command:

```
screen /dev/tty.board_name 115200
```

We also used ampy to transfer files to and from the board. On mac this can be installed using: 

```
pip install adafruit-ampy
```

## Running the experiment

To run the experiments on the board, simply transfer the files using ampy and begin. 

## MQTT Broker

We have used [Adafruit](https://io.adafruit.com) as our MQTT broker. The dashboard we ended up with can be seen [here](https://io.adafruit.com/abho/dashboards/design-build-dashboard)

## Built With

* [PyCharm](https://www.jetbrains.com/pycharm/download/#section=mac) - Python IDE Used
* [Eclipse](http://www.eclipse.org/downloads/) - Java IDE Used


## Authors

* **Alexander Holstrup** - [Github Page](https://github.com/Holstrup)
* **Lasse Starklit** - [Github Page](https://github.com/lassestarklit)
* **Abdelali Khatibi** - [Github Page](https://github.com/thecoder2297)


You can see the individual contributions at the [insights](https://github.com/Holstrup/DesignBuild4/graphs/contributors)

## Acknowledgments

Thanks to Giorgi and Mr. Ph.D Luca for helping us out
