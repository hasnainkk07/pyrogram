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

from typing import Union

import hasnainkk
from hasnainkk import raw


class UnblockUser:
    async def unblock_user(
        self: "hasnainkk.Client",
        user_id: Union[int, str]
    ) -> bool:
        """Unblock a user.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            user_id (``int`` | ``str``)::
                Unique identifier (int) or username (str) of the target user.
                For you yourself you can simply use "me" or "self".
                For a contact that exists in your Telegram address book you can use his phone number (str).

        Returns:
            ``bool``: True on success

        Example:
            .. code-block:: python

                await app.unblock_user(user_id)
        """
        return bool(
            await self.invoke(
                raw.functions.contacts.Unblock(
                    id=await self.resolve_peer(user_id)
                )
            )
        )
