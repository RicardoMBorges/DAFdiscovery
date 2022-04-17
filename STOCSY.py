def STOCSY(target,X,ppm):
    
    """
    Function designed to calculate covariance/correlation and plots its color coded projection of NMR spectrum
    Originally designed for NMR, but not limited to NMR
        
    target - driver peak to be used 
    X -      the data itself (samples as columns and chemical shifts as rows)
    ppm -    the axis 
    
    Created on Mon Feb 14 21:26:36 2022
    @author: R. M. Borges and Stefan Kuhn
    """
    
    import numpy as np
    from scipy import stats
    import matplotlib.pyplot as plt
    from matplotlib import collections as mc
    import pylab as pl
    import math
    import os
        
    if type(target) == float:
        idx = np.abs(ppm - target).idxmin() #axis='index') #find index for a given target
        target_vect = X.iloc[idx] #locs the values of the target(th) index from different 'samples'
    else:
        target_vect = target
    #print(target_vect)
    
    #compute Correlation and Covariance
    """Matlab - corr=(zscore(target_vect')*zscore(X))./(size(X,1)-1);"""
    corr = (stats.zscore(target_vect.T,ddof=1)@stats.zscore(X.T,ddof=1))/((X.T.shape[0])-1)
        
    """#Matlab - covar=(target_vect-mean(target_vect))'*(X-repmat(mean(X),size(X,1),1))./(size(X,1)-1);"""
    covar = (target_vect-(target_vect.mean()))@(X.T-(np.tile(X.T.mean(),(X.T.shape[0],1))))/((X.T.shape[0])-1)
        
    x = np.linspace(0, len(covar), len(covar))
    y = covar
    points = np.array([x, y]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    
    fig, axs = plt.subplots(1, 1, sharex=True, sharey=True, figsize=(16,4))
    norm = plt.Normalize(corr.min(), corr.max())
    lc = mc.LineCollection(segments, cmap='jet', norm=norm)
    lc.set_array(corr)
    lc.set_linewidth(2)
    line = axs.add_collection(lc)
    fig.colorbar(line, ax=axs)
    axs.set_xlim(x.min(), x.max())
    axs.set_ylim(y.min(), y.max())
    axs.invert_xaxis()
        
    #This sets the ticks to ppm values
    minppm = min(ppm)
    maxppm = max(ppm)
    ticksx = []
    tickslabels = []
    if maxppm<30:
       ticks = np.linspace(int(math.ceil(minppm)), int(maxppm), int(maxppm)-math.ceil(minppm)+1)
    else:
       ticks = np.linspace(int(math.ceil(minppm / 10.0)) * 10, (int(math.ceil(maxppm / 10.0)) * 10)-10, int(math.ceil(maxppm / 10.0))-int(math.ceil(minppm / 10.0)))
    currenttick=0;
    for ppm in ppm:
       if currenttick<len(ticks) and ppm>ticks[currenttick]:
           position=int((ppm-minppm)/(maxppm-minppm)*max(x))
           if position<len(x):
               ticksx.append(x[position])
               tickslabels.append(ticks[currenttick])
           currenttick=currenttick+1
    plt.xticks(ticksx,tickslabels, fontsize=12)
    axs.set_xlabel('ppm', fontsize=14)
    axs.set_ylabel(f"Covariance with \n signal at {target:.2f} ppm", fontsize=14)
    axs.set_title(f'STOCSY from signal at {target:.2f} ppm', fontsize=16)

    text = axs.text(1, 1, '')
    lnx = plt.plot([60,60], [0,1.5], color='black', linewidth=0.3)
    lny = plt.plot([0,100], [1.5,1.5], color='black', linewidth=0.3)
    lnx[0].set_linestyle('None')
    lny[0].set_linestyle('None')

    def hover(event):
        if event.inaxes == axs:
            inv = axs.transData.inverted()
            maxcoord=axs.transData.transform((x[0], 0))[0]
            mincoord=axs.transData.transform((x[len(x)-1], 0))[0]
            ppm=((maxcoord-mincoord)-(event.x-mincoord))/(maxcoord-mincoord)*(maxppm-minppm)+minppm
            cov=covar[int(((maxcoord-mincoord)-(event.x-mincoord))/(maxcoord-mincoord)*len(covar))]
            cor=corr[int(((maxcoord-mincoord)-(event.x-mincoord))/(maxcoord-mincoord)*len(corr))]
            text.set_visible(True)
            text.set_position((event.xdata, event.ydata))
            text.set_text('{:.2f}'.format(ppm)+" ppm, covariance: "+'{:.6f}'.format(cov)+", correlation: "+'{:.2f}'.format(cor))
            lnx[0].set_data([event.xdata, event.xdata], [-1, 1])
            lnx[0].set_linestyle('--')
            lny[0].set_data([x[0],x[len(x)-1]], [cov,cov])
            lny[0].set_linestyle('--')
        else:
            text.set_visible(False)
            lnx[0].set_linestyle('None')
            lny[0].set_linestyle('None')
        fig.canvas.draw_idle()

    fig.canvas.mpl_connect("motion_notify_event", hover)    
    pl.show()
    if not os.path.exists('images'):
        os.mkdir('images')
    plt.savefig(f"images/stocsy_from_{target}.pdf", transparent=True, dpi=300)
    
    return corr, covar
