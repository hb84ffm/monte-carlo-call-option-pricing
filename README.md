# monte-carlo-call-option-pricing

A Python module to price a Euroepan call option at t=0 by Monte Carlo simulation, which is benchmarked against Black Schoels formula.

### FEATURES
- Simulates stock prices following a geometric Brownian motion
- Calculates payoffs at t=T and averages the paths
- Discounts the resut to t=0
  
### INSTALLATION
1. Clone the repository:<br>
       git clone https://github.com/hb84ffm/monte-carlo-call-option-pricing.git<br>
       cd monte-carlo-call-option-pricing<br>

2. Create & activate your virtual environment:<br>
       python3 -m venv venv<br>
       source venv/bin/activate      # On Mac/Linux<br>
       venv\Scripts\activate         # On Windows

3. Install dependencies:<br>
       pip install -r requirements.txt

### USAGE
1. Instantiate class CallPriceEU with attributes<br>
   CallPriceEU(S0=start_stock_price, K=strike, r=rate, sigma=volatility, T=timeframe, samples=nr_of_iterations)<br>
3. Apply method run() afterwards, which orchestrates the simulation and plotting of the two bar charts<br>

### EXAMPLE WORKFLOW
See provided Jupyter notebook **example.ipynb** for explanation.

### AUTHOR
For questions or feedback reach out to me via: [GitHub](https://github.com/hb84ffm).
