
import asyncio
import os
from dotenv import load_dotenv

from viam.robot.client import RobotClient
from viam.rpc.dial import Credentials, DialOptions
from viam.components.motor import Motor

"""
    Credentials are imported through a .env file with the following structure:
    ADDRESS=robot.organisation.viam.cloud
    SECRET=yoursecret
"""
load_dotenv()


async def connect():
    creds = Credentials(
        type='robot-location-secret',
        payload=os.getenv('SECRET'))
    opts = RobotClient.Options(
        refresh_interval=0,
        dial_options=DialOptions(credentials=creds)
    )
    return await RobotClient.at_address(os.getenv('ADDRESS'), opts)


async def main():
    robot = await connect()

    # mymotor
    mymotor = Motor.from_robot(robot, "mymotor")
    mymotor_return_value = await mymotor.is_moving()
    print(f"mymotor is_moving return value: {mymotor_return_value}")

    # Custom DoCommand example
    await mymotor.do_command({"log": "message"})
    print("Check the log entries on app.viam.com!")


    # Don't forget to close the robot when you're done!
    await robot.close()

if __name__ == '__main__':
    asyncio.run(main())
