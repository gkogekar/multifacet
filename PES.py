import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import cantera as ct

plt.rcParams['figure.figsize'] = (18, 6)
plt.rcParams['axes.linewidth'] = 2
plt.rc('xtick', labelsize=16)
plt.rc('ytick', labelsize=16)
plt.rc('axes', labelsize=16)
plt.rc('legend', fontsize=16)
plt.rcParams['lines.markersize'] = 10
plt.rcParams['lines.linewidth'] = 3
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.rcParams['xtick.major.size'] = 10
plt.rcParams['xtick.major.width'] = 2
plt.rcParams['ytick.major.size'] = 10
plt.rcParams['ytick.major.width'] = 2
plt.rcParams['legend.edgecolor'] = 'k'
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams["legend.framealpha"] = 1
plt.rcParams['xtick.major.pad'] = 8
plt.rcParams['ytick.major.pad'] = 8
plt.rcParams['legend.handletextpad'] = 0.2
plt.rcParams['legend.columnspacing'] = 0.1
plt.rcParams['legend.labelspacing'] = 0.1
plt.rcParams['legend.title_fontsize'] = 14
plt.rcParams['axes.formatter.limits'] = (-3, 6)

colormap = plt.cm.Dark2
colors = [colormap(i) for i in np.linspace(0, 1, 4)]


gs = gridspec.GridSpec(nrows=1, ncols=2)
gs.update(wspace=0.25, hspace=0.4)

ax0 = plt.subplot(gs[0, 0])
ax1 = plt.subplot(gs[0, 1])

ax0.set_ylim([-100,200])
ax0.set_xlim([0,3])
ax0.get_xaxis().set_visible(False)
ax0.spines['right'].set_visible(False)
ax0.spines['top'].set_visible(False)
ax0.spines['bottom'].set_visible(False)
ax0.set_ylabel('$\mathrm{enthalpy\ (kJ\,mol^{-1})}$')

va_offset=4
Hf_H=-23.4
Hf_ref=-82.7
#############old approach#####################
#CH3CH2CH3
Hf_CH3CH2CH3=-82.7-Hf_ref
ax0.plot((0.5,1),(Hf_CH3CH2CH3,Hf_CH3CH2CH3),linestyle='solid',color='k')
ax0.text(0.75,Hf_CH3CH2CH3-va_offset,'$\mathrm{CH_3CH_2CH_{3(g)}}$',va='top',ha='center',size=12)

#CH3CH2CH3_ads
Hf_CH3CH2CH3_ads=-121.27-Hf_ref
ax0.plot((2,2.5),(Hf_CH3CH2CH3_ads,Hf_CH3CH2CH3_ads),linestyle='solid',color='k')
ax0.text(2.25,Hf_CH3CH2CH3_ads-va_offset,'$\mathrm{CH_3CH_2CH_3^*}$',va='top',ha='center',size=12)

#connecting lines
#ax0.plot((3,4),(Hf_CH3CH2CH3,Hf_CH3CH2CH3_ads),linestyle='dashed',color='k', linewidth=1)
#ax0.plot((7,8),(Hf_CH3CH2CH3_ads,Hf_CH2CH2CH3_ads),linestyle='dashed',color='k', linewidth=1)
#ax0.plot((11,12),(Hf_CH2CH2CH3_ads,Hf_CH2CHCH3_ads),linestyle='dashed',color='k', linewidth=1)
#ax0.plot((15,16),(Hf_CH2CHCH3_ads,Hf_CH2CHCH3),linestyle='dashed',color='k', linewidth=1)
