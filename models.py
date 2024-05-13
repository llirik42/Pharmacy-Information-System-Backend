from sqlmodel import SQLModel, Field


class SongBase(SQLModel):
    name: str = Field(nullable=True)
    artist: str = Field(max_length=190)


class Song(SongBase, table=True):
    id: int = Field(primary_key=True)


class SongCreate(SongBase):
    pass
