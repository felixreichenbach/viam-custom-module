"""
This file registers the model with the Python SDK.
"""

from viam.components.motor import Motor
from viam.resource.registry import Registry, ResourceCreatorRegistration

from .mymotor import MyMotor

Registry.register_resource_creator(Motor.SUBTYPE, MyMotor.MODEL, ResourceCreatorRegistration(MyMotor.new, MyMotor.validate))
