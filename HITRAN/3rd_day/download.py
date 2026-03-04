from hapi import *

db_begin('data')

######Downloading and describing data ######

#getHelp(fetch)

#fetch('H2O', 1, 1, 3400, 4100)
#-----------------------------------------------------------------------------------
####fetch(TableName, M, I, numin, numax, ParameterGroups=[], Parameters=[])
#    INPUT PARAMETERS:
#        TableName:   local table name to fetch in (required)
#        M:           HITRAN molecule number       (required)
#        I:           HITRAN isotopologue number   (required)
#        numin:       lower wavenumber bound       (required)
#        numax:       upper wavenumber bound       (required)
#-------------------------------------------------------------------------------------


#tableList()
#describeTable('H2O')


#getHelp(fetch_by_ids)

#--------------------------------------------------------------------------------------------
#fetch_by_ids(TableName, iso_id_list, numin, numax, ParameterGroups=[], Parameters=[])
#    INPUT PARAMETERS:
#        TableName:   local table name to fetch in (required)
#        iso_id_list: list of isotopologue id's    (required)
#        numin:       lower wavenumber bound       (required)
#        numax:       upper wavenumber bound       (required)
#    OUTPUT PARAMETERS:
#-------------------------------------------------------------------------------------------

#fetch_by_ids('O2',[36,37,38], 12000, 14000, ParameterGroups=['160-char','Galatry'])

#tableList()
#describeTable('O2')

#fetch_by_ids('O2',[36,37,38], 12000, 14000, ParameterGroups=['160-char'],Parameters=['deltap_air','beta_g_air','gamma_air', 'gamma_self', 'delta_self', 'deltap_self', 'n_self','beta_g_self'])

#tableList()
#describeTable('O2')
