import numpy as np
import matplotlib.pyplot as plt

# 1.0
l1 = [18.549402, 14.267712, 12.387618, 11.116716, 10.136514, 9.571157, 9.09768, 8.691488, 8.441079, 8.198432, 8.01242, 7.897546, 7.8028245, 7.614753, 7.507476, 7.453701, 7.3405223, 7.447168, 7.250163, 7.256733, 7.1834307, 7.146586, 7.083405, 7.1295333, 7.16728, 7.026777, 7.058446, 6.9797378, 6.9391294, 6.999518, 6.92807, 6.8966784, 6.881043, 6.933018, 6.839692, 6.9120555, 6.8534446, 6.888605, 6.875004, 6.7522845, 6.75896, 6.817028, 6.809641, 6.8304663, 6.754351, 6.8358603, 6.765737, 6.790146, 6.807997, 6.7842517, 6.6766257, 6.7430005, 6.761759, 6.7715793, 6.7147703, 6.745879, 6.688818, 6.7148604, 6.7083416, 6.727006, 6.7337737, 6.683754, 6.735021, 6.679993, 6.765992, 6.6732984, 6.7050123, 6.737373, 6.6758094, 6.7631025, 6.648692, 6.6476173, 6.7093415, 6.683508, 6.681868, 6.6919136, 6.6480985, 6.7164564, 6.7100945, 6.6749973, 6.7481346, 6.6126027, 6.706434, 6.684577, 6.70283, 6.708121, 6.708267, 6.6526523, 6.6036067, 6.5733795, 6.576994, 6.632297, 6.682824, 6.6251364, 6.704896, 6.737325, 6.6184516, 6.628071, 6.6563306, 6.7227306, 6.6203985, 6.589006, 6.622777, 6.6329794, 6.600759, 6.6895742, 6.6607733, 6.6494284, 6.572845, 6.5837727, 6.676371, 6.6568885, 6.5960164, 6.697293, 6.5909376, 6.643124, 6.7027216, 6.622371, 6.7451572, 6.6304183, 6.563631, 6.6809316, 6.6349225, 6.6257544, 6.6698356, 6.6736383, 6.6914444, 6.6118035, 6.7940755, 6.7560678, 6.731879, 6.6058683, 6.652779, 6.7588058, 6.6307592, 6.6453023, 6.678011, 6.6730633, 6.6395545, 6.7094774, 6.7099657, 6.680325, 6.5433655, 6.563259, 6.6092954, 6.6323113, 6.6928787, 6.688227, 6.6361165, 6.640495, 6.6858883, 6.63101, 6.5583744, 6.6035094, 6.6063247, 6.6683555, 6.6457496, 6.578378, 6.648278, 6.597507, 6.7490697, 6.6130486, 6.735935, 6.6016316, 6.6297874, 6.635093, 6.5872803, 6.679843, 6.6106944, 6.652872, 6.5909166, 6.6571198, 6.583375, 6.667419, 6.635896, 6.692758, 6.583105, 6.6949077, 6.687576, 6.6291223, 6.659659, 6.709957, 6.7676196, 6.6648974, 6.679065, 6.6334524, 6.650449, 6.721487, 6.66724, 6.6561794, 6.7222924, 6.712871, 6.680649, 6.761318, 6.7624893, 6.5676036, 6.6293573, 6.59877, 6.6693125, 6.696628]
a1 = [0.349126213592233, 0.429126213592233, 0.46601941747572817, 0.5013592233009708, 0.5363106796116505, 0.5328155339805826, 0.5405825242718446, 0.5510679611650485, 0.5724271844660194, 0.5355339805825243, 0.5697087378640777, 0.5766990291262136, 0.5499029126213593, 0.5700970873786407, 0.566990291262136, 0.5875728155339806, 0.553009708737864, 0.5603883495145631, 0.5693203883495146, 0.5759223300970874, 0.5623300970873787, 0.5603883495145631, 0.5887378640776699, 0.5899029126213592, 0.5852427184466019, 0.5677669902912621, 0.5766990291262136, 0.5732038834951456, 0.585631067961165, 0.589126213592233, 0.5883495145631068, 0.5844660194174758, 0.5464077669902913, 0.5972815533980582, 0.6003883495145631, 0.581747572815534, 0.5976699029126213, 0.5786407766990291, 0.5805825242718446, 0.5755339805825243, 0.5976699029126213, 0.5988349514563107, 0.5906796116504854, 0.589126213592233, 0.5755339805825243, 0.5763106796116505, 0.5724271844660194, 0.5805825242718446, 0.6011650485436894, 0.6007766990291262, 0.5751456310679611, 0.5980582524271845, 0.6019417475728155, 0.5879611650485437, 0.6, 0.5910679611650486, 0.6077669902912621, 0.5557281553398058, 0.6019417475728155, 0.6100970873786408, 0.5922330097087378, 0.5549514563106797, 0.5716504854368932, 0.5728155339805825, 0.585631067961165, 0.6007766990291262, 0.5949514563106796, 0.5801941747572815, 0.5910679611650486, 0.5662135922330097, 0.5712621359223301, 0.5864077669902913, 0.5778640776699029, 0.5627184466019417, 0.6093203883495145, 0.589126213592233, 0.5848543689320388, 0.5992233009708738, 0.5933980582524272, 0.5852427184466019, 0.6, 0.5673786407766991, 0.581747572815534, 0.5980582524271845, 0.6085436893203884, 0.5778640776699029, 0.5879611650485437, 0.6011650485436894, 0.5922330097087378, 0.5844660194174758, 0.5941747572815534, 0.5953398058252427, 0.5937864077669903, 0.5739805825242719, 0.5918446601941748, 0.6042718446601941, 0.5930097087378641, 0.6089320388349515, 0.5968932038834951, 0.5984466019417476] + [0.6011650485436894, 0.581747572815534, 0.5922330097087378, 0.5840776699029127, 0.6135922330097088, 0.5844660194174758, 0.5770873786407767, 0.5829126213592233, 0.6132038834951457, 0.5479611650485436, 0.5895145631067961, 0.5840776699029127, 0.5712621359223301, 0.5922330097087378, 0.5852427184466019, 0.6015533980582525, 0.5732038834951456, 0.5805825242718446, 0.5836893203883495, 0.5945631067961165, 0.5875728155339806, 0.6015533980582525, 0.5922330097087378, 0.6058252427184466, 0.5763106796116505, 0.5883495145631068, 0.6046601941747572, 0.5786407766990291, 0.5996116504854369, 0.5992233009708738, 0.5937864077669903, 0.5770873786407767, 0.5580582524271844, 0.5716504854368932, 0.5949514563106796, 0.6003883495145631, 0.6019417475728155, 0.5930097087378641, 0.5848543689320388, 0.5984466019417476, 0.5864077669902913, 0.5875728155339806, 0.5774757281553398, 0.5867961165048544, 0.5988349514563107, 0.5988349514563107, 0.5704854368932039, 0.5899029126213592, 0.6050485436893204, 0.592621359223301, 0.6031067961165049, 0.5464077669902913, 0.6194174757281553, 0.5704854368932039, 0.5902912621359223, 0.6058252427184466, 0.6066019417475729, 0.6050485436893204, 0.6, 0.5829126213592233, 0.6042718446601941, 0.6023300970873786, 0.6050485436893204, 0.6050485436893204, 0.5988349514563107, 0.6003883495145631, 0.5875728155339806, 0.5953398058252427, 0.582135922330097, 0.5887378640776699, 0.5871844660194174, 0.5766990291262136, 0.6019417475728155, 0.5879611650485437, 0.6093203883495145, 0.5906796116504854, 0.592621359223301, 0.5965048543689321, 0.5918446601941748, 0.6, 0.494368932038835, 0.5922330097087378, 0.5906796116504854, 0.6104854368932039, 0.5642718446601942, 0.5883495145631068, 0.6077669902912621, 0.5386407766990291, 0.5949514563106796, 0.5840776699029127, 0.5840776699029127, 0.5794174757281554, 0.6038834951456311, 0.5918446601941748, 0.5790291262135923, 0.581747572815534, 0.6007766990291262, 0.6077669902912621, 0.5739805825242719, 0.6058252427184466]
# 1.5x
l2 = [18.726128, 14.243249, 12.357524, 11.024664, 10.026348, 9.41291, 9.106738, 8.809407, 8.560738, 8.481699, 8.413594, 8.27698, 8.179033, 8.161177, 8.081215, 8.058779, 7.9298854, 7.9794407, 7.985637, 7.969444, 7.916736, 7.88046, 7.865052, 7.9524636, 7.8669753, 7.7809505, 7.821668, 7.842856, 7.7885475, 7.8133984, 7.783332, 7.7627263, 7.8300605, 7.778517, 7.850733, 7.7789125, 7.6967773, 7.7598224, 7.7875395, 7.673283, 7.754722, 7.7266726, 7.793219, 7.709442, 7.7001853, 7.653694, 7.7317276, 7.79266, 7.761382, 7.657106, 7.825858, 7.7344394, 7.755173, 7.7548223, 7.7117505, 7.7714024, 7.745838, 7.728301, 7.668009, 7.7278643, 7.7486095, 7.646454, 7.696991, 7.734344, 7.645451, 7.7290926, 7.705253, 7.7938437, 7.7571974, 7.752286, 7.725459, 7.7689424, 7.7119193, 7.7925653, 7.7631116, 7.7149363, 7.711734, 7.6685367, 7.765062, 7.771234, 7.7196584, 7.818006, 7.844465, 7.7191935, 7.7009892, 7.7251916, 7.7717953, 7.730236, 7.7187786, 7.7236123, 7.7867856, 7.769878, 7.698918, 7.8041916, 7.703381, 7.7704387, 7.774724, 7.8921833, 7.824645, 7.837076, 7.8177233, 7.8135405, 7.8939424, 7.7682357, 7.768167, 7.8702855, 7.808147, 7.7923403, 7.7528872, 7.844267, 7.78452, 7.833455, 7.8041196, 7.7685637, 7.8358245, 7.9327135, 7.779284, 7.8307323, 7.7925305, 7.803567, 7.782404, 7.9136157, 7.737366, 7.8377085, 7.751321, 7.731179, 7.80842, 7.805253, 7.8242006, 7.91498, 7.855997, 7.7992215, 7.8655066, 7.820173, 7.8004436, 7.8500204, 7.8478785, 7.8229375, 7.8443203, 7.841781, 7.8643823, 7.8855004, 7.756328, 7.8427596, 7.814773, 7.886516, 7.7752085, 7.8197436, 7.856299, 7.781367, 7.798145, 8.01545, 7.899169, 7.8453894, 7.820225, 7.934762, 7.8540154, 7.8565736, 7.884167, 7.8891654, 7.8780494, 7.905764, 7.918781, 7.9467874, 7.9270306, 7.841154, 7.8424406, 7.793018, 7.7875247, 7.919047, 7.789353, 7.8598013, 7.895638, 7.7572317, 7.825139, 7.75661, 7.91163, 7.8564205, 7.9370117, 7.802981, 7.870284, 7.90142, 7.9015126, 7.932147, 7.8759394, 8.018438, 7.8499384, 7.964654, 7.878607, 7.953523, 7.918307, 7.861701, 7.8430705, 7.944494, 8.009651, 7.9340405, 7.9404745, 7.9719367, 7.8631916, 7.8941946]
a2 = [0.35572815533980584, 0.43106796116504853, 0.4551456310679612, 0.46174757281553397, 0.46601941747572817, 0.5293203883495146, 0.5398058252427185, 0.5398058252427185, 0.5537864077669903, 0.5332038834951456, 0.5448543689320389, 0.5479611650485436, 0.5580582524271844, 0.5619417475728156, 0.5289320388349514, 0.5266019417475728, 0.5440776699029126, 0.5623300970873787, 0.5650485436893203, 0.5724271844660194, 0.5572815533980583, 0.5553398058252427, 0.5658252427184466, 0.5545631067961165, 0.5506796116504854, 0.5339805825242718, 0.5483495145631068, 0.5398058252427185, 0.5666019417475728, 0.5464077669902913, 0.5615533980582524, 0.5603883495145631, 0.5700970873786407, 0.5720388349514564, 0.5724271844660194, 0.566990291262136, 0.5568932038834952, 0.5685436893203883, 0.5592233009708738, 0.5444660194174757, 0.556504854368932, 0.5759223300970874, 0.552621359223301, 0.5246601941747573, 0.5623300970873787, 0.5580582524271844, 0.5475728155339806, 0.5568932038834952, 0.5328155339805826, 0.5514563106796116, 0.5429126213592232, 0.5627184466019417, 0.5840776699029127, 0.5510679611650485, 0.570873786407767, 0.5685436893203883, 0.5483495145631068, 0.5906796116504854, 0.516504854368932, 0.5770873786407767, 0.5366990291262136, 0.574757281553398, 0.5433009708737864, 0.5033009708737864, 0.5677669902912621, 0.5631067961165048, 0.5786407766990291, 0.552621359223301, 0.5522330097087379, 0.5673786407766991, 0.5700970873786407, 0.5906796116504854, 0.5359223300970873, 0.5475728155339806, 0.5778640776699029, 0.5514563106796116, 0.5864077669902913, 0.5638834951456311, 0.5588349514563107, 0.5728155339805825, 0.5766990291262136, 0.5328155339805826, 0.5394174757281553, 0.5735922330097087, 0.5572815533980583, 0.5584466019417476, 0.5697087378640777, 0.5460194174757281, 0.5704854368932039, 0.5724271844660194, 0.5495145631067961, 0.5561165048543689, 0.570873786407767, 0.5448543689320389, 0.5464077669902913, 0.5553398058252427, 0.5153398058252427, 0.5693203883495146, 0.5662135922330097, 0.556504854368932, 0.5662135922330097, 0.5460194174757281, 0.566990291262136, 0.5739805825242719, 0.5347572815533981, 0.56, 0.5619417475728156, 0.5689320388349515, 0.5689320388349515, 0.530873786407767, 0.5693203883495146, 0.574368932038835, 0.581747572815534, 0.541747572815534, 0.5328155339805826, 0.570873786407767, 0.5790291262135923, 0.570873786407767, 0.5537864077669903, 0.5732038834951456, 0.5642718446601942, 0.5774757281553398, 0.553009708737864, 0.5623300970873787, 0.5514563106796116, 0.5681553398058252, 0.5805825242718446, 0.5654368932038835, 0.5751456310679611, 0.5693203883495146, 0.566990291262136, 0.5623300970873787, 0.5351456310679612, 0.5662135922330097, 0.549126213592233, 0.537864077669903, 0.5724271844660194, 0.5673786407766991, 0.5809708737864078, 0.5246601941747573, 0.56, 0.5483495145631068, 0.5324271844660194, 0.5631067961165048, 0.56, 0.5650485436893203, 0.566990291262136, 0.5666019417475728, 0.5700970873786407, 0.5324271844660194, 0.5739805825242719, 0.553009708737864, 0.5219417475728155, 0.5479611650485436, 0.581747572815534, 0.563495145631068, 0.5405825242718446, 0.5425242718446602, 0.574368932038835, 0.5646601941747573, 0.5658252427184466, 0.5646601941747573, 0.5673786407766991, 0.5607766990291262, 0.5596116504854369, 0.5786407766990291, 0.5774757281553398, 0.5650485436893203, 0.5654368932038835, 0.545242718446602, 0.574368932038835, 0.5522330097087379, 0.5510679611650485, 0.5790291262135923, 0.5464077669902913, 0.5572815533980583, 0.5510679611650485, 0.5545631067961165, 0.5211650485436893, 0.5596116504854369, 0.5102912621359224, 0.5801941747572815, 0.5413592233009709, 0.5654368932038835, 0.5584466019417476, 0.5615533980582524, 0.5712621359223301, 0.5592233009708738, 0.5176699029126214, 0.5289320388349514, 0.5409708737864077, 0.5514563106796116, 0.5693203883495146, 0.5735922330097087, 0.5603883495145631, 0.5596116504854369, 0.5502912621359223, 0.5153398058252427, 0.556504854368932, 0.553009708737864]
# 0.5x
l3 = [18.27745, 13.988808, 12.264441, 11.0346, 10.303102, 9.956442, 9.541262, 9.27303, 9.08943, 9.082669, 8.838885, 8.8502035, 8.79736, 8.666309, 8.661598, 8.65922, 8.4929695, 8.488186, 8.505897, 8.544994, 8.461514, 8.466672, 8.50369, 8.406162, 8.480226, 8.341516, 8.446232, 8.38563, 8.320538, 8.4867935, 8.402239, 8.352382, 8.236732, 8.374318, 8.28123, 8.345205, 8.266233, 8.300801, 8.360254, 8.343566, 8.326347, 8.2915, 8.397274, 8.279629, 8.2381, 8.357032, 8.2342615, 8.26914, 8.18007, 8.204477, 8.284548, 8.254393, 8.240278, 8.250605, 8.268553, 8.244882, 8.179741, 8.256789, 8.179271, 8.199561, 8.041349, 8.187735, 8.245251, 8.330335, 8.194419, 8.238212, 8.217009, 8.162132, 8.214946, 8.317675, 8.49007, 8.213868, 8.272911, 8.172522, 8.254416, 8.195395, 8.263298, 8.160324, 8.247864, 8.368467, 8.23833, 8.21959, 8.195475, 8.216056, 8.205339, 8.26808, 8.196556, 8.267612, 8.211711, 8.214964, 8.183248, 8.259297, 8.1662655, 8.1697645, 8.185854, 8.250076, 8.155765, 8.275748, 8.17962, 8.214527, 8.211021, 8.2858095, 8.221406, 8.309188, 8.275056, 8.283644, 8.325519, 8.300132, 8.310376, 8.233692, 8.216678, 8.359338, 8.177821, 8.219408, 8.362502, 8.148237, 8.1757965, 8.234352, 8.241923, 8.332663, 8.234736, 8.06991, 8.163951, 8.383669, 8.254871, 8.243581, 8.292756, 8.246684, 8.179678, 8.195836, 8.263591, 8.326005, 8.311714, 8.206957, 8.1837845, 8.268806, 8.332776, 8.220215, 8.359058, 8.192219, 8.215352, 8.265208, 8.230563, 8.3001175, 8.296818, 8.222637, 8.443088, 8.220205, 8.298189, 8.216976, 8.434507, 8.265788, 8.245445, 8.241691, 8.264757, 8.27747, 8.298599, 8.248283, 8.238752, 8.345876, 8.21372, 8.1929035, 8.286113, 8.292381, 8.39461, 8.308247, 8.2298975, 8.248569, 8.156261, 8.190983, 8.3271055, 8.288957, 8.27842, 8.319564, 8.247104, 8.324687, 8.255347, 8.229782, 8.31935, 8.214602, 8.100539, 8.356392, 8.372905, 8.333265, 8.393769, 8.234118, 8.241735, 8.271332, 8.200519, 8.247919, 8.29624, 8.220727, 8.373215, 8.22129, 8.272325, 8.263035, 8.281703, 8.384675, 8.295842, 8.408965]
a3 = [0.34640776699029124, 0.4155339805825243, 0.46640776699029124, 0.4893203883495146, 0.5145631067961165, 0.5266019417475728, 0.5347572815533981, 0.5250485436893204, 0.5421359223300971, 0.5223300970873787, 0.538252427184466, 0.4912621359223301, 0.5394174757281553, 0.5638834951456311, 0.5479611650485436, 0.5460194174757281, 0.5413592233009709, 0.5592233009708738, 0.5250485436893204, 0.5351456310679612, 0.5188349514563106, 0.5429126213592232, 0.5421359223300971, 0.5390291262135922, 0.5495145631067961, 0.5576699029126213, 0.5099029126213592, 0.5234951456310679, 0.5518446601941748, 0.5413592233009709, 0.5196116504854369, 0.5588349514563107, 0.509126213592233, 0.5386407766990291, 0.501747572815534, 0.5475728155339806, 0.5335922330097087, 0.5332038834951456, 0.537864077669903, 0.5537864077669903, 0.5440776699029126, 0.5495145631067961, 0.5347572815533981, 0.5316504854368932, 0.5413592233009709, 0.523883495145631, 0.5421359223300971, 0.5297087378640777, 0.5289320388349514, 0.549126213592233, 0.5172815533980583, 0.5300970873786408, 0.5549514563106797, 0.5401941747572816, 0.5502912621359223, 0.5518446601941748, 0.5366990291262136, 0.5506796116504854, 0.5250485436893204, 0.527378640776699, 0.5363106796116505, 0.5592233009708738, 0.5654368932038835, 0.5588349514563107, 0.5335922330097087, 0.5421359223300971, 0.5495145631067961, 0.5289320388349514, 0.5429126213592232, 0.5467961165048544, 0.5615533980582524, 0.553009708737864, 0.5289320388349514, 0.538252427184466, 0.545242718446602, 0.5394174757281553, 0.5227184466019418, 0.5425242718446602, 0.5433009708737864, 0.5592233009708738, 0.5549514563106797, 0.52, 0.541747572815534, 0.5444660194174757, 0.5363106796116505, 0.5561165048543689, 0.5242718446601942, 0.5607766990291262, 0.5549514563106797, 0.5405825242718446, 0.5172815533980583, 0.5335922330097087, 0.5541747572815534, 0.5654368932038835, 0.537864077669903, 0.52, 0.5436893203883495, 0.5685436893203883, 0.5246601941747573, 0.5332038834951456] + [0.5495145631067961, 0.5460194174757281, 0.5553398058252427, 0.5192233009708738, 0.5324271844660194, 0.516504854368932, 0.5207766990291263, 0.5227184466019418, 0.5483495145631068, 0.5436893203883495, 0.4621359223300971, 0.5518446601941748, 0.5269902912621359, 0.5370873786407767, 0.5355339805825243, 0.5580582524271844, 0.5607766990291262, 0.5475728155339806, 0.5561165048543689, 0.5724271844660194, 0.563495145631068, 0.5510679611650485, 0.5145631067961165, 0.5689320388349515, 0.56, 0.534368932038835, 0.5483495145631068, 0.5429126213592232, 0.5557281553398058, 0.5347572815533981, 0.5394174757281553, 0.5561165048543689, 0.5366990291262136, 0.5471844660194175, 0.545631067961165, 0.5324271844660194, 0.5460194174757281, 0.5425242718446602, 0.5172815533980583, 0.5300970873786408, 0.5475728155339806, 0.5642718446601942, 0.5429126213592232, 0.5479611650485436, 0.566990291262136, 0.574368932038835, 0.5580582524271844, 0.5533980582524272, 0.5448543689320389, 0.5227184466019418, 0.5483495145631068, 0.5207766990291263, 0.5623300970873787, 0.5495145631067961, 0.538252427184466, 0.5370873786407767, 0.5549514563106797, 0.516504854368932, 0.5083495145631068, 0.56, 0.5335922330097087, 0.5475728155339806, 0.545631067961165, 0.5390291262135922, 0.49320388349514566, 0.45475728155339806, 0.5662135922330097, 0.5603883495145631, 0.530873786407767, 0.5398058252427185, 0.5297087378640777, 0.5332038834951456, 0.4629126213592233, 0.5293203883495146, 0.5495145631067961, 0.5467961165048544, 0.5320388349514563, 0.49592233009708736, 0.5207766990291263, 0.5502912621359223, 0.545242718446602, 0.5324271844660194, 0.538252427184466, 0.556504854368932, 0.5339805825242718, 0.5370873786407767, 0.530873786407767, 0.5258252427184466, 0.5390291262135922, 0.5312621359223301, 0.5487378640776699, 0.5320388349514563, 0.5588349514563107, 0.5405825242718446, 0.5642718446601942, 0.5188349514563106, 0.5460194174757281, 0.5370873786407767, 0.5227184466019418, 0.5258252427184466]

