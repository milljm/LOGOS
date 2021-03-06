# Copyright 2020, Battelle Energy Alliance, LLC
# ALL RIGHTS RESERVED
"""
Created on February 2, 2021

@author: mandd
"""

#External Modules---------------------------------------------------------------
import numpy as np
import math
import copy
#External Modules End-----------------------------------------------------------

#Internal Modules---------------------------------------------------------------
from PluginsBaseClasses.ExternalModelPluginBase import ExternalModelPluginBase
#Internal Modules End-----------------------------------------------------------


class BaseKnapsackModel(ExternalModelPluginBase):
  """
    This class is designed to create the BaseKnapsack model
  """
  def __init__(self):
    """
      Constructor
      @ In, None
      @ Out, None
    """
    ExternalModelPluginBase.__init__(self)
    
    self.capacity      = None    # capacity value of the knapsack
    self.penaltyFactor = 1.0     # penalty factor that is used when the capacity constraint is not satisfied
    self.outcome       = None    # ID of the variable which indicates if the chosen elements satisfy the capacity constraint
    self.choiceValue   = None    # ID of the variable which indicates the sum of the values of the chosen project elements
    
  def _readMoreXML(self, container, xmlNode):
    """
      Method to read the portion of the XML that belongs to the BaseKnapsack model
      @ In, container, object, self-like object where all the variables can be stored
      @ In, xmlNode, xml.etree.ElementTree.Element, XML node that needs to be read
      @ Out, None
    """
    container.mapping    = {}
    
    for child in xmlNode:
      if child.tag == 'capacity':
        self.capacity = float(child.text.strip())
      elif child.tag == 'penaltyFactor':
        self.penaltyFactor = float(child.text.strip())
      elif child.tag == 'outcome':
        self.outcome = child.text.strip()
      elif child.tag == 'choiceValue':
        self.choiceValue = child.text.strip()
      elif child.tag == 'map':
        container.mapping[child.text.strip()] = [child.get('value'),child.get('cost')]
      elif child.tag == 'variables':
        variables = [str(var.strip()) for var in child.text.split(",")]
      else:
        raise IOError("BaseKnapsackModel: xml node " + str (child.tag) + " is not allowed")
      
      
  def initialize(self, container, runInfoDict, inputFiles):
    """
      Method to initialize the BaseKnapsack model
      @ In, container, object, self-like object where all the variables can be stored
      @ In, runInfoDict, dict, dictionary containing all the RunInfo parameters (XML node <RunInfo>)
      @ In, inputFiles, list, list of input files (if any)
      @ Out, None
    """
    pass      
      
      
  def run(self, container, inputDict):
    """
      This method calculates the sum of the chosen element values and check if the capacity constraint
      is satisfied
      @ In, container, object, self-like object where all the variables can be stored
      @ In, inputDict, dict, dictionary of inputs from RAVEN
    """   
    totalValue = 0.0  
    
    for key in container.mapping:
      if key in inputDict.keys() and inputDict[key] in [0.0,1.0]:
        if inputDict[key] == 1.0:
          testValue = self.capacity - inputDict[container.mapping[key][1]]
          if testValue >= 0:
            self.capacity   = self.capacity   - inputDict[container.mapping[key][1]]
            totalValue = totalValue + inputDict[container.mapping[key][0]]
          else:
            self.capacity   = self.capacity   - inputDict[container.mapping[key][1]]
            totalValue = totalValue - inputDict[container.mapping[key][0]] * self.penaltyFactor
        elif inputDict[key] == 0.0:
          pass
        else:
          raise IOError("BaseKnapsackModel: variable " + str(key) + " does not have a 0/1 value.")
      else:
        raise IOError("BaseKnapsackModel: variable " + str(key) + " is not found in the set of input variables.")
      
    if self.capacity>=0:
      container.__dict__[self.outcome] =  0.
    else:
      container.__dict__[self.outcome] = 1.
      
    container.__dict__[self.choiceValue] = totalValue