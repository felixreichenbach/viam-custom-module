# Viam Custom Model Example

A simple example of how to implement a custom motor model and how to extend it with a custom DoCommand in Python. To create the file structure and generate the boiler plate code segments, the [Viam Module Generator](https://github.com/viam-labs/generator-viam-module) was used.

## Prerequisits

A robot instance has been created and is registered with the viam cloud backend.

## Installation and Configuration

1. Clone the Github repo
2. Get the path to the run.sh file
3. Go to [Viam App](https://app.viam.com)
4. Add a new module to the configuration: Name: ```mymotor``` and Executable Path: ```<-Your-Path-To->/run.sh```
5. Add a new component to the configuration: 
``` {
      "namespace": "rdk",
      "attributes": {},
      "depends_on": [],
      "type": "motor",
      "name": "mymotor",
      "model": "custom:motor:mymotor"
    }
```
6. If not running already start the viam-server
    
## Usage

1. Create a .env file in the same directory as the run.sh file
2. Add your credentials to it:
```
    ADDRESS=robot.organisation.viam.cloud
    SECRET=your-secret
```
3. Run ```python robot.py``` -> you should see the following console output:
```
    mymotor is_moving return value: True
    Check the log entries on app.viam.com!
```
4. In the viam server console output or via app.viam.com under Logs you should be able to find the following entry:
```
Command log with message executed!
```
5. Feel free to play with the do_command client in robot.py and the execution part in mymotor.py to trigger a warning message in the logs or customize it to your needs.
