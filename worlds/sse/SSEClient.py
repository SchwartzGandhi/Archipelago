from __future__ import annotations

import asyncio
import collections
import time
from typing import Optional

import dolphin_memory_engine

from dataclasses import dataclass

import ModuleUpdate
from .Options import SSEOptions
from .Addresses import SSEAddresses
import dolphin_memory_engine as dme

ModuleUpdate.update()

import Utils

from NetUtils import ClientStatus
from CommonClient import gui_enabled, logger, get_base_parser, ClientCommandProcessor, \
    CommonContext, server_loop

CONNECTION_REFUSED_GAME_STATUS = (
    "Dolphin failed to connect. Please load a randomized ROM for The Wind Waker. Trying again in 5 seconds..."
)
CONNECTION_REFUSED_SAVE_STATUS = (
    "Dolphin failed to connect. Please load into the save file. Trying again in 5 seconds..."
)
CONNECTION_LOST_STATUS = (
    "Dolphin connection was lost. Please restart your emulator and make sure The Wind Waker is running."
)
CONNECTION_CONNECTED_STATUS = "Dolphin connected successfully."
CONNECTION_INITIAL_STATUS = "Dolphin connection has not been initiated."


class SSECommandProcessor(ClientCommandProcessor):
    """
    Command Processor for The Subspace Emissary client commands.

    This class handles commands specific to The Subspace Emissary.
    """

    def __init__(self, ctx: CommonContext):
        """
        Initialize the command processor with the provided context.

        :param ctx: Context for the client.
        """
        super().__init__(ctx)

    def _cmd_dolphin(self) -> None:
        """
        Display the current Dolphin emulator connection status.
        """
        if isinstance(self.ctx, SSEContext):
            logger.info(f"Dolphin Status: {self.ctx.dolphin_status}")


class SSEContext(CommonContext):
    """"""
    command_processor = SSECommandProcessor
    game: str = "The Subspace Emissary"

    def __init__(self, server_address: Optional[str], password: Optional[str]) -> None:
        super().__init__(server_address, password)

        self.curr_stage: int