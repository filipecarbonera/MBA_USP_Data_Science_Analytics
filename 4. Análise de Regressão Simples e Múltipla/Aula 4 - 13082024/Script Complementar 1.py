# Modelo 1 aux1, somente com a preditora 'rh1'

modelo1_aux1 = sm.OLS.from_formula('salario ~ rh1',
                                   df_salarios).fit()

modelo1_aux1.summary()

#%%
# Procedimento Stepwise no 'modelo1'

from statstests.process import stepwise

modelo1_step = stepwise(modelo1, pvalue_limit=0.05)

#%%
# Modelo 1 aux2, somente com a preditora 'econometria1'

modelo1_aux2 = sm.OLS.from_formula('salario ~ econometria1',
                                   df_salarios).fit()

modelo1_aux2.summary() # igual output do procedimento Stepwise acima

#%%
# Modelo 1 aux3, rodando 'rh1' em função de 'econometria1'

modelo1_aux3 = sm.OLS.from_formula('rh1 ~ econometria1',
                                   df_salarios).fit()

modelo1_aux3.summary()

#%% Disgnóstico de Multicolinearidade

# Cálculo da Tolerance

tolerance1 = 1 - modelo1_aux3.rsquared
tolerance1

# Cálculo do VIF
VIF1 = 1/tolerance1
VIF1

#%%
# Modelo 2 aux1, rodando 'rh2' em função de 'econometria2'

modelo2_aux1 = sm.OLS.from_formula('rh2 ~ econometria2',
                                   df_salarios).fit()

modelo2_aux1.summary()


#%% Disgnóstico de Multicolinearidade

# Cálculo da Tolerance

tolerance2 = 1 - modelo2_aux1.rsquared
tolerance2

# Cálculo do VIF
VIF2 = 1/tolerance2
VIF2

#%% 
# Procedimento Stepwise no 'modelo2' (Boa notícia!)

from statstests.process import stepwise

modelo2_step = stepwise(modelo2, pvalue_limit=0.05)

#%%
# Modelo 2 aux1, somente com a preditora 'econometria2'

modelo2_aux2 = sm.OLS.from_formula('salario ~ econometria2',
                                   df_salarios).fit()

modelo2_aux2.summary()
