"""
The :mod:`ndlib.models.opinions` module contains common opinion dynamics network models from research literature.
"""

__author__ = 'rossetti'
__license__ = "GPL"
__email__ = "giulio.rossetti@gmail.com"

from .SimilarityDrivenBCM import SimilarityDrivenBCM
from .EmpiricalBoundedConfidenceModel import EmpiricalBoundedConfidenceModel
from .AdaptivePeerPressureAlgorithmicBiasModel import AdaptivePeerPressureAlgorithmicBiasModel
from .AdaptiveAlgorithmicBiasModel import AdaptiveAlgorithmicBiasModel
from .AlgorithmicBiasMediaModel import AlgorithmicBiasMediaModel
from .AlgorithmicBiasModel import AlgorithmicBiasModel
from .CognitiveOpDynModel import CognitiveOpDynModel
from .MajorityRuleModel import MajorityRuleModel
from .QVoterModel import QVoterModel
from .SznajdModel import SznajdModel
from .VoterModel import VoterModel
from .WHKModel import WHKModel
from .ARWHKModel import ARWHKModel
from .HKModel import HKModel


__all__ = [
    'SimilarityDrivenBCM'
    'EmpiricalBoundedConfidenceModel'
    'AdaptivePeerPressureAlgorithmicBiasModel'
    'AdaptiveAlgorithmicBiasModel'
    'AlgorithmicBiasMediaModel'
    'AlgorithmicBiasModel',
    'CognitiveOpDynModel',
    'MajorityRuleModel',
    'QVoterModel',
    'SznajdModel',
    'VoterModel',
    'WHKModel',
    'ARWHKModel',
    'HKModel'
]
