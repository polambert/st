#!/usr/bin/python3

from source.SettingsLoader import *
from source.Runtime import *

from source.Commands import *

## Load Settings
settings = SettingsLoader.ReadFile("config/settings.conf")

## Initialize Everything
Commands.Init()

## Start
Runtime.Run(settings)
