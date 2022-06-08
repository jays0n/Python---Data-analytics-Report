###############################################################################################################################################################
#
# Módulo : ENG Classe DataFrame             Data de Criação: 02/06/2022
#
# Objetivo: Módulo para aquisição de dados de fontes externas: Planilhas, Base de Dados SQL, Txt, entre outros.
#
# Ultimas alterações: Criação
#
# Data da ultima alteração: 01/06/2022
#
# Desenvolvedor: Francisco J. E. de Sousa
#
# Contato: e-mail: francisco.sousa1993@outlook.com      tel: (21) 96965-6759
#
###############################################################################################################################################################

# Imports:

import pandas as pd
from numpy import vstack
from EngConstants import *


# Class #1:

class DataBaseSource(object):
    def __init__(self,pDbType=ENG_DBTYPE_CSV):
        self.dbType=pDbType
        self.dbDataFrame=None

    def SetType(self,pType=ENG_DBTYPE_CSV):
        self.dbType=pType

    def ReadDataFromSource(self,path,headers=None, separator=';',sheet_name=0, sqlCmd='',sqlConnection=None,sqlTable_Name='',xPath=''):
        if self.dbType==ENG_DBTYPE_CSV or self.dbType==ENG_DBTYPE_TXT:
            self.dbDataFrame=pd.read_csv(path,separator,headers)

        elif self.dbType==ENG_DBTYPE_XLS:
            self.dbDataFrame=pd.read_excel(path,sheet_name,headers)

        elif self.dbType==ENG_DBTYPE_SQL:
            if not sqlCmd=='' and not sqlConnection==None:
                self.dbDataFrame=pd.read_sql_query(sqlCmd,sqlConnection)

            elif sqlConnection!=None and sqlTable_Name!='':
                self.dbDataFrame=pd.read_sql_table(sqlTable_Name,sqlConnection)

        elif self.dbType==ENG_DBTYPE_JSON:
            self.dbDataFrame=pd.read_json(path)

        elif self.dbType==ENG_DBTYPE_XML:
            self.dbDataFrame=pd.read_xml(path,xPath)

    def GetDataAsArray(self):
        return self.dbDataFrame.to_numpy()

    def GetColumn(self, column_number,isVertical=True):     
        idexColumns=self.dbDataFrame.columns
        if isVertical:
            return vstack(self.dbDataFrame[idexColumns[column_number]].to_numpy())
        else:
            return self.dbDataFrame[idexColumns[column_number]].to_numpy()

    def GetRow(self,row_number):
        return self.dbDataFrame.iloc[[row_number]].to_numpy()

    def GetColumns(self,columns_number):
        idexColumns=self.dbDataFrame.columns
        return self.dbDataFrame[idexColumns[columns_number]].to_numpy()

    def GetRow(self,rows_number):
        return self.dbDataFrame.iloc[rows_number].to_numpy()




