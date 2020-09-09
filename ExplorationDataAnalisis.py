# 7)*Pending* Translate columns to English 

# 1) Null/NaN inputs will be droped
lavf_all = lavf_all.drop(lavf_all.loc[lavf_all['violencia_tipo'].isnull()].index)
lavf_all = lavf_all.drop(lavf_all.loc[lavf_all['agresor_cantidad'].isnull()].index)
lavf_all = lavf_all.drop(lavf_all.loc[lavf_all['victima_rango_etario'].isnull()].index)

# 2) Columns "llamado_provincia" and "llamado_provincia_indec_id" are the same zone (Buenos Aires City)."Case_id" will be dropped as it doesn't apport any relevant information to this project. 
lavf_all_new = lavf_all.drop(['llamado_provincia_indec_id','llamado_provincia', 'caso_id'], axis=1)

# 6) New Features  'llamado_fecha_hora', estas nuevas features van a ser el "año","mes","dia", "hora completa","hora" y "momento del dia"
lavf_all_new['llamado_fecha_hora'] = pd.to_datetime(lavf_all_new['llamado_fecha_hora'])
lavf_all_new['año'] = lavf_all_new['llamado_fecha_hora'].dt.year
lavf_all_new['mes'] = lavf_all_new['llamado_fecha_hora'].dt.month
lavf_all_new['nro_día'] = lavf_all_new['llamado_fecha_hora'].dt.dayofweek
lavf_all_new.loc[(lavf_all_new['nro_día'] == 0), 'día'] = 'Lunes'
lavf_all_new.loc[(lavf_all_new['nro_día'] == 1), 'día'] = 'Martes'
lavf_all_new.loc[(lavf_all_new['nro_día'] == 2), 'día'] = 'Miercoles'
lavf_all_new.loc[(lavf_all_new['nro_día'] == 3), 'día'] = 'Jueves'
lavf_all_new.loc[(lavf_all_new['nro_día'] == 4), 'día'] = 'Viernes'
lavf_all_new.loc[(lavf_all_new['nro_día'] == 5), 'día'] = 'Sabado'
lavf_all_new.loc[(lavf_all_new['nro_día'] == 6), 'día'] = 'Domingo'
lavf_all_new = lavf_all_new.drop(['nro_día'], axis=1)
lavf_all_new['hora'] = lavf_all_new['llamado_fecha_hora'].dt.time
lavf_all_new['hora_sola'] = lavf_all_new['llamado_fecha_hora'].dt.hour

lavf_all_new.loc[(lavf_all_new['hora_sola'] >= 0) & (lavf_all_new['hora_sola'] < 6), 'momento_del_dia'] = 'Trasnoche'
lavf_all_new.loc[(lavf_all_new['hora_sola'] >= 6) & (lavf_all_new['hora_sola'] < 12), 'momento_del_dia']   = 'Mañana'
lavf_all_new.loc[(lavf_all_new['hora_sola'] >= 12) & (lavf_all_new['hora_sola'] < 18), 'momento_del_dia']   = 'Tarde'
lavf_all_new.loc[(lavf_all_new['hora_sola'] >= 18) & (lavf_all_new['hora_sola'] < 24), 'momento_del_dia']   = 'Noche'



# 5) Finally, raws with "No data" and "NN/NA" will be removed. (4958, 19)
lavf_preparacion1 = lavf_all_new.drop(lavf_all_new[(lavf_all_new['victima_edad'] == 'Sin Datos') 
                                                   | (lavf_all_new['victima_edad'] == '999') 
                                                   | (lavf_all_new['victima_rango_etario'] == 'Sin datos') 
                                                   | (lavf_all_new['victima_rango_etario'] == 'Sin Datos')
                                                   | (lavf_all_new['llamante_genero'] == 'NS/NC')
                                                   | (lavf_all_new['violencia_tipo'] == 'Sin datos')
                                                   | (lavf_all_new['violencia_tipo'] == 'No es un caso de Violencia Familiar')
                                                   | (lavf_all_new['violencia_tipo'] == 'No es un caso de Vio')
                                                   | (lavf_all_new['llamado_derivacion'] == 'No se trata de un caso de violencia familiar')
                                                  ].index, inplace = False)

lavf_preparacion2 = lavf_preparacion1.drop(lavf_preparacion1[(lavf_preparacion1['llamante_descripcion'] == 'Ns/Nc') 
                                                   | (lavf_preparacion1['llamante_vinculo_ninios_presentes'] == 'Sin datos') 
                                                   | (lavf_preparacion1['llamante_vinculo_ninios_presentes'] == 'NS/NC') 
                                                   | (lavf_preparacion1['victima_genero'] == 'NS/NC')
                                                   | (lavf_preparacion1['agresor_genero'] == 'NS/NC')
                                                   | (lavf_preparacion1['agresor_relacion_victima'] == 'Ns/Nc')   
                                                  ].index, inplace = False)

convert_dict = {'victima_cantidad': int, 'victima_edad': int}
lavf_preparacion3 = lavf_preparacion2.astype(convert_dict)

print("Nos quedamos con un dataset final equivalente al 19% del original importado, es decir, nos quedamos con 1/5 de los samples")

# 3) Several Upper/Lower case and spelling mistakes will be amend.