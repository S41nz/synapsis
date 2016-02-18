'''
Created on 22/01/2016

@author: S41nz
'''
from db.enums.db_interface_type import DBInterfaceType
from db.graph.neo4j_db_interface import Neo4jDBInterface

class DBInterfaceFactory(object):
    '''
    Factory class that is in charge of creating the different types of instances for DBInterface implementation.
    '''
    
    #Methods
    @staticmethod
    def createDBInterface(interfaceType):
        '''
        Factory method to create the instance of any specific DBInterface implementation.
        '''
        if interfaceType == DBInterfaceType.NEO_4J_DATABASE:
            return Neo4jDBInterface()
        