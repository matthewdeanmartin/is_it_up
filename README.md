is_it_up
--------

As Library
----------
This does a variety of checks ordered by speed to see if a machine is up. It should give a "No!" answer fast. It should be smart about re-attempting slow checks, e.g. using exponential backoff.

Life with out this tool
-----------------------
Without this tool, we attempt to make a connection, it times out after 60 seconds. It is up to us to determine what part of the stack is down (the DNS, the server, the webserver, the app on the webserver). It is also us to decide how often to retry. It is also up to us to maintain state if we want to do exponential backoff.


As Command Line Tool
--------------------
If we get around to it, it will have a command line interface. Many commandline variations on ping already exist. This could be used as a health check for AWS EC2 or AWS ECR machines.

Scenarios
---------
- Resolve DNS name
- Redis- ping host, ping redis
- Ec2 instance- ping, use boto3 to wait until reboot has finished
- Database- ping host, connect to 'public' databases, like tempdb
- Maintain state so that if a slow check just happened and failed, it doesn't happen again for an exponential time gap.
- Possibly provide an asncy event for waiting until a system is back up
