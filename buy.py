from urllib.request import urlopen


class BitcoinBuy():
    def __init__(self, account, threshold):
        #账户余额
        self.account = account
        #阈值
        self.threshold = threshold
        self.last_price = 0
        self.now_price = self.get_price()

    def decide(self):
        if self.now_price - self.last_price >= self.range:
            self.sell()
        elif self.last_price - self.now_price >= self.range:
            self.buy()

    def get_price(self):
        url = 'http://blockchain.info/ticker'
        response = urlopen(url)
        price = response.read().decode()


    def get_account(self):
        pass

    def buy(self):
        account = self.get_account()
        price = self.get_price()
        #购买的数量（整数个）
        buy_num = account // price
        cost = price * buy_num
        self.account = account - cost

    def sell(self):
        pass


if __name__ == '__main__':
    pass