# NadarayaWatsonKernelRegression
The Nadraya-Watson kernel estimator is a nonparametric regression method. This repository demonstrates this nonparametric regression method in univarate form.

The nonparametric estimation plays an important role in engineering, econometric, bioinformatics, etc. While parametric estimators assumed the unknown function characteristics can be represented by one or a certain number of parameters; on the other hand, the nonparametric estimation does not assume the unknown function characteristics to be represented by any parameters. Therefore it plays a crucial role in nonlinear models. 

One of the major nonparametric estimation technique is the so-called Nadraya-Watson kernel estimators [1]. Although this regression technique does not represent the unknown model by any parameters, in the formation of the Nadraya-Watson kernel estimators, there is a smoothing parameter that need to be specified. This pre-specified smoothing parameter controls how much local observations are allowed in order to formulate the estimation, and needs to be carefully specified. A too-small smoothing parameter will lead the final estimation to be overfitting, while a too-large smoothing parameter will lead the final estimation to be underfitting. In this repository, we do not only formulate the Nadraya-Watson kernel estimator, but also demonstrate using the cross-calidation approach in selecting the proper smoothing parameter. 

We use the input-output signal from a Hammerstein model to demonstrate the algorithm. The identification of the nonlinear characteristics within a Hammerstein model can be found in [1]. As a comparison, we show the two arbitarily selected smoothig parameter senarios that correspond to overfitting and underfitting, and we finally demonstrate the properly selected kernel bandwidth through the cross-validation approach.

[1] Włodzimierz Greblicki, Mirosław Pawlak, "Nonparametric system identification", Cambridge Press, 2006.
