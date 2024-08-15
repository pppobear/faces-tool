class NewFace:
    id: int
    unlock_type: int | None
    condition: str | None
    file_url: str
    pic_url: str
    unlock_pic: str | None

    def __init__(self, id_: int, unlock_type: int | None, condition: str | None, file_url: str, pic_url: str, unlock_pic: str | None):
        self.id = id_
        self.unlock_type = unlock_type
        self.condition = condition
        self.file_url = file_url
        self.pic_url = pic_url
        self.unlock_pic = unlock_pic

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "unlockType": self.unlock_type,
            "condition": self.condition,
            "fileUrl": self.file_url,
            "picUrl": self.pic_url,
            "unlockPic": self.unlock_pic
        }

    @staticmethod
    def from_dict(data: dict) -> 'NewFace':
        return NewFace(
            id_=data['id'],
            unlock_type=data['unlockType'],
            condition=data['condition'],
            file_url=data['fileUrl'],
            pic_url=data['picUrl'],
            unlock_pic=data.get('unlockPic', None)
        )


class NewFaceTab:
    name: str
    faces: list[NewFace]

    def __init__(self, name: str, faces: list[NewFace]):
        self.name = name
        self.faces = faces

    def to_dict(self) -> dict:
        return {
            'tab': self.name,
            'faceVos': [face.to_dict() for face in self.faces]
        }

    @staticmethod
    def from_dict(data: dict) -> 'NewFaceTab':
        return NewFaceTab(
            name=data['tab'],
            faces=[NewFace.from_dict(face_data) for face_data in data['faceVos']]
        )


def serialize_to_dict_list(tabs: list[NewFaceTab]) -> list[dict]:
    return [tab.to_dict() for tab in tabs]


def deserialize_tabs(data: list[dict]):
    return [NewFaceTab.from_dict(d) for d in data]
