'''
Created on 27/01/2016

@author: S41nz
'''

from db.db_interface import DBInterface
from db.enums.db_interface_type import DBInterfaceType
from py2neo import Graph
from py2neo.core import authenticate

class Neo4jDBInterface(DBInterface):
    '''
    This is the DBInterface implementation to connect and interact with Neo4j GraphDatabases
    '''
    
    #Constant for non-secure http protocol prefix
    NON_SECURE_PROTOCOL = "http://"
    #Constant for default non-secure connection
    DEFAULT_NON_SECURE_URL =  "localhost:7474/db/data"
    #Constant for secure http protocol prefix
    SECURE_PROTOCOL = "https://"
    #Constant for default secure connection
    DEFAULT_SECURE_URL =  "localhost:7473/db/data"
    

    def __init__(self):
        '''
        Constructor
        '''
        #Initialize the default attributes
        self.dbInterfaceType = DBInterfaceType.NEO_4J_DATABASE
        self.isDBConnected = False
        

    def connect(self, user=None, password=None, url=None):
        
        connectionResult = False
        
        httpProtocol = Neo4jDBInterface.NON_SECURE_PROTOCOL
        targetUrl = Neo4jDBInterface.DEFAULT_NON_SECURE_URL
        
        #Check for the URL first
        if url is not None:
            targetUrl = url
        
        credentialsData = ""
        #Check for the credentials then
        if user is not None and len(user) > 0 and password is not None and len(password) > 0:
            #
            credentialsData = user+":"+password+"@"
            httpProtocol = Neo4jDBInterface.SECURE_PROTOCOL
            if url is None:
                #Change the default port for secure connections
                targetUrl = Neo4jDBInterface.DEFAULT_SECURE_URL
                
            #Perform the authentication first
            authenticate(targetUrl,user,password)
            
        
        #Construct the final URL for connection
        connectionString = httpProtocol+credentialsData+targetUrl
        
        self.targetGraph = Graph(connectionString)
        
        #Update the connection state of the instance
        self.isDBConnected = True
        connectionResult = True
      
        return connectionResult    
        

    def closeConnection(self):
        #Nothing to do here for the moment
        return
        


    def executeQuery(self,query):
        
        queryResult = None
        if self.targetGraph is not None and query is not None and len(query) > 0:
            queryResult = self.targetGraph.cypher.execute(query)
            
        return queryResult
        

        