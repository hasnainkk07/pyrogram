#  hasnainkk - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#
#  This file is part of hasnainkk.
#
#  hasnainkk is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  hasnainkk is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with hasnainkk.  If not, see <http://www.gnu.org/licenses/>.

import hasnainkk
from hasnainkk import raw
from .menu_button import MenuButton


class MenuButtonCommands(MenuButton):
    """A menu button, which opens the bot's list of commands.
    """

    def __init__(self):
        super().__init__("commands")

    async def write(self, client: "hasnainkk.Client") -> "raw.types.BotMenuButtonCommands":
        return raw.types.BotMenuButtonCommands()
