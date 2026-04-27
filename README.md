# RimWorld Mod Load Order Sorter Trey Runner

A simple Python tool that takes a Steam Workshop collection ID and generates a sorted RimWorld mod load order based on priority rules.

---

## Overview

This project pulls mods from a public Steam Workshop collection and sorts them based on keywords such as frameworks, DLCs, and content types. The goal is to improve load order organization beyond simple alphabetical sorting.

---

## Features

- Accepts a Steam Workshop collection ID
- Retrieves all mods from the collection using Steam API
- Filters out invalid or missing mods
- Sorts mods based on priority (frameworks before assets)
- Displays a clean load order list in the terminal

---

## Requirements

- Python 3
- requests library

Install dependencies:

```bash
python -m pip install requests
