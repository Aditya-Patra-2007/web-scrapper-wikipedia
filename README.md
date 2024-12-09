# Wikipedia Web Scraper

A Python-based web scraper that extracts information from Wikipedia pages. This tool allows users to search for Wikipedia articles and retrieve both the infobox data and the first two paragraphs of the article.

## Features

- Search for Wikipedia articles
- Display similar article suggestions
- Extract infobox data (key-value pairs)
- Retrieve article introductory paragraphs
- Interactive command-line interface

## Prerequisites

Before running this script, you need to have Python installed on your system along with the following packages:

```
wikipedia
requests
beautifulsoup4
```

## Installation

1. Clone this repository or download the Python file
2. Install the required packages using pip:
   ```
   pip install wikipedia-api
   pip install requests
   pip install beautifulsoup4
   ```

## How to Run

1. Open your terminal or command prompt
2. Navigate to the project directory
3. Run the script:
   ```
   python "web scrapper wikipedia.py"
   ```
4. Follow the interactive prompts:
   - Enter your search term when prompted with "search:"
   - From the list of similar articles, choose the exact one you want
   - Enter the exact title of the article you want to read about

## Usage Example

```
search: Python
['Python', 'Python (programming language)', 'Pythonidae', 'Python (mythology)', ...]
which one is it search it below
search: Python (programming language)
```

The script will then display:
1. The infobox information in a key-value format
2. The first two paragraphs of the article

## Note

- Make sure you have an active internet connection
- The search term should be precise for better results
- The script will continue running until manually stopped
