class Solution:
    def addBinary(self, a: str, b: str) -> str:
        tam = max([len(a), len(b)])
        a = "0" * (tam - len(a)) + a
        b = "0" * (tam - len(b)) + b
        resp = ""
        plus_one = False
        for x in range(tam - 1, -1, -1):
            if a[x] == "1" and b[x] == "1":
                if plus_one:
                    resp = "1" + resp
                else:
                    resp = "0" + resp
                    plus_one = True
            if (a[x] == "0" and b[x] == "1") or (a[x] == "1" and b[x] == "0"):
                if plus_one:
                    resp = "0" + resp
                else:
                    resp = "1" + resp
            if a[x] == "0" and b[x] == "0":
                if plus_one:
                    resp = "1" + resp
                    plus_one = False
                else:
                    resp = "0" + resp
        if plus_one:
            resp = "1" + resp

        return resp
