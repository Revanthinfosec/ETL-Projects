# These were the last steps for the process

Using processors, create a NiFi flow:

To extract data, use the GetFile processor.
Use the Python script to convert data using the ExecuteScript processor.
Use the PutSQL processor to load data into the database.


# Configure processors for NiFi:

Provide input/output routes, script paths, database connection information, and other configuration options for each processor.
Utilize the NiFi Flow.
Observe the data passing across the pipeline by starting the NiFi flow.

# Check the Outcomes:
To confirm that the data has been loaded correctly, check the target database.

