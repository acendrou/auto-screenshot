# auto-screenshot
This project aims to be a simple way to automatically save a screenshot of your monitor every 30 seconds.
The images are saved in a folder that is named after the current date and the filenames are also using datetime.

## Features matrix

| features                           | V1                 | V2                 | V3                 |
|------------------------------------|--------------------|--------------------|--------------------|
| folder by day                      | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
| multiple monitor support           | :x:                | :heavy_check_mark: | :heavy_check_mark: |
| ability to be halted and restarted | :x:                | :x:                | :heavy_check_mark: |
| configuration made outside .py     | :x:                | :x:                | :heavy_check_mark: |

## Support matrix
Tested on :

| platform           | V1                 | V2                 | V3                 |
|--------------------| -------------------|--------------------|--------------------|
| Windows 7          | :heavy_check_mark: | :x:                | :x:                |
| Windows 10         | :x:                | :heavy_check_mark: | :heavy_check_mark: |
| Linux UBUNTU 20.04 | :x:                | :heavy_check_mark: | :x:                |

## Installation

This project is written in Python 3. Libraries dependencies can be obtained from Pypi and they are listed in file requirements.txt in each app folder.