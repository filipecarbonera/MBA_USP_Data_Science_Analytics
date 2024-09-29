df_saeb_rend['codigo'] = df_saeb_rend['codigo'].astype('str')

#%%
# Teste de Breusch-Pagan (Cálculo Manual) - REZA!

df_saeb_rend['up'] = ((df_saeb_rend['residuos'])**2)/\
    (((df_saeb_rend['residuos'])**2).sum()/25530)
    
modelo_aux = sm.OLS.from_formula('up ~ fitted',
                                 df_saeb_rend).fit()

modelo_aux.summary()

from statsmodels.stats.anova import anova_lm
anova_table = anova_lm(modelo_aux, typ=2)
anova_table

SQReg = anova_table.sum_sq.iloc[0]/2
SQReg

p_value = stats.chi2.pdf(SQReg, 1)*2
p_value

#%%
# Teste de Breusch-Pagan com o modelo com dummies

teste_bp = breusch_pagan_test(modelo_saeb_dummies_uf) #criação do objeto 'teste_bp'
chisq, p = teste_bp #definição dos elementos contidos no objeto 'teste_bp'
alpha = 0.05 #nível de significância
if p > alpha:
    print('Não se rejeita H0 - Ausência de Heterocedasticidade')
else:
	print('Rejeita-se H0 - Existência de Heterocedasticidade')

#%%
# Dummização da variável 'uf' com n dummies

df_saeb_rend_dummies = pd.get_dummies(df_saeb_rend, columns=['uf'],
                                      dtype=int,
                                      drop_first=False)

df_saeb_rend_dummies

#%%
lista_colunas = list(df_saeb_rend_dummies.drop(columns=['municipio',
                                                        'codigo',
                                                        'escola',
                                                        'rede',
                                                        'saeb',
                                                        'fitted',
                                                        'residuos','up',
                                                        'uf_BA']).columns)
formula_dummies_modelo = ' + '.join(lista_colunas)
formula_dummies_modelo = "saeb ~ " + formula_dummies_modelo

#%%
# Estimação do novo modelo 'modelo_saeb_dummies_uf2'

modelo_saeb_dummies_uf2 = sm.OLS.from_formula(formula_dummies_modelo,
                                               df_saeb_rend_dummies).fit()

# Parâmetros do modelo 'modelo_saeb_dummies_uf2'
modelo_saeb_dummies_uf2.summary()

#%%
# Teste de Breusch-Pagan no novo modelo

teste_bp = breusch_pagan_test(modelo_saeb_dummies_uf2) #criação do objeto 'teste_bp'
chisq, p = teste_bp #definição dos elementos contidos no objeto 'teste_bp'
alpha = 0.05 #nível de significância
if p > alpha:
    print('Não se rejeita H0 - Ausência de Heterocedasticidade')
else:
	print('Rejeita-se H0 - Existência de Heterocedasticidade')