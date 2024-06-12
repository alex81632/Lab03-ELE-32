import OwnCodifier
import CanalBSC
import OwnDecodifier

if __name__ == "__main__":
    u = [1, 0, 1, 1, 0]
    oc = OwnCodifier.OwnCodifier()
    cBSC = CanalBSC.CanalBSC(0.1)
    od = OwnDecodifier.OwnDecodifier()
    v = oc.codify(u.copy())
    print(v)
    r = cBSC.canal(v.copy())
    print(r)
    s = od.decodify(r.copy())
    print(s)
