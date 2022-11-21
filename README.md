# Overview 
This is a script for scraping Trackman grouped reports and outputting them in an appended fashion by club. This allows multiple trackman sessions to be continually updated to in order to have a continuous log of shots. Any advanced grouping, querying, etc. functionality of the script's output must be done in a separate environment. 

## Usage

Running the python script with the following command: 
`./python3 main.py --url 'https://mytrackman.com/system/dynamic-report?r=...'`
Will parse the report for all supported stats, and create entries in the `out/` directory for clubs present in the trackman report.

Currently the supported stats are:
* Club Path
* Face To Path
* Face Angle
* Carry Distance
* Total Distance
* Club Speed
* Ball Speed
* Smash Factor
* Apex Height
* Side Deviation
* Impact Height
* Impact Offset
* Spin Axis
* Spin Rate
* Attack Angle
* Swing Direction
* Dynamic Loft
* Low Point Distance


