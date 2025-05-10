from cycler import cycler
import matplotlib.pyplot as plt


def setup_viz():
    cores = plt.get_cmap('Set2').colors
    ciclo_cores = cycler('color', cores)
    plt.rc('axes', prop_cycle=ciclo_cores)
    
    
    
    
def formatador_abreviado(x, pos):
        if x >= 1_000_000_000:
            return f'{x/1_000_000_000:.1f}B'
        elif x >= 1_000_000:
            return f'{x/1_000_000:.1f}M'
        elif x >= 1_000:
            return f'{x/1_000:.0f}k'
        else:
            return f'{x:.0f}'