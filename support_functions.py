import json
import numpy as np

# === Conversion ===
def energy_to_tot(x, a, b, c, t):
	return np.where(x >= get_thl(a, b, c, t), a*x + b + float(c)/(x - t), 0)

def tot_to_energy(x, a, b, c, t):
    return 1./(2*a) * ( t*a + x - b + np.sqrt((b + t*a - x)**2 - 4*a*c) )

def get_thl(a, b, c, t):
    return 1./(2*a) * ( t*a - b + np.sqrt((b + t*a)**2 - 4*a*c) )

def get_t(THL, a, b, c):
    return (2*a*b**2 - 4*a*b*THL + 2*a*THL**2 + np.pi*b*c - np.pi*c*THL)/(2*c)

# === Spectrum ===
def exp_decay(x, A, k, c):
    return A * np.exp(-k * x) + c

def smear_spectrum(data, sigma_params):
    data = np.asarray( data )
    sigma = np.abs(exp_decay(data, *sigma_params))
    data_smear = np.random.normal(data, scale=sigma)
    return data_smear

# === JSON ===
def load_json(fn):
    with open(fn, 'r') as f:
        d = json.load(f)
    return np.asarray(d['x']), np.asarray(d['y'])

def dump_json(fn, x, y):
    with open(fn, 'w') as f:
        json.dump({'x': x.tolist(), 'y': y.tolist()}, f)

# === ETC ===
def get_color(c, N, idx):
    import matplotlib as mpl
    cmap = mpl.cm.get_cmap(c)
    norm = mpl.colors.Normalize(vmin=0.0, vmax=N - 1)
    return cmap(norm(idx))
