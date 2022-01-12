# -*- coding:utf-8 -*-
"""
Author:秦帅波
time:2021/8/17 10:44
desc:
"""
from bs4 import BeautifulSoup

# data='''<a class="nav-link match-link-stats" href="/football/matches/match867851_Kalteng_Putra-Arema-online/" title="Stat"></a>'''
# data = '''<a class="tag" href="http://ask.globecancer.com/tag/zhongliujiyinjiance.html">肿瘤基因检测</a>'''
# data = '''<li class="tagPopup">
# <a class="tag" href="http://ask.globecancer.com/tag/zhuanyixingyixianai.html">
#
#                                         转移性胰腺癌
#                                         </a>
# </li>'''
'''某一页问题列表获取'''
question_data = '''<h4 class="news__item-title mt0">
<a class="mr10" href="http://ask.globecancer.com/q-1088.html" target="_blank">
四期肾癌有什么好的治疗方法吗？
</a>
</h4> '''
soup = BeautifulSoup(str(question_data), 'html.parser')
# print(soup.select_one('.match-link-stats')['href'])
print('问题:', soup.select_one(".news__item-title").text.strip())  # 获取对应内容
print('链接:', soup.select_one('.mr10')['href'])  # 获取对应链接
# print(soup.select_one(".news__item-title mt0").get_text)  # 获取对应内容

