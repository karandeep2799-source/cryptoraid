"""Tests for trading strategies."""
import unittest
from datetime import datetime
from strategies.base_strategy import TradeSignal
from strategies.paddle_3way_strategy import Paddle3WayStrategy
from strategies.dca_strategy import DCAStrategy


class TestTradeSignal(unittest.TestCase):
    """Test trade signal generation."""
    
    def test_signal_creation(self):
        signal = TradeSignal(
            symbol='ETHUSDT',
            action='buy',
            price=1000.0,
            quantity=1.0,
            confidence=0.8,
            reason='Test signal',
            timestamp=datetime.now()
        )
        self.assertEqual(signal.symbol, 'ETHUSDT')
        self.assertEqual(signal.action, 'buy')
        self.assertEqual(signal.price, 1000.0)


class TestPaddleStrategy(unittest.TestCase):
    """Test Paddle3Way strategy."""
    
    def setUp(self):
        config = {
            'paddle_count': 3,
            'min_profit': 1,
            'max_position_size': 1000,
            'stop_loss_percent': 5
        }
        self.strategy = Paddle3WayStrategy(config, None)
    
    def test_strategy_initialization(self):
        self.assertEqual(self.strategy.paddle_count, 3)
        self.assertEqual(self.strategy.min_profit, 1)


class TestDCAStrategy(unittest.TestCase):
    """Test DCA strategy."""
    
    def setUp(self):
        config = {
            'buy_interval': 3600,
            'buy_amount': 50
        }
        self.strategy = DCAStrategy(config, None)
    
    def test_strategy_initialization(self):
        self.assertEqual(self.strategy.buy_amount, 50)


if __name__ == '__main__':
    unittest.main()
