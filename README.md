# Project UNVEIL

## Introduction

In the past few years, numerous privacy vulnerabilities have been discovered in the WiFi standards and their implementations for mobile devices. These vulnerabilities allow an attacker to collect large amounts of data on the device user, which could be used to infer sensitive information such as religion, gender, and sexual orientation. Solutions for these vulnerabilities are often hard to design and typically require many years to be widely adopted, leaving many devices at risk.

Project UNVEIL presents an interactive and extendable platform to demonstrate the consequences of these attacks. The platform performs passive and active attacks on smartphones to collect and analyze data leaked through WiFi and communicate the analysis results to users through simple and interactive visualizations.

The platform currently performs two attacks. First, it captures probe requests sent by nearby devices and combines them with public WiFi location databases to generate a map of locations previously visited by the device users. Second, it creates rogue access points with SSIDs of popular public WiFis (e.g. _Heathrow WiFi, Railways WiFi) and records the resulting internet traffic. This data is then analyzed and presented in a format that highlights the privacy leakage. The platform has been designed to be easily extendable to include more attacks and to be easily deployable in public spaces. We hope that UNVEIL will help raise public awareness of privacy risks of WiFi networks.

The work was published as a [demo paper](https://dl.acm.org/doi/10.1145/3308558.3314143) in [The Web Conference 2019 (WWW '19)](https://www2019.thewebconf.org/).

This repository has the code for deployment of [UNVEIL](https://dl.acm.org/doi/10.1145/3308558.3314143) on any platform with docker.

## Usage instructions

UNVEIL provides a frontend interface to control the platform, accessible via a browser (has been tested with Chrome and Firefox).

### Control screen

`localhost:3000/control`

UNVEIL experiment can be controlled via a control screen available at above URL. You need to enter the PIN to access the screen. This is PIN has to be set in the backend during deployment, more details in [deployment section](#deployment).

![Control screen with PIN](docs/imgs/control_pin.png)

Once you enter the control screen you can see the buttons to:

- start the experiment i.e. start collecting data from raspberry pis.
- show setup and experiment steps on the [setup screen](#setup-screen)
- show data on [probe screen](#probe-screen)
- show data on [devices screen](#devices-screen)

You can also see fake data by clicking on `fake` option.

![Control screen full](docs/imgs/control_full.png)

### [Setup screen](#setup-screen)

`localhost:3000/setup`

Setup screen shows how the wifi works for general public to understand and experimental setup that includes the arrangement of raspberry pis and the devices. This has been built according to the [Data Observatory](https://www.imperial.ac.uk/data-science/data-observatory/) at [Imperial College London](https://www.imperial.ac.uk).

### [Probe screen](#probe-screen)

`localhost:3000/probe`

Probe screen shows the summary of the probe requests captured. More details are available in our [paper](https://dl.acm.org/doi/10.1145/3308558.3314143).

### [Devices screen](#devices-screen)

`localhost:3000/data1`
`localhost:3000/data2`

These show the data from the devices that was captured when they were connected to our access point. More details in our [paper](https://dl.acm.org/doi/10.1145/3308558.3314143).

`localhost:3000/screenshots`

These are the screenshots of the HTTP URLs accessed by the connected devices. This screen also contains some news articles on the WiFi attacks that have happened in the past.

## System architecture

The UNVEIL platform is designed to be modular and easily ex-
tendable. It is structured into three main components:

- Raspberry Pi(s): to collect data and perform the attack. [Code](https://github.com/computationalprivacy/unveil-pi-data-collector).
- Backend Server: responsible for managing the demonstration, components, data, and analyses in the experiment. It uses [Redis](https://redis.io/) and [MongoDB](https://www.mongodb.com/). [Code](https://github.com/computationalprivacy/unveil-backend).
- Visualization Server: for serving the web pages that visualize the results of data analyses and allow to control the demonstration. [Code](https://github.com/computationalprivacy/unveil-frontend).

### External APIs used

We use certain external APIs for the platform to work correctly. You need to create accounts for this APIs and provide credentials during deployment.

1. [Google APIs](https://console.developers.google.com/apis/dashboard) for Spreadheet that stores the opted-out MAC addresses.
2. [Wigle API](https://api.wigle.net/) for fetching addresses of WiFi Access Points.

## [Deployment](#deployment)

### Requirements

1. A server with [docker engine](https://docs.docker.com/engine/) and [docker-compose](https://docs.docker.com/compose/) installed to deploy frontend and backend services. This repository contains all the code needed for server deployments
2. [Raspberry Pi(s)](https://www.raspberrypi.org/) with an external antenna (we use [Alfa Network AWUS036NHA](https://www.alfa.com.tw/products_detail/7.htm) for our internal testing). The [unveil-data-collector](https://github.com/computationalprivacy/unveil-pi-data-collector) contains the code and details for deploying a raspberry pi with UNVEIL.

**Note: You can run and test the platform even without raspberry pi. We provide fake data for the same purpose.**

### Configuration files

You can find all the configuration files in `configs` folder of the repository.

1. `google_api_creds.json`: Contains Google API credentials to use for accessing spreadsheets containing opted out MAC addresses.
2. `production.py`: Settings file for Django backend service. Set the Spreadsheet ID for optout of MAC addresses and other settings.
3. `runtimeConfig.js`: Contains configuration for frontend. Provide the backend details that frontend should connect to and center of the map when the system starts. By default it is set to London.

Before deploying:

- check the docker compose file and all volumes being mounted,
- set all the parameters as per the requirements, and
- do change the password for `redis`, and update the `production.py` accordingly.

### Commands

#### Copy configuration files

```shell
cp ./configs/change_me.google_api_creds.json ./configs/google_api_creds.json
cp ./configs/change_me.production.py ./configs/production.py
cp ./configs/change_me.runtimeConfig.py ./configs/runtimeConfig.py
```

Make changes to the configuration files as required.

#### Deploy docker

```shell
# pull the images
sudo docker-compose -f unveil-deployment.yml pull

# create db folder
mkdir db
touch db/wifi.sqlite3

# create folder for logs
mkdir logs

# start the containers
sudo docker-compose -f unveil-deployment.yml up
```

### Deploy Raspberry Pi

Instructions to setup the Raspberry Pi can be found in [this repository](https://github.com/computationalprivacy/unveil-pi-data-collector).

After setting up the Pi, you will need to register the Pi in the database, located in folder `db/wifi.sqlite3`. This can be done by manually creating a record in the table `security_manager_accesstokens`. You have to add a name for the Pi and corresponding access token, which is to be added in the configuration of the Pi as well. You can use any SQLite DB editor for this purpose.

Multiple raspberry pis can be dployed with UNVEIL.

## Contact

For support please raise issues in the repository and we will try to address them at earliest.
