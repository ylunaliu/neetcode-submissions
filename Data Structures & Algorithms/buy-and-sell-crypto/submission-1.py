class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price_so_far=float('inf')
        max_profit_so_far=0
        for price in prices:
            if price< min_price_so_far:
                min_price_so_far = price
            max_profit_so_far = max(max_profit_so_far, price-min_price_so_far)
        return max_profit_so_far