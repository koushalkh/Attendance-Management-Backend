import cognitive_face as CF
from .global_variables import personGroupId, Key

def train():
    CF.Key.set(Key)
    res = CF.person_group.train(personGroupId)
    print(res)
    print("Training complete")
