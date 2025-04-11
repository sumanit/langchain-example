
import pandas as pd


df = pd.read_excel('/Users/suman6/Downloads/角色配置表格.xlsx')
dicts = [dict(row) for index, row in df.iterrows()]

for dictItem in dicts:
	agent_role_pin = dictItem.get('agentRolePin')
	name = dictItem.get('name')
	head_pic = dictItem.get('overview')
	overview = dictItem.get('agentRoleType')
	recall_content = dictItem.get('')
	agent_role_type = dictItem.get('')
	agent_role_identity_type = dictItem.get('')
	home_header_background = dictItem.get('homeHeaderBackground')
	im_chat_background = dictItem.get('imChatBackground')
	description	= dictItem.get('description').replace("\n", "")
	biz_code = dictItem.get('bizCode')
	quick_tools = dictItem.get('quickTools')
	guess_asks = dictItem.get('guessAsks').replace("\n", "")
	enable_private_message = dictItem.get('enablePrivateMessage')
	enable_comment = dictItem.get('enableComment')
	enable_reply_comment = dictItem.get('enableReplyComment')
	enable_home = dictItem.get('enableHome')
	enable_app_inner_msg = dictItem.get('enableAppInnerMsg')
	enable_guess_ask = dictItem.get('enableGuessAsk')
	enable_highlight_word = dictItem.get('enableHighlightWord')
	language_style = 'NULL'
	heat_value = 'NULL'
	enable_push = dictItem.get('enablePush')
	print(f"INSERT INTO `jdh_ai_kangkang`.`agent_role_info` ( `agent_role_pin`, `name`, `head_pic`, `overview`, `recall_content`,"
		  f" `agent_role_type`, `agent_role_identity_type`, `home_header_background`, `im_chat_background`, `description`, "
		  f"`biz_code`, `quick_tools`, `guess_asks`, `enable_private_message`, `enable_comment`, "
		  f"`enable_reply_comment`, `enable_home`, `enable_app_inner_msg`, `enable_guess_ask`, `heat_value`, "
		  f"`heat_time`, `enable_highlight_word`, `language_style`, `create_time`, `update_time`, "
		  f"`create_user`, `update_user`, `yn`, `ts`, `enable_push`) "
		  f"VALUES ("
		  f"'{agent_role_pin}', '{name}','{head_pic}', '{overview}', '{recall_content}',"
		  f" {agent_role_type}, {agent_role_identity_type}, '{home_header_background}', '{im_chat_background}', '{description}',"
		  f" '{biz_code}', '{quick_tools}', '{guess_asks}', {enable_private_message}, {enable_comment}, "
		  f"{enable_reply_comment}, {enable_home}, {enable_app_inner_msg}, {enable_guess_ask}, {heat_value}, "
		  f"now(), {enable_highlight_word}, {language_style}, now(), now(), "
		  f"'suman6', 'suman6', 1, now(), {enable_push});")
