class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver_sep_1 = list(map(int, version1.split(".")))
        ver_sep_2 = list(map(int, version2.split(".")))

        if len(ver_sep_1) > len(ver_sep_2):
            for _ in range(len(ver_sep_1) - len(ver_sep_2)):
                ver_sep_2.append(0)

        if len(ver_sep_1) < len(ver_sep_2):
            for _ in range(len(ver_sep_2) - len(ver_sep_1)):
                ver_sep_1.append(0)

        for v1, v2 in zip(ver_sep_1, ver_sep_2):
            if int(v1) > int(v2):
                return 1

            if int(v1) < int(v2):
                return -1

        return 0
