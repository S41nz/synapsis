'''
Created on 08/03/2016

@author: S41nz
'''

from abc import ABCMeta,abstractmethod
from synapsis.db.db_interface import DBInterface

class DBGraphHelper:
    '''
    This interface defines the functionality for high level operations with graph-based databases
    '''
    
    #Define the tag for abstract class
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def initialize(self):
        '''
        Method primitive that defines any possible routine for helper initialization purposes
        '''
    
    def setDBInterface(self,newDBInterface):
        '''
        Mutator method that sets the reference to the corresponding DBInterface implementation for graph db operations.
        '''
        self.dbInterface = newDBInterface
    
    def getDBInterfaceType(self):
        '''
        Accessor method to get the type of the DB interface that is being used.
        '''
        if self.dbInterface is not None:
            return self.dbInterface.getDBInterfaceType()
        else:
            return None
    
    @abstractmethod
    def loadEntity(self,name,relationshipAttributes):
        '''
        Method primitive to load an entity with their corresponding peer relationships filtered by a set of attributes
        '''
    
    @abstractmethod
    def loadEntitiesByType(self,entityType):
        '''
        Method primitive that loads all the entities that satisfy a given type of node in the graph
        '''
    
    @abstractmethod
    def createEntity(self,name,entityType):
        '''
        Method primitive that creates a new entity of a given type
        '''
    
    @abstractmethod
    def createRelationship(self,entityA,entityB,attribute):
        '''
        Method primitive that defines the functionality to create a new relationship between two existing entities under a specific attribute
        '''
    
    @abstractmethod
    def getRelationshipAttributes(self,entityA,entityB):
        '''
        Method primitive that defines the functionality to get all the relationship attributes that relates two existing entities
        '''
    
    @abstractmethod
    def getCommonAttributes(self,entities):
        '''
        Method primitive that defines a functionality to get all the common relationship attributes that relates a set of provided existing entities
        '''
        