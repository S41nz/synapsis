'''
Created on 22/01/2016

@author: S41nz
'''
from abc import ABCMeta,abstractmethod
from db.enums.db_interface_type import DBInterfaceType

class DBInterface(metaclass=ABCMeta):
    '''
    This interface defines the basic functionality that an interface with any kind of database should have.
    '''
    

    def __init__(self):
        '''
        Constructor
        '''
        #Initialize the connection status flag.
        self.isDBConnected = False
        #Initialize the db interface type
        self.dbInterfaceType = DBInterfaceType.UNDEFINED
        
    @abstractmethod
    def connect(self,user,password,url=None):
        '''
        This method is to connect to a given database, with an optional url parameter for remote connections.
        '''
    @abstractmethod
    def closeConnection(self):
        '''
        This method is to close the existing connection if any.
        '''
    
    @abstractmethod
    def executeQuery(self):
        '''
        This defines the interface for executing any query on a given database. This will return the query result object
        '''
    def isConnectedToDB(self):
        '''
        Accesor method that communicates whether or not the connection to the database is up or down.
        '''
        return self.isDBConnected
    
    def getDBInterfaceType(self):
        '''
        Accessor method to obtain the current type of DB interface
        '''
        return self.dbInterfaceType