# uae
<pre>
0. Python libraries installation is needed to run animedaily.py
   animedaily.py is a program to generate png files for entered Country.
In order to install the necessary libraries, see https://github.com/ytakefuji/python-novice
1. Download new_deaths.csv file.
2. python animedaily.py
   United Arab Emirates
3. convert -delay 10 -loop 5 *.png uae.gif
   convert is a command to convert png files into a gif file
In order to use a convert command, install ImageMagick for your OS.
</pre>


The new_deaths.csv is downloaded from the following site: 

https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/jhu/new_deaths.csv

This site is also available: 
https://covid.ourworldindata.org/data/ecdc/new_deaths.csv

the number of predicted daily deaths due to the covid-19 in UAE.
In the graph, black line: the number of daily deaths, blue line: predicted curve using 285 days, red line changing the number of daysfrom 100 to 285 days from Jan. 7 2021 for curve-fitting.

<img src='uae.gif' height=400 width=600>
