"""
Implementation of a User.
"""


class User:
    """
    Class definition of a User.
    """

    def __init__(self, id: int) -> None:
        """
        Initialization.
        """
        self.id = id
        usernames: list[str] = [
            "Blake",
            "Ricky",
            "Shelley",
            "Dave",
            "George",
            "John",
            "James",
            "Mitch",
            "Williamson",
            "Burry",
            "Vennett",
            "Shipley",
            "Geller",
            "Rickert",
            "Carrell",
            "Baum",
            "Brownfield",
            "Lippmann",
            "Moses",
        ]

        self.username: str = f"{usernames[id % len(usernames)]}#{id}"

    def __eq__(self, other):
        """
        Equality.
        """
        return isinstance(other, User) and self.id == other.id

    def __lt__(self, other):
        """
        Less than.
        """
        return isinstance(other, User) and self.id < other.id

    def __gt__(self, other):
        """
        Greater than.
        """
        return isinstance(other, User) and self.id > other.id

    def __repr__(self) -> str:
        """
        String representation.
        """
        return "".join(self.username)
