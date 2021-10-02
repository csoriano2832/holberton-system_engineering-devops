# Postmortem (*Mock scenario*)
## Issue Summary:

On Saturday, October 2 between the times of 3:04 PM and 4:01 PM (AST) we 
experienced an outage of one of our main database systems. Nearly 80% of of our 
users were affected by a logical error in the system in which data would not be 
stored successfully but the user was not made aware of this therefore causing 
problems later on when trying to load the data from the database.

## Timeline:

* 3:04 PM - One of our QA Engineers reports user complaints coming in from the 
company dedicated communication line.
* 3:10 PM - The Database Manager, Lead Software Engineer, and Project Manager 
gathered in the conference room to discuss possible causes to the problem.
* 3:25 PM - Database management was switched to secondary backup system while 
engineers reset the main system for a possible solution but to no avail.
* 3:37 PM - A team of programmers were sent in to review the code of the system 
and found a logical error in the data storage method; data was being saved 
locally.
* 3:49 PM - A hotfix was implemented after a team ran several tests on it and 
returning successfully.
* 3:55 PM - Database management was switched back to the main system.
* 4:01 PM - Users reported the system was back to normal.

## Root Cause and Resolution:

The main cause of the problem was due to an update on the software in which the 
team of programmers were looking to save up to 65% of proccesing power by 
offloading data older than 1 year to a local server but didn't take into account
deltatime therefore all data was being saved locally. Due to this, the 
programmers implemented a function that takes into account real world time 
instead of computer time.

## Corrective and Preventative Measures:

* Teams that handle the code will now make sure to code review each other's 
latest work before updating the system to assure quality.
* Database monitoring will be established to detect possible problems in the 
systems sooner and save time on correcting it.
