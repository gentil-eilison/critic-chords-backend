class Stat:
    def __init__(
        self, 
        reviews_liked: int, 
        albums_rated: int, 
        reviews_written: int
    ):
        self._reviews_liked = reviews_liked
        self._albums_rated = albums_rated
        self._reviews_written = reviews_written
    

    @property
    def reviews_liked(self) -> str:
        return self._reviews_liked

    @property
    def albums_rated(self) -> str:
        return self._albums_rated

    @property
    def reviews_written(self) -> str:
        return self._reviews_written
