
import asyncio

from viam.robot.client import RobotClient
from viam.rpc.dial import Credentials, DialOptions
from viam.components.motor import Motor


async def connect():
    creds = Credentials(
        type='robot-location-secret',
        payload='inkfhj1ednexdgfd2w67ooneye8g0tr4yoiu5k6b0fwoqrjm')
    opts = RobotClient.Options(
        refresh_interval=0,
        dial_options=DialOptions(credentials=creds)
    )
    return await RobotClient.at_address('mac-legacy-main.ijvyv7a6iy.viam.cloud', opts)


async def main():
    robot = await connect()

    # mymotor
    mymotor = Motor.from_robot(robot, "mymotor")
    mymotor_return_value = await mymotor.is_moving()
    print(f"mymotor is_moving return value: {mymotor_return_value}")

    await mymotor.do_command({})
    print("Check the log entries on app.viam.com!")


    # Don't forget to close the robot when you're done!
    await robot.close()

if __name__ == '__main__':
    asyncio.run(main())
