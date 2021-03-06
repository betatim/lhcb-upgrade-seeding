#-- GAUDI jobOptions generated on Wed Jul  1 18:07:17 2015
#-- Contains event types : 
#--   13104013 - 116 files - 100556 events - 408.08 GBytes


#--  Extra information about the data processing phases:


#--  Processing Pass Step-127830 

#--  StepId : 127830 
#--  StepName : Digi14U2 for Upgrade studies with spillover - 2015 Baseline NoRichSpillover 
#--  ApplicationName : Boole 
#--  ApplicationVersion : v29r6 
#--  OptionFiles : $APPCONFIGOPTS/Boole/Default.py;$APPCONFIGOPTS/Boole/Boole-Upgrade-Baseline-20150522.py;$APPCONFIGOPTS/Boole/EnableSpillover.py;$APPCONFIGOPTS/Boole/Upgrade-RichMaPMT-NoSpilloverDigi.py;$APPCONFIGOPTS/Boole/xdigi.py;$APPCONFIGOPTS/Persistency/Compression-ZLIB-1.py; 
#--  DDDB : fromPreviousStep 
#--  CONDDB : fromPreviousStep 
#--  ExtraPackages : AppConfig.v3r210 
#--  Visible : N 


#--  Processing Pass Step-127809 

#--  StepId : 127809 
#--  StepName : Sim08h for Upgrade with nu = 7.6 (L=2x10^33), with spillover - MD - 2015 Baseline Geometry - Pythia8 
#--  ApplicationName : Gauss 
#--  ApplicationVersion : v47r2 
#--  OptionFiles : $APPCONFIGOPTS/Gauss/Beam7000GeV-md100-nu7.6-HorExtAngle.py;$APPCONFIGOPTS/Gauss/EnableSpillover-25ns.py;$DECFILESROOT/options/@{eventType}.py;$LBPYTHIA8ROOT/options/Pythia8.py;$APPCONFIGOPTS/Gauss/G4PL_FTFP_BERT_EmNoCuts.py;$APPCONFIGOPTS/Gauss/Gauss-Upgrade-Baseline-20150522.py;$APPCONFIGOPTS/Persistency/Compression-ZLIB-1.py 
#--  DDDB : dddb-20150424 
#--  CONDDB : sim-20140204-vc-md100 
#--  ExtraPackages : AppConfig.v3r210;DecFiles.v27r45 
#--  Visible : Y 


#--  Processing Pass Step-127812 

#--  StepId : 127812 
#--  StepName : Reco15U1 for Upgrade studies - 2015 Baseline Geometry 
#--  ApplicationName : Brunel 
#--  ApplicationVersion : v47r6p1 
#--  OptionFiles : $APPCONFIGOPTS/Brunel/MC-WithTruth.py;$APPCONFIGOPTS/Brunel/Brunel-Upgrade-Baseline-20150522.py;$APPCONFIGOPTS/Brunel/Upgrade-RichPmt.py;$APPCONFIGOPTS/Brunel/patchUpgrade1.py;$APPCONFIGOPTS/Brunel/xdst.py;$APPCONFIGOPTS/Persistency/Compression-ZLIB-1.py 
#--  DDDB : fromPreviousStep 
#--  CONDDB : fromPreviousStep 
#--  ExtraPackages : AppConfig.v3r210 
#--  Visible : Y 

from Gaudi.Configuration import * 
from GaudiConf import IOHelper
IOHelper('ROOT').inputFiles(['LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000001_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000002_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000003_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000004_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000005_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000006_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000007_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000008_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000009_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000010_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000011_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000012_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000013_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000014_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000015_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000016_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000017_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000018_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000019_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000020_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000021_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000022_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000023_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000024_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000025_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000026_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000027_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000028_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000029_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000030_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000031_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000032_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000033_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000034_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000035_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000036_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000037_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000038_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000039_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000040_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000041_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000042_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000043_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000044_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000045_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000046_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000047_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000048_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000049_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000050_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000051_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000052_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000053_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000054_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000055_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000056_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000057_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000058_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000059_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000060_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000061_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000062_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000063_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000064_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000065_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000066_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000067_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000068_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000069_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000070_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000071_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000072_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000073_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000074_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000075_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000076_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000077_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000078_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000079_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000080_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000081_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000082_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000083_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000084_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000085_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000086_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000087_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000088_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000089_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000090_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000091_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000092_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000093_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000094_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000095_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000096_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000097_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000098_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000099_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000100_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000101_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000102_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000103_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000104_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000105_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000106_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000107_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000108_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000109_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000110_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000111_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000112_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000113_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000114_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000115_1.xdst',
'LFN:/lhcb/MC/Upgrade/XDST/00045401/0000/00045401_00000116_1.xdst'
], clear=True)
