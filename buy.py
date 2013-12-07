class BitcoinBuy():
    def __init__(self, account, range):
        #账户余额
        self.account = account
        #设置波动范围
        self.range = range
        self.last_price = 0
        self.now_price = 0

    def decide(self):
        if self.now_price - self.last_price >= self.range:
            self.sell()
        elif self.last_price - self.now_price >= self.range:
            self.buy()

    def get_price(self):
        pass

    def get_account(self):
        pass

    def buy(self):
        account = self.get_account()
        price = self.get_price()

    def sell(self):
        pass