'''问题对应答案获取验证'''
# answer_data = '''<div class="answercontent"><p>术后一旦出现扩散转移，肯定是晚期了，针对晚期的患者，是以保守治疗为主，靶向药不失为比较合适的治疗手段之一，但是靶向药终究会出现耐药的，所以有条件的话可以配合细胞免疫治疗，或者PD-1免疫检查点抑制剂，增强靶向药的效果，降低副作用，延长靶向药的耐药时间，最大限度的延长患者的生命，提高患者的生存质量，希望我的回答对你有所帮助。</p><div class="appendcontent">                       </div></div>'''
# answer_data = '''<p>(一)胰腺癌的组织学类型参照2010版WHO胰腺癌组织学分类（附件6）。</p>'''
# answer_data = '''<p>&nbsp;基本病情：</p><p>患者女性，61岁。2014年1月确诊为卵巢高级浆液性乳头状腺癌, IIIc期，随后接受全子宫+双侧输卵管+卵巢切除术，网膜和部分直肠也被切除。之后患者进行六个周期的紫杉醇和卡铂化疗，复发后又多次调整方案，病情仍然没有得到有效控制。 1/2018年进⾏的CT显示出现新的右肺肿物。4/2018年的复查CT显示，一些结节减小，另一些结节增大。</p><p>会诊结果</p><p>为了寻求更有效的治疗方案，患者通过国内权威的癌症患者服务平台--全球肿瘤医生网申请了全球排名第一的MD安德森癌症中心，著名的妇科癌症专家David M Gershenson教授进行会诊，以下是部分会诊报告：</p><p>1、你推荐的下⼀步治疗⽅案是什么（药物）？</p><p>2/2018年的CA 125⽔平已降⾄167，2014年4⽉14⽇的⽔平为224.0。 除⾮CA 125 开始显着上升，否则我会建议继续使⽤Doxil，直到CA 125或CT清楚的证实疾病进展。 为排除伴随肺癌的诊断，建议进⾏细针穿刺活检。 如果卵巢癌有进⼀步的疾病进展，可考虑使⽤PARP抑制剂，如olaparib或niraparib。 然⽽，这些药物在没有BRCA胚系细胞突变的患者中通常不会⾮常积极。</p><p>2、您是否建议她现在进⾏基因测试或PD-1测试？</p><p>此时，我会推荐肿瘤组织的基因组分析来鉴定任何可能成为可⽤新药靶点的常突变。 其中⼏项测试也将检查PD-1。建议你与中国的医⽣核实，如果国内没有这个测试，可以由美国的⼏家公司或医院来测试。 Foundation One就是⼀个很好的平台。⾎液检查也可以使⽤，但是⽬前还没有很好的研究或进展。</p><p>会诊专家介绍</p><h1>David M. Gershenson博士</h1><p>在妇科肿瘤学领域以及妇女的健康和福祉方面，他获得了无数的临床，组织和科学成就，Gershenson教授是德克萨斯大学医学院安德森癌症中心妇科肿瘤学和生殖医学系教授兼前任主席，在IGCS第15届澳大利亚墨尔本双年会上，David M. Gershenson医师获得国际妇科癌症协会（IGCS）卓越奖。</p><p>Gershenson博士在妇科肿瘤的诊断和临床管理中的作用一直处于全球最高水平。世界各地的富有成就的妇科肿瘤专家，也会向他咨询有关护理患有这些肿瘤的女性的问题。</p><p>Gershenson教授于1979年加入MD Anderson教职，1998至2012年担任部门主席。他将他的临床和转化研究专注于罕见卵巢肿瘤：低度浆液性肿瘤，透明细胞癌，粘液性癌，恶性卵巢生殖细胞肿瘤和卵巢性索间质肿瘤。此外，他在开发专注于罕见卵巢癌患者新型疗法的临床试验方面发挥了重要作用。他的研究也报道了与晚期或复发性卵巢透明细胞癌和粘液癌相关的不良预后。自1999年以来，Gershenson先生一直担任MD Anderson NCI资助的卵巢癌SPORE联合首席研究员，最近还担任“针对女性低级别卵巢浆液性癌的个性化治疗”联合项目负责人，</p><p>Gershenson在该领域的专业知识远远超出了MD Anderson，他在许多国家和国际组织中担任领导职务，其中包括：NCI赞助的合作团体NRG肿瘤学，罕见肿瘤委员会主席以及NRG国际试验的首席研究员和英国的一个研究小组，研究卵巢复发性低度浆液性癌; NCI妇科癌症指导委员会共同主席，该委员会批准了北美所有妇科癌症的新的III期和随机II期临床试验; 妇女癌症基金会主席，这是妇产科肿瘤学家协会的全国基金会，其主要任务包括研究经费资助和公众教育以及妇科癌症的认识; 妇科肿瘤学杂志名誉编委。</p><p>在他的所有成就中，Gershenson说他最引以自豪的是引进了下一代妇科肿瘤学家，以改变患者的生活。</p><p>对于癌症患者来说，找到一个好的专家是抗癌的第一步也是最重要的一步！</p><p>好消息是，现在癌症患者可通过全球肿瘤医生网申请Gershenson教授的会诊，得到权威的诊疗方案！</p><p>会诊流程：</p><p>1、患者提供完善病历资料</p><p>2、整理翻译病例资料，预约会诊时间</p><p>3、美国专家远程视频会诊（患者国内的主治医生参与）</p><p>4、视频会诊后5个工作日出具会诊报告</p><p>5、全球肿瘤医生网协助患者实施下一步治疗方案......</p><p>申请电话：400-666-7998</p><p>申请邮箱：doctor.huang@globecancer.com</p><p>美国专家会诊对癌症患者意义重大！</p><p>1、得到一些额外的有关诊疗的信息只会更有帮助！</p><p>换一双眼睛，换个思维，也许会产生与初诊不同的意见，在第二诊疗意见和原始诊疗意见一致时，患者会更放心也更信任尊重自己的主诊医生，在治疗过程中会更配合。 当第二诊疗意见和原始诊疗意见不同时，进一步的讨论和分析自然也会有助于避免错误或不必要的治疗。总而言之，第二诊疗意见可以帮助患者对自己的疾病更为了解。</p><p>2、获得更加全面、客观的诊疗建议！</p><p>由美国权威癌症专家制定诊疗方案，对于帮助患者确诊病情，挽救生命起到至关重要的作用。做出医学第二建议的医生不参与对患者的直接治疗，不会涉及相关利益，因此对患者做出的诊断和治疗建议会更加的匹配，客观和公正。</p><p>3、获得美国最新的癌症治疗方案！</p><p>美国癌症的新药物和治疗手段层出不穷，更新迅速 ，针对患者病情的新药、新技术、基因检测、免疫治疗等国际先进治疗手段需要通过国际医学第二建议才能获得权威建议，此外有些新的治疗技术和药物方案尚未在国际上发表，也只能通过与美国专家沟通才能了解。</p><p>寻求美国专家会诊需要注意的事项！</p><ol><li>要和自己的现任主诊医生沟通，获得理解和支持，甚至可以请自己的主治医生推荐专家及参与视频会诊，因为医生之间的沟通往往更有效，双方共同制定下一步治疗方案，患者的医生可以在国内实施美国专家给出的建议，这对患者十分有利的。</li><li>提供远程视频会诊的机构/医生的水准很大程度上决定了治疗方案的可信度和价值。建议经济条件允许范围内，选择最权威的医院/医生。</li><li>要尽可能将自己相关的病历和各种化验、影像、病理报告收集全，并根据要求提供完整资料。</li></ol><p><br></p><p>&nbsp;</p><p>写给国内癌症患者的话：</p><p>如今出国看病不是什么新鲜事儿了，远程国际医疗服务也就在键盘和指尖，这些都是患者的福音。</p><p>对于考虑赴美就医的患者，先进行一次远程会诊对决定是否赴美就医无疑有很大帮助（提供第二诊疗意见的美国医生也有可能转变为患者赴美后的主诊医生）。</p><p>如果患者没有计划赴美就医，那么，获得自己国内现任主诊医生的理解和支持尤为关键。一方面是因为你需要医生的帮助来收集完整的病历和检查结果，另一方面，会诊后美国专家给出的治疗方案也有很大可能需要国内主诊医生来实施，因此，如果主诊医生能参与会诊过程，一起讨论患者下一步可实施的最佳治疗方案，将能够使患者最大获益！</p><p></p><p>&nbsp;</p><p><br></p>                             </div>'''
# answer_data='''<p></p>, <p></p>, <p></p>, <p>　　透明细胞为主型肾癌的一线治疗-舒尼替尼</p>, <p>　　透明细胞型肾细胞癌的一线治疗首选分子靶向治疗。研究发现大部分肾透明细胞癌中细胞存在VHL基因缺失或失活，从而引起HIF基因上调，导致PDGF、VEGF、CaIX等基因过度表达，这些肿瘤发生、发展的生物学机制有可能是透明细胞型肾细胞癌分子靶向治疗的应用基础。</p>, <p>　　舒尼替尼</p>, <p>　　舒尼替尼(sunitinib)是多靶点受体酪氨酸激酶抑制剂，主要作用靶点为血管内皮生长因子受体1-2(VEGFR1-2)、血小板衍生生长因子受体(PDGFR-α，PDGFR-β)、干细胞生长因子受体(c-KIT)以及FMS样酪氨酸激酶3(FLT-3)，具有抗肿瘤血管生成、抑制肿瘤细胞增殖的作用。</p>, <p>　　2007年新英格兰杂志报道舒尼替尼与α干扰素1：1对比一线治疗转移性肾透明细胞癌Ⅲ期临床研究，共入组750例患者，90%患者为MSKCC中低度风险，中位PFS分别为11个月和5个月(HR0.42，95%CI0.32～0.54;P&lt;0.001)，客观缓解率分别为31%和6%(P&lt;0.001)，中位生存期分别为26.4个月和21.8个月(P=0.051)。</p>, <p>　　从而奠定了舒尼替尼一线治疗肾透明细胞癌的地位。舒尼替尼一线治疗中国转移性肾细胞癌患者的多中心Ⅳ期临床研究结果显示客观有效率为31.1%，其中位PFS为14.2个月，中位OS为30.7个月。</p>, <p>　　基于上述临床数据，推荐舒尼替尼用于晚期透明细胞型肾细胞癌的一线治疗，用法为：50mg，qd口服，4/2方案(服药4周，停药2周)给药。</p>, <p>　　考虑舒尼替尼4/2给药方案血液学毒性不良反应发生率高，可选择2/1方案52(服药2周，停药1周)，耐受性提高，疗效未受影响。</p>, <p><br/></p>, <p></p>, <p></p>, <p></p>'''
answer_data = '''<p><span>始于19世纪初的手术治疗，经过不断发展，实现了“治愈”一小部分患者的目标；始于19世纪末的放射治疗，发展到上世纪50年代，多带带或联合的作用使得约1/3患者治愈；始于20世纪初的化疗，又进一步提高了肿瘤的治疗效果。三种传统治疗方法走向极致，但远未达到人们期望的治疗目标。肿瘤的免疫治疗虽发展晚，却以前所未有的速度进入临床，并有望最终成为治愈肿瘤的重要武器。随着医学的进步，个性化癌症疫苗已成为精准医疗的目标之一，被全球生物医药公司争先研究，希望能够通过激活人体自身免疫系统，来杀灭癌细胞！无论是用于预防传染病还是预防和治疗癌症，疫苗都可以通过类似的机制发挥作用：它们教导免疫系统将传染性病原体或癌细胞识别为需要消除的外来物质。癌细胞表面存在特殊的蛋白质，通过靶向这些蛋白质，免疫系统可以特异性地消除癌细胞，同时不伤害正常的细胞。近两年，全球癌症疫苗研发遍地开花，目前发现在各个癌症中取得了令人振奋的研究数据，而这些疫苗主要依靠人体内的三类免疫细胞制备。全球肿瘤医生网医学部查阅了大量文献，为大家挑选了一些已进入临床应用的癌症疫苗，希望给患者多一份希望和战胜癌症的信心！基于树突细胞的癌症疫苗树突状细胞(Dendritic Cells,DC)：是一群异质性的细胞, 抗原提呈功能最强, 是唯一能够激活初始型T细胞的专职抗原递呈细胞。人体的免疫系统中本来就有这种树突状细胞，但数量和活力都不够围歼癌变细胞的程度。有潜力成为树突状细胞的前体细胞可以通过一个特定的方法从血液中分离出来。借助于某种特定的信使，在试管中分离出来的细胞可以获得免疫能力。当前体细胞成熟为树突状细胞时，他们即可捕获特定的蛋白质（例如肿瘤抗原）。 由于树突状细胞抗肿瘤特性与疫苗原理一致，因此树突细胞疗法在临床中更多的被称为树突细胞疫苗。目前树突状细胞肿瘤疫苗正在被迅速、广泛的研究 ,并且已在动物实验和早期的临床实验中取得了很有意义的结果。这些研究结果表明: 树突状细胞肿瘤疫苗不仅能够诱发针对原发肿瘤的免疫应答 , 而且也能够诱发针对转移肿瘤的免疫应答 , 并且 CD4 + 、 CD8 + T 淋巴细胞和自然杀伤细胞 ( natur e kille r cells, N Ks)都参与抗肿瘤免疫应答。树突细胞可通过各种方式用于癌症疫苗接种，包括：1）体内树突细胞捕获的非靶向肽/蛋白和基于核酸的疫苗，2）直接与抗树突抗体偶联的抗原组成的疫苗，3 ）由体外产生的负载抗原的树突组成的疫苗。树突细胞疫苗的临床应用我国目前批准的细胞免疫治疗的临床试验项目不多，DC细胞疗法的价值、安全性和潜力还有待挖掘。相信一旦整体政策完备推出，将带动我国相关临床治疗的操作规范和标准执行，为我国肿瘤患者治疗增添新选择。美国，德国，日本等医疗水平发达的国家，对树突细胞的研发及临床应用走在世界前列。美国PROVENGE疫苗（前列腺癌）2010年4月29日，FDA批准了首个癌症治疗疫苗PROVENGE(sipuleucel T)用于晚期前列腺癌的治疗，使该药成为第一个在美国被批准用于治疗的树突细胞疗法，开创了癌症免疫治疗的新时代，这项批复标志着20年的不懈努力终于取得成功。产品名Provenge公司美国Denreon公司制备方式未知用途癌症疫苗价格93000美元德国LANEX-DC疫苗德国癌症治疗专家Frank Gansauge教授，带队研发的LANEX-DC是一种利用肿瘤抗原对患者自体树突（DC）细胞进行特异性免疫刺激培养，以DC细胞为基础的肿瘤疫苗技术。通过采集患者血液，分离、筛选出高纯度DC细胞，混合了细胞因子GM-CSF、肿瘤特异性抗原（PAP）等物质进行培育，使DC细胞活化，再回输患者，激活患者体内的T淋巴细胞，从而产生针对大量表达PAP的肿瘤细胞的特异性免疫杀伤效应，消灭癌细胞！临床已证实对人类已知的恶性肿瘤，如肺癌、肝癌、肾癌、乳腺癌、皮肤癌等多种肿瘤有效。详情点击：德国树突细胞疫苗治疗原理介绍这种树突细胞免疫治疗方案在其他国家不是没有，但是收效甚微，目前在国内的顶级医科大学研发的产品其活性因子的生存期只有21天，也就意味着21天内就要进行下一个疗程。而LDG团队的LANEX-DC治疗法采用高度提纯的树突细胞，一个疗程可以维持6个月，更重要的是他们把病患的复发率从50%降低到7%。同时细胞活性因子从培养室到植入患者体内，之间的存活时间可以持续8个小时，目前国内医科大学制备后基本存活时间就在20分钟之内。 技术上存在巨大差距。产品名LANEX-DC公司LDG Labor实验室制备方式树突DC自体免疫细胞用途实体肿瘤价格38万元/次（亚太地区）日本树突细胞融合细胞疫苗融合细胞疫苗是世界领先的癌症研究中心哈佛大学Dana-farber癌症研究所与东京慈惠医科大学共同开发，是最具前瞻性的癌症免疫治疗。利用患者自身的癌细胞来攻击癌细胞，确立了至今为止全新的癌症治疗方法。价格约35万人民币。详情点击：日本新一代融合细胞疗法横空出世，精准狙击癌细胞！这是一种很理想的疗法，我们都知道癌症形成的原因之一，就是癌细胞隐藏的很好，树突细胞无法识别癌细胞，大家想象一下，把自己的癌细胞和树突细胞融合，形成携带多种癌细胞表面的特异性抗原的树突细胞，这些树突细胞就具备了识别肿瘤细胞的能力，我们把这些细胞回输导体内，他就会教导体细胞去识别不同的癌抗原的癌细胞，一组去找a抗原，一组去找b抗原癌细胞，把他们统统消灭，同时结合增强体内T细胞的辅助治疗白细胞介素12一起使用，能够有效增加杀手T细胞的数量，从而达到最佳的抗癌效果。目前在国际上被广泛研究。 </span><img alt="人体内的这类免疫细胞竟能制成挽救生命的癌症疫苗" src="http://p3.pstatp.com/large/pgc-image/581f551a428b44b89c3f5f3b6e8259dc"/><span>  简单来说，就是利用患者自身的癌细胞，与患者自身的树突细胞进行体外融合。得到能够表达所有癌抗原的新树突细胞，制备成个体化的融合细胞疫苗。将融合细胞回输入患者体内识别癌细胞。树突细胞疫苗三大临床优势1.基于高度特异全身和局部的细胞免疫重建，对癌细胞清除更具靶向性，更精准高效。机体各种常见的病毒感染性疾病和肿瘤的发生与机体DC功能的缺失或缺陷有直接关系，所以恢复体内特异性DC功能成为治疗和预防这类疾病的关键。T-DC由于特异性的优势抗原表位肽的使用，使被激活的T细胞具有特异性和靶向性，通过修复、恢复和增强患者自身细胞免疫功能，打破了机体免疫全身和局部的耐受状态，从而实现全身和局部机体免疫的重建。2.持续启动以非溶胞为核心杀伤模式的清除机制，安全性高研究证明，T-DC主要以以动员体内各种细胞因子为主要手段来清除靶目标，这使得重建的免疫系统在清除靶目标的同时大大降低了对正常细胞损伤作用。3.具有疫苗特性的长期作用，实现预防和治疗的有机结合体外重建的DC在回输体内时可以激活静息T细胞产生初次免疫应答的细胞，激活的T细胞可以被点状放大并进一步增殖。一个树突能激活100～3000 个T细胞。大部分效应T细胞发挥清除病毒的作用，另一部分会存活长达十几年到几十年成为记忆性T细胞，在下一次接触到低剂量抗原就可发生高强度的免疫应答。所以，基于T-DC修复和重建的免疫防护系统可以持续发挥作用数十年，并在适当的条件下可以重新进入循环发挥作用。这五类患者最适合使用树突细胞疫苗需要注意的是，树突细胞疫苗疗法对于晚期癌症患者肿瘤的缩小效果不明显，针对晚期癌症的患者在保持生活品质的同时有延长寿命的效果；作为术后的辅助治疗法可以抑制复发，治疗效果可维持较长时间；与化疗、靶向药、PD1抑制剂等其它疗法联合治疗，效果会更佳。因此，这五类患者最适合：肿瘤手术前体质较差，术后恢复慢，且害怕隐匿性癌细胞没有被彻底根除的患者。放疗、化疗后，免疫力低下，副作用反应明显(如食欲减退、恶心、脱发、皮肤炎症等),期望增加化放化疗效果的患者。由于害怕放化疗的毒副作用，希望利用各种治疗手段实现治疗效果的患者。肿瘤晚期癌细胞已经全身扩散，但常规治疗方法已无能为力，期望延长生存期，提高生活质量的患者。接受免疫检查点抑制剂的患者。主要适用于实体肿瘤：头颈部肿瘤、食道癌、肺癌、胃癌、乳腺癌、肝癌、胰腺癌、结直肠癌、卵巢癌、子宫癌、肾癌、前列腺 癌、恶性黑色素瘤、肉瘤、部分恶性淋巴瘤。树突细胞疫苗的国际最新研究临床中正在开展许多针对癌症的治疗性疫苗接种途径。在国际临床试验官网clinicaltrials.gov中搜索术语树突细胞疫苗，有54个临床研究。这些研究中的一个共同特征是疫苗接种的关键步骤是将癌抗原有效呈递给T细胞（图2）。因为DC是最有效的抗原呈递细胞，因此，利用它们的多样性可能产生改进的治疗性疫苗。树突细胞疫苗在各个癌症中取得了令人振奋的研究数据，想了解临床试验详细招募信息的患者可致电全球肿瘤医生网医学部进行初步评估（400-666-7998） </span><img alt="人体内的这类免疫细胞竟能制成挽救生命的癌症疫苗" src="http://p1.pstatp.com/large/pgc-image/a0dbdc56587f464baafaaf1d4fb9bf7a"/><span>  树突疫苗的制备流程从人体外周血提取并纯化单个核细胞，加入诱导因子，诱导并培养树突状细胞（DC）诱导DC细胞（树突状细胞）成熟并大量增殖，再以肿瘤优势抗原表位肽冲击DCDC发育成具有生物活性的效应DC，回输人体后将会迁移到淋巴组织中并将肿瘤抗原信息递呈给下一级T淋巴细胞，形成肿瘤抗原特异性细胞毒T淋巴细胞（CTL）肿瘤抗原特异性CTL特异、靶向、主动的攻击血液、肝脏、或其他组织中的肿瘤抗原这些“被激活的”执行细胞会“记住”陌生的结构特征，它们到达血液循环系统并分散在身体各个部位，搜索不同的具有某种特点的组织和细胞。写给病友的话五十年前，麻疹，腮腺炎和风疹疫苗的开发挽救了许多生命。当癌症逃离天然保护屏障时，需要什么才能引发治疗性免疫免疫。自从我们对主要问题的理解于1996年（Hsu等人，1996年）发起的第一次离体DC临床试验以来，我们已经走了很长的路。未来的新抗原疫苗试验将招募更多的晚期患者测试疫苗的疗效，利用预测来提高有效的新抗原和检查点抑制剂和其他免疫疗法协同试验的抗原呈递的改进方法，”科学家们说。“如果成功，在随后的试验中，个体化疫苗将被用于各类癌症，拥有足够数量的新抗原接种疫苗具有巨大潜力。我们期待，从现在起20年后，人类能够接种疫苗来预防癌症，战胜癌症，相信这一天离我们不远了！</span></p>'''
# answer_data = '''<div class="work-show-box" style="margin-top:0px;  padding:10px">  <p></p><section><section><section><section><section><section><section><section><section><p>颅底肿瘤是发生于颅底及其邻近结构部位的肿瘤，颅内肿瘤是发生在颅内脑、脑膜组织的肿瘤。由于颅底、颅内肿瘤的结构复杂、周围正常组织包含重要的结构，因此颅内、颅底肿瘤的治疗是临床棘手的问题。</p></section></section></section></section></section><section><section><section><section><section><section><section><p>Zap-X®系统是一种最新型的放射治疗系统，主要用于对脑部和头颈部肿瘤/病变进行放射治疗。</p></section></section><section><section><p>早在2017年，该系统就经美国FDA批准(K171804)，2018年又获得我国创新医疗器械特别审批程序。2019年我院成为国内首台、全球第二台该套系统装机的单位。</p></section></section></section><section><section><br></section><section><br></section></section></section></section></section></section><p><span style="color: rgb(192, 0, 0);"><strong>Zap-X®系统是一种最新型的放射治疗系统</strong></span>，主要用于对脑部和头颈部肿瘤/病变进行放射治疗。</p></section></section><section><section><p>早在2017年，该系统就经美国FDA批准(K171804)，2018年又获得我国创新医疗器械特别审批程序。2019年我院成为国内首台、全球第二台该套系统装机的单位。</p></section></section><section><section><section><section></section></section></section></section></section></section><p></p><section><section><p>目前，我院放射治疗科联合神经外科，开展一项应用Zap-X™ Radiosurgery Systems（X射线立体定向放射外科治疗系统）治疗脑部和头颈部肿瘤/病变的临床试验研究。</p><p>伦理审批编号：2019伦审第022号</p></section></section><section><section></section></section><section><section><p>★&nbsp; 最新型放射治疗系统—Zap-X®系统</p></section></section><section><section><p>本研究专门针对脑部和头颈部肿瘤/病变进行无创、免费放射外科治疗。</p></section></section><section><section><section><section><section><section><section><section><section><p>Zap-X™系统的优点据调查，Zap-X™系统具有无创治疗，治疗后效果显著和无术后感染风险的优点，创新的机械设计可以更好的保护肿瘤周围正常组织，缩短放疗时间，实现精确放射外科治疗。</p></section></section></section></section></section></section></section><section><section><section><section><p>国外研究表明该系统治疗脑部和头颈部肿瘤/病变具有良好的临床效果。</p></section></section></section></section></section></section><section><p></p></section><section><section><section><section><section><section><p><span style="color: rgb(192, 0, 0);"><strong>可获得的福利</strong></span></p></section></section></section></section><section><section><br></section></section></section></section><section><section><p>1. 免除参与研究者的相关检查费。</p><p>（包括1次CT检查、3次核磁检查、相关身体状态评估等）</p><p><br></p><p>2. &nbsp;免去应用Zap-X®系统放射治疗的费用。并由经验丰富的临床医学专家团队对疾病进行密切评估和细致治疗，专家将对随访及后续治疗进行指导。</p></section></section><section><section><section><section><section><section><p>入组要求</p></section></section></section></section><section><section><br></section></section></section></section><section><section><p>1. 年龄与性别不限。</p><p>2.&nbsp;&nbsp;由MRI或CT扫描见到可测量的脑部及头颈部肿瘤，肿瘤数量不超过3个，且肿瘤没有明显占位效应，无颅内压增高征兆，脑中线移位必须小于10mm。</p><p>（如不确定自己的情况，可到放射治疗科咨询，可加号）</p><p>3. &nbsp;经医生评价后，判断日常体能状态及器官功能可以接受放射外科治疗。</p><p>4. 能够配合所有的治疗要求。</p><p>5. 参与临床试验签署知情同意书。</p></section></section><section><section><p>符合以上要求者，并经由项目负责专家审核后方可获得入组资格。</p></section></section><section><p><br></p></section><section><section><section><section><section><section><p>排除条件</p></section></section></section></section><section><section><br></section></section></section></section><section><section><p>1.&nbsp;体重大于150公斤的受试者。</p><p>2. 病灶距离视交叉＜3 mm或位于脑干的受试者。</p><p>3. 参加试验前四周内参加过其他药物临床试验者。</p><p>4. 参加试验前两周内曾接受过静脉化学治疗或口服治疗脑瘤的化疗药物（如替莫唑胺等）者。</p><p>5. 参加试验期间有可能接受静脉化学治疗或口服治疗脑瘤的化疗药物（如替莫唑胺等）者。</p><p>6. 不能进行MRI检查的受试者。</p><p>7. 在脑部或头颈部区域已经或将要植入铁磁性装置的受试者，其装置可能会干扰MRI结果判读。</p><p>8. 具有严重的幽闭恐惧症的受试者。</p><p>9. 已怀孕的女性受试者。</p><p>10.无论男女，在治疗期有计划怀孕或不愿意采取避孕措施的受试者。</p></section></section><p></p><p>11.由研究者判断不适合参与本试验的其他情<span style="font-family: -apple-system-font, BlinkMacSystemFont, &quot;Helvetica Neue&quot;, &quot;PingFang SC&quot;, &quot;Hiragino Sans GB&quot;, &quot;Microsoft YaHei UI&quot;, &quot;Microsoft YaHei&quot;, Arial, sans-serif; font-size: 17px; text-align: justify; background-color: rgb(255, 255, 255);">况。</span></p><p></p>                             </div>'''
# answer_data = '''                                 <p>　　肾癌特殊部位转移的治疗原则</p><p>　　肾癌常见的转移部位分别为肺(45.2%)、骨(29.5%)、淋巴结(21.8%)、肝(20.3%)、肾上腺(8.9%)、脑(8.1%)、腹膜后(6.9%)等。</p><p>　　其中肝、骨、脑的转移由于具有压迫周围神经或组织、严重影响生活质量以及预后不良等特点而在处理上存在一些特殊性。</p><p><br></p>                             </div>'''
# answer_data = '''<div class="answercontent">                                                                          <p style="margin-top: 0px; margin-bottom: 0px; padding: 0px; color: rgb(61, 61, 61); font-family: 微软雅黑, &quot;Microsoft YaHei&quot;, PingFangSC-Ultralight, sans-serif; font-size: 14px; white-space: normal; line-height: 1.75em;">该理论诞生于1936年，至今已经有80余年的发展历史。</p><p style="margin-top: 0px; margin-bottom: 0px; padding: 0px; color: rgb(61, 61, 61); font-family: 微软雅黑, &quot;Microsoft YaHei&quot;, PingFangSC-Ultralight, sans-serif; font-size: 14px; white-space: normal; line-height: 1.75em;">　　据日本京都大学、大阪大学的研究小组，于2015 年10月29日举行的日本癌症治疗学会(http://www.jsco.or.jp/jpn/)，第53届学术集会上，发表的实例报告显示，对37名头颈部末期癌症患者进行临床试验后，半数以上患者的癌细胞消失了。</p><p style="margin-top: 0px; margin-bottom: 0px; padding: 0px; color: rgb(61, 61, 61); font-family: 微软雅黑, &quot;Microsoft YaHei&quot;, PingFangSC-Ultralight, sans-serif; font-size: 14px; white-space: normal; line-height: 1.75em;">　　此外，从2005年6月至2011年9月，BNCT在20例复发性高级脑膜瘤中治疗28次。所有患者之前都接受了强化治疗，如多次手术和多次放疗。其中19例患者接受硼中子俘获疗法，这些患者的原始肿瘤大小在4.3 cm3和109 cm3之间，治疗两个月后，平均肿瘤体积减少64.5%。中位随访时间为13个月。六名患者在研究发表时仍然活着; 目前，硼中子俘获治疗组和诊断后的中位生存时间分别为45.7个月(32.4-70.7个月)和14.1个月(8.6-40.4个月);在有症状的病例中，硼中子俘获治疗后，如偏瘫和面部疼痛得到显著改善。专家推测:硼中子俘获疗法对高级脑膜瘤可能特别有效。(https://thejns.org/view/journals/j-neurosurg/119/4/article-p837.xml)</p><p style="line-height: 1.75em;"><audio controls="controls" style="display: none;"></audio></p>                                                                    <div class="appendcontent">                   <div> </div>'''
# soup = BeautifulSoup(str(answer_data), 'html.parser')
soup = BeautifulSoup(str(answer_data), 'html.parser')
print(type(soup))
print(type(answer_data))
# print('问题对应的答案', soup.select_one(".answercontent").text.strip())  # 获取对应内容

