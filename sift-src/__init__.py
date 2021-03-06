"""
Module Sift for calculating SIFT keypoint using PyOpenCL
"""
version = "0.1.0"
import os
sift_home = os.path.dirname(os.path.abspath(__file__))
import sys, logging
logging.basicConfig()
from .plan import SiftPlan
from .match import MatchPlan

