class Solution:

    def encode(self, strs: List[str]) -> str:
        print("innn", strs, "")
        if [] == strs:
            return "0000099999"
        elif  [""] ==strs:
            return ""
        return "-".join(strs)


    def decode(self, s: str) -> List[str]:
        print("outtt----",)
        if s == "0000099999":
            return []
        if s == "":
            return [""]
        return s.split("-")
