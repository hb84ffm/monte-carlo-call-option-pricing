import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style="darkgrid")

class CallPriceEU:
    def __init__(self,S0,K,r,sigma,T,samples):
        self.S0=S0
        self.K=K
        self.r=r
        self.sigma=sigma
        self.T=T
        self.samples=samples

    def _estimate_call_price_mc(self):
        """Estimates the call price C0 by Monte Carlo simulations"""
        Z = np.random.normal(0,1,self.samples) # sample N(0,1) random numbers
        ST = self.S0*np.exp((self.r-0.5*self.sigma**2)*self.T+self.sigma*np.sqrt(self.T)*Z) # calculate terminal stock prices following a GBM & use S0
        payoff=np.maximum(ST-self.K,0) # calculate payoff
        C0_mc=np.exp(-self.r * self.T) * np.mean(payoff) # calculate MC estimator
        return C0_mc

    def _estimate_call_price_bs(self):
        """Estimates the call price C0 by Black Scholes formula"""
        d1 = (np.log(self.S0/self.K)+(self.r+0.5*self.sigma**2)*self.T)/(self.sigma*np.sqrt(self.T))
        d2 = d1-self.sigma * np.sqrt(self.T)
        C0_bs =self.S0*ss.norm.cdf(d1) - self.K * np.exp(-self.r * self.T) * ss.norm.cdf(d2)
        return C0_bs
    
    def _plot_prices(self,C0_mc, C0_bs):
        """Plot Monte Carlo VS Black Scholes option prices as bar charts"""
        prices = [C0_mc, C0_bs]
        labels = ['Monte Carlo', 'Black Scholes']
        x=np.arange(len(labels))

        plt.figure(figsize=(6,4))
        plt.bar(x, prices, width=0.4, color=['#0C0058', '#F06406'])
        plt.xticks(np.arange(len(labels)), labels, fontsize=8)
        plt.yticks(fontsize=8)
        plt.ylabel('Call price', fontsize=8)
        plt.title('Comparison of European call price  at t=0 (Black Scholes VS Monte Carlo)', fontsize=9)
        
        # format each bar & axis
        for i in range(len(prices)):
            plt.text(x[i], prices[i] + 0.5, f"{prices[i]:.4f}", ha='center', fontsize=7)
        plt.ylim(0, max(prices)*1.1)

        # Create the parameter text block
        param_text = (f"INPUTS:\nK={self.K}\nr={self.r}\nsigma={self.sigma}\n"
                      f"S0={self.S0}\nT={self.T}\nSamples={self.samples}")

        # Add text box with inputs to the plot
        plt.text(0.4, # x axis (0=left, 1=right)
                0.90, # y axis (0=bottom, 1=top)
                param_text,
                fontsize=8,
                verticalalignment='top',
                horizontalalignment='left',
                bbox=dict(facecolor='white', alpha=0.8, edgecolor='gray', boxstyle='round,pad=0.5'),
                transform=plt.gca().transAxes) 

        plt.show()

    def run(self):
        """ Orchestrate private methods to calculate prices and plot the chart"""
        mc_price = self._estimate_call_price_mc()
        bs_price = self._estimate_call_price_bs()
        self._plot_prices(mc_price,bs_price) # _plot_prices does not return anything, hence no assignment
