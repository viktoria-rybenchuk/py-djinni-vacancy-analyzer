# Scrapy Data Analysis

This project includes code for scraping job data from a website using Scrapy and analyzing the scraped data using pandas and matplotlib.


## Table of Contents

- [Project Title](#project-title)
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)


## Introduction

The purpose of this project is to analyze the demand for technology skills using Python and provide insights into the job market. The project aims to assist individuals and organizations in understanding the current trends and requirements in the technology industry. By leveraging web scraping techniques and data analysis, the project extracts job data from Djinni and performs various analyses to identify the demand for different technologies.

## Features

   - The Scrapy spider (DjinniSpider) scrapes job data from a specific URL.
   - The scraped data includes information such as job title, company name, experience level, technologies, viewers, and applicants.
   - The scraped data is stored in a CSV file (scraped_data.csv) using the CsvItemExporter provided by Scrapy. 
   - The pandas library is used to load and analyze the scraped data. 
   - Various data analysis operations are performed, including grouping and aggregating data, generating plots, and calculating correlations. 
   - The results of the analysis are displayed using matplotlib.


## Installation
````
git clone git@github.com:viktoria-rybenchuk/py-djinni-vacancy-analyzer.git
pip install requirements.txt
scrapy crawl djinni
````