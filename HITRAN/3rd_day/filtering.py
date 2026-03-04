from hapi import *

db_begin('data')

###### 3.3. Filtering and outputting_data ######

#### getHelp(select)
###   -> Specifying a list of parameters
#---------------------------------------------------------------------------------------------------------------------
#select(TableName, DestinationTableName='__BUFFER__', ParameterNames=None, Conditions=None, Output=True, File=None)
#    INPUT PARAMETERS:
#        TableName:            name of source table              (required)
#        DestinationTableName: name of resulting table           (optional)
#        ParameterNames:       list of parameters or expressions (optional)
#        Conditions:           list of logincal expressions      (optional)
#        Output:   enable (True) or suppress (False) text output (optional)
#        File:     enable (True) or suppress (False) file output (optional)
#---------------------------------------------------------------------------------------------------------------------

#select('H2O')

#select('H2O', Conditions=('between','nu',4000,4100))

#select('H2O', ParameterNames=('nu','sw'), Conditions=('between','nu',4000,4100))

#describeTable('H2O')

Cond = ('And', ('BETWEEN', 'nu', 3500, 4000), ('>=', 'sw', 1e-19))
select('H2O', Conditions=Cond, DestinationTableName='tmp')