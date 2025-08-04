#!/usr/bin/env python3
"""
Automatinis Taupuolis.lt generatorius
Veikia kaip cron job arba serverio procesas
"""

import os
import sys
import time
import logging
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess

# Logging nustatymai
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('generator.log'),
        logging.StreamHandler()
    ]
)

class GeneratorHandler(FileSystemEventHandler):
    """Stebi Google Sheets failų pakeitimus"""
    
    def __init__(self):
        self.last_run = 0
        self.cooldown = 60  # 60 sekundžių cooldown tarp generavimų
    
    def on_modified(self, event):
        if event.is_directory:
            return
        
        # Patikrinti, ar praėjo pakankamai laiko nuo paskutinio generavimo
        current_time = time.time()
        if current_time - self.last_run < self.cooldown:
            return
        
        # Patikrinti, ar failas yra Google Sheets arba credentials
        if event.src_path.endswith('.json') or 'credentials' in event.src_path:
            logging.info(f"Pakeitimas aptiktas: {event.src_path}")
            self.run_generator()
            self.last_run = current_time
    
    def run_generator(self):
        """Paleisti generatorių"""
        try:
            logging.info("Pradedamas automatinis generavimas...")
            
            # Paleisti generatorių (jau esame generator kataloge)
            result = subprocess.run([sys.executable, 'generate.py'], 
                                  capture_output=True, text=True)
            
            if result.returncode == 0:
                logging.info("Generavimas sėkmingai baigtas!")
                logging.info(f"Output: {result.stdout}")
            else:
                logging.error(f"Generavimo klaida: {result.stderr}")
                
        except Exception as e:
            logging.error(f"Klaida paleidžiant generatorių: {e}")

def run_continuous():
    """Veikti kaip nuolatinis procesas"""
    logging.info("Pradedamas automatinis generatorius...")
    
    # Sukurti observer
    event_handler = GeneratorHandler()
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=False)
    observer.start()
    
    try:
        # Paleisti pradinį generavimą
        event_handler.run_generator()
        
        # Veikti nuolat
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        logging.info("Stabdant automatinį generatorių...")
        observer.stop()
    
    observer.join()

def run_once():
    """Paleisti generatorių vieną kartą"""
    logging.info("Paleidžiamas generatorius vieną kartą...")
    
    try:
        result = subprocess.run([sys.executable, 'generate.py'], 
                              capture_output=True, text=True)
        
        if result.returncode == 0:
            logging.info("Generavimas sėkmingai baigtas!")
            return True
        else:
            logging.error(f"Generavimo klaida: {result.stderr}")
            return False
            
    except Exception as e:
        logging.error(f"Klaida: {e}")
        return False

def setup_cron():
    """Nustatyti cron job (Linux/Mac)"""
    project_root = os.path.dirname(os.getcwd())  # Grįžti į pagrindinį katalogą
    cron_command = f"*/5 * * * * cd {project_root}/generator && {sys.executable} auto_generator.py --once"
    
    print("Pridėkite šią eilutę į crontab (crontab -e):")
    print(cron_command)
    print("\nArba paleiskite:")
    print(f"echo '{cron_command}' | crontab -")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Taupuolis.lt automatinis generatorius')
    parser.add_argument('--once', action='store_true', help='Paleisti vieną kartą')
    parser.add_argument('--cron', action='store_true', help='Rodyti cron nustatymus')
    
    args = parser.parse_args()
    
    if args.cron:
        setup_cron()
    elif args.once:
        run_once()
    else:
        run_continuous() 