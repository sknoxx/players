
# Players Project

## Overview

This repository provides tools for scraping, processing, and analysing football player data. The project includes scripts for extracting player information from web sources, managing player datasets, and handling football-related names and locators.

## Directory Structure

- `football_names.py` — Utilities for handling football player names.
- `players.csv` — Dataset containing football player information.
- `players.py` — Core logic for managing and processing player data.
- `scrape_players.py` — Script for scraping football player data from web sources.
- `wik_page_locators.py` — Locators and utilities for Wikipedia page extraction.
- `__pycache__/` — Compiled Python files (auto-generated).

## Requirements

- Python 3.8 or higher
- Required packages: requests, pandas, beautifulsoup4

## Installation

1. Clone the repository:
   ```pwsh
   git clone https://github.com/sknoxx/players.git
   ```
2. Install dependencies:
   ```pwsh
   pip install -r requirements.txt
   ```

## Usage

- To scrape player data:
  ```pwsh
  python scrape_players.py
  ```
- To process or analyse player data:
  ```pwsh
  python players.py
  ```

## Licence

This project is licensed under the MIT Licence.

## Contact

For queries or contributions, please contact the repository owner.
