import matplotlib.pyplot as plt

def plot_market_cap_dist(df):
    df_sorted= df.sort_values(by='Market Cap (USD)', ascending=False)
    top= df_sorted.head()
    fig, ax= plt.subplots()
    ax.barh(top['Company'], top['Market Cap (USD)'])
    ax.set_xlabel('Market Cap (USD)')
    ax.set_ylabel('Company')
    ax.set_title('Top 5 Companies by Market Cap')
    return fig