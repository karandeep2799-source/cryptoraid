"""Tests for risk management."""
import unittest
from risk_management import RiskManager


class TestRiskManager(unittest.TestCase):
    """Test risk management controls."""
    
    def setUp(self):
        config = {
            'max_daily_loss_percent': 2,
            'max_position_size': 1000,
            'max_concurrent_trades': 3,
            'stop_loss_percent': 5,
            'trailing_stop_percent': 2
        }
        self.risk_manager = RiskManager(config)
    
    def test_can_trade_initial(self):
        """Test that trading is allowed initially."""
        self.assertTrue(self.risk_manager.can_trade())
    
    def test_validate_position(self):
        """Test position validation."""
        valid = self.risk_manager.validate_position('ETHUSDT', 500)
        self.assertTrue(valid)
        
        invalid = self.risk_manager.validate_position('ETHUSDT', 2000)
        self.assertFalse(invalid)
    
    def test_add_position(self):
        """Test adding position."""
        self.risk_manager.add_position('ETHUSDT', 1000.0, 1.0)
        self.assertIn('ETHUSDT', self.risk_manager.positions)
    
    def test_portfolio_risk(self):
        """Test portfolio risk calculation."""
        risk = self.risk_manager.get_portfolio_risk()
        self.assertIn('open_positions', risk)
        self.assertIn('can_trade', risk)


if __name__ == '__main__':
    unittest.main()
