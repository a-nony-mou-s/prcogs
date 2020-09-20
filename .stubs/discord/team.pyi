from typing import List, Optional

from .asset import Asset
from .enums import TeamMembershipState
from .user import BaseUser

class Team:
    id: int
    name: str
    icon: Optional[str]
    owner_id: int
    members: List[TeamMember]
    @property
    def icon_url(self) -> Asset: ...
    @property
    def owner(self) -> Optional[TeamMember]: ...

class TeamMember(BaseUser):
    team: Team
    membership_state: TeamMembershipState
