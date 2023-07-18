from typing import ClassVar, Coroutine, Mapping, Sequence, Any, Dict, Optional, Tuple, cast
from typing_extensions import Self
from viam.components.component_base import ValueTypes

from viam.module.types import Reconfigurable
from viam.proto.app.robot import ComponentConfig
from viam.proto.common import ResourceName, Vector3
from viam.resource.base import ResourceBase
from viam.resource.types import Model, ModelFamily

from viam.components.motor import Motor
from viam.logging import getLogger

import time
import asyncio

LOGGER = getLogger(__name__)

class MyMotor(Motor, Reconfigurable):
    MODEL: ClassVar[Model] = Model(ModelFamily("custom", "motor"), "mymotor")
    
    # create any class parameters here, 'some_pin' is used as an example (change/add as needed)
    some_pin: int

    # Constructor
    @classmethod
    def new(cls, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]) -> Self:
        my_class = cls(config.name)
        my_class.reconfigure(config, dependencies)
        return my_class

    # Validates JSON Configuration
    @classmethod
    def validate(cls, config: ComponentConfig):
        # here we validate config, the following is just an example and should be updated as needed
        some_pin = config.attributes.fields["some_pin"].number_value
        if some_pin == "":
            raise Exception("A some_pin must be defined")
        return

    # Handles attribute reconfiguration
    def reconfigure(self, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]):
        # here we initialize the resource instance, the following is just an example and should be updated as needed
        self.some_pin = int(config.attributes.fields["some_pin"].number_value)
        return

    """ Implement the methods the Viam RDK defines for the Motor API (rdk:components:motor) """

    
    async def set_power(
        self,
        power: float,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ):
        """
        Sets the "percentage" of power the motor should employ between -1 and 1.
        When ``power`` is negative, the rotation will be in the backward direction.

        Args:
            power (float): Power between -1 and 1
                (negative implies backwards).
        """
        ...

    
    async def go_for(
        self,
        rpm: float,
        revolutions: float,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ):
        """
        Spin the motor the specified number of ``revolutions`` at specified ``rpm``.
        When ``rpm`` or ``revolutions`` is a negative value, the rotation will be in the backward direction.
        Note: if both ``rpm`` and ``revolutions`` are negative, the motor will spin in the forward direction.

        Args:
            rpm (float): Speed at which the motor should move in rotations per minute
                (negative implies backwards).
            revolutions (float): Number of revolutions the motor should run for
                (negative implies backwards).
        """
        ...

    
    async def go_to(
        self,
        rpm: float,
        position_revolutions: float,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ):
        """
        Spin the motor to the specified position (provided in revolutions from home/zero),
        at the specified speed, in revolutions per minute.
        Regardless of the directionality of the ``rpm`` this function will move
        the motor towards the specified position.

        Args:
            rpm (float): Speed at which the motor should rotate (absolute value).
            position_revolutions (float): Target position relative to home/zero, in revolutions.
        """
        ...

    
    async def reset_zero_position(
        self,
        offset: float,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ):
        """
        Set the current position (modified by ``offset``) to be the new zero (home) position.

        Args:
            offset (float): The offset from the current position to new home/zero position.
        """
        ...

    
    async def get_position(
        self,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> float:
        """
        Report the position of the motor based on its encoder.
        The value returned is the number of revolutions relative to its zero position.
        This method will raise an exception if position reporting is not supported by the motor.

        Returns:
            float: Number of revolutions the motor is away from zero/home.
        """
        return 1

    
    async def get_properties(
        self,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> Motor.Properties:
        return Motor.Properties(position_reporting=True)
        # TODO: "Properties" was not defined -> seems not covered by the tool yet thus remapped to Motor.Properties
        """
        Report a dictionary mapping optional properties to
        whether it is supported by this motor.

        Returns:
            Properties: Map of feature names to supported status.
        """

    
    async def stop(
        self,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ):
        """
        Stop the motor immediately, without any gradual step down.
        """
        ...

    
    async def is_powered(
        self,
        *,
        extra: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None,
        **kwargs,
    ) -> Tuple[bool, float]:
        """
        Returns whether or not the motor is currently running.

        Returns:
            bool: Indicates whether the motor is currently powered.
            float: The current power percentage of the motor
        """
        return [True, 0.5]

    
    async def is_moving(self) -> bool:
        """
        Get if the motor is currently moving.

        Returns:
            bool: Whether the motor is moving.
        """
        return True

    async def do_command(self, command: Mapping[str, ValueTypes], *, timeout: float | None = None, **kwargs) -> Coroutine[Any, Any, Mapping[str, ValueTypes]]:
        for (key, value) in command.items():
            if key == "log":
                LOGGER.info(f'Info: Command {key} with {value} executed!')
            else:
                LOGGER.warning(f'Info: Random command {key}: {value} executed!')
        return {}