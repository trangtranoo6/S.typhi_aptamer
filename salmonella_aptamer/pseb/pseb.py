import numpy as np
from tqdm import tqdm
from propy.PseudoAAC import GetPseudoAAC, _Hydrophobicity, _hydrophilicity, _residuemass, _pK1, _pK2, _pI

properties = [_Hydrophobicity, _hydrophilicity, _residuemass, _pK1, _pK2, _pI]
LAMBDA = 10

def _getVector(sample, lamda = LAMBDA):
    res = GetPseudoAAC(sample,lamda = lamda,weight = 0.7,AAP = properties)
    return np.array([i for i in res.values()])

def getVectors(samples, lamda = LAMBDA):
    vectors = []
    for i in tqdm(samples):
        vectors.append(_getVector(i, lamda))
    return np.array(vectors)

def validatePeptide(peptides, lamda = LAMBDA):
    res = []
    for peptide in peptides:
        if any(x in peptide for x in ['U','X','>']):
            continue
        if len(peptide) <= lamda:
            continue
        res.append(peptide)
    return res