x = list(range(1, len(l1)+1))
fig, ax = plt.subplots()
ax2 = ax.twinx()
ax.plot(x, a1, marker='*', linewidth=1, markevery=8, label="1. top-5 acc. (output dimension 204 of $\phi_e$ and $\phi_b$")
ax.plot(x, a2, marker='1', linewidth=1, markevery=8, label="2. top-5 acc. (output dimension 306 of $\phi_e$ and $\phi_b$")
ax.plot(x, a3, marker='2', linewidth=1, markevery=8, label="3. top-5 acc. (output dimension 102 of $\phi_e$ and $\phi_b$")
ax2.plot(x, l1, "k", marker='*', linewidth=1, markevery=8, linestyle='dashed', label="1. training loss")
ax2.plot(x, l2, color="gray", marker='1', linewidth=1, markevery=8, linestyle='dashed', label="2. training loss")
ax2.plot(x, l3, color="gray", marker='2', linewidth=1, markevery=8, linestyle='dashed', label="3. training loss")

ax.set_xlabel('epochs (times of using a training dataset)')
ax.set_ylabel('top-5 accuracy')
ax2.set_ylabel('training loss')
ax.legend(fontsize=8, loc="center", bbox_to_anchor=(0.65, 0.45))
ax2.legend(fontsize=8, loc='center', bbox_to_anchor=(0.75, 0.3))
plt.show()