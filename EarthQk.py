import urllib.request
import json
import sys

def main():
# accessing the page

        webURL = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php"
        urlData = urllib.request.urlopen(webURL)
        x = urlData.getcode() # code the specified page replies with

        if x == 200:
                print("_____________________________________________________________________________") # for design
                print("| OK, connected.")
                print("| Welcome. Configure options:")
                tCounter = 0 # will go through time options
                time = ["hour", "day", "week", "month"] # available time options
                print("| Press [n/N] button to change option configuration. Type [d/D] or [d/Done]")
                print("| to move forward.")
                optTime = "| Time period: " + time[tCounter]    # default time option
                print(optTime)
                inpt = str(input("| ")) # user's input
                while True:
                        if "n" in inpt:
                                tCounter += 1
                                if tCounter == 4: # code will not brake if range is larger than list
                                        tCounter = 0 # will start with default option
                                print("| Time period: " + time[tCounter]) # reacts to any changes
                                inpt = str(input("| ")) # user's input after each change
                        elif "d" or "done" or "D" or "Done" in inpt:
                                configuration = {}      # creates a dictionary
                                configuration["Period"] = time[tCounter]        # adds a value and a key to it
                                break
                mCounter = 0 # will go through magnitude options
                magn = ["all", "1.0", "2.5", "4.5", "significant"] # available magnitude options
                equakes = "| Magnitude: " + magn[mCounter] # default magnitude option
                print(equakes)
                inpt = str(input("| ")) # user's input
                while True:
                        if "n" in inpt:
                                mCounter += 1
                                if mCounter == 5: # code will not brake if range is larger than list
                                        mCounter = 0 # will start with default option
                                print("| Magnitude: " + magn[mCounter]) # reacts to any changes
                                inpt = str(input("| ")) # user's input after each change
                        elif "d" or "done" or "D" or "Done" in inpt:
                                configuration["Magnitude"] = magn[mCounter] # adds a value and a key to the dictionary
                                break
                
# main part of the code, how program will be working
                
                webURL = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/" # link base
                webURL = webURL + magn[mCounter] + "_" + time[tCounter] + ".geojson" # automates link choice according to configuration
                urlData = urllib.request.urlopen(webURL).read() # reads contents in HTML
                jdata = json.loads(urlData) # loads contents in JSON

                # working with JSON
                if "title" in jdata["metadata"]:
                        print("|", jdata["metadata"]["title"])
                        print("| ")
                        print("|", jdata["metadata"]["count"], "earthquakes in past " + time[tCounter] +".")
                        for i in jdata["features"]:     # goes through several events in JSON
                                report = i["properties"]["felt"]
                                feel = i["properties"]["felt"]
                                geo = i["properties"]["place"]
                                mag = i["properties"]["mag"]
                                if report == None:
                                        print("|", str(mag), "points,", str(geo))
                                else:
                                        print("|", str(mag), "points,", "felt like", str(feel) + str(","), str(geo))
                else:
                        print("| No data.") # in case something is working not as intended
        else:
                print("| Error, not connected.") # if status code is not 200 for any reason
                
        msg = str(input("| Type anything to close the program and [r/R] to run it again: "))
        # broken into two parts because Python does not execute the sought feature properly
        if msg == "r":
                main()
        elif msg == "R":
                main()
        else:
                sys.exit()

if __name__ == "__main__":
        main()
