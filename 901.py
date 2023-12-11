class StockSpanner:

    def __init__(self):
        self.prices = []
        self.spans = []

    def next(self, price: int) -> int:
        if len(self.prices) == 0:
            self.prices.append(price)
            self.spans.append(1)
            return 1
        idx = len(self.spans)-1
        span_count = 1
        while idx >= 0 and self.prices[idx] <= price:
            span_count += self.spans[idx]
            idx -= self.spans[idx]
        self.prices.append(price)
        self.spans.append(span_count)
        return span_count


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
