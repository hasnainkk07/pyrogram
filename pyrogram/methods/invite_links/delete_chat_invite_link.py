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


class DeleteChatInviteLink:
    async def delete_chat_invite_link(
        self: "hasnainkk.Client",
        chat_id: Union[int, str],
        invite_link: str,
    ) -> bool:
        """Delete an already revoked invite link.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier for the target chat or username of the target channel/supergroup
                (in the format @username).

            invite_link (``str``):
                The revoked invite link to delete.

        Returns:
            ``bool``: On success ``True`` is returned.
        """

        return await self.invoke(
            raw.functions.messages.DeleteExportedChatInvite(
                peer=await self.resolve_peer(chat_id),
                link=invite_link,
            )
        )
