from flask import jsonify


class UserRepository:
    def insert(self, request):
        request.data

    def update(self):
        ...

    def destroy(self):
        ...

    def show(self):
        ...

    def all(self):
        return [
            {
                "name": "Emilia"
            },
            {
                "name": "João"
            }
        ]
