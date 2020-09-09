#lavf = llamados atendidos violencia familiar = Family violence attended calls

#Loading data from 2017
lavf17 = pd.read_csv('llamados-atendidos-violencia-familiar-2017.csv')
#Standarizing the column names acording next years columns
lavf17.rename(columns = {'llamante_quien_llama':'llamante_descripcion'}, inplace = True)

#Loading data from 2018
lavf1801 = pd.read_csv('llamados-atendidos-violencia-familiar-201801.csv')
lavf1802 = pd.read_csv('llamados-atendidos-violencia-familiar-201802.csv')
lavf1803 = pd.read_csv('llamados-atendidos-violencia-familiar-201803.csv')
lavf1804 = pd.read_csv('llamados-atendidos-violencia-familiar-201804.csv')
lavf1805 = pd.read_csv('llamados-atendidos-violencia-familiar-201805.csv')
lavf1806 = pd.read_csv('llamados-atendidos-violencia-familiar-201806.csv')
lavf1807 = pd.read_csv('llamados-atendidos-violencia-familiar-201807.csv')
lavf1808 = pd.read_csv('llamados-atendidos-violencia-familiar-201808.csv')
lavf1809 = pd.read_csv('llamados-atendidos-violencia-familiar-201809.csv')
lavf1810 = pd.read_csv('llamados-atendidos-violencia-familiar-201810.csv')
lavf1811 = pd.read_csv('llamados-atendidos-violencia-familiar-201811.csv')
lavf1812 = pd.read_csv('llamados-atendidos-violencia-familiar-201812.csv')

#Loading data from 2019
lavf1901 = pd.read_csv('llamados-atendidos-violencia-familiar-2019-trimestre-1.csv')
lavf1902 = pd.read_csv('llamados-atendidos-violencia-familiar-2019-trimestre-2.csv')
lavf1903 = pd.read_csv('llamados-atendidos-violencia-familiar-2019-trimestre-3.csv')

#Concatenate 2018 data sets

lavf18 = pd.concat([lavf1801,lavf1802,lavf1803,lavf1804,lavf1805,lavf1806,lavf1807,lavf1808,lavf1809,lavf1810,lavf1811], axis = 0,  join = "outer" , ignore_index = False)

#December failed because columns names unmatched. After checking its de same data with different column name, Its standarized.
  ##### ==> rename(columns = {'llamante_quien_llama':'llamante_descripcion'})
lavf18.columns = ['caso_id', 'llamante_descripcion', 'llamante_genero',
        'llamante_vinculo_ninios_presentes', 'violencia_tipo', 'victima_edad',
       'victima_rango_etario', 'victima_genero', 'victima_cantidad',
      'agresor_cantidad', 'agresor_genero', 'agresor_relacion_victima',
     'llamado_derivacion', 'llamado_fecha_hora', 'llamado_provincia',
    'llamado_provincia_indec_id']

#Concatenate December
lavf18 = pd.concat([lavf18,lavf1812], axis = 0,  join = "outer" , ignore_index = False)

#Same for 2019
lavf19 = pd.concat([lavf1902,lavf1903], axis = 0,  join = "outer" , ignore_index = False)
lavf19.columns = ['caso_id', 'llamante_descripcion', 'llamante_genero','llamante_vinculo_ninios_presentes', 'violencia_tipo','victima_edad',  'victima_rango_etario','victima_genero','victima_cantidad','agresor_cantidad','agresor_genero','agresor_relacion_victima',
     'llamado_derivacion','llamado_fecha_hora','llamado_provincia','llamado_provincia_indec_id']
lavf19 = pd.concat([lavf1901,lavf19], axis = 0,  join = "outer" , ignore_index = False)

#Join all in 1 df
lavf_all = pd.concat([lavf17,lavf18,lavf19], axis = 0,  join = "outer" , ignore_index = False)

######
#lavf_all.shape = (23420, 16)


print('The data sets has been standarized and joined into "lavf_all". Now is ready to start ExplorationDataAnalisis ')
