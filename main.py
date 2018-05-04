import BPM
from BPM import BPMdata, triggerAquisition


triggerAquisition()
bpm1 = BPMdata(1)
bpm2 = BPMdata(2)

print(bpm1.sumSigAmpSpectrum())