print('问题对应的答案:')
list = []
for i in soup:
    print('获取的标签:', i, '\n')
    soup = BeautifulSoup(str(i), 'html.parser')
    print(i.string)  # 获取对应内容
    list.append(i.string)
print(list)

'''对百度知道页面具体问题内容进行爬取'''
# baidu = '''<span class="related-restrict-title grid">健康和生病的人都需要做基因检测吗？</span>'''
baidu='''<span class="grid-r f-aid ff-arial">2020-02-28</span>, <span class="ml-5 ff-arial">10</span>, <span class="f-aid">- 广告</span>, <span class="grid-r f-aid ff-arial">2018-02-26</span>, <span class="related-restrict-title grid">健康人可以去做成人基因检测吗</span>, <span class="ml-5 ff-arial">3</span>, <span class="grid-r f-aid ff-arial">2017-07-06</span>'''
soup = BeautifulSoup(str(baidu), 'html.parser')
print('百度页面上的类型：', type(soup))
print('对应内容：', soup.select_one(".related-restrict-title").text.strip())  # 获取对应内容

'''对百度知道首页搜索问题进行爬取'''
# baidu = '''<a href="http://zhidao.baidu.com/question/574340026.html?fr=iks&amp;word=%B5%E7%CA%D3%B9%E3%B8%E6&amp;ie=gbk" data-log="fm:as,pos:ti,si:1,st:0,title:非常常见的电视广告有哪些？" target="_blank" class="ti">非常常见的<em>电视广告</em>有哪些？</a>'''
baidu = '''<dt class="dt mb-3 line" alog-alias="result-title-0">
<a href="http://zhidao.baidu.com/question/986216295541729779.html?fr=iks&amp;word=%B0%D9%B6%C8%D6%AA%B5%C0&amp;ie=gbk" data-log="fm:as,pos:ti,si:1,st:0,title:百度云电脑版网页" target="_blank" class="ti"><em>百度</em>云电脑版网页</a>
</dt>'''
soup = BeautifulSoup(str(baidu), 'html.parser')
print('该页面类型：', type(soup))  # 页面类型<class 'bs4.BeautifulSoup'>
# print('页面列表内容：', soup.select_one(".fm:as,pos:ti,si:1,st:0,title:").text.strip())
print('页面列表内容：', soup.select_one(".dt mb-3 line")['href'])

