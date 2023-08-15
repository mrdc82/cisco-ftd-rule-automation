<h1> FTD Payload Build and Rule Implementation via API (Python) </h1>
<h2> Overview </h2>
This project came about from witnessing and experiencing first hand the frustration, and time consuming task of manual FTD rule implementions.
<br>Our department deals with upwards of 50 changes a day at our busiest, and at our slowest, nothing less than 30 changes a day on average.
<br>
This project has come about as a way to improve this daily process, by automating the rule implementation by making use of python automation and the FMC API<br>
<br>Our department uses a ticket logging system called ServiceNow, and the process of requesting rules is as follows.<br>

_Business Unit logs a ticket in ServiceNow, with the source,destination,port information. SNOW builds this into a table._<br>
_Our Data Centre Automation team extracts this info, and determines which firewall the ip address belongs to_<br>
_Our team receives a file, as is presented in CHG0001.txt, to use for preparing rules onto the FMC_<br><br>
You may have a different ticketing system, or a different process entirely, so feel free to reach out to me to collaborate on some ideas for your system or process for rule requests. :-)
<h2> The Process </h2>
<p><b>Stage 1 - build_policyid_files.py</b>
<p>The first portion of the task is for the engineer to select the file which contains the FTD rules.<br>
There is a set standard of how the initial file must be formatted, and that is included in the repo as CHG00001.txt<br>
<br>Once the file is selected, the script will process the file into individual files based on the FTD Policy Name, and appended
with the change order number.
<p><b>Note: </b>The newly generated text file name will be used both for the Policy name to deploy to, and the rule name on the policy<br>
<br><b>Stage 2 - payload_generator.py</b>
<p>Now that the files are generated in the format FTDname_CHGxxx.txt, the next phase
is to run the payload generator. When run, the engineer will be asked to select the newly generated text file.
The payload generator iterates the file, and extracts the source,destination and ports.
<b>Note: The FTD API does not consider an already created port, and adds the item into the FTD
as a seperate object, ie, will add to the FTD rule the same port as many times as it is listed in the payload.</b>
<br><br>To curb this issue, i have removed any duplicate ports from a temporary list before building the payload.
<br><br>At this stage, the payload is generated, yet still does not contain a rule id. This will generate, and populate via Stage 3.
<p><b>Stage 3 Final Step - PUT_acp_new_rules.py</b><br>
<br>This is the implementation phase, but still does some formatting before implementation.<br>
<br>First the script will build a new blank rule, which only contains the rule name, and log settings.
This is so that we can then use the update rule API to populate our existing rule with the relevant values from the payload.
<p>
The important thing here is that we have a dictionary which contains the policy id as a value for the FTD name, since the url will use id's and not name values.<br>
<br>
Now for the final stage, when run, the first step of stage 2 is to build a blank rule using the blank rule function. We do this because the second function will need an existing rule to update.
The policyid is implemented into the url as a variable.<br>
<br>Now that the rule is generated, the script will use the new rule id to populate into the payload
we generated in step 2, and will be used as a variable in our rule update function.
<p><b>Note: If a rule exists and you try to create a rule with the same name, you will be presented with an invalid key error. I need to build exception handling into the code which i will add in version 2.</p>
<h2>Conclusion</h2>
This project is still a 3 step system, and does not iterate through the list of files automatically. That will come in to play with a new feature release.
<br>Also, this project does not look through existing ftd rules, and merge changes together, it generates an entirely new rule.
Which in my opinion, is a better and safer method of implementation, as it makes backing out of changes alot easier and safer than modifying a working rule.
<h2>Key Take-away</h2>
This project serves to save time and effort spent manually implementing rules.
In a completed project working in production for ASA rule implementations, the evidence shows that where it used to take roughly 45 minutes, and 3 engineers to implement, has now been brought down to less than 10 minutes, and requires only 1 engineer to run with.
<h2>Key things to note</h2>
- In the PUT_acp_new_rules script, you must populate a dictionary containing your ftd policy id's, tied into the policy name.
- The port protocols also refer to a dictionary located in the payload_generator script. This dictionary contains the protocol number for the designated port type.<br>
- All duplicate ports are removed before the API put request, as for some reason this gets duplicated in the rule implementation. Fortunately it is not the case for ip addresses.



