class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        buy_ind, sell_ind = 0, 1
        maybe_buy_ind = 0

        for i in range(1, len(prices)):
            if prices[i] - prices[maybe_buy_ind] >= prices[sell_ind] - prices[buy_ind]:
                sell_ind = i
                buy_ind = maybe_buy_ind
                print('buy', i, sell_ind, buy_ind)
            if prices[i] < prices[maybe_buy_ind]:
                maybe_buy_ind = i
                print('comp', prices[i], prices[buy_ind])

        return max(0, prices[sell_ind] - prices[buy_ind])
            

            