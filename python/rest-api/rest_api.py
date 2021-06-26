import json


class RestAPI(object):
    def __init__(self, database=None):
        self.database = {
            user["name"]: self._cleanup_user(user) for user in database["users"]
        }

    def get(self, url, payload=None):
        if url == "/users":
            payload = {"users": []} if payload is None else json.loads(payload)
            return json.dumps(self._get_user_data(users=payload["users"]))
        else:
            raise ValueError(f"unknown url: {url}")

    def post(self, url, payload=None):
        if url == "/add":
            payload = json.loads(payload)
            return json.dumps(self._add_user(name=payload["user"]))
        elif url == "/iou":
            payload = json.loads(payload)
            return json.dumps(
                self._add_iou(
                    lender=payload["lender"],
                    borrower=payload["borrower"],
                    amount=payload["amount"],
                )
            )
        else:
            raise ValueError(f"unknown url: {url}")

    def _get_user_data(self, users):
        return {
            "users": sorted(
                [v for k, v in self.database.items() if k in users],
                key=lambda x: x["name"],
            )
        }

    @staticmethod
    def _cleanup_user(user):
        user["owed_by"] = {k: v for k, v in user["owed_by"].items() if v != 0}
        user["owes"] = {k: v for k, v in user["owes"].items() if v != 0}
        user["balance"] = sum(v for k, v in user["owed_by"].items()) - sum(
            v for k, v in user["owes"].items()
        )
        return user

    def _add_user(self, name):
        if name not in self.database:
            new_user = {"name": name, "owes": {}, "owed_by": {}, "balance": 0}
            self.database[name] = new_user
            return new_user

    def _add_iou(self, lender, borrower, amount):
        lender_obj = dict(self.database[lender])
        borrower_obj = dict(self.database[borrower])

        balance = (
            lender_obj["owed_by"].get(borrower, 0)
            - lender_obj["owes"].get(borrower, 0)
            + amount
        )
        if balance >= 0:
            lender_obj["owed_by"][borrower] = balance
            lender_obj["owes"][borrower] = 0
            borrower_obj["owed_by"][lender] = 0
            borrower_obj["owes"][lender] = balance
        else:
            lender_obj["owed_by"][borrower] = 0
            lender_obj["owes"][borrower] = -balance
            borrower_obj["owed_by"][lender] = -balance
            borrower_obj["owes"][lender] = 0

        lender_obj = self._cleanup_user(lender_obj)
        borrower_obj = self._cleanup_user(borrower_obj)

        self.database[lender], self.database[borrower] = (lender_obj, borrower_obj)

        return {"users": sorted([lender_obj, borrower_obj], key=lambda x: x["name"])}
