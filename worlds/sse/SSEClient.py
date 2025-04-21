from __future__ import annotations

import asyncio
import collections
import time
from dataclasses import dataclass

import ModuleUpdate
from .Options import SSEOptions
import dolphin_memory_engine as dme

ModuleUpdate.update()

import Utils

from NetUtils import ClientStatus
from CommonClient import gui_enabled, logger, get_base_parser, ClientCommandProcessor, \
    CommonContext, server_loop