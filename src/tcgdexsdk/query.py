from urllib.parse import quote


class Query:
    def __init__(self):
        self.params = []
        
    def encode(self, value):
        return quote(
            str(value)
            .replace('?', '%3F')
            .replace(r'["\'\\u0300-\\u036f]', '')
        )

    def build(self):
        return '?' + '&'.join(
            f"{self.encode(item['key'])}={self.encode(item['value'])}" for item in self.params
        )

    def includes(self, key: str, value: str):
        return self.contains(key, value)

    def like(self, key: str, value: str):
        return self.contains(key, value)

    def contains(self, key: str, value: str):
        self.params.append({'key': key, 'value': value})
        return self

    def equal(self, key: str, value: str):
        self.params.append({'key': key, 'value': f'eq:{value}'})
        return self

    def sort(self, key: str, order: str):
        self.params.append({'key': 'sort:field', 'value': key})
        self.params.append({'key': 'sort:order', 'value': order})
        return self

    def greaterOrEqualThan(self, key: str, value: int):
        self.params.append({'key': key, 'value': f'gte:{value}'})
        return self
        
    def gte(self, key: str, value: int):
        return self.greaterOrEqualThan(key, value)

    def lesserOrEqualThan(self, key: str, value: int):
        self.params.append({'key': key, 'value': f'lte:{value}'})
        return self
        
    def lte(self, key: str, value: int):
        return self.lesserOrEqualThan(key, value)

    def greaterThan(self, key: str, value: int):
        self.params.append({'key': key, 'value': f'gt:{value}'})
        return self
        
    def gt(self, key: str, value: int):
        return self.greaterThan(key, value)

    def lesserThan(self, key: str, value: int):
        self.params.append({'key': key, 'value': f'lt:{value}'})
        return self
        
    def lt(self, key: str, value: int):
        return self.lesserThan(key, value)

    def isNull(self, key: str):
        self.params.append({'key': key, 'value': 'null:'})
        return self

    def paginate(self, page: int, itemsPerPage: int):
        self.params.append({'key': 'pagination:page', 'value': page})
        self.params.append({
            'key': 'pagination:itemsPerPage',
            'value': itemsPerPage
        })
        return self
        
    def notEqual(self, key: str, value: str):
        self.params.append({'key': key, 'value': f'neq:{value}'})
        return self

    def notContains(self, key: str, value: str):
        self.params.append({'key': key, 'value': f'not:{value}'})
        return self

    def notIncludes(self, key: str, value: str):
        return self.notContains(key, value)

    def notLike(self, key: str, value: str):
        return self.notContains(key, value)

    def notNull(self, key: str):
        self.params.append({'key': key, 'value': 'notnull:'})
        return self