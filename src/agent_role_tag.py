from tokenize import String

import pandas as pd

agentRoleDict = {'评论罗伯特':'jdhapp5100',
	'林黛玉'  :'jdhapp5101',
	'妇科医生' :'jdhapp5102',
	'白娘子'  :'jdhapp5103',
	'妲己'   :'jdhapp5104',
	'儿科医生' :'jdhapp5105',
	'顾北辰'  :'jdhapp5106',
	'华妃'   :'jdhapp5107',
	'心晴'   :'jdhapp5108',
	'捕头小六' :'jdhapp5109',
	'周公解梦' :'jdhapp5112',
	'魔镜夸夸机':'jdhapp5110',
	'嗅嗅'   :'jdhapp5111',
	'厨艺达人' :'jdhapp5113',
	'夫妻那些事儿':'jdhapp5114',
	'铲屎官'  :'jdhapp5115',
	'李佳琦'  :'jdhapp5116',
	'刘畊皇'  :'jdhapp5117',
	'我是养生唐':'jdhapp5118',
	'恋爱顾问小诺':'jdhapp5119',
	'140岁老头':'jdhkk0002',
	'美容弹弹弹':'jdhkk0003',
	'潇洒宝妈' :'jdhapp5120',
	'哆啦 B 梦' :'jdhapp5124',
	'李叔聊养老':'jdhapp5125',
	'马匀'   :'jdhapp5126',
	'奶娃小萌萌':'jdhapp5127',
	'超级育儿师':'jdhapp5128',
	'吐槽鸭'  :'jdhapp5129',
	'大熊猫花花':'jdhapp5130',
	'陈大可'  :'jdhapp5131',
	'消化科医生':'jdhapp5133',
	'心血管医生':'jdhapp5134',
	'老中医'  :'jdhapp5135',
	'身体器官会说话':'jdhapp5136',
	'口腔科医生':'jdhapp5137',
	'呼吸科医生':'jdhapp5138',
	'营养师'  :'jdhapp5139',
	'药师'   :'jdhapp5140',
	'男科医生' :'jdhkk0001',
	'吃不胖营养师':'jdhapp5132'
				 }


df = pd.read_excel('/Users/suman6/Downloads/多智能体与标签对应关系.xlsx')
dicts = [dict(row) for index, row in df.iterrows()]

for dictItem in dicts:
	agentRoleName = dictItem.get('角色名称')
	if type(agentRoleName) is not str:
		continue
	agentRolePin = agentRoleDict.get(agentRoleName.strip())
	if(agentRolePin):
		#for tag in dictItem['对应标签'].split(','):
			#print(f"INSERT INTO `agent_role_user_tag_relation` (`agent_role_pin`, `user_tag_code`, `create_time`, `update_time`, `create_user`, `update_user`, `yn`, `ts`) VALUES ('{agentRolePin}', '{tag}', now(), now(), 'suman35', 'suman35', 1, now());")
		recallContent = dictItem.get('站内信固定文案')
		print(f"update agent_role_info set recall_content='{recallContent}' where agent_role_pin='{agentRolePin}';")

