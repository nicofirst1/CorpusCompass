"""
Main module to start Corpus Compass
"""
import sys
from src.corpus_compass_app import CorpusCompassApp


if __name__ == "__main__":
    app = CorpusCompassApp(sys.argv)
    app.start()
