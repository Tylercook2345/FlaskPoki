def to_dict(self):
    return{
        'id': self.id,
        'title': self.title,
        'image': self.image,
        'caption': self.caption,
        'date_created': self.date_created,
        'user_id': self.user_id
    }