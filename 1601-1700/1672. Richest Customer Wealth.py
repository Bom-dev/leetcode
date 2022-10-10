class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        rich = 0
        for account in accounts:
            rich = max(sum(account), rich)
        return rich

# class Solution:
#     def maximumWealth(self, accounts: List[List[int]]) -> int:
#         wealthes = []
#         total = 0
#         for i in range(len(accounts)):
#             for x in range(len(accounts[i])):
#                 total += accounts[i][x]
#             wealthes.append(total)
#             total = 0
#         return max(wealthes)