'''写入文件'''
import pandas as pd

# 假设有列表a
# a = ['An attemped build of gfortran from a fresh', 'With a new download of gfortran the build now fails', 'While bootstrapping I noticed.checking for compiler with P', 'define weakexternexpr Pragma expr.', 'Reading the documention at  url  console objdir', 'The 20051227 version of gfortran has 144 new', 'Volker Reichelt  reicheltigpm.', 'javax.security.auth. loginException no configured', 'I was going to do a enablecheckingrelease buil to', 'Allrecursive Error 1.make2  all Error 2', 'libjava fails to build in a cross compiler using newlib', 'Gcc cannot process inlined assembler when configured for power', 'The following testcase..extern int f1 void .', 'The compiler builds but when it tries to build libgcc', 'Gcc 4.2 miscompiles binutils on Linux', 'I just tried to compile Suse package gnomeprint0']
# b = [1,2,3,4,5]
# # 将list转为dataframe 显然就变成一列了
# d = pd.DataFrame(a)
# d1 = pd.DataFrame(b)
# d.to_csv('data/demo.csv', index=False, mode='a', header=None) # mode表示追加 在追加时会将列名也作为一行进行追加，故header隐藏表头（列名）
# d1.to_csv('data/demo.csv', index=False, mode='a', header=None) # mode表示追加 在追加时会将列名也作为一行进行追加，故header隐藏表头（列名）


"""写入csv文件"""
# from pandas import DataFrame
# import numpy as np
#
# a=[1,2,3,4,5,6]
# b=[7,8,9,10,11,12]
#
# frequence_array=np.array(a)[:,np.newaxis]
# amplitude_array=np.array(b)[:,np.newaxis]
# print("frequence_array.shape",frequence_array.shape)
# concatenate_array=np.concatenate((frequence_array,amplitude_array),axis=1)
# print("concatenate_array",concatenate_array)
# print("concatenate_array",concatenate_array.shape)
# data=DataFrame(concatenate_array,columns=["frequence","amplitude"])
# data.to_csv("data/demo.csv")
