"""
investment.py Module is for calculating Fixed Deposit and SIP investment

"""
class investment:
    """
    Investment Class is used represent an investment
    This Contains Operations to calculate

    Attributes:
        amount (float): investment amount
        returns_rate (float): returns rate 12% => 12
        time (int): time in years
        number (int) : No.of times interest is calculated per year
    """
    def __init__(self,amount,return_rate,time,number):
        self._amount = amount
        self._return_rate = return_rate
        self._time = time
        self._number = number

    @property
    def amount(self):
        """
        Getter for amount
        
        Returns Amount
        """
        return self._amount
    @property
    def return_rate(self):
        """
        Getter for return_rate
        
        Returns return rate
        """
        return self._return_rate
    @property
    def time(self):
        """
        Getter for time
        
        retruns defined time period
        """
        return self._time
    @property
    def number(self):
        """
        This getter is for no of times interest is calculated
        retruns int
        """
        return self.number
    def calculation(self):
        """
        Docstring for calculation
        """
        pass
    
class FixedDeposit(investment):
    """
    This is Sub class of investment for calculating fixed deposit
    Attributes:
        amount (float): investment amount
        returns_rate (float): returns rate 12% => 12
        time (int): time in years
        number (int) : No.of times interest is calculated per year
    """
    def calculation(self):
        """
        This Method Calculates Fixed Despoit
        
        returns total_amount(Float)
        By default no of times interest calculated in a year is one
        """
        returns = self.returns_rate/100
        total_amount = self._amount * ( 1 + (returns/self._number)) ** (self._time * self._number)
        return total_amount

class SIP(investment):
    """
    This is sub class of investment which is used for calculating SIP

    """
    def calculation(self):
        """
        This Calculation is for SIP
        
        retruns total amount in which type of integer is float
        """
        months = self.time * 12
        yearly_returns = self.returns_rate/100
        returns = yearly_returns/12
        total_amount = (
            self.amount
            * (((1 + returns) ** months - 1) / returns)
            * (1 + returns)
        )
        return total_amount