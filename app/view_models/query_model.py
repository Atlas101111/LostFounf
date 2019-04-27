
class QueryModel:  # QueryModel can carry the data that HTML needs to render itself
    def __init__(self, lost_info):  # input can be IDCard_info or lost_info
        self.id = lost_info['id']  # id of the record
        self.category = lost_info['category']
        self.title = lost_info['title']
        self.nickname = lost_info['nickname']
        self.description = lost_info['description']
        self.location = lost_info['location']
        self.contact = lost_info['contact']
        self.picture = lost_info['picture']
        if 'cardID' in lost_info:
            self.cardID = lost_info['cardID']









