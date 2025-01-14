# SunSynk API
Sunsynk (Deye) inverter srcipt for getting data and changing using python

The purpose of this Python code is to retrieve the plant id and current power generation data from a Sunsynk inverter. Using this information you can then choose to take actions based on this data - e.g. trigger IoT devices, lights, notifications, adjust inverter settings etc.

Requirements
SunSynk account created on https://sunsynk.net/ site, and an SunSynk inverter that has internet connectivity using the wifi enable data logger. (https://www.sunsynk.org/remote-monitoring) You should be able to login to sunsynk.org
In Linux do nano  .profile and save the data instead of sharing it in the script
export sunsynk_email='email'
export sunsynk_password='password'
After its saved and exit do ~/.profile to activate the variables so that the script can access it
Use printenv or env command to check if its available to use

Steps
Confirm connectivity to inverter from wifi or internet.

From terminal run the Python file with two arguments in the command-line, the first being your Sunsynk.net username/email and the second being your password for this site. These arguments are used programatically to retrieve the bearer token to for API requests.

The command example would be:

python3 sunsynk_get_generation.py <my_username/email> <my_password>
The output by default runs both functions which will display the bearer token, the plant id and the real-time power generation.
