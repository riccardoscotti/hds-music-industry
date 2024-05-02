Indice 

* Introduzione 
    x modello di business di spotify 
    x definizioni di termini tecnici (MAUs, Ad MAUs ecc.)
    x domande di ricerca 

* Dataset 
    x dati finanziari spotify
    x download apk
    x manipolazioni sui dataframe (non sui dati)
    x aggregazione in quarter dati apk
    x visualizzazione di alcuni dati (grezzi)

* Metodo proposto
    x calcolo changepoint
        x PELT con rbf 
    x pearson e spearman 
    x granger causality
    x calcolo MAUs marginali (∆)

<!-- * Risultati sperimentali
    x calcolo changepoint
        x PELT con rbf
    x pearson, spearman e kendall tau corrrelation
    - granger causality -->

* Risultati sperimentali 
    1) Fonti di guadagno di Spotify
        x correlazioni sui gross profit (tra gross profit e MAUs) 
        x granger su dove si trovano correlazioni forti
        x changepoint per vedere se corrispondono 
    2) Quanto l'apk influenza gli utenti di Spotify
        x correlazione tra download apk e utenti (totali, premium e ad)
        x correlazione tra download apk e gross profit (totale, premium e ad)
        x correlazione tra download apk e MAUs marginali (solo su premium)
        x granger causality tra download apk e premium MAUs/gross profit

* Osservazioni e conclusioni
    1) Fonti di guadagno di spotify
        - changepoint a fine 2020 a causa lockdown 
        - valore delle azioni in crescita 
        - i premium influenzano i guadagni maggiormente, ma anche gli ad sono utili
    
    2) 
* Bibliografia


=============================================
PELT (Pruned Exact Linear Time) is an algorithm used for changepoint detection, particularly in time series analysis. It belongs to the family of dynamic programming algorithms and is designed to find the optimal changepoint partitioning of a time series while minimizing a given cost function.

Here's how PELT works:

Segmentation: PELT starts by dividing the time series into smaller segments, each containing a single data point. These segments represent potential changepoints.
Cost Calculation: For each segment, PELT calculates the cost of fitting a model to the data within that segment. This cost is typically based on some measure of goodness-of-fit or error between the model and the data.
Dynamic Programming: PELT then uses dynamic programming to efficiently find the optimal changepoint partitioning by recursively evaluating the costs of merging adjacent segments or keeping them separate.
Pruning: As PELT iterates through the segments, it prunes the search space by discarding suboptimal partitionings. This pruning step helps improve the algorithm's efficiency.
Optimization: PELT continues this process until it finds the optimal partitioning of the time series into changepoints, minimizing the total cost.
The penalty coefficient in PELT refers to a parameter used to balance the trade-off between the goodness-of-fit within segments and the number of segments (changepoints). Essentially, it penalizes the algorithm for creating additional changepoints. A higher penalty coefficient leads to fewer changepoints, while a lower penalty coefficient allows for more changepoints.

The choice of penalty coefficient depends on the specific characteristics of the data and the desired sensitivity to changepoints. A higher penalty coefficient is suitable for detecting significant changes in the data, while a lower penalty coefficient may be preferred for detecting subtle changes. It's often determined empirically or through cross-validation based on the application requirements. Adjusting the penalty coefficient allows users to control the level of granularity in the changepoint detection process.