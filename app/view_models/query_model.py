

class QueryViewModel:  # QueryModel can carry the data that HTML needs to render itself
    def __init__(self, info):  # input is a list of KeyedTuple
        self.id = info.id
        self.category = info.category
        self.title = info.title
        self.description = info.description
        self.location = info.location
        self.contact = info.contact
        self.contact_info = info.contact_info
        self.cardID = info.cardID
        self.kind = info.kind
#        self.nickname = info.user.nickname
#        self.avatarUrl = info.user.avatarUrl
        self.photo = info.photo

    def keys(self):
        # result = ['category', 'title', 'description', 'location',
        #           'contact', 'contact_info', 'nickname', 'avatarUrl',
        #           'photo']
        result = ['id', 'category', 'title', 'description', 'location',
                  'contact', 'contact_info', 'kind', 'photo']
        if self.cardID != '0':
            result.append('cardID')
        return result

    def __getitem__(self, o):
        return getattr(self, o)


class QueryModelCollection:
    def __init__(self):
        self.total = 0
        self.data = []
        self.keyword = ''

    def fill(self, infos, keyword):
        self.keyword = keyword
        self.total = len(infos)
        self.data = [dict(QueryViewModel(info)) for info in infos]
        print(self.data)

    def keys(self):
        return ['total', 'data', 'keyword']

    def __getitem__(self, o):
        return getattr(self, o)





