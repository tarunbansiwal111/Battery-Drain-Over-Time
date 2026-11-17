# Battery Drain Over Time

A small Python project that calculates battery usage from sample readings and plots the battery level over time.

## What it does

- Prints a table of battery levels and the drain between consecutive readings.
- Calculates the total battery drain across the sample period.
- Displays a line chart of battery percentage over time.

## Requirements

- Python 3
- Packages listed in [`requirements.txt`](requirements.txt)

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

Run the analysis:

```bash
python battery_drain.py
```

The script prints the readings and drain summary in the terminal, then opens a chart window. The sample times and battery percentages are defined near the top of `battery_drain.py`; edit those lists to analyze different readings.
