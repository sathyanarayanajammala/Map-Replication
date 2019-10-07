# Distributed Key-Value (KV) store



## About .rar files present in the repo

Map-replica.rar(process 1) file is having rest controllers to store the data in key-value pair store. Here Map-replica.rar and Map-replica2.rar (process 2) are the same projects running in different ports(8081,8082).

Map-sync.rar is the synchronization program, which contains the sync logic between process 1 and process 2. 

## Compile and Execute

1. Download or three .rar files(Map-replica.rar,Map-replica2.rar and Map-sync.rar)
2. Unzip the above files.
3. Open three projects in Intellij.
4. Run maven install
5. Execute them as spring-boot applications or Run as the main program.

## Test Cases
 
```
Test case 1: open the browser and rung the below url
             http://localhost:8081/set/test1/test1val
Test case 2: open the browser and rung the below url
             http://localhost:8082/get
             Restult: {"test1":"test1val"}
Test case 3: open the browser and rung the below url
             http://localhost:8082/set/test1/test1val
Test case 4: open the browser and rung the below url
             http://localhost:8081/get
             {"test2":"test2value","test1":"test1val"}

```
Here we can add any no.of replica services with minimal changes in sync service. The automation of sync service is not implemented in this project.
