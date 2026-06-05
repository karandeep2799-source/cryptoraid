"""Enhanced Trading Bot Main Entry Point."""
import logging
import sys
import time
import os
from configparser import ConfigParser
from pathlib import Path
from art import text2art

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/cryptoraid.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class CryptoRaidBot:
    """Main trading bot orchestrator."""
    
    def __init__(self, config_path: str):
        """
        Initialize the trading bot.
        
        Args:
            config_path: Path to configuration file
        """
        # Create necessary directories
        Path('logs').mkdir(exist_ok=True)
        Path('data').mkdir(exist_ok=True)
        
        # Load configuration
        self.config = ConfigParser()
        self.config.read(config_path)
        
        # Print banner
        welcome = text2art(f"CryptoRaid v{self.config['core']['version']}")
        logger.info(f"\n{welcome}")
        logger.info("Trading bot initialized successfully")
    
    def run(self):
        """
        Main bot loop.
        """
        logger.info("Starting trading bot...")
        
        try:
            iteration = 0
            while True:
                iteration += 1
                logger.debug(f"Iteration {iteration}")
                logger.info(f"Bot running - Iteration {iteration}")
                
                # Sleep before next iteration
                time.sleep(int(self.config['main']['interval']))
                
        except KeyboardInterrupt:
            logger.info("Bot interrupted by user")
        except Exception as e:
            logger.error(f"Critical error: {e}")
            sys.exit(1)


if __name__ == "__main__":
    bot = CryptoRaidBot('config.ini')
    bot.run()